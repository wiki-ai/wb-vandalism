
from revscoring.datasources import Datasource
from revscoring.datasources.revision import metadata


def process_comment(metadata):
    return metadata.comment


comment = Datasource("revision_metadata.comment", process_comment, depends_on=[metadata])
