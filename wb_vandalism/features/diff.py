from wb_vandalism.datasources.diff import (
    added_sitelinks, removed_sitelinks, changed_sitelinks,
    added_labels, removed_labels, changed_labels)
from revscoring.features import Feature

def process_no_added_sitelinks(added_sitelinks):
    return len(added_sitelinks)

number_added_sitelinks = Feature("number_added_sitelinks", process_no_added_sitelinks, returns=int,
                        depends_on=[added_sitelinks])

def process_no_removed_sitelinks(removed_sitelinks):
    return len(removed_sitelinks)

number_removed_sitelinks = Feature("number_removed_sitelinks", process_no_removed_sitelinks, returns=int,
                        depends_on=[removed_sitelinks])

def process_no_changed_sitelinks(changed_sitelinks):
    return len(changed_sitelinks)

number_changed_sitelinks = Feature("number_changed_sitelinks", process_no_changed_sitelinks, returns=int,
                        depends_on=[changed_sitelinks])

def process_no_added_labels(added_labels):
    return len(added_labels)

number_added_labels = Feature("number_added_labels", process_no_added_labels, returns=int,
                        depends_on=[added_labels])

def process_no_removed_labels(removed_labels):
    return len(removed_labels)

number_removed_labels = Feature("number_removed_labels", process_no_removed_labels, returns=int,
                        depends_on=[removed_labels])

def process_no_changed_labels(changed_labels):
    return len(changed_labels)

number_changed_labels = Feature("number_changed_labels", process_no_changed_labels, returns=int,
                        depends_on=[changed_labels])
