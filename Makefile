datasets/wikidata.rev_reverted.20k_balanced_2015.tsv: \
		datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv
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
		--version 0.0.4 \
                -p 'cache_size=1000' \
		--label-type=bool > \
	models/wikidata.reverted.linear_svc.model

datasets/wikidata.prelabeled_revisions.20k_balanced_2015.tsv: \
		datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv
	cat datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv | \
	editquality prelabel https://wikidata.org \
		--trusted-groups=abusefilter,arbcom,bureaucrat,checkuser,rollbacker,sysop,bot \
		--trusted-edits=1000 \
		--verbose > \
	datasets/wikidata.prelabeled_revisions.20k_balanced_2015.tsv

tuning_reports/wikidata.reverted.md: \
		datasets/wikidata.features_reverted.20k_balanced_2015.tsv 
	cat datasets/wikidata.features_reverted.20k_balanced_2015.tsv | cut -f2- | \
	revscoring tune \
		config/damaging_classifiers.params.yaml \
		wb_vandalism.feature_lists.wikidata.reverted \
		--cv-timeout=60 \
		--debug \
		--label-type=bool > \
	tuning_reports/wikidata.damaging.md
