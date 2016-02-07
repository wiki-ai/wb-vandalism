from .wikidata import (
    general_features, user_related_features, features_to_catch_certain_type,
    features_to_reduce_false_positives)

general = general_features
general_and_type = general_features + features_to_catch_certain_type
general_type_and_feedback = (
    general_features + features_to_catch_certain_type +
    features_to_reduce_false_positives)

general_and_user = general_features + user_related_features

# All features
all = (general_features + features_to_catch_certain_type +
       features_to_reduce_false_positives + user_related_features)
