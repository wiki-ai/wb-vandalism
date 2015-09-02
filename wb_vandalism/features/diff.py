from wb_vandalism.datasources.diff import (
    sitelinks_differ, labels_differ, aliases_differ,
    descriptions_differ, claims_differ)
from wb_vandalism.datasources import (
    parsed_parent_revision_text, parsed_revision_text)

from revscoring.features import Feature


current_item = parsed_revision_text.item
past_item = parsed_parent_revision_text.item


def process_no_added_sitelinks(sitelinks_differ):
    return len(sitelinks_differ.added())

number_added_sitelinks = Feature("number_added_sitelinks", process_no_added_sitelinks, returns=int,
                        depends_on=[sitelinks_differ])

def process_no_removed_sitelinks(removed_sitelinks):
    return len(sitelinks_differ.removed())

number_removed_sitelinks = Feature("number_removed_sitelinks", process_no_removed_sitelinks, returns=int,
                        depends_on=[sitelinks_differ])

def process_no_changed_sitelinks(sitelinks_differ):
    return len(sitelinks_differ.changed())

number_changed_sitelinks = Feature("number_changed_sitelinks", process_no_changed_sitelinks, returns=int,
                        depends_on=[sitelinks_differ])

def process_no_added_labels(labels_differ):
    return len(labels_differ.added())

number_added_labels = Feature("number_added_labels", process_no_added_labels, returns=int,
                        depends_on=[labels_differ])

def process_no_removed_labels(labels_differ):
    return len(labels_differ.removed())

number_removed_labels = Feature("number_removed_labels", process_no_removed_labels, returns=int,
                        depends_on=[labels_differ])

def process_no_changed_labels(labels_differ):
    return len(labels_differ.changed())

number_changed_labels = Feature("number_changed_labels", process_no_changed_labels, returns=int,
                        depends_on=[labels_differ])
def process_no_added_descriptions(descriptions_differ):
    return len(descriptions_differ.added())

number_added_descriptions = Feature("number_added_descriptions", process_no_added_descriptions, returns=int,
                        depends_on=[descriptions_differ])

def process_no_removed_descriptions(descriptions_differ):
    return len(descriptions_differ.removed())

number_removed_descriptions = Feature("number_removed_descriptions", process_no_removed_descriptions, returns=int,
                        depends_on=[descriptions_differ])

def process_no_changed_descriptions(descriptions_differ):
    return len(descriptions_differ.changed())

number_changed_descriptions = Feature("number_changed_descriptions", process_no_changed_descriptions, returns=int,
                        depends_on=[descriptions_differ])

def process_no_added_aliases(aliases_differ, current_item, past_item):
    no_added = 0
    for lang in aliases_differ.added():
        no_added += len(aliases_differ.added()[lang])
    for lang in aliases_differ.changed():
        for alias in aliases_differ.changed()[lang]:
            if alias in current_item.aliases[alias] and alias not in \
                    past_item.aliases[lang]:
                no_added += 1
    return no_added

number_added_aliases = Feature("number_added_aliases", process_no_added_aliases, returns=int,
                        depends_on=[aliases_differ, current_item, past_item])

def process_no_removed_aliases(aliases_differ, current_item, past_item):
    no_removed = 0
    for lang in aliases_differ.removed():
        no_removed += len(aliases_differ.removed()[lang])
    for lang in aliases_differ.changed():
        for alias in aliases_differ.changed()[lang]:
            if alias not in current_item.aliases[alias] and alias in \
                    past_item.aliases[lang]:
                no_removed += 1
    return no_removed

number_removed_aliases = Feature("number_removed_aliases", process_no_removed_aliases, returns=int,
                        depends_on=[aliases_differ, current_item, past_item])

# There is no need for changed aliases,
