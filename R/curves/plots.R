source("loader/test_scores.R")

test_scores = load.test_scores(reload=T)


score_stats = function(score, reverted){
    positives = sum(reverted)
    negatives = length(reverted) - positives

    if(length(unique(score)) > 500){
        thresholds = quantile(score, seq(0, 1, 0.01))
    }else{
        thresholds = unique(score)
    }
    thresholds = c(thresholds, thresholds+0.0001)

    rows = lapply(
        thresholds,
        function(threshold){
            predicted = score >= threshold
            reverted = reverted
            correct = sum(predicted == reverted)
            true_positives = sum(predicted & reverted)

            data.table(
                score = threshold,
                accuracy = correct / length(predicted),
                precision = true_positives / sum(predicted),
                recall = true_positives / sum(reverted),
                filter_rate = 1 - (sum(predicted) / length(predicted))
            )
        }
    )
    stats = rbindlist(rows, use.names=T)
    stats[order(stats$score),]
}

score_stat_groups = rbind(
    cbind(
        score_stats(test_scores$general, test_scores$reverted),
        data.table(feature_set = "general")
    ),
    cbind(
        score_stats(test_scores$general_and_context, test_scores$reverted),
        data.table(feature_set = "general_and_context")
    ),
    cbind(
        score_stats(test_scores$general_context_and_type, test_scores$reverted),
        data.table(feature_set = "general_context_and_type")
    ),
    cbind(
        score_stats(test_scores$general_and_user, test_scores$reverted),
        data.table(feature_set = "general_and_user")
    ),
    cbind(
        score_stats(test_scores$all, test_scores$reverted),
        data.table(feature_set = "all")
    )
)


# Precision/recall
svg("curves/plots/wikidata.reverted.precision_recall.general_context_type.svg",
    height=5, width=7)
ggplot(
    score_stat_groups[
        feature_set %in% c("general", "general_and_context",
                           "general_context_and_type"),
    ],
    aes(x=recall, y=precision, group=feature_set, linetype=feature_set)
) +
theme_bw() +
geom_abline(slope=-1, intercept=1, color="#BBBBBB", linetype=2) +
geom_line() +
scale_x_continuous("recall") +
scale_y_continuous("precision")
dev.off()

svg("curves/plots/wikidata.reverted.precision_recall.general_user_all.svg",
    height=5, width=7)
ggplot(
    score_stat_groups[
        feature_set %in% c("general_and_user", "all"),
    ],
    aes(x=recall, y=precision, group=feature_set, linetype=feature_set)
) +
theme_bw() +
geom_abline(slope=-1, intercept=1, color="#BBBBBB", linetype=2) +
geom_line() +
scale_x_continuous("recall") +
scale_y_continuous("precision")
dev.off()

# Filter-rate/recall
svg("curves/plots/wikidata.reverted.filter-rate_recall.general_context_type.svg",
    height=5, width=7)
ggplot(
    score_stat_groups[
        feature_set %in% c("general", "general_and_context",
                           "general_context_and_type"),
    ],
    aes(x=recall, y=filter_rate, group=feature_set, linetype=feature_set)
) +
theme_bw() +
geom_vline(xintercept=0.90, color="#BBBBBB", linetype=2) +
geom_line() +
scale_x_continuous("recall") +
scale_y_continuous("filter-rate")
dev.off()


svg("curves/plots/wikidata.reverted.filter-rate_recall.general_user_all.svg",
    height=5, width=7)
ggplot(
    score_stat_groups[
        feature_set %in% c("general_and_user", "all"),
    ],
    aes(x=recall, y=filter_rate, group=feature_set, linetype=feature_set)
) +
theme_bw() +
geom_vline(xintercept=0.90, color="#BBBBBB", linetype=2) +
geom_line() +
scale_x_continuous("recall") +
scale_y_continuous("filter-rate")
dev.off()
