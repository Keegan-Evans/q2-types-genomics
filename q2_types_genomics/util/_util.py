import pandas as pd
from qiime2.plugin import ValidationError


def verify_features(features_present: list,
                     required_features: list) -> bool:

    missing_features = []

    for feature in required_features:
        if feature not in features_present:
            missing_features.append(feature)

    if missing_features:
        raise ValidationError(
                'Required features %s not found in input data'
                   % (missing_features,))

def find_feature_labels(data,
                        comment_character: str,
                        commented_labels: bool,
                        headerless: bool = False,
                        sep: str = '\t'):

    first_data_line = index_of_first_data_line(data,
                                               comment_character,
                                               commented_labels)

    labels = data[first_data_line - 1]
    labels = labels.split(sep)

    # remove comment character
    if commented_labels:
        labels = strip_comment_character(labels=labels,
                                 comment_character=comment_character)

    labels = [label.strip() for label in labels]
    return labels

def strip_comment_character(labels: list, comment_character: str):
    labels = [labels[0].lstrip(comment_character)] + labels[1:]
    return labels

def read_labels(data, label_line):
    data_list = list(data)
    print(data_list)

def index_of_first_data_line(data, comment_character, commented_labels):

    i = 0

    for i, line in enumerate(data, 0):

        if line[0] == comment_character:
            continue

        if commented_labels:
            return i
        else:
            return i + 1

def _subset_features(desired_features,
                     data_to_subset):

    data_features = find_feature_labels(data_to_subset)
    
    feature_indexes = _get_feature_index(desired_features,
                                         data_features)
    
def _get_feature_index(desired_features,
                       all_features):
    feature_indexes = []

    for i, label in enumerate(all_features, 0):
        if label in desired_features:
            feature_indexes.append(i)
