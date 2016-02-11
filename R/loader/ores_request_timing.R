source("env.R")
source("util.R")

load.ores_request_timing = tsv_loader(
    paste(DATA_DIR, "ores_request_timing.tsv", sep="/"),
    "ORES_REQUEST_TIMING"
)
