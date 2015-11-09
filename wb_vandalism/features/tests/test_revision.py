import json
import os
import pickle

from nose.tools import eq_
from revscoring.dependencies import solve

from .. import revision
from ...datasources.revision import comment, item_doc

dir = os.path.dirname(os.path.realpath(__file__))
ALAN_TOURING = json.load(open(os.path.join(dir, "alan_touring.json")))
AARON_HALFAKER = json.load(open(os.path.join(dir, "aaron_halfaker.json")))


def test_comment_matches():
    has_foo = revision.comment_matches('.*foo.*')

    eq_(solve(has_foo, cache={comment: "Bar waffle hats banana"}),
        False)

    eq_(solve(has_foo, cache={comment: "Here comes the foobar!"}),
        True)

    eq_(has_foo,
        pickle.loads(pickle.dumps(has_foo)))


def test_has_property():
    has_p106 = revision.has_property('P106')
    has_p999 = revision.has_property('P999')

    eq_(solve(has_p106, cache={item_doc: AARON_HALFAKER}),
        True)

    eq_(solve(has_p999, cache={item_doc: AARON_HALFAKER}),
        False)

    eq_(has_p106,
        pickle.loads(pickle.dumps(has_p106)))


def test_has_property_value():
    has_p106_q82594 = revision.has_property_value('P106', "Q82594")
    has_p106_test = revision.has_property_value('P106', "Test")
    has_p999_foo = revision.has_property_value('P999', "Foo")

    eq_(solve(has_p106_q82594, cache={item_doc: AARON_HALFAKER}),
        True)

    eq_(solve(has_p106_test, cache={item_doc: AARON_HALFAKER}),
        False)

    eq_(solve(has_p999_foo, cache={item_doc: AARON_HALFAKER}),
        False)

    eq_(has_p106_q82594,
        pickle.loads(pickle.dumps(has_p106_q82594)))


def test_number_claims():

    eq_(solve(revision.number_claims, cache={item_doc: AARON_HALFAKER}),
        17)

    eq_(solve(revision.number_claims, cache={item_doc: ALAN_TOURING}),
        71)

    eq_(revision.number_claims,
        pickle.loads(pickle.dumps(revision.number_claims)))


def test_number_sources():
    eq_(solve(revision.number_sources, cache={item_doc: AARON_HALFAKER}),
        1)

    eq_(solve(revision.number_sources, cache={item_doc: ALAN_TOURING}),
        53)

    eq_(revision.number_sources,
        pickle.loads(pickle.dumps(revision.number_sources)))


def test_number_qualifiers():
    eq_(solve(revision.number_qualifiers, cache={item_doc: AARON_HALFAKER}),
        4)

    eq_(solve(revision.number_qualifiers, cache={item_doc: ALAN_TOURING}),
        6)

    eq_(revision.number_qualifiers,
        pickle.loads(pickle.dumps(revision.number_qualifiers)))


def test_number_aliases():
    eq_(solve(revision.number_aliases, cache={item_doc: AARON_HALFAKER}),
        0)

    eq_(solve(revision.number_aliases, cache={item_doc: ALAN_TOURING}),
        11)

    eq_(revision.number_aliases,
        pickle.loads(pickle.dumps(revision.number_aliases)))


def test_number_labels():
    eq_(solve(revision.number_labels, cache={item_doc: AARON_HALFAKER}),
        4)

    eq_(solve(revision.number_labels, cache={item_doc: ALAN_TOURING}),
        126)

    eq_(revision.number_labels,
        pickle.loads(pickle.dumps(revision.number_labels)))


def test_number_descriptions():
    eq_(solve(revision.number_descriptions, cache={item_doc: AARON_HALFAKER}),
        2)

    eq_(solve(revision.number_descriptions, cache={item_doc: ALAN_TOURING}),
        22)

    eq_(revision.number_descriptions,
        pickle.loads(pickle.dumps(revision.number_descriptions)))


def test_number_sitelinks():
    eq_(solve(revision.number_sitelinks, cache={item_doc: AARON_HALFAKER}),
        1)

    eq_(solve(revision.number_sitelinks, cache={item_doc: ALAN_TOURING}),
        134)

    eq_(revision.number_sitelinks,
        pickle.loads(pickle.dumps(revision.number_sitelinks)))


def test_number_badges():
    eq_(solve(revision.number_badges, cache={item_doc: AARON_HALFAKER}),
        0)

    eq_(solve(revision.number_badges, cache={item_doc: ALAN_TOURING}),
        5)

    eq_(revision.number_badges,
        pickle.loads(pickle.dumps(revision.number_badges)))
