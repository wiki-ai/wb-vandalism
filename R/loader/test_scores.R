source("env.R")
source("util.R")

load.test_scores = tsv_loader(
    paste(DATA_DIR, "wikidata.reverted.experimental_models.test_scores.tsv", sep="/"),
    "TEST_SCORES",
    function(dt){
        reverted = dt$reverted == "True"
        dt$reverted = NULL
        dt$reverted = reverted
        dt
    }
)
