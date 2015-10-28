import json

import pywikibase
from revscoring.datasources import Datasource
from revscoring.datasources.revision import text


def process_item(text):
    item = pywikibase.ItemPage()
    item.get(content=json.loads(text))
    return item


item = Datasource("parsed_revision.item", process_item, depends_on=[text])
