import unittest

from revscoring.extractors import APIExtractor
from mw.api import Session

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


if __name__ == '__main__':
    unittest.main()
