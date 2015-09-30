import unittest

from revscoring.extractors import APIExtractor
from mwapi import Session

from wb_vandalism.features import diff
extractor = APIExtractor(Session("https://www.wikidata.org/w/api.php"))


class TestFeaturesDiff(unittest.TestCase):

    def test_sitelinks(self):
        sitelinks = list(extractor.extract(
            [240706544, 236855267, 251864785, 239687610],
            [diff.number_added_sitelinks,
             diff.number_changed_sitelinks,
             diff.number_removed_sitelinks,]))
        self.assertEqual(sitelinks[0][1][0], 1)
        self.assertEqual(sitelinks[0][1][1], 0)
        self.assertEqual(sitelinks[0][1][2], 0)

        self.assertEqual(sitelinks[1][1][0], 0)
        self.assertEqual(sitelinks[1][1][1], 1)
        self.assertEqual(sitelinks[1][1][2], 0)

        self.assertEqual(sitelinks[2][1][0], 0)
        self.assertEqual(sitelinks[2][1][1], 0)
        self.assertEqual(sitelinks[2][1][2], 1)

        self.assertEqual(sitelinks[3][1][0], 0)
        self.assertEqual(sitelinks[3][1][1], 0)
        self.assertEqual(sitelinks[3][1][2], 0)

    def test_labels(self):
        labels = list(extractor.extract(
            [122000849, 125669106, 218755228, 120548238],
            [diff.number_added_labels,
             diff.number_changed_labels,
             diff.number_removed_labels,]))
        self.assertEqual(labels[0][1][0], 3)
        self.assertEqual(labels[0][1][1], 0)
        self.assertEqual(labels[0][1][2], 0)

        self.assertEqual(labels[1][1][0], 0)
        self.assertEqual(labels[1][1][1], 0)
        self.assertEqual(labels[1][1][2], 5)

        self.assertEqual(labels[2][1][0], 0)
        self.assertEqual(labels[2][1][1], 1)
        self.assertEqual(labels[2][1][2], 0)

        self.assertEqual(labels[3][1][0], 0)
        self.assertEqual(labels[3][1][1], 0)
        self.assertEqual(labels[3][1][2], 0)

    def test_descriptions(self):
        descriptions = list(extractor.extract(
            [120350776, 254330860, 190113221, 247209411],
            [diff.number_added_descriptions,
             diff.number_changed_descriptions,
             diff.number_removed_descriptions,]))
        self.assertEqual(descriptions[0][1][0], 2)
        self.assertEqual(descriptions[0][1][1], 0)
        self.assertEqual(descriptions[0][1][2], 0)

        self.assertEqual(descriptions[1][1][0], 0)
        self.assertEqual(descriptions[1][1][1], 0)
        self.assertEqual(descriptions[1][1][2], 1)

        self.assertEqual(descriptions[2][1][0], 0)
        self.assertEqual(descriptions[2][1][1], 1)
        self.assertEqual(descriptions[2][1][2], 0)

        self.assertEqual(descriptions[3][1][0], 0)
        self.assertEqual(descriptions[3][1][1], 0)
        self.assertEqual(descriptions[3][1][2], 0)

    def test_aliases(self):
        aliases = list(extractor.extract(
            [310052, 254332219, 185753253],
            [diff.number_added_aliases,
             diff.number_removed_aliases,]))
        self.assertEqual(aliases[0][1][0], 1)
        self.assertEqual(aliases[0][1][1], 0)

        self.assertEqual(aliases[1][1][0], 0)
        self.assertEqual(aliases[1][1][1], 1)

        self.assertEqual(aliases[2][1][0], 0)
        self.assertEqual(aliases[2][1][1], 0)

    def test_claims(self):
        claims = list(extractor.extract(
            [247177183, 218756354, 247170322, 218755228],
            [diff.number_added_claims,
             diff.number_changed_claims,
             diff.number_removed_claims,]))
        self.assertEqual(claims[0][1][0], 1)
        self.assertEqual(claims[0][1][1], 0)
        self.assertEqual(claims[0][1][2], 0)

        self.assertEqual(claims[1][1][0], 0)
        self.assertEqual(claims[1][1][1], 0)
        self.assertEqual(claims[1][1][2], 1)

        self.assertEqual(claims[2][1][0], 0)
        self.assertEqual(claims[2][1][1], 1)
        self.assertEqual(claims[2][1][2], 0)

        self.assertEqual(claims[3][1][0], 0)
        self.assertEqual(claims[3][1][1], 0)
        self.assertEqual(claims[3][1][2], 0)



if __name__ == '__main__':
    unittest.main()
