import unittest

from revscoring.extractors import APIExtractor
from mw.api import Session

from wb_vandalism.features import revision
extractor = APIExtractor(Session("https://www.wikidata.org/w/api.php"))


class TestFeaturesRevision(unittest.TestCase):

    def test_claims(self):
        # Alan Turing, Turing Award
        human = list(extractor.extract([240706544, 248025762],
                                       [revision.is_human]))
        self.assertTrue(human[0][1][0])
        self.assertFalse(human[1][1][0])
        # Alan Turing, Aaron Halfaker
        features = list(extractor.extract(
            [240706544, 244168271],
            [revision.is_blp, revision.number_claims]))
        self.assertTrue(features[1][1][0])
        self.assertFalse(features[0][1][0])
        self.assertEqual(features[0][1][1], 62)
        self.assertEqual(features[1][1][1], 17)

    def test_sources_and_qualifiers(self):
        res = list(extractor.extract(
            240706544, [revision.number_sources, revision.number_qualifiers]))
        self.assertEqual(res[0], 30)
        self.assertEqual(res[1], 2)

    def test_context(self):
        res = list(extractor.extract(
            240706544, [revision.number_aliases,
                        revision.number_labels,
                        revision.number_descriptions]))
        self.assertEqual(res[0], 10)
        self.assertEqual(res[1], 125)
        self.assertEqual(res[2], 21)

    def test_sitelinks(self):
        sitelinks = list(extractor.extract(
            240706544, [revision.number_sitelinks]))
        self.assertEqual(sitelinks[0], 134)


if __name__ == '__main__':
    unittest.main()
