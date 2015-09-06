from revscoring.features.feature import Modifier
from ..datasources import parsed_revision_text
from ..datasources.diff import changed_claims

from Levenshtein import ratio

class has_property_value(Modifier):
    def __init__(self, property, value):
        self.property = property
        self.value = value
        name = "has_property_value({0}, {1})".format(repr(property), repr(value))
        super().__init__(name, self._process, returns=bool,
                         depends_on=[parsed_revision_text.item])

    def _process(self, item):
        values = item.claims.get(self.property, [])
        return self.value in [i.target for i in values]


class has_property_changed(Modifier):
    def __init__(self, property):
        self.property = property
        name = "has_property_changed({0})".format(repr(property))
        super().__init__(name, self._process, returns=bool,
                         depends_on=[changed_claims])

    def _process(self, changed_claims):
        return self.property in [claims[0].id for claims in changed_claims]
