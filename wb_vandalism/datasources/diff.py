from revscoring.datasources.datasource import Datasource

from . import parent_revision, revision
from .util import DictDiffer

current_item = revision.item
past_item = parent_revision.item


def process_sitelinks(current_item, past_item):
    past_sitelinks = past_item.sitelinks if past_item is not None else {}
    differ = DictDiffer(current_item.sitelinks, past_sitelinks)
    return differ

sitelinks_differ = Datasource("diff.sitelinks_differ", process_sitelinks,
                              depends_on=[current_item, past_item])


def process_labels(current_item, past_item):
    past_labels = past_item.labels if past_item is not None else {}
    differ = DictDiffer(current_item.labels, past_labels)
    return differ

labels_differ = Datasource("diff.labels_differ", process_labels,
                            depends_on=[current_item, past_item])


def process_aliases(current_item, past_item):
    past_aliases = past_item.aliases if past_item is not None else {}
    differ = DictDiffer(current_item.aliases, past_aliases)
    return differ

aliases_differ = Datasource("diff.aliases_differ", process_aliases,
                            depends_on=[current_item, past_item])


def process_descriptions(current_item, past_item):
    past_descriptions = past_item.descriptions if past_item is not None else {}
    differ = DictDiffer(current_item.descriptions, past_descriptions)
    return differ

descriptions_differ = Datasource("diff.descriptions_differ",
                                 process_descriptions,
                                 depends_on=[current_item, past_item])


def process_claims(current_item, past_item):
    past_claims = past_item.claims if past_item is not None else {}
    differ = DictDiffer(current_item.claims, past_claims)
    return differ

claims_differ = Datasource("diff.claims_differ", process_claims,
                           depends_on=[current_item, past_item])


def process_badges(current_item, past_item):
    past_badges = past_item.badges if past_item is not None else {}
    differ = DictDiffer(current_item.badges, past_badges)
    return differ

badges_differ = Datasource("diff.badges_differ", process_badges,
                           depends_on=[current_item, past_item])


def process_added_claims(claims_differ, current_item, past_item):
    added_claims = []
    for p_number in claims_differ.added():
        added_claims += current_item.claims[p_number]
    for p_number in claims_differ.changed():
        parent_guids = [claim.snak for claim in past_item.claims[p_number]]
        for claim in current_item.claims[p_number]:
            if claim.snak not in parent_guids:
                added_claims.append(claim)

    return added_claims

added_claims = Datasource("diff.added_claims", process_added_claims,
                          depends_on=[claims_differ, current_item, past_item])


def process_removed_claims(claims_differ, current_item, past_item):
    removed_claims = []
    for p_number in claims_differ.removed():
        removed_claims += past_item.claims[p_number]
    for p_number in claims_differ.changed():
        current_guids = [claim.snak for claim in past_item.claims[p_number]]
        for claim in past_item.claims[p_number]:
                if claim.snak not in current_guids:
                    removed_claims.append(claim)

    return removed_claims

removed_claims = Datasource("diff.removed_claims", process_removed_claims,
                            depends_on=[claims_differ, current_item,
                                        past_item])


def process_changed_claims(claims_differ, current_item, past_item):
    changed_claims = []
    for p_number in claims_differ.changed():
        parent_guids = {claim.snak:claim
                        for claim in past_item.claims[p_number]}
        for claim in current_item.claims[p_number]:
            if claim.snak in parent_guids and \
               claim not in past_item.claims[p_number]:
                changed_claims.append(tuple([parent_guids[claim.snak], claim]))

    return changed_claims

changed_claims = Datasource("diff.changed_claims", process_changed_claims,
                            depends_on=[claims_differ, current_item,
                                        past_item])


def process_added_sources(changed_claims):
    added_sources = []
    for old_claim, new_claim in changed_claims:
        parent_guids = []
        for source in old_claim.sources:
            for p_number in source:
                parent_guids += [claim.hash for claim in source[p_number]]
        for source in new_claim.sources:
            for p_number in source:
                for claim in source[p_number]:
                    if claim.hash not in parent_guids:
                        added_sources.append(claim)
    return added_sources

added_sources = Datasource("diff.added_sources", process_added_sources,
                           depends_on=[changed_claims])


def process_removed_sources(changed_claims):
    removed_sources = []
    for old_claim, new_claim in changed_claims:
        current_guids = []
        for source in new_claim.sources:
            for p_number in source:
                current_guids += [claim.hash for claim in source[p_number]]
        for source in old_claim.sources:
            for p_number in source:
                for claim in source[p_number]:
                    if claim.hash not in current_guids:
                        removed_sources.append(claim)
    return removed_sources

removed_sources = Datasource("diff.removed_sources", process_removed_sources,
                             depends_on=[changed_claims])


def process_added_qualifiers(changed_claims):
    added_qualifiers = []
    for old_claim, new_claim in changed_claims:
        parent_guids = []
        for p_number in old_claim.qualifiers:
            parent_guids += [claim.hash
                             for claim in old_claim.qualifiers[p_number]]
        for p_number in new_claim.qualifiers:
            for claim in new_claim.qualifiers[p_number]:
                if claim.hash not in parent_guids:
                    added_qualifiers.append(claim)
    return added_qualifiers

added_qualifiers = Datasource("diff.added_qualifiers", process_added_qualifiers,
                              depends_on=[changed_claims])


def process_removed_qualifiers(changed_claims):
    removed_qualifiers = []
    for old_claim, new_claim in changed_claims:
        current_guids = []
        for p_number in new_claim.qualifiers:
            current_guids += [claim.hash
                              for claim in new_claim.qualifiers[p_number]]
        for p_number in old_claim.qualifiers:
            for claim in old_claim.qualifiers[p_number]:
                if claim.hash not in current_guids:
                    removed_qualifiers.append(claim)
    return removed_qualifiers

removed_qualifiers = Datasource("diff.removed_qualifiers",
                                process_removed_qualifiers,
                                depends_on=[changed_claims])
