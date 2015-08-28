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


def process_added_sitelinks(current_item, past_item):
    differ = DictDiffer(current_item.sitelinks, past_item.sitelinks)
    return differ.added()

added_sitelinks = Datasource("diff.added_sitelinks", process_added_sitelinks,
                             depends_on=[current_item, past_item])

def process_removed_sitelinks(current_item, past_item):
    differ = DictDiffer(current_item.sitelinks, past_item.sitelinks)
    return differ.removed()

removed_sitelinks = Datasource("diff.removed_sitelinks", process_removed_sitelinks,
                               depends_on=[current_item, past_item])

def process_changed_sitelinks(current_item, past_item):
    differ = DictDiffer(current_item.sitelinks, past_item.sitelinks)
    return differ.changed()

changed_sitelinks = Datasource("diff.changed_sitelinks", process_changed_sitelinks,
                               depends_on=[current_item, past_item])

def process_added_labels(current_item, past_item):
    differ = DictDiffer(current_item.labels, past_item.labels)
    return differ.added()

added_labels = Datasource("diff.added_labels", process_added_labels,
                          depends_on=[current_item, past_item])

def process_removed_labels(current_item, past_item):
    differ = DictDiffer(current_item.labels, past_item.labels)
    return differ.removed()

removed_labels = Datasource("diff.removed_labels", process_removed_labels,
                            depends_on=[current_item, past_item])

def process_changed_labels(current_item, past_item):
    differ = DictDiffer(current_item.labels, past_item.labels)
    return differ.changed()

changed_labels = Datasource("diff.changed_labels", process_changed_labels,
                            depends_on=[current_item, past_item])
