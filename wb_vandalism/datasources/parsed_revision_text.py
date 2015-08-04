import pywikibase
from revscoring.datasources import Datasource, revision_text


def process_item(revision_text):
    return pywikibase.ItemPage(content=revision_text)


item = Datasource("item", process_item, depends_on=[revision_text])
