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

    def test_claims2(self):
        claims = list(extractor.extract(
            [202163969, 120548238, 254825767, 247168960],
            [diff.number_changed_identifiers,
             diff.P21_changed,
             diff.P27_changed,
             diff.P569_changed,
             diff.P18_changed]))
        self.assertEqual(claims[0][1][0], 1)
        self.assertEqual(claims[1][1][0], 0)
        self.assertEqual(claims[2][1][0], 0)
        self.assertEqual(claims[3][1][0], 0)

        self.assertTrue(claims[1][1][1])
        self.assertFalse(claims[0][1][1])
        self.assertFalse(claims[2][1][1])
        self.assertFalse(claims[3][1][1])

        self.assertTrue(claims[2][1][2])
        self.assertFalse(claims[0][1][2])
        self.assertFalse(claims[1][1][2])
        self.assertFalse(claims[3][1][2])

        self.assertTrue(claims[3][1][3])
        self.assertFalse(claims[0][1][3])
        self.assertFalse(claims[1][1][3])
        self.assertFalse(claims[2][1][3])

        self.assertTrue(claims[0][1][4])
        self.assertFalse(claims[1][1][4])
        self.assertFalse(claims[2][1][4])
        self.assertFalse(claims[3][1][4])

    def test_sources(self):
        sources = list(extractor.extract(
            [66760648, 254947152, 254947223, 254825767],
            [diff.number_added_sources,
             diff.number_removed_sources,]))
        self.assertEqual(sources[0][1][0], 1)
        self.assertEqual(sources[0][1][1], 0)

        self.assertEqual(sources[1][1][0], 0)
        self.assertEqual(sources[1][1][1], 1)

        self.assertEqual(sources[2][1][0], 1)
        self.assertEqual(sources[2][1][1], 1)

        self.assertEqual(sources[3][1][0], 0)
        self.assertEqual(sources[3][1][1], 0)

    def test_qualifiers(self):
        qualifiers = list(extractor.extract(
            [247171078, 254967043, 254966946, 254825767],
            [diff.number_added_qualifiers,
             diff.number_removed_qualifiers,]))
        self.assertEqual(qualifiers[0][1][0], 1)
        self.assertEqual(qualifiers[0][1][1], 0)

        self.assertEqual(qualifiers[1][1][0], 0)
        self.assertEqual(qualifiers[1][1][1], 1)

        self.assertEqual(qualifiers[2][1][0], 1)
        self.assertEqual(qualifiers[2][1][1], 1)

        self.assertEqual(qualifiers[3][1][0], 0)
        self.assertEqual(qualifiers[3][1][1], 0)

    def test_badges(self):
        badges = list(extractor.extract(
            [154279576, 254993634, 254987433, 236855267],
            [diff.number_added_badges,
             diff.number_removed_badges,]))
        self.assertEqual(badges[0][1][0], 1)
        self.assertEqual(badges[0][1][1], 0)

        self.assertEqual(badges[1][1][0], 0)
        self.assertEqual(badges[1][1][1], 1)

        self.assertEqual(badges[2][1][0], 1)
        self.assertEqual(badges[2][1][1], 1)

        self.assertEqual(badges[3][1][0], 0)
        self.assertEqual(badges[3][1][1], 0)

    def test_mean_distance(self):
        distances = list(extractor.extract(
            [194250199, 190113221, 172464444, 88485789],
            [diff.mean_distance_descriptions,
             diff.mean_distance_labels]))
        self.assertEqual(distances[0][1][0], 0)
        self.assertEqual(distances[0][1][1], 0)

        self.assertEqual(distances[1][1][0], 0.4736842105263158)
        self.assertEqual(distances[1][1][1], 0)

        self.assertEqual(distances[2][1][0], 0)
        self.assertEqual(distances[2][1][1], 0)

        self.assertEqual(distances[3][1][0], 0)
        self.assertEqual(distances[3][1][1], 0.4545454545454546)


if __name__ == '__main__':
    unittest.main()
