source("loader/ores_request_timing.R")

timing = load.ores_request_timing(reload=T)

batches = timing[
    grouping == "batch",
    list(rev_id=min(rev_id), revisions=length(rev_id)),
    list(timing=timing, wiki, grouping)
]

timing_grouped = rbind(
    timing[grouping == "single" & timing > 0.15,],
    timing[grouping == "cached" & timing < 0.15,],
    batches[,list(rev_id, timing=timing/revisions, wiki, grouping)]
)


svg("speed/plots/ores_wikidatawiki_response_timing.single_batch_and_cached.svg",
    height=5, width=7)
ggplot(
    timing_grouped[wiki == "wikidatawiki" | wiki == "wikidata",],
    aes(x=timing, group=grouping, fill=grouping)
) +
theme_bw() +
geom_density(adjust=2, alpha=0.5) + scale_fill_grey() +
scale_x_log10("Time to response", breaks=c(0.01, 0.12, 0.53, 1.1, 5, 10))
dev.off()
