import pickle

from mwapi import Session
from nose.tools import eq_
from revscoring.extractors import APIExtractor

from wb_vandalism.features import revision

extractor = APIExtractor(Session("https://www.wikidata.org/w/api.php"))


def test_claims():
    # Alan Turing, Turing Award
    human = list(extractor.extract([240706544, 248025762],
                                   [revision.is_human]))
    assert human[0][1][0]
    assert not human[1][1][0]
    # Alan Turing, Aaron Halfaker
    features = list(extractor.extract(
        [240706544, 244168271],
        [revision.is_blp, revision.number_claims]))
    assert features[1][1][0]
    assert not features[0][1][0]
    eq_(features[0][1][1], 62)
    eq_(features[1][1][1], 17)

    eq_(revision.is_human,
        pickle.loads(pickle.dumps(revision.is_human)))


def test_sources_and_qualifiers():
    res = list(extractor.extract(
        240706544, [revision.number_sources, revision.number_qualifiers]))
    eq_(res[0], 30)
    eq_(res[1], 2)

    eq_(revision.number_sources,
        pickle.loads(pickle.dumps(revision.number_sources)))

    eq_(revision.number_qualifiers,
        pickle.loads(pickle.dumps(revision.number_qualifiers)))


def test_context():
    res = list(extractor.extract(
        240706544, [revision.number_aliases,
                    revision.number_labels,
                    revision.number_descriptions]))
    eq_(res[0], 10)
    eq_(res[1], 125)
    eq_(res[2], 21)

    eq_(revision.number_aliases,
        pickle.loads(pickle.dumps(revision.number_aliases)))

    eq_(revision.number_labels,
        pickle.loads(pickle.dumps(revision.number_labels)))

    eq_(revision.number_descriptions,
        pickle.loads(pickle.dumps(revision.number_descriptions)))


def test_sitelinks():
    sitelinks = list(extractor.extract(
        240706544, [revision.number_sitelinks]))
    eq_(sitelinks[0], 134)

    eq_(revision.number_sitelinks,
        pickle.loads(pickle.dumps(revision.number_sitelinks)))


def test_badges():
    badges = list(extractor.extract(
        240706544, [revision.number_badges]))
    eq_(badges[0], 4)

    eq_(revision.number_badges,
        pickle.loads(pickle.dumps(revision.number_badges)))
