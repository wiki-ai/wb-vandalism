conn_user = --defaults-file=~/.my.research.cnf -u research

mysql_args = $(conn_user) -h analytics-store.eqiad.wmnet

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

experimental_models: \
	models/wikidata.reverted.general.rf.model \
	models/wikidata.reverted.general_and_context.rf.model \
	models/wikidata.reverted.general_context_and_type.rf.model \
	models/wikidata.reverted.general_and_user.rf.model \
	models/wikidata.reverted.all.rf.model

datasets/wikidatawiki.revision_sample.nonbot_user_edit_type.1m_2015.tsv: \
		sql/revision_sample.nonbot_user_edit_type.1m_2015.sql
	cat sql/revision_sample.nonbot_user_edit_type.1m_2015.sql | \
	mysql $(mysql_args) wikidatawiki > \
	datasets/wikidata.revision_sample.nonbot_user_edit_type.1m_2015.tsv

datasets/wikidata.revision_sample.nonbot_user_edit_type_reverted.1m_2015.tsv: \
		datasets/wikidata.revision_sample.nonbot_user_edit_type.1m_2015.tsv
	cat datasets/wikidata.revision_sample.nonbot_user_edit_type.1m_2015.tsv | \
	editquality label_reverted \
		--host https://wikidata.org \
		--revert-radius 3 \
		--revert-window 168 \
		--verbose > \
	datasets/wikidata.revision_sample.nonbot_user_edit_type_reverted.1m_2015.tsv

datasets/wikidata_nonbot_sample.created: \
		sql/wikidata_nonbot_sample.create.sql
	cat sql/wikidata_nonbot_sample.create.sql | \
	mysql $(mysql_args) staging > \
	datasets/wikidata_nonbot_sample.created

datasets/wikidata_nonbot_sample.loaded: \
		datasets/wikidata_nonbot_sample.created
	ln -sf datasets/wikidata.revision_sample.nonbot_user_edit_type.1m_2015.tsv wikidata_nonbot_sample && \
	mysqlimport $(mysql_args) --local --ignore-lines=1 staging wikidata_nonbot_sample; \
	rm -f wikidata_nonbot_sample > \
	datasets/wikidata_nonbot_sample.loaded

datasets/wikidata_nonbot_reverted_sample.created: \
		sql/wikidata_nonbot_reverted_sample.create.sql
	cat sql/wikidata_nonbot_reverted_sample.create.sql | \
	mysql $(mysql_args) staging > \
        datasets/wikidata_nonbot_reverted_sample.created

datasets/wikidata_nonbot_reverted_sample.loaded: \
		datasets/wikidata_nonbot_reverted_sample.created
	ln -sf datasets/wikidata.revision_sample.nonbot_user_edit_type_reverted.1m_2015.cleaned.tsv wikidata_nonbot_reverted_sample && \
	mysqlimport $(mysql_args) --local --ignore-lines=1 staging wikidata_nonbot_reverted_sample; \
	rm -f wikidata_nonbot_reverted_sample > \
	datasets/wikidata_nonbot_reverted_sample.loaded

###  The 500k sample ####
datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv: \
		sql/revision_sample.nonbot_with_exclusions.500k_2015.sql
	cat sql/revision_sample.nonbot_with_exclusions.500k_2015.sql | \
	mysql $(mysql_args) wikidatawiki > \
	datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv


datasets/wikidata.rev_reverted.nonbot.non_excluded.tsv: \
		datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv
	cat datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv | \
	grep -P "rev_id\texclusion_criteria|[0-9]+\tNULL" | cut -f1 | \
	editquality label_reverted \
		--host https://wikidata.org \
		--revert-radius 5 \
		--revert-window 168 \
		--exclude-reverting "/\* client" \
		--verbose > \
	datasets/wikidata.rev_reverted.nonbot.non_excluded.tsv

datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv: \
		datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv \
		datasets/wikidata.rev_reverted.nonbot.non_excluded.tsv
	tail -n+2 datasets/wikidata.revision_sample.nonbot_with_exclusions.500k_2015.tsv | \
	grep -v NULL | \
	sed -r "s/([0-9]+)\t[a-Z_]+/\1\tFalse/" | \
	cat datasets/wikidata.rev_reverted.nonbot.non_excluded.tsv - | \
	shuf > \
	datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv

datasets/wikidata.rev_reverted.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv
	head -n 400000 datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv > \
	datasets/wikidata.rev_reverted.nonbot.400k_2015.training.tsv

datasets/wikidata.rev_reverted.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv
		tail -n+400001 datasets/wikidata.rev_reverted.nonbot.500k_2015.tsv > \
		datasets/wikidata.rev_reverted.nonbot.100k_2015.testing.tsv

datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.rev_reverted.nonbot.400k_2015.training.tsv
	cat datasets/wikidata.rev_reverted.nonbot.400k_2015.training.tsv | \
	revscoring extract_features \
		wb_vandalism.feature_lists.experimental.all \
		--host https://wikidata.org \
		--include-revid \
		--verbose > \
	datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv

datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.rev_reverted.nonbot.100k_2015.testing.tsv
	cat datasets/wikidata.rev_reverted.nonbot.100k_2015.testing.tsv | \
	revscoring extract_features \
		wb_vandalism.feature_lists.experimental.all \
		--host https://wikidata.org \
		--include-revid \
		--verbose > \
	datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv

# General
datasets/wikidata.features_reverted.general.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv | \
	cut -f1-33 > \
	datasets/wikidata.features_reverted.general.nonbot.400k_2015.training.tsv

datasets/wikidata.features_reverted.general.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv | \
	cut -f1-33 > \
	datasets/wikidata.features_reverted.general.nonbot.100k_2015.testing.tsv

# General and context
datasets/wikidata.features_reverted.general_and_context.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv | \
	cut -f1-47 > \
	datasets/wikidata.features_reverted.general_and_context.nonbot.400k_2015.training.tsv

datasets/wikidata.features_reverted.general_and_context.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv | \
	cut -f1-47 > \
	datasets/wikidata.features_reverted.general_and_context.nonbot.100k_2015.testing.tsv

# General, context and type
datasets/wikidata.features_reverted.general_context_and_type.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv | \
	cut -f1-54 > \
	datasets/wikidata.features_reverted.general_context_and_type.nonbot.400k_2015.training.tsv

datasets/wikidata.features_reverted.general_context_and_type.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv | \
	cut -f1-54 > \
	datasets/wikidata.features_reverted.general_context_and_type.nonbot.100k_2015.testing.tsv

# General and user
datasets/wikidata.features_reverted.general_and_user.nonbot.400k_2015.training.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv | \
	cut -f1-33 > \
	datasets/wikidata.features_reverted.general_and_user.nonbot.400k_2015.training.tsv

datasets/wikidata.features_reverted.general_and_user.nonbot.100k_2015.testing.tsv: \
		datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv
	cat datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv | \
	cut -f1-33,55-60 > \
	datasets/wikidata.features_reverted.general_and_user.nonbot.100k_2015.testing.tsv

models/wikidata.reverted.general.rf.pretest.model: \
		datasets/wikidata.features_reverted.general.nonbot.400k_2015.training.tsv
	cut datasets/wikidata.features_reverted.general.nonbot.400k_2015.training.tsv -f2- | \
	revscoring train_model \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.experimental.general \
		--version 0.0.1 \
		-p 'max_features="log2"' \
		-p 'criterion="entropy"' \
		-p 'min_samples_leaf=1' \
		-p 'n_estimators=80' \
		--balance-sample-weight \
		--center --scale \
		--label-type=bool > \
	models/wikidata.reverted.general.rf.pretest.model

models/wikidata.reverted.general.rf.model: \
		models/wikidata.reverted.general.rf.pretest.model \
		datasets/wikidata.features_reverted.general.nonbot.100k_2015.testing.tsv
	cut datasets/wikidata.features_reverted.general.nonbot.100k_2015.testing.tsv -f2- | \
	revscoring test_model \
		models/wikidata.reverted.general.rf.pretest.model \
		-s 'pr' -s 'roc' \
		-s 'recall_at_fpr(max_fpr=0.10)' \
		-s 'filter_rate_at_recall(min_recall=0.90)' \
		-s 'filter_rate_at_recall(min_recall=0.75)' \
		--label-type=bool > \
	models/wikidata.reverted.general.rf.model

models/wikidata.reverted.general_and_context.rf.pretest.model: \
		datasets/wikidata.features_reverted.general_and_context.nonbot.400k_2015.training.tsv
	cut datasets/wikidata.features_reverted.general_and_context.nonbot.400k_2015.training.tsv -f2- | \
	revscoring train_model \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.experimental.general_and_context \
		--version 0.0.1 \
		-p 'max_features="log2"' \
		-p 'criterion="entropy"' \
		-p 'min_samples_leaf=1' \
		-p 'n_estimators=80' \
		--balance-sample-weight \
		--center --scale \
		--label-type=bool > \
	models/wikidata.reverted.general_and_context.rf.pretest.model

models/wikidata.reverted.general_and_context.rf.model: \
		models/wikidata.reverted.general_and_context.rf.pretest.model \
		datasets/wikidata.features_reverted.general_and_context.nonbot.100k_2015.testing.tsv
	cut datasets/wikidata.features_reverted.general_and_context.nonbot.100k_2015.testing.tsv -f2- | \
	revscoring test_model \
		models/wikidata.reverted.general_and_context.rf.pretest.model \
		-s 'pr' -s 'roc' \
		-s 'recall_at_fpr(max_fpr=0.10)' \
		-s 'filter_rate_at_recall(min_recall=0.90)' \
		-s 'filter_rate_at_recall(min_recall=0.75)' \
		--label-type=bool > \
	models/wikidata.reverted.general_and_context.rf.model

models/wikidata.reverted.general_context_and_type.rf.pretest.model: \
		datasets/wikidata.features_reverted.general_context_and_type.nonbot.400k_2015.training.tsv
	cut datasets/wikidata.features_reverted.general_context_and_type.nonbot.400k_2015.training.tsv -f2- | \
	revscoring train_model \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.experimental.general_context_and_type \
		--version 0.0.1 \
		-p 'max_features="log2"' \
		-p 'criterion="entropy"' \
		-p 'min_samples_leaf=1' \
		-p 'n_estimators=80' \
		--balance-sample-weight \
		--center --scale \
		--label-type=bool > \
	models/wikidata.reverted.general_context_and_type.rf.pretest.model

models/wikidata.reverted.general_context_and_type.rf.model: \
		models/wikidata.reverted.general_context_and_type.rf.pretest.model \
		datasets/wikidata.features_reverted.general_context_and_type.nonbot.100k_2015.testing.tsv
	cut datasets/wikidata.features_reverted.general_context_and_type.nonbot.100k_2015.testing.tsv -f2- | \
	revscoring test_model \
		models/wikidata.reverted.general_context_and_type.rf.pretest.model \
		-s 'pr' -s 'roc' \
		-s 'recall_at_fpr(max_fpr=0.10)' \
		-s 'filter_rate_at_recall(min_recall=0.90)' \
		-s 'filter_rate_at_recall(min_recall=0.75)' \
		--label-type=bool > \
	models/wikidata.reverted.general_context_and_type.rf.model

models/wikidata.reverted.general_and_user.rf.pretest.model: \
		datasets/wikidata.features_reverted.general_and_user.nonbot.400k_2015.training.tsv
	cut datasets/wikidata.features_reverted.general_and_user.nonbot.400k_2015.training.tsv -f2- | \
	revscoring train_model \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.experimental.general_and_user \
		--version 0.0.1 \
		-p 'max_features="log2"' \
		-p 'criterion="entropy"' \
		-p 'min_samples_leaf=1' \
		-p 'n_estimators=80' \
		--balance-sample-weight \
		--center --scale \
		--label-type=bool > \
	models/wikidata.reverted.general_and_user.rf.pretest.model

models/wikidata.reverted.general_and_user.rf.model: \
		models/wikidata.reverted.general_and_user.rf.pretest.model \
		datasets/wikidata.features_reverted.general_and_user.nonbot.100k_2015.testing.tsv
	cut datasets/wikidata.features_reverted.general_and_user.nonbot.100k_2015.testing.tsv -f2- | \
	revscoring test_model \
		models/wikidata.reverted.general_and_user.rf.pretest.model \
		-s 'pr' -s 'roc' \
		-s 'recall_at_fpr(max_fpr=0.10)' \
		-s 'filter_rate_at_recall(min_recall=0.90)' \
		-s 'filter_rate_at_recall(min_recall=0.75)' \
		--label-type=bool > \
	models/wikidata.reverted.general_and_user.rf.model

models/wikidata.reverted.all.rf.pretest.model: \
		datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv
	cut datasets/wikidata.features_reverted.all.nonbot.400k_2015.training.tsv -f2- | \
	revscoring train_model \
		revscoring.scorer_models.RF \
		wb_vandalism.feature_lists.experimental.all \
		--version 0.0.1 \
		-p 'max_features="log2"' \
		-p 'criterion="entropy"' \
		-p 'min_samples_leaf=1' \
		-p 'n_estimators=80' \
		--balance-sample-weight \
		--center --scale \
		--label-type=bool > \
	models/wikidata.reverted.all.rf.pretest.model

models/wikidata.reverted.all.rf.model: \
		models/wikidata.reverted.all.rf.pretest.model \
		datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv
	cut datasets/wikidata.features_reverted.all.nonbot.100k_2015.testing.tsv -f2- | \
	revscoring test_model \
		models/wikidata.reverted.all.rf.pretest.model \
		-s 'pr' -s 'roc' \
		-s 'recall_at_fpr(max_fpr=0.10)' \
		-s 'filter_rate_at_recall(min_recall=0.90)' \
		-s 'filter_rate_at_recall(min_recall=0.75)' \
		--label-type=bool > \
	models/wikidata.reverted.all.rf.model
