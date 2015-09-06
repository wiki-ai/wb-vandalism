from wb_vandalism.datasources.diff import (
    sitelinks_differ, labels_differ, aliases_differ,
    descriptions_differ, added_claims,
    removed_claims, changed_claims,
    added_sources, removed_sources, changed_sources,
    added_qualifiers, removed_qualifiers, changed_qualifiers)
from wb_vandalism.datasources import (
    parsed_parent_revision_text, parsed_revision_text)

from revscoring.features import Feature
from .feature import has_property_changed

from Levenshtein import ratio

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

# There is no need for changed aliases.


def process_no_added_claims(added_claims):
    return len(added_claims)

number_added_claims = Feature("number_added_claims", process_no_added_claims, returns=int,
                        depends_on=[added_claims])


def process_no_removed_claims(removed_claims):
    return len(removed_claims)

number_removed_claims = Feature("number_removed_claims", process_no_removed_claims, returns=int,
                        depends_on=[removed_claims])


def process_no_changed_claims(changed_claims):
    return len(changed_claims)

number_changed_claims = Feature("number_changed_claims", process_no_changed_claims, returns=int,
                        depends_on=[changed_claims])


def process_no_changed_identifiers(changed_claims):
    counter = 0
    for old, new in changed_claims:
        if isinstance(old.target, str):
            counter += 1
    return counter

number_changed_identifiers = Feature("number_changed_identifiers", process_no_changed_identifiers, returns=int,
                        depends_on=[changed_claims])

def process_en_label_touched(labels_differ):
    return 'en' in labels_differ.changed()

en_label_touched = Feature("en_label_touched", process_en_label_touched, returns=bool,
                        depends_on=[labels_differ])


P21_changed = has_property_changed('P21')

P27_changed = has_property_changed('P27')

P54_changed = has_property_changed('P54')

P569_changed = has_property_changed('P569')

P18_changed = has_property_changed('P18')

P109_changed = has_property_changed('P109')

P373_changed = has_property_changed('P373')

P856_changed = has_property_changed('P856')

def process_no_added_sources(added_sources):
    return len(added_sources)

number_added_sources = Feature("number_added_sources", process_no_added_sources, returns=int,
                        depends_on=[added_sources])

def process_no_removed_sources(removed_sources):
    return len(removed_sources)

number_removed_sources = Feature("number_removed_sources", process_no_removed_sources, returns=int,
                        depends_on=[removed_sources])

def process_no_changed_sources(changed_sources):
    return len(changed_sources)

number_changed_sources = Feature("number_changed_sources", process_no_changed_sources, returns=int,
                        depends_on=[changed_sources])
def process_no_added_qualifiers(added_qualifiers):
    return len(added_qualifiers)

number_added_qualifiers = Feature("number_added_qualifiers", process_no_added_qualifiers, returns=int,
                        depends_on=[added_qualifiers])

def process_no_removed_qualifiers(removed_qualifiers):
    return len(removed_qualifiers)

number_removed_qualifiers = Feature("number_removed_qualifiers", process_no_removed_qualifiers, returns=int,
                        depends_on=[removed_qualifiers])

def process_no_changed_qualifiers(changed_qualifiers):
    return len(changed_qualifiers)

number_changed_qualifiers = Feature("number_changed_qualifiers", process_no_changed_qualifiers, returns=int,
                        depends_on=[changed_qualifiers])


def process_mean_distance_desc(parent, current, differ):
    changed = differ.changed()
    if not changed:
        return 0.0
    distance = 0
    for lang in changed:
        distance += 1 - ratio(current.descriptions[lang], parent.descriptions[lang])
    return distance / len(changed)

mean_distance_descriptions =  Feature("mean_distance_descriptions", process_mean_distance_desc, returns=float,
                        depends_on=[past_item, current_item, descriptions_differ])


def process_mean_distance_labels(parent, current, differ):
    changed = differ.changed()
    if not changed:
        return 0.0
    distance = 0
    for lang in changed:
        distance += 1 - ratio(current.labels[lang], parent.labels[lang])
    return distance / len(changed)

mean_distance_labels =  Feature("mean_distance_descriptions", process_mean_distance_labels, returns=float,
                        depends_on=[current_item, past_item, labels_differ])
