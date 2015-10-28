import json

import pywikibase
from revscoring.datasources import Datasource
from revscoring.datasources.parent_revision import text


def process_item(text):
    if text is None:
        return None
    else:
        item = pywikibase.ItemPage()
        item.get(content=json.loads(text))
        return item


item = Datasource("parsed_parent_revision.item", process_item, depends_on=[text])
