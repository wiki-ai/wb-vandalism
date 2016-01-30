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

models/wikidata.reverted.rf.model: \
		datasets/wikidata.features_reverted.20k_balanced_2015.tsv
	cut datasets/wikidata.features_reverted.20k_balanced_2015.tsv -f2- | \
	revscoring train_test \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.wikidata.reverted \
		--version 0.0.4 \
		-p 'max_features="log2"' \
                -p 'criterion="entropy"' \
                -p 'min_samples_leaf=1' \
                -p 'n_estimators=80' \
                --label-type=bool > \
        models/wikidata.reverted.rf.model

datasets/wikidata.prelabeled_revisions.20k_balanced_2015.tsv: \
		datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv
	cat datasets/wikidata.sampled_revisions.20k_balanced_2015.tsv | \
	editquality prelabel https://wikidata.org \
		--trusted-groups=abusefilter,arbcom,bureaucrat,checkuser,rollbacker,sysop,bot \
		--trusted-edits=1000 \
		--verbose > \
	datasets/wikidata.prelabeled_revisions.20k_balanced_2015.tsv

tuning_reports/wikidata.reverted.roc_auc.md: \
		datasets/wikidata.features_reverted.20k_balanced_2015.tsv
	cat datasets/wikidata.features_reverted.20k_balanced_2015.tsv | cut -f2- | \
	revscoring tune \
		config/damaging_classifiers.params.yaml \
		wb_vandalism.feature_lists.wikidata.reverted \
		--cv-timeout=60 \
		--debug \
		--scoring=roc_auc \
		--label-type=bool > \
	tuning_reports/wikidata.reverted.roc_auc.md

tuning_reports/wikidata.reverted.pr_auc.md: \
		datasets/wikidata.features_reverted.20k_balanced_2015.tsv
	cat datasets/wikidata.features_reverted.20k_balanced_2015.tsv | cut -f2- | \
	revscoring tune \
		config/damaging_classifiers.params.yaml \
		wb_vandalism.feature_lists.wikidata.reverted \
		--cv-timeout=60 \
		--debug \
		--scoring=pr_auc \
		--label-type=bool > \
	tuning_reports/wikidata.reverted.pr_auc.md


### Study of Wikidata! ###

datasets/wikidatawiki.revision_sample.nonbot_user_edit_type.1m_2015.tsv: \
		sql/revision_sample.nonbot_user_edit_type.1m_2015.sql
	cat sql/revision_sample.nonbot_user_edit_type.1m_2015.sql | \
	mysql $(mysql_args) wikidatawiki > \
	datasets/wikidata.revision_sample.nonbot_user_edit_type.1m_2015.sql

datasets/wikidatawiki.revision_sample.nonbot_user_edit_type_reverted.1m_2015.tsv: \
		datasets/wikidatawiki.revision_sample.nonbot_user_edit_type.1m_2015.tsv
	cat datasets/wikidatawiki.revision_sample.nonbot_user_edit_type.1m_2015.tsv | \
	editquality label_reverted \
		--host https://wikidata.org \
		--revert-radius 3 \
		--revert-window 99999999 \
		--verbose >
	datasets/wikidatawiki.revision_sample.nonbot_user_edit_type_reverted.1m_2015.tsv
