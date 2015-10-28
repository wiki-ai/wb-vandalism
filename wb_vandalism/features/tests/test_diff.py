import pickle

from mwapi import Session
from nose.tools import eq_
from revscoring.extractors import APIExtractor

from wb_vandalism.features import diff

extractor = APIExtractor(Session("https://www.wikidata.org/w/api.php"))


def test_sitelinks():
    sitelinks = list(extractor.extract(
        [240706544, 236855267, 251864785, 239687610],
        [diff.number_added_sitelinks,
         diff.number_changed_sitelinks,
         diff.number_removed_sitelinks]))
    eq_(sitelinks[0][1][0], 1)
    eq_(sitelinks[0][1][1], 0)
    eq_(sitelinks[0][1][2], 0)

    eq_(sitelinks[1][1][0], 0)
    eq_(sitelinks[1][1][1], 1)
    eq_(sitelinks[1][1][2], 0)

    eq_(sitelinks[2][1][0], 0)
    eq_(sitelinks[2][1][1], 0)
    eq_(sitelinks[2][1][2], 1)

    eq_(sitelinks[3][1][0], 0)
    eq_(sitelinks[3][1][1], 0)
    eq_(sitelinks[3][1][2], 0)

    eq_(diff.number_added_sitelinks,
        pickle.loads(pickle.dumps(diff.number_added_sitelinks)))

    eq_(diff.number_changed_sitelinks,
        pickle.loads(pickle.dumps(diff.number_changed_sitelinks)))

    eq_(diff.number_removed_sitelinks,
        pickle.loads(pickle.dumps(diff.number_removed_sitelinks)))

def test_labels():
    labels = list(extractor.extract(
        [122000849, 125669106, 218755228, 120548238],
        [diff.number_added_labels,
         diff.number_changed_labels,
         diff.number_removed_labels]))
    eq_(labels[0][1][0], 3)
    eq_(labels[0][1][1], 0)
    eq_(labels[0][1][2], 0)

    eq_(labels[1][1][0], 0)
    eq_(labels[1][1][1], 0)
    eq_(labels[1][1][2], 5)

    eq_(labels[2][1][0], 0)
    eq_(labels[2][1][1], 1)
    eq_(labels[2][1][2], 0)

    eq_(labels[3][1][0], 0)
    eq_(labels[3][1][1], 0)
    eq_(labels[3][1][2], 0)

    eq_(diff.number_added_labels,
        pickle.loads(pickle.dumps(diff.number_added_labels)))

    eq_(diff.number_changed_labels,
        pickle.loads(pickle.dumps(diff.number_changed_labels)))

    eq_(diff.number_removed_labels,
        pickle.loads(pickle.dumps(diff.number_removed_labels)))

def test_descriptions():
    descriptions = list(extractor.extract(
        [120350776, 254330860, 190113221, 247209411],
        [diff.number_added_descriptions,
         diff.number_changed_descriptions,
         diff.number_removed_descriptions]))
    eq_(descriptions[0][1][0], 2)
    eq_(descriptions[0][1][1], 0)
    eq_(descriptions[0][1][2], 0)

    eq_(descriptions[1][1][0], 0)
    eq_(descriptions[1][1][1], 0)
    eq_(descriptions[1][1][2], 1)

    eq_(descriptions[2][1][0], 0)
    eq_(descriptions[2][1][1], 1)
    eq_(descriptions[2][1][2], 0)

    eq_(descriptions[3][1][0], 0)
    eq_(descriptions[3][1][1], 0)
    eq_(descriptions[3][1][2], 0)

    eq_(diff.number_added_descriptions,
        pickle.loads(pickle.dumps(diff.number_added_descriptions)))

    eq_(diff.number_changed_descriptions,
        pickle.loads(pickle.dumps(diff.number_changed_descriptions)))

    eq_(diff.number_removed_descriptions,
        pickle.loads(pickle.dumps(diff.number_removed_descriptions)))

def test_aliases():
    aliases = list(extractor.extract(
        [310052, 254332219, 185753253],
        [diff.number_added_aliases,
         diff.number_removed_aliases,]))
    eq_(aliases[0][1][0], 1)
    eq_(aliases[0][1][1], 0)

    eq_(aliases[1][1][0], 0)
    eq_(aliases[1][1][1], 1)

    eq_(aliases[2][1][0], 0)
    eq_(aliases[2][1][1], 0)

    eq_(diff.number_added_aliases,
        pickle.loads(pickle.dumps(diff.number_added_aliases)))

    eq_(diff.number_removed_aliases,
        pickle.loads(pickle.dumps(diff.number_removed_aliases)))

def test_claims():
    claims = list(extractor.extract(
        [247177183, 218756354, 247170322, 218755228],
        [diff.number_added_claims,
         diff.number_changed_claims,
         diff.number_removed_claims]))
    eq_(claims[0][1][0], 1)
    eq_(claims[0][1][1], 0)
    eq_(claims[0][1][2], 0)

    eq_(claims[1][1][0], 0)
    eq_(claims[1][1][1], 0)
    eq_(claims[1][1][2], 1)

    eq_(claims[2][1][0], 0)
    eq_(claims[2][1][1], 1)
    eq_(claims[2][1][2], 0)

    eq_(claims[3][1][0], 0)
    eq_(claims[3][1][1], 0)
    eq_(claims[3][1][2], 0)

    eq_(diff.number_added_claims,
        pickle.loads(pickle.dumps(diff.number_added_claims)))

    eq_(diff.number_changed_claims,
        pickle.loads(pickle.dumps(diff.number_changed_claims)))

    eq_(diff.number_removed_claims,
        pickle.loads(pickle.dumps(diff.number_removed_claims)))

def test_claims2():
    claims = list(extractor.extract(
        [202163969, 120548238, 254825767, 247168960],
        [diff.number_changed_identifiers,
         diff.P21_changed,
         diff.P27_changed,
         diff.P569_changed,
         diff.P18_changed]))
    eq_(claims[0][1][0], 1)
    eq_(claims[1][1][0], 0)
    eq_(claims[2][1][0], 0)
    eq_(claims[3][1][0], 0)

    assert claims[1][1][1]
    assert not claims[0][1][1]
    assert not claims[2][1][1]
    assert not claims[3][1][1]

    assert claims[2][1][2]
    assert not claims[0][1][2]
    assert not claims[1][1][2]
    assert not claims[3][1][2]

    assert claims[3][1][3]
    assert not claims[0][1][3]
    assert not claims[1][1][3]
    assert not claims[2][1][3]

    assert claims[0][1][4]
    assert not claims[1][1][4]
    assert not claims[2][1][4]
    assert not claims[3][1][4]

    eq_(diff.number_changed_identifiers,
        pickle.loads(pickle.dumps(diff.number_changed_identifiers)))

    eq_(diff.P21_changed,
        pickle.loads(pickle.dumps(diff.P21_changed)))

    eq_(diff.P27_changed,
        pickle.loads(pickle.dumps(diff.P27_changed)))

    eq_(diff.P569_changed,
        pickle.loads(pickle.dumps(diff.P569_changed)))

    eq_(diff.P18_changed,
        pickle.loads(pickle.dumps(diff.P18_changed)))


def test_sources():
    sources = list(extractor.extract(
        [66760648, 254947152, 254947223, 254825767],
        [diff.number_added_sources,
         diff.number_removed_sources]))
    eq_(sources[0][1][0], 1)
    eq_(sources[0][1][1], 0)

    eq_(sources[1][1][0], 0)
    eq_(sources[1][1][1], 1)

    eq_(sources[2][1][0], 1)
    eq_(sources[2][1][1], 1)

    eq_(sources[3][1][0], 0)
    eq_(sources[3][1][1], 0)

    eq_(diff.number_added_sources,
        pickle.loads(pickle.dumps(diff.number_added_sources)))

    eq_(diff.number_removed_sources,
        pickle.loads(pickle.dumps(diff.number_removed_sources)))


def test_qualifiers():
    qualifiers = list(extractor.extract(
        [247171078, 254967043, 254966946, 254825767],
        [diff.number_added_qualifiers,
         diff.number_removed_qualifiers]))
    eq_(qualifiers[0][1][0], 1)
    eq_(qualifiers[0][1][1], 0)

    eq_(qualifiers[1][1][0], 0)
    eq_(qualifiers[1][1][1], 1)

    eq_(qualifiers[2][1][0], 1)
    eq_(qualifiers[2][1][1], 1)

    eq_(qualifiers[3][1][0], 0)
    eq_(qualifiers[3][1][1], 0)

    eq_(diff.number_added_qualifiers,
        pickle.loads(pickle.dumps(diff.number_added_qualifiers)))

    eq_(diff.number_removed_qualifiers,
        pickle.loads(pickle.dumps(diff.number_removed_qualifiers)))


def test_badges():
    badges = list(extractor.extract(
        [154279576, 254993634, 254987433, 236855267],
        [diff.number_added_badges,
         diff.number_removed_badges]))
    eq_(badges[0][1][0], 1)
    eq_(badges[0][1][1], 0)

    eq_(badges[1][1][0], 0)
    eq_(badges[1][1][1], 1)

    eq_(badges[2][1][0], 1)
    eq_(badges[2][1][1], 1)

    eq_(badges[3][1][0], 0)
    eq_(badges[3][1][1], 0)

    eq_(diff.number_added_badges,
        pickle.loads(pickle.dumps(diff.number_added_badges)))

    eq_(diff.number_removed_badges,
        pickle.loads(pickle.dumps(diff.number_removed_badges)))


def test_mean_distance():
    distances = list(extractor.extract(
        [194250199, 190113221, 172464444, 88485789],
        [diff.mean_distance_descriptions,
         diff.mean_distance_labels]))
    eq_(distances[0][1][0], 0)
    eq_(distances[0][1][1], 0)

    eq_(distances[1][1][0], 0.4736842105263158)
    eq_(distances[1][1][1], 0)

    eq_(distances[2][1][0], 0)
    eq_(distances[2][1][1], 0)

    eq_(distances[3][1][0], 0)
    eq_(distances[3][1][1], 0.4545454545454546)

    eq_(diff.mean_distance_descriptions,
        pickle.loads(pickle.dumps(diff.mean_distance_descriptions)))

    eq_(diff.mean_distance_labels,
        pickle.loads(pickle.dumps(diff.mean_distance_labels)))


def test_languages():
    distances = list(extractor.extract(
        [194250199, 190113221, 172464444, 264056515],
        [diff.proportion_of_langauge_added]))
    eq_(distances[0][1][0], 0)

    eq_(distances[1][1][0], 0)

    eq_(distances[2][1][0], 0)

    eq_(distances[3][1][0], 0.5)

    eq_(diff.proportion_of_langauge_added,
        pickle.loads(pickle.dumps(diff.proportion_of_langauge_added)))
