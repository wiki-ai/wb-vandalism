import pywikibase
import json
from revscoring.datasources import Datasource, revision_text


def process_item(revision_text):
    item = pywikibase.ItemPage()
    item.get(content=json.loads(revision_text))


item = Datasource("item", process_item, depends_on=[revision_text])
