from wb_vandalism.datasources.parsed_revision_text import item
from revscoring.features import Feature
from .feature import has_property_value
import pywikibase



def process_no_claims(item):
    no_claims = 0
    for property_name in item.claims:
        no_claims += len(item.claims[property_name])
    return no_claims

number_claims = Feature("number_claims", process_no_claims, returns=int,
                        depends_on=[item])


def process_no_aliases(item):
    no_aliases = 0
    for lang in item.aliases:
        no_aliases += len(item.aliases[lang])
    return no_aliases


number_aliases = Feature("number_aliases", process_no_aliases, returns=int,
                        depends_on=[item])


def process_no_sources(item):
    no_sources = 0
    for property_name in item.claims:
        for claim in item.claims[property_name]:
            no_sources += len(claim.sources)
    return no_sources


number_sources = Feature("number_sources", process_no_sources, returns=int,
                        depends_on=[item])


def process_no_qualifiers(item):
    no_qualifiers = 0
    for property_name in item.claims:
        for claim in item.claims[property_name]:
            no_qualifiers += len(claim.qualifiers)
    return no_qualifiers

number_qualifiers = Feature("number_qualifiers", process_no_qualifiers, returns=int,
                        depends_on=[item])


def process_no_badges(item):
    no_badges = 0
    for wiki in item.badges:
        no_badges += len(item.badges[wiki])
    return no_badges

number_badges = Feature("number_badges", process_no_badges, returns=int,
                        depends_on=[item])


def process_no_labels(item):
    return len(item.labels)

number_labels = Feature("number_labels", process_no_labels, returns=int,
                        depends_on=[item])


def process_no_sitelinks(item):
    return len(item.sitelinks)

number_sitelinks = Feature("number_sitelinks", process_no_sitelinks, returns=int,
                        depends_on=[item])


def process_no_descriptions(item):
    return len(item.descriptions)

number_descriptions = Feature("number_descriptions", process_no_descriptions, returns=int,
                        depends_on=[item])

is_human = has_property_value('P31', pywikibase.ItemPage('Q5'))


def process_is_blp(item):
    return 'P569' in item.claims and 'P570' not in item.claims

is_blp = Feature("is_blp", process_is_blp, returns=bool,
                        depends_on=[item])
