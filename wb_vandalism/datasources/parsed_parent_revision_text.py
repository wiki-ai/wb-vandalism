import pywikibase
import json
from revscoring.datasources import Datasource
from revscoring.datasources.parent_revision import text


def process_item(text):
    item = pywikibase.ItemPage()
    item.get(content=json.loads(text))
    return item


item = Datasource("item", process_item, depends_on=[text])
