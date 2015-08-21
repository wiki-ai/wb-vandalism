from wb_vandalism.datasources.parsed_revision_text import item
from revscoring.features import Feature


def process_no_claims(item):
    no_claims = 0
    for property_name in item.claims:
        no_claims += len(item.claims[property_name])
    return no_claims


number_claims = Feature("number_claims", process_no_claims, returns=int,
                        depends_on=[item])
