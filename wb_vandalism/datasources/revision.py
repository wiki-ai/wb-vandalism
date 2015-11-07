import json

from revscoring.datasources import Datasource
from revscoring.datasources.revision import metadata, text

import pywikibase


def process_item(text):
    item = pywikibase.ItemPage()
    item.get(content=json.loads(text))
    return item

item = Datasource("revision.item", process_item, depends_on=[text])


def process_comment(metadata):
    return metadata.comment

comment = Datasource("revision.comment", process_comment, depends_on=[metadata])
