import json

from revscoring.datasources import Datasource
from revscoring.datasources.revision import metadata, text

import pywikibase


def process_item_doc(text):
    return json.loads(text)

item_doc = Datasource("revision.item_doc", process_item_doc,
                       depends_on=[text])


def process_item(item_doc):
    item = pywikibase.ItemPage()
    item.get(content=item_doc)
    return item

item = Datasource("revision.item", process_item,
                  depends_on=[item_doc])


def process_comment(metadata):
    return metadata.comment

comment = Datasource("revision.comment", process_comment, depends_on=[metadata])
