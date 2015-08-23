from revscoring.features import Modifier

from ..datasources import revision


class has_property_value(Modifier):
  def __init__(self, property, value):
    self.property = property
    self.value = value
    name = "has_property_value({0}, {1})".format(repr(property), repr(value))
    super().__init__(name, self._process, returns=bool,
                     depends_on=[revision.item])

  def _process(self, item):
    values = item.claims.get(self.property, [])
    return self.value in [i.target for i in values]
