from .wikidata import (
    general_features, user_related_features, features_to_catch_certain_type,
    features_to_reduce_false_positives)

first_model = general_features
second_model = general_features + features_to_catch_certain_type
third_model = (
    general_features + features_to_catch_certain_type +
    features_to_reduce_false_positives)

forth_model = general_features + user_related_features

# All features
fifth_model = third_model + user_related_features
