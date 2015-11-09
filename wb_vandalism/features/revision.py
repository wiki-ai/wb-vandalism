import re

from revscoring.features import Feature
from wb_vandalism.datasources.revision import comment, item


class comment_matches(Feature):
    """
    Returns True if the revision comment matches a regular expression

    :Parameters:
        regex : `str`
            A regular expression to apply to the comment
        name : `str`
            A name to associate with the feature.  If not set, the feature's
            name will be 'comment_matches(<regex>)'
    """
    def __init__(self, regex, name=None):
        self.regex = regex
        if name is None:
            name = "comment_matches({0})".format(repr(regex))
        super().__init__(name, self._process, returns=bool,
                         depends_on=[comment])

    def _process(self, comment):
        return bool(re.match(self.regex, comment))


class has_property(Feature):
    """
    Returns True if the specified property exists


    :Parameters:
        property : `str`
            The name of a property (usually preceeded by "P")
        name : `str`
            A name to associate with the feature.  If not set, the feature's
            name will be 'has_property(<property>)'
    """
    def __init__(self, property, name=None):
        self.property = property
        if name is None:
            name = "has_property({0})" \
                   .format(repr(property))
        super().__init__(name, self._process, returns=bool,
                         depends_on=[item])

    def _process(self, item):
        return self.property in item.claims


class has_property_value(Feature):
    """
    Returns True if the specified property matches the provided value.

    :Parameters:
        property : `str`
            The name of a property (usually preceeded by "P")
        value : `mixed`
            The value to match
        name : `str`
            A name to associate with the feature.  If not set, the feature's
            name will be 'has_property_value(<property>, <value>)'
    """
    def __init__(self, property, value, name=None):
        self.property = property
        self.value = value
        if name is None:
            name = "has_property_value({0}, {1})" \
                   .format(repr(property), repr(value))
        super().__init__(name, self._process, returns=bool,
                         depends_on=[item])

    def _process(self, item):
        values = item.claims.get(self.property, [])
        return self.value in (i.target for i in values)


def process_no_claims(item):
    no_claims = 0
    for property_name in item.claims:
        no_claims += len(item.claims[property_name])
    return no_claims

number_claims = Feature("number_claims", process_no_claims, returns=int,
                        depends_on=[item])


def process_no_aliases(item):
    no_aliases = 0
    for lang in item.aliases:
        no_aliases += len(item.aliases[lang])
    return no_aliases

number_aliases = Feature("number_aliases", process_no_aliases, returns=int,
                         depends_on=[item])


def process_no_sources(item):
    no_sources = 0
    for property_name in item.claims:
        for claim in item.claims[property_name]:
            no_sources += len(claim.sources)
    return no_sources

number_sources = Feature("number_sources", process_no_sources, returns=int,
                         depends_on=[item])


def process_no_qualifiers(item):
    no_qualifiers = 0
    for property_name in item.claims:
        for claim in item.claims[property_name]:
            no_qualifiers += len(claim.qualifiers)
    return no_qualifiers

number_qualifiers = Feature("number_qualifiers", process_no_qualifiers,
                            returns=int, depends_on=[item])


def process_no_badges(item):
    no_badges = 0
    for wiki in item.badges:
        no_badges += len(item.badges[wiki])
    return no_badges

number_badges = Feature("number_badges", process_no_badges, returns=int,
                        depends_on=[item])


def process_no_labels(item):
    return len(item.labels)

number_labels = Feature("number_labels", process_no_labels, returns=int,
                        depends_on=[item])


def process_no_sitelinks(item):
    return len(item.sitelinks)

number_sitelinks = Feature("number_sitelinks", process_no_sitelinks,
                           returns=int, depends_on=[item])


def process_no_descriptions(item):
    return len(item.descriptions)

number_descriptions = Feature("number_descriptions", process_no_descriptions,
                              returns=int, depends_on=[item])
