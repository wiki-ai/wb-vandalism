from revscoring import Feature
from revscoring.features import revision_oriented, temporal, wikibase, wikitext
from revscoring.features.modifiers import div, max, sub

general = [
    wikibase.revision.parent.claims,
    wikibase.revision.parent.properties,
    wikibase.revision.parent.aliases,
    wikibase.revision.parent.sources,
    wikibase.revision.parent.qualifiers,
    wikibase.revision.parent.badges,
    wikibase.revision.parent.labels,
    wikibase.revision.parent.sitelinks,
    wikibase.revision.parent.descriptions,
    wikibase.revision.diff.sitelinks_added,
    wikibase.revision.diff.sitelinks_removed,
    wikibase.revision.diff.sitelinks_changed,
    wikibase.revision.diff.labels_added,
    wikibase.revision.diff.labels_removed,
    wikibase.revision.diff.labels_changed,
    wikibase.revision.diff.descriptions_added,
    wikibase.revision.diff.descriptions_removed,
    wikibase.revision.diff.descriptions_changed,
    wikibase.revision.diff.aliases_added,
    wikibase.revision.diff.aliases_removed,
    wikibase.revision.diff.properties_added,
    wikibase.revision.diff.properties_removed,
    wikibase.revision.diff.properties_changed,
    wikibase.revision.diff.claims_added,
    wikibase.revision.diff.claims_removed,
    wikibase.revision.diff.claims_changed,
    wikibase.revision.diff.identifiers_changed,
    wikibase.revision.diff.sources_added,
    wikibase.revision.diff.sources_removed,
    wikibase.revision.diff.qualifiers_added,
    wikibase.revision.diff.qualifiers_removed,
    wikibase.revision.diff.badges_added,
    wikibase.revision.diff.badges_removed
]

user_rights = [
    revision_oriented.revision.user.in_group(
        {'bot'}, name="revision.user.is_bot"),
    revision_oriented.revision.user.in_group(
        {'checkuser', 'bureaucrat', 'oversight'},
        name="revision.user.has_advanced_rights"),
    revision_oriented.revision.user.in_group(
        {'sysop'}, name="revision.user.is_admin"),
    revision_oriented.revision.user.in_group(
        {'rollbacker', 'abusefilter', 'autopatrolled', 'reviewer'},
        name="revision.user.is_curator")
]

protected_user = [
    revision_oriented.revision.user.is_anon,
    temporal.revision.user.seconds_since_registration
]
