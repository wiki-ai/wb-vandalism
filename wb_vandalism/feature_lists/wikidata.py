from revscoring.features import user
from revscoring.features.modifiers import not_, log

from ..features import diff, revision


class properties:
    """
    Mapping of english descriptions to property identifiers
    """
    IMAGE = 'P18'
    SEX_OR_GENDER = 'P21'
    COUNTRY_OF_CITIZENSHIP = 'P27'
    INSTANCE_OF = 'P31'
    MEMBER_OF_SPORTS_TEAM = 'P54'
    SIGNATURE = 'P109'
    COMMONS_CATEGORY = 'P373'
    DATE_OF_BIRTH = 'P569'
    DATE_OF_DEATH = 'P570'
    OFFICIAL_WEBSITE = 'P856'


class items:
    """
    Mapping of english descriptions to item idenifiers
    """
    HUMAN = 'Q5'

# Comment features
is_client_delete = revision.comment_matches(r"^\/\* clientsitelink\-remove\:",
                                            name='revision.is_client_delete')
is_merge_into = revision.comment_matches(r"^\/\* wbmergeitems\-to\:",
                                         name='revision.is_merge_into')
is_merge_from = revision.comment_matches(r"^\/\* wbmergeitems\-from\:",
                                         name='revision.is_merge_from')
is_revert = \
    revision.comment_matches(r"^Reverted edits by \[\[Special\:Contributions",
                             name='revision.is_revert')
is_rollback = revision.comment_matches(r"^Undid revision ",
                                       name='revision.is_rollback')
is_restore = revision.comment_matches(r"^Restored revision ",
                                      name='revision.is_restore')
is_item_creation = revision.comment_matches(r"^\/\* wbsetentity \*\/",
                                            name='revision.is_item_creation')

# Properties changed
sex_or_gender_changed = \
    diff.property_changed(properties.SEX_OR_GENDER,
                          name='diff.sex_or_gender_changed')
country_of_citizenship_changed = \
    diff.property_changed(properties.COUNTRY_OF_CITIZENSHIP,
                          name='diff.country_of_citizenship_changed')
member_of_sports_team_changed = \
    diff.property_changed(properties.MEMBER_OF_SPORTS_TEAM,
                          name='diff.member_of_sports_team_changed')
date_of_birth_changed = \
    diff.property_changed(properties.DATE_OF_BIRTH,
                          name='diff.date_of_birth_changed')
image_changed = \
    diff.property_changed(properties.IMAGE,
                          name='diff.image_changed')
signature_changed = \
    diff.property_changed(properties.SIGNATURE,
                          name='diff.signature_changed')
commons_category_changed = \
    diff.property_changed(properties.COMMONS_CATEGORY,
                          name='diff.commons_category_changed')
official_website_changed = \
    diff.property_changed(properties.OFFICIAL_WEBSITE,
                          name='diff.official_website_changed')

# Status
is_human = \
    revision.has_property_value(properties.INSTANCE_OF, items.HUMAN,
                                name='revision.is_human')
has_birthday = \
    revision.has_property(properties.DATE_OF_BIRTH,
                          name='revision.has_birthday')
dead = \
    revision.has_property(properties.DATE_OF_BIRTH,
                          name='revision.dead')
is_blp = has_birthday.and_(not_(dead))


reverted = [
#    revscoring.features.diff.longest_repeated_char_added,
#    revscoring.features.diff.longest_token_added,
#    log(revscoring.features.diff.numeric_chars_added + 1),
#    log(revscoring.features.diff.numeric_chars_removed + 1),
#    revscoring.features.diff.proportion_of_chars_added,
#    revscoring.features.diff.proportion_of_chars_removed,
#    revscoring.features.diff.proportion_of_numeric_chars_added,
#    revscoring.features.diff.proportion_of_symbolic_chars_added,
#    revscoring.features.diff.proportion_of_uppercase_chars_added,
#    log(revscoring.features.diff.symbolic_chars_added + 1),
#    log(revscoring.features.diff.symbolic_chars_removed + 1),
#    log(revscoring.features.diff.uppercase_chars_added + 1),
#    log(revscoring.features.diff.uppercase_chars_removed + 1),
#    revscoring.features.diff.bytes_changed + 1,
#    revscoring.featuresdiff.bytes_changed_ratio,
#    page.is_content_namespace,
#    parent_revision.was_same_user,
    log(user.age + 1),
    diff.number_added_sitelinks,
    diff.number_removed_sitelinks,
    diff.number_changed_sitelinks,
    diff.number_added_labels,
    diff.number_removed_labels,
    diff.number_changed_labels,
    diff.number_added_descriptions,
    diff.number_removed_descriptions,
    diff.number_changed_descriptions,
    diff.number_added_aliases,
    diff.number_removed_aliases,
    diff.number_added_claims,
    diff.number_removed_claims,
    diff.number_changed_claims,
    diff.number_changed_identifiers,
    diff.en_label_touched,
    diff.number_added_sources,
    diff.number_removed_sources,
    diff.number_added_qualifiers,
    diff.number_removed_qualifiers,
    diff.number_added_badges,
    diff.number_removed_badges,
#    diff.mean_distance_descriptions,
#    diff.mean_distance_labels,
    diff.proportion_of_qid_added,
    diff.proportion_of_language_added,
    diff.proportion_of_links_added,
    is_client_delete,
    is_merge_into,
    is_merge_from,
    is_revert,
    is_rollback,
    is_restore,
    is_item_creation,
    sex_or_gender_changed,
    country_of_citizenship_changed,
    member_of_sports_team_changed,
    date_of_birth_changed,
    image_changed,
    signature_changed,
    commons_category_changed,
    official_website_changed,
    log(revision.number_claims + 1),
    log(revision.number_aliases + 1),
    log(revision.number_sources + 1),
    log(revision.number_qualifiers + 1),
    log(revision.number_badges + 1),
    log(revision.number_labels + 1),
    log(revision.number_sitelinks + 1),
    log(revision.number_descriptions + 1),
    is_human,
    is_blp,
    user.is_bot,
    user.is_anon,
]
