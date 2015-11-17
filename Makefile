
datasets/wikidata.rev_reverted.20k_balanced_2015.tsv: \
                datasets/wikidata.sampled_revision.20k_balanced_2015.tsv
        cat datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv | \
        editquality label_reverted \
                --host https://wikidata.org \
                --revert-radius 3 \
                --verbose > \
        datasets/wikidata.rev_reverted.20k_balanced_2015.tsv

datasets/wikidata.features_reverted.20k_balanced_2015.tsv: \
		datasets/wikidata.rev_reverted.20k_balanced_2015.tsv
	cat datasets/wikidata.rev_reverted.20k_balanced_2015.tsv | \
	revscoring extract_features \
		wb_vandalism.feature_lists.wikidata.reverted \
		--host https://wikidata.org \
                --verbose \
		--include-revid > \
	datasets/wikidata.features_reverted.20k_balanced_2015.tsv

models/wikidata.reverted.linear_svc.model: \
		datasets/wikidata.features_reverted.20k_balanced_2015.tsv
	cut datasets/wikidata.features_reverted.20k_balanced_2015.tsv -f2- | \
	revscoring train_test \
		revscoring.scorer_models.LinearSVC \
		wb_vandalism.feature_lists.wikidata.reverted \
		--version 0.0.2 \
		--label-type=bool > \
	models/wikidata.reverted.linear_svc.model
