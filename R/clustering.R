source("util.R")
library(mixtools)

cluster_init = list(
    short_within = list(
        color = "deepskyblue1",
        lambda = .55,
        mu = 2,
        sigma = 2
    ),
    long_within = list(
        color = "navyblue",
        lambda = .22,
        mu = 7,
        sigma = 2.75
    ),
    within = list(
        color = "blue",
        lambda = .77,
        mu = 6.7,
        sigma = 2.75
    ),
    between = list(
        color = "red",
        lambda = .15,
        mu = 16.5,
        sigma = 2.2
    ),
    "break" = list(
        color = "green",
        lambda = .05,
        mu = 22.5,
        sigma = 2.5
    )
)

cluster_inits = function(clusters){
    inits = data.table(
        lambda=sapply(clusters, function(c){cluster_init[[c]]$lambda}),
        mu=sapply(clusters, function(c){cluster_init[[c]]$mu}),
        sigma=sapply(clusters, function(c){cluster_init[[c]]$sigma})
    )
    inits
}

fit_intertimes = function(intertimes, clusters){
    
    inits = cluster_inits(clusters)
    
    fit = normalmixEM(
        log(sample(intertimes[intertimes > 0], 50000, replace=T), base=2),
        lambda=inits$lambda,
        mu=inits$mu,
        sigma=inits$sigma,
        maxit=500
    )
    
    cluster_fits = list()
    for(cluster_i in 1:length(clusters)){
        cluster_fits[[clusters[cluster_i]]] = list(
            mu=fit$mu[cluster_i],
            sigma=fit$sigma[cluster_i],
            lambda=fit$lambda[cluster_i]
        )
    }
    cluster_fits
}


plot_frequencies = function(intertimes){
    ggplot(
        data.table(x=intertimes),
        aes(
            x=x
        )
    ) +
    geom_histogram(
        fill="#cccccc",
        color="#888888",
        binwidth=1/5,
        aes(y = (..density../sum(..density..)) * 1.5)
    ) +
    scale_x_log10(
        "\nInter-activity time",
        breaks=c(
            5,
            60,
            7*60,
            60*60,
            24*60*60,
            7*24*60*60,
            30*24*60*60,
            356*24*60*60
        ),
        labels=c("5 sec.", "minute", "7 min.", "hour", "day",
                 "week", "month", "year")
    ) +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position="top"
    ) +
    scale_y_continuous("Density\n") +
    theme_bw()
}

plot_clusters = function(intertimes, clusters=c("within", "between"), fit=NULL){
    intertimes = intertimes[intertimes > 0]
    if(is.null(fit)){
        fit = fit_intertimes(intertimes, clusters)
    }
    
    g = plot_frequencies(intertimes)
    
    max_intertime = max(intertimes)
    dists = rbindlist(
        lapply(
            clusters,
            function(cluster){
                log_norm = function(x){
                    dnorm(x, fit[[cluster]]$mu, fit[[cluster]]$sigma) *
                    fit[[cluster]]$lambda
                }
                data.table(
                    x = 2^seq(0,log2(max_intertime),.01),
                    y = log_norm(seq(0,log2(max_intertime),.01)),
                    cluster = cluster
                )
            }
        )
    )
    
    g = g +
    geom_area(
        data=dists,
        aes(x=x,y=y, fill=cluster),
        alpha=0.25,
        position="identity"
    ) +
    geom_line(
        data=dists,
        aes(x=x,y=y, color=cluster),
    )
    
    color_values = sapply(
        clusters,
        function(c){
            cluster_init[[c]]$color
        }
    )
    names(color_values) = clusters
    
    g = g +
    scale_fill_manual(
        name="Clusters",
        values=color_values,
        breaks=clusters,
        guide="legend"
    ) +
    scale_color_manual(
        name="Clusters",
        values=color_values,
        breaks=clusters,
        guide="legend"
    ) +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position="top"
    )
    
    g
}

theoretical_roc = function(intertimes, clusters, fit=NULL){
    intertimes = intertimes[intertimes > 0]
    if(is.null(fit)){
        fit = fit_intertimes(intertimes, clusters)
    }
    
    x = seq(0, max(log2(intertimes)), .1)
    
    within_clusters = intersect(clusters, c("within", "short_within",
                                            "long_within"))
    within_mass = sum(sapply(within_clusters, function(c){fit[[c]]$lambda}))
    
    tp = 0
    for(c in within_clusters){
        tp = tp + pnorm(x, fit[[c]]$mu, fit[[c]]$sigma) *
                  (fit[[c]]$lambda/within_mass)
    }
    
    external_clusters = setdiff(clusters, within_clusters)
    external_mass = sum(sapply(external_clusters, function(c){fit[[c]]$lambda}))
    
    fp = 0
    for(c in external_clusters){
        fp = fp + pnorm(x, fit[[c]]$mu, fit[[c]]$sigma) *
             (fit[[c]]$lambda/external_mass)
    }
    
    data.table(threshold=2^x, true_positive=tp, false_positive=fp)
    
}

plot_roc = function(intertimes, clusters=c("within", "between"), fit=NULL){
    roc = theoretical_roc(intertimes, clusters, fit)
    ggplot(
        roc,
        aes(x=false_positive, y=true_positive)
    ) +
    geom_line() +
    geom_line(
        data=data.table(x=c(0,1), y=c(0, 1)),
        aes(
            x=x,
            y=x
        ),
        linetype=2,
        color="#888888"
    ) +
    scale_x_continuous("\nFalse positive rate") +
    scale_y_continuous("True positive rate\n") +
    theme_bw()
}

plot_true_and_false_positives = function(intertimes,
                                         clusters=c("within", "between"),
                                         fit=NULL){
    
    ggplot(
        with(
            theoretical_roc(intertimes, clusters, fit),
            rbind(
                data.table(
                    x=threshold,
                    y=true_positive,
                    label="true positive"
                ),
                data.table(
                    x=threshold,
                    y=false_positive,
                    label="false positive"
                )
            )
        ),
        aes(x=x, y=y, linetype=label, color=label)
    ) +
    geom_line() +
    theme_bw() +
    scale_x_log10(
        "\nInter-activity threshold",
        breaks=c(
            5,
            60,
            7*60,
            60*60,
            24*60*60,
            7*24*60*60,
            30*24*60*60,
            356*24*60*60
        ),
        labels=c("5 sec.", "minute", "7 min.", "hour", "day",
                 "week", "month", "year")
    ) +
    scale_color_manual(
        name="",
        values=c("true positive"="blue", "false positive"="red"),
        guide="legend"
    ) +
    scale_linetype_manual(
        name="",
        values=c("true positive"=1, "false positive"=2),
        guide="legend"
    ) +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position="top"
    ) +
    scale_y_continuous("Rate\n")
}

plot_true_and_false_positive_difference = function(intertimes,
                                         clusters=c("within", "between"),
                                         fit=NULL){
    
    ggplot(
        theoretical_roc(intertimes, clusters, fit),
        aes(x=threshold, y=true_positive - false_positive)
    ) +
    geom_line() +
    theme_bw() +
    scale_x_log10(
        "\nInter-activity threshold",
        breaks=c(
            5,
            60,
            7*60,
            60*60,
            24*60*60,
            7*24*60*60,
            30*24*60*60,
            356*24*60*60
        ),
        labels=c("5 sec.", "minute", "7 min.", "hour", "day",
                 "week", "month", "year")
    ) +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    scale_y_continuous("TP rate - FP rate\n")
}

# generates AUC
area_under_theoretical_roc = function(intertimes, clusters, fit=NULL) {
    theoretical_roc(intertimes, clusters, fit) -> roc
    sum = 0
    for (i in 2:dim(roc)[1]) {
        lastRow = roc[i-1]
        row = roc[i]
        width = row$false_positive - lastRow$false_positive
        avgHeight = (row$true_positive + lastRow$true_positive)/2
        sum = sum + width*avgHeight
    }
    sum
}

# Generates an optimal cutoff between clusters
extract_cutoff = function(fit, left="between", right="within") {
   # optimal cutoff is described by quadratic equation
   if (fit[[left]]$mu > fit[[right]]$mu) {
      tmp = left
      left = right
      right = tmp
   }

   s1 = fit[[left]]$sigma
   s2 = fit[[right]]$sigma
   m1 = fit[[left]]$mu
   m2 = fit[[right]]$mu
   l1 = fit[[left]]$lambda
   l2 = fit[[right]]$lambda

   a =  1/(2*s1*s1) - 1/(2*s2*s2)
   b = -1*m1/(s1*s1) + m2/(s2*s2)
   c = m1*m1/(2*s1*s1) - m2*m2/(2*s2*s2) - log(s2*l1/(s1*l2))

   # cutoff is one of two values
   cut1 = (-b + sqrt(b*b-4*a*c))/2/a
   cut2 = (-b - sqrt(b*b-4*a*c))/2/a

   # compute the cut as the one that is inbetween the means.
   cut = 0
   if ((m1 <= cut1) && (cut1 <= m2)) {
     cut = cut1
   } else {
     cut = cut2
   }
   cut
}

# Splits intertimes based on optimal clusters
split_clusters = function(intertimes, clusters, fit=NULL) {
    intertimes = intertimes[intertimes > 0]
    if(is.null(fit)){
        fit = fit_intertimes(intertimes, clusters)
    }
    
    # there is probably a cleaner way to write this code...
    breaks = 1:(length(clusters)+1)
    breaks[1] = -Inf

    for (i in 2:length(clusters)) {
      # transform to non-log space
            breaks[i] = 2**extract_cutoff(fit, clusters[i-1], clusters[i])
    }
    breaks[length(clusters)+1] = Inf

    clusts = list()
    for (i in 2:length(breaks)) {
        cluster = intertimes[(intertimes > breaks[i-1]) &
                             (intertimes <= breaks[i])]
        clusts[[clusters[i-1]]] = cluster
    }
    clusts
}

var_reduction = function(intertimes, clusters, fit=NULL) {
    intertimes = intertimes[intertimes > 0]
    clusts = split_clusters(intertimes, clusters, fit)

    totalVar = var(log2(intertimes))
    for (cluster in clusters) {
      totalVar = totalVar - var(log2(clusts[[cluster]]))
    }
    totalVar
}


davies_boulin = function(intertimes, clusters, fit=NULL) {
    clusts = split_clusters(intertimes, clusters, fit)
    centroids = lapply(clusts, function(x){mean(x)})
    
    computeS = function(cluster) {
      points = clusts[[cluster]]
      points = abs(points - centroids[[cluster]])
      mean(points)
    }

    S = lapply(clusters, computeS)
    names(S) <- clusters

    dindex = 0
    for(cluster in clusters) {
        maxR = -1
        for (cluster2 in clusters) {
            if (cluster2 != cluster) {
                Mij = abs(centroids[[cluster]] - centroids[[cluster2]])
                R = (S[[cluster]] + S[[cluster2]])/ Mij
                maxR = max(R, maxR)
            }
        }
        dindex = dindex + maxR
    }
    dindex/length(clusters)
}

average_entropy = function(intertimes, clusters, fit=NULL) {
    intertimes = intertimes[intertimes > 0]
    if(is.null(fit)){
        fit = fit_intertimes(intertimes, clusters)
    }

    entropy = function(intertime) {
        if (intertime == 0) {
          intertime = 0.1
        }
        intertime = log(intertime, base=2)
        pxc = 1:length(clusters)
        for(i in 1:length(clusters)) {
            cluster = clusters[i]
            pxc[i] = fit[[cluster]]$lambda *
                     dnorm(intertime, fit[[cluster]]$mu,
            fit[[cluster]]$sigma)
        }
        pxc = pxc/sum(pxc)
        ent = 0
        for(pc in pxc) {
          ent = ent - pc*log(pc)
        }
        ent
    }
    mean(sapply(intertimes, entropy))
    
}
 
plot_clusters_datasets = function(datasets, clusters, split){
    frequencies = rbindlist(
        lapply(
            datasets,
            function(dataset){
                merge(
                    dataset$data[intertime>0,
                        list(
                            site = dataset$site,
                            event = dataset$event,
                            frequency = length(user_id)
                        ),
                        list(
                            intertime = 1.45^floor(log(intertime, base=1.45))
                        )
                    ],
                    dataset$data[intertime>0,
                        list(
                            site = dataset$site,
                            event = dataset$event,
                            n = length(user_id)
                        )
                    ],
                    by=c("site", "event")
                )
            }
        )
    )
    
    fits = lapply(
        datasets,
        function(dataset){
            fit_intertimes(dataset$data$intertime, clusters)
        }
    )
    
    
    dbis = rbindlist(
        lapply(
            datasets,
            function(dataset){
                fit = fits[[paste(dataset$site, dataset$event)]]
                data.table(
                    site=dataset$site,
                    event=dataset$event,
                    dbi=davies_boulin(dataset$data$intertime, clusters, fit)
                )
            }
        )
    )
    
    dists = rbindlist(
        lapply(
            datasets,
            function(dataset){
                fit = fits[[paste(dataset$site, dataset$event)]]
                if(!is.null(split) & !is.na(split)){
                    threshold = tryCatch(
                        2^extract_cutoff(fit, split[1], split[2]),
                        error=function(e){NA}
                    )
                }else{
                    threshold = NA
                }
                max_intertime = max(dataset$data$intertime)
                
                rbindlist(
                    lapply(
                        clusters,
                        function(cluster){
                            log_norm = function(x){
                                dnorm(x, fit[[cluster]]$mu,
                                      fit[[cluster]]$sigma) *
                                fit[[cluster]]$lambda
                            }
                            data.table(
                                site=dataset$site,
                                event=dataset$event,
                                threshold=threshold,
                                intertime = 2^seq(0,log2(max_intertime),.01),
                                density =
                                    log_norm(seq(0,log2(max_intertime),.01)),
                                cluster = cluster
                            )
                        }
                    )
                )
            }
        )
    )
    
    
    cluster_colors = sapply(cluster_init, function(c){c$color})
    
    ggplot(
        frequencies[intertime > 0],
        aes(
            x=intertime,
            y=frequency/n
        )
    ) +
    facet_wrap(~ site + event, ncol=1) +
    geom_bar(
        fill="#EEEEEE",
        color="#555555",
        stat="identity"
    ) +
    geom_area(
        data=dists,
        aes(x=intertime,y=density*.55, fill=cluster),
        alpha=0.5,
        position="identity"
    ) +
    geom_line(
        data=dists,
        aes(x=intertime,y=density*.55, color=cluster),
    ) +
    geom_vline(
        data=dists,
        aes(xintercept=threshold),
        linetype=2
    ) +
    geom_text(
        data=dbis,
        aes(
            x=Inf,
            y=Inf,
            label=paste("DBi:", round(dbi, 2))
        ),
        vjust=1,
        hjust=1,
        size=3
    ) +
    scale_x_log10(
        "Inter-activity time",
        breaks=c(
            5,
            60,
            7*60,
            60*60,
            24*60*60,
            7*24*60*60,
            30*24*60*60,
            356*24*60*60
        ),
        labels=c("5 sec.", "minute", "7 min.", "hour", "day",
                 "week", "month", "year")
    ) +
    scale_y_continuous("") +
    scale_fill_manual(
        name="Clusters",
        values=cluster_colors,
        breaks=names(cluster_colors),
        guide="legend"
    ) +
    scale_color_manual(
        name="Clusters",
        values=cluster_colors,
        breaks=names(cluster_colors),
        guide="legend"
    ) +
    theme_bw() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position="top"
    )
}
