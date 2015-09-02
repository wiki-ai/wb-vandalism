from . import parsed_parent_revision_text, parsed_revision_text
from revscoring.datasources.datasource import Datasource

current_item = parsed_revision_text.item
past_item = parsed_parent_revision_text.item

# Copied from
# http://stackoverflow.com/questions/1165352/calculate-difference-in-keys-contained-in-two-python-dictionaries
class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)

    def added(self):
        return self.set_current - self.intersect

    def removed(self):
        return self.set_past - self.intersect

    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])


def process_sitelinks(current_item, past_item):
    differ = DictDiffer(current_item.sitelinks, past_item.sitelinks)
    return differ

sitelinks_differ = Datasource("diff.sitelinks_differ", process_sitelinks,
                             depends_on=[current_item, past_item])


def process_labels(current_item, past_item):
    differ = DictDiffer(current_item.labels, past_item.labels)
    return differ

labels_differ = Datasource("diff.labels_differ", process_labels,
                            depends_on=[current_item, past_item])


def process_aliases(current_item, past_item):
    differ = DictDiffer(current_item.aliases, past_item.aliases)
    return differ

aliases_differ = Datasource("diff.aliases_differ", process_aliases,
                          depends_on=[current_item, past_item])


def process_descriptions(current_item, past_item):
    differ = DictDiffer(current_item.descriptions, past_item.descriptions)
    return differ

descriptions_differ = Datasource("diff.descriptions_differ", process_descriptions,
                          depends_on=[current_item, past_item])


def process_claims(current_item, past_item):
    differ = DictDiffer(current_item.claims, past_item.claims)
    return differ

claims_differ = Datasource("diff.claims_differ", process_claims,
                          depends_on=[current_item, past_item])
