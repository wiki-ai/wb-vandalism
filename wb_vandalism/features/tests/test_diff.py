import json
import os
import pickle

from nose.tools import eq_
from revscoring.dependencies import solve

from .. import diff
from ...datasources.parent_revision import item_doc as parent_item_doc
from ...datasources.revision import item_doc

pwd = os.path.dirname(os.path.realpath(__file__))
ALAN_TOURING = json.load(open(os.path.join(pwd, "alan_touring.json")))
ALAN_TOURING_OLD = json.load(open(os.path.join(pwd, "alan_touring.old.json")))
AARON_HALFAKER = json.load(open(os.path.join(pwd, "aaron_halfaker.json")))


def test_property_changed():
    p69_changed = diff.property_changed("P69")
    p9999_changed = diff.property_changed("P9999")

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(p69_changed, cache=cache), True)
    eq_(solve(p9999_changed, cache=cache), False)

    eq_(p69_changed, pickle.loads(pickle.dumps(p69_changed)))


def test_sitelinks():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_sitelinks, cache=cache), 0)
    eq_(solve(diff.number_changed_sitelinks, cache=cache), 1)
    eq_(solve(diff.number_removed_sitelinks, cache=cache), 133)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_sitelinks, cache=cache), 26)
    eq_(solve(diff.number_changed_sitelinks, cache=cache), 2)
    eq_(solve(diff.number_removed_sitelinks, cache=cache), 0)

    eq_(diff.number_added_sitelinks,
        pickle.loads(pickle.dumps(diff.number_added_sitelinks)))
    eq_(diff.number_changed_sitelinks,
        pickle.loads(pickle.dumps(diff.number_changed_sitelinks)))
    eq_(diff.number_removed_sitelinks,
        pickle.loads(pickle.dumps(diff.number_removed_sitelinks)))


def test_labels():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_labels, cache=cache), 0)
    eq_(solve(diff.number_changed_labels, cache=cache), 4)
    eq_(solve(diff.number_removed_labels, cache=cache), 122)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_labels, cache=cache), 18)
    eq_(solve(diff.number_changed_labels, cache=cache), 2)
    eq_(solve(diff.number_removed_labels, cache=cache), 6)

    eq_(diff.number_added_labels,
        pickle.loads(pickle.dumps(diff.number_added_labels)))
    eq_(diff.number_changed_labels,
        pickle.loads(pickle.dumps(diff.number_changed_labels)))
    eq_(diff.number_removed_labels,
        pickle.loads(pickle.dumps(diff.number_removed_labels)))


def test_descriptions():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_descriptions, cache=cache), 1)
    eq_(solve(diff.number_changed_descriptions, cache=cache), 1)
    eq_(solve(diff.number_removed_descriptions, cache=cache), 21)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_descriptions, cache=cache), 15)
    eq_(solve(diff.number_changed_descriptions, cache=cache), 1)
    eq_(solve(diff.number_removed_descriptions, cache=cache), 0)

    eq_(diff.number_added_descriptions,
        pickle.loads(pickle.dumps(diff.number_added_descriptions)))
    eq_(diff.number_changed_descriptions,
        pickle.loads(pickle.dumps(diff.number_changed_descriptions)))
    eq_(diff.number_removed_descriptions,
        pickle.loads(pickle.dumps(diff.number_removed_descriptions)))


def test_aliases():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_aliases, cache=cache), 0)
    eq_(solve(diff.number_removed_aliases, cache=cache), 11)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_aliases, cache=cache), 2)
    eq_(solve(diff.number_removed_aliases, cache=cache), 0)

    eq_(diff.number_added_aliases,
        pickle.loads(pickle.dumps(diff.number_added_aliases)))
    eq_(diff.number_removed_aliases,
        pickle.loads(pickle.dumps(diff.number_removed_aliases)))


def test_claims():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_claims, cache=cache), 17)
    eq_(solve(diff.number_changed_claims, cache=cache), 0)
    eq_(solve(diff.number_removed_claims, cache=cache), 51)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_claims, cache=cache), 46)
    eq_(solve(diff.number_changed_claims, cache=cache), 10)
    eq_(solve(diff.number_removed_claims, cache=cache), 2)

    eq_(diff.number_added_claims,
        pickle.loads(pickle.dumps(diff.number_added_claims)))
    eq_(diff.number_changed_claims,
        pickle.loads(pickle.dumps(diff.number_changed_claims)))
    eq_(diff.number_removed_claims,
        pickle.loads(pickle.dumps(diff.number_removed_claims)))


def test_identifiers():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_changed_identifiers, cache=cache), 0)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_changed_identifiers, cache=cache), 1)

    eq_(diff.number_changed_identifiers,
        pickle.loads(pickle.dumps(diff.number_changed_identifiers)))


def test_sources():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_sources, cache=cache), 0)
    eq_(solve(diff.number_removed_sources, cache=cache), 0)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_sources, cache=cache), 26)
    eq_(solve(diff.number_removed_sources, cache=cache), 1)

    eq_(diff.number_added_sources,
        pickle.loads(pickle.dumps(diff.number_added_sources)))
    eq_(diff.number_removed_sources,
        pickle.loads(pickle.dumps(diff.number_removed_sources)))


def test_qualifiers():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_qualifiers, cache=cache), 0)
    eq_(solve(diff.number_removed_qualifiers, cache=cache), 0)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_qualifiers, cache=cache), 0)
    eq_(solve(diff.number_removed_qualifiers, cache=cache), 0)

    eq_(diff.number_added_qualifiers,
        pickle.loads(pickle.dumps(diff.number_added_qualifiers)))
    eq_(diff.number_removed_qualifiers,
        pickle.loads(pickle.dumps(diff.number_removed_qualifiers)))


def test_badges():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.number_added_badges, cache=cache), 0)
    eq_(solve(diff.number_removed_badges, cache=cache), 5)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.number_added_badges, cache=cache), 5)
    eq_(solve(diff.number_removed_badges, cache=cache), 0)

    eq_(diff.number_added_badges,
        pickle.loads(pickle.dumps(diff.number_added_badges)))
    eq_(diff.number_removed_badges,
        pickle.loads(pickle.dumps(diff.number_removed_badges)))


def test_mean_distance():
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.mean_distance_descriptions, cache=cache),
              0.47916666666666663)
    eq_(solve(diff.mean_distance_labels, cache=cache), 0.6)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.mean_distance_descriptions, cache=cache),
        0.01754385964912286)
    eq_(solve(diff.mean_distance_labels, cache=cache),
        0.44727272727272727)

    eq_(diff.mean_distance_descriptions,
        pickle.loads(pickle.dumps(diff.mean_distance_descriptions)))
    eq_(diff.mean_distance_labels,
        pickle.loads(pickle.dumps(diff.mean_distance_labels)))


def test_languages():
    print(dir(diff))
    cache = {item_doc: AARON_HALFAKER, parent_item_doc: ALAN_TOURING}
    eq_(solve(diff.proportion_of_language_added, cache=cache), 0)

    cache = {item_doc: ALAN_TOURING, parent_item_doc: ALAN_TOURING_OLD}
    eq_(solve(diff.proportion_of_language_added, cache=cache), 0.0)

    eq_(diff.proportion_of_language_added,
        pickle.loads(pickle.dumps(diff.proportion_of_language_added)))
