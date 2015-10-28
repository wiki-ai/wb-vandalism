import re

from Levenshtein import ratio
from revscoring.features import Feature

from wb_vandalism.datasources import (parsed_parent_revision_text,
                                      parsed_revision_text)
from wb_vandalism.datasources.diff import (added_claims, added_qualifiers,
                                           added_sources, aliases_differ,
                                           badges_differ, changed_claims,
                                           descriptions_differ, labels_differ,
                                           removed_claims, removed_qualifiers,
                                           removed_sources, sitelinks_differ)

from .feature import has_property_changed

current_item = parsed_revision_text.item
past_item = parsed_parent_revision_text.item


def process_no_added_sitelinks(sitelinks_differ):
    return len(sitelinks_differ.added())

number_added_sitelinks = Feature(
    "number_added_sitelinks", process_no_added_sitelinks, returns=int,
    depends_on=[sitelinks_differ])


def process_no_removed_sitelinks(sitelinks_differ):
    return len(sitelinks_differ.removed())

number_removed_sitelinks = Feature(
    "number_removed_sitelinks", process_no_removed_sitelinks, returns=int,
    depends_on=[sitelinks_differ])


def process_no_changed_sitelinks(sitelinks_differ):
    return len(sitelinks_differ.changed())

number_changed_sitelinks = Feature(
    "number_changed_sitelinks", process_no_changed_sitelinks, returns=int,
    depends_on=[sitelinks_differ])


def process_no_added_labels(labels_differ):
    return len(labels_differ.added())

number_added_labels = Feature(
    "number_added_labels", process_no_added_labels, returns=int,
    depends_on=[labels_differ])


def process_no_removed_labels(labels_differ):
    return len(labels_differ.removed())

number_removed_labels = Feature(
    "number_removed_labels", process_no_removed_labels, returns=int,
    depends_on=[labels_differ])


def process_no_changed_labels(labels_differ):
    return len(labels_differ.changed())

number_changed_labels = Feature(
    "number_changed_labels", process_no_changed_labels, returns=int,
    depends_on=[labels_differ])


def process_no_added_descriptions(descriptions_differ):
    return len(descriptions_differ.added())

number_added_descriptions = Feature(
    "number_added_descriptions", process_no_added_descriptions, returns=int,
    depends_on=[descriptions_differ])


def process_no_removed_descriptions(descriptions_differ):
    return len(descriptions_differ.removed())

number_removed_descriptions = Feature(
    "number_removed_descriptions", process_no_removed_descriptions,
    returns=int, depends_on=[descriptions_differ])


def process_no_changed_descriptions(descriptions_differ):
    return len(descriptions_differ.changed())

number_changed_descriptions = Feature(
    "number_changed_descriptions", process_no_changed_descriptions,
    returns=int, depends_on=[descriptions_differ])


def process_no_added_aliases(aliases_differ, current_item, past_item):
    no_added = 0
    for lang in aliases_differ.added():
        no_added += len(current_item.aliases[lang])
    for lang in aliases_differ.changed():
        for alias in current_item.aliases[lang]:
            if alias not in past_item.aliases[lang]:
                no_added += 1
    return no_added

number_added_aliases = Feature(
    "number_added_aliases", process_no_added_aliases, returns=int,
    depends_on=[aliases_differ, current_item, past_item])


def process_no_removed_aliases(aliases_differ, current_item, past_item):
    no_removed = 0
    for lang in aliases_differ.removed():
        no_removed += len(past_item.aliases[lang])
    for lang in aliases_differ.changed():
        for alias in past_item.aliases[lang]:
            if alias not in current_item.aliases[lang]:
                no_removed += 1
    return no_removed

number_removed_aliases = Feature(
    "number_removed_aliases", process_no_removed_aliases, returns=int,
    depends_on=[aliases_differ, current_item, past_item])

# There is no need for changed aliases.


def process_no_added_claims(added_claims):
    return len(added_claims)

number_added_claims = Feature(
    "number_added_claims", process_no_added_claims, returns=int,
    depends_on=[added_claims])


def process_no_removed_claims(removed_claims):
    return len(removed_claims)

number_removed_claims = Feature(
    "number_removed_claims", process_no_removed_claims, returns=int,
    depends_on=[removed_claims])


def process_no_changed_claims(changed_claims):
    return len(changed_claims)

number_changed_claims = Feature(
    "number_changed_claims", process_no_changed_claims, returns=int,
    depends_on=[changed_claims])


def process_no_changed_identifiers(changed_claims):
    counter = 0
    for old, new in changed_claims:
        if isinstance(old.target, str):
            counter += 1
    return counter

number_changed_identifiers = Feature(
    "number_changed_identifiers", process_no_changed_identifiers, returns=int,
    depends_on=[changed_claims])


def process_en_label_touched(labels_differ):
    return 'en' in labels_differ.changed()

en_label_touched = Feature(
    "en_label_touched", process_en_label_touched, returns=bool,
    depends_on=[labels_differ])


P21_changed = has_property_changed('P21')

P27_changed = has_property_changed('P27')

P54_changed = has_property_changed('P54')

P569_changed = has_property_changed('P569')

P18_changed = has_property_changed('P18')

P109_changed = has_property_changed('P109')

P373_changed = has_property_changed('P373')

P856_changed = has_property_changed('P856')


def process_no_added_sources(added_sources):
    return len(added_sources)

number_added_sources = Feature(
    "number_added_sources", process_no_added_sources, returns=int,
    depends_on=[added_sources])


def process_no_removed_sources(removed_sources):
    return len(removed_sources)

number_removed_sources = Feature(
    "number_removed_sources", process_no_removed_sources, returns=int,
    depends_on=[removed_sources])


def process_no_added_qualifiers(added_qualifiers):
    return len(added_qualifiers)

number_added_qualifiers = Feature(
    "number_added_qualifiers", process_no_added_qualifiers, returns=int,
    depends_on=[added_qualifiers])


def process_no_removed_qualifiers(removed_qualifiers):
    return len(removed_qualifiers)

number_removed_qualifiers = Feature(
    "number_removed_qualifiers", process_no_removed_qualifiers, returns=int,
    depends_on=[removed_qualifiers])


def process_no_added_badges(badges_differ, current_item, past_item):
    no_added = 0
    for lang in badges_differ.added():
        no_added += len(current_item.badges[lang])
    for lang in badges_differ.changed():
        for badge in current_item.badges[lang]:
            if badge not in past_item.badges[lang]:
                no_added += 1
    return no_added

number_added_badges = Feature(
    "number_added_badges", process_no_added_badges, returns=int,
    depends_on=[badges_differ, current_item, past_item])


def process_no_removed_badges(badges_differ, current_item, past_item):
    no_removed = 0
    for lang in badges_differ.removed():
        no_removed += len(past_item.badges[lang])
    for lang in badges_differ.changed():
        for badge in past_item.badges[lang]:
            if badge not in current_item.badges[lang]:
                no_removed += 1
    return no_removed

number_removed_badges = Feature(
    "number_removed_badges", process_no_removed_badges, returns=int,
    depends_on=[badges_differ, current_item, past_item])

# There is no need for changed badges.


def process_mean_distance_desc(parent, current, differ):
    changed = differ.changed()
    if not changed:
        return 0.0
    distance = 0
    for lang in changed:
        distance += (
            1 - ratio(current.descriptions[lang], parent.descriptions[lang]))
    return distance / len(changed)

mean_distance_descriptions = Feature(
    "mean_distance_descriptions", process_mean_distance_desc, returns=float,
    depends_on=[past_item, current_item, descriptions_differ])


def process_mean_distance_labels(parent, current, differ):
    changed = differ.changed()
    if not changed:
        return 0.0
    distance = 0
    for lang in changed:
        distance += 1 - ratio(current.labels[lang], parent.labels[lang])
    return distance / len(changed)

mean_distance_labels = Feature(
    "mean_distance_labels", process_mean_distance_labels, returns=float,
    depends_on=[current_item, past_item, labels_differ])


def process_proportion_of_qid_added(current_item, past_item):
    re_qid = re.compile(r'Q\d{1,8}')
    current_item_qids = len(re.findall(re_qid, str(current_item.toJSON())))
    past_item_qids = len(re.findall(re_qid, str(past_item.toJSON())))
    return float(current_item_qids - past_item_qids) / \
        float(current_item_qids + 1)

# AF/38
proportion_of_qid_added = Feature(
    "proportion_of_qid_added", process_proportion_of_qid_added, returns=float,
    depends_on=[current_item, past_item])

# AF/8
LANGUAGE_REGEXES = (r"(a(frikaa?ns|lbanian?|lemanha|ng(lais|ol)|ra?b(e?|"
                    r"[ei]c|ian?|isc?h)|rmenian?|ssamese|azeri|z[eə]rba"
                    r"(ijani?|ycan(ca)?|yjan)|нглийский)|b(ahasa( (indonesia|"
                    r"jawa|malaysia|melayu))?|angla|as(k|qu)e|[aeo]ng[ao]?li|"
                    r"elarusian?|okmål|osanski|ra[sz]il(ian?)?|ritish( "
                    r"kannada)?|ulgarian?)|c(ebuano|hina|hinese( simplified)?"
                    r"|zech|roat([eo]|ian?)|atal[aà]n?|рпски|antonese)|[cč]"
                    r"(esky|e[sš]tina)|d(an(isc?h|sk)|e?uts?ch)|e(esti|ll[hi]"
                    r"nika|ng(els|le(ski|za)|lisc?h)|spa(g?[nñ]h?i?ol|nisc?h)"
                    r"|speranto|stonian|usk[ae]ra)|f(ilipino|innish|ran[cç]"
                    r"(ais|e|ez[ao])|ren[cs]h|arsi|rancese)|g(al(ego|ician)|"
                    r"uja?rati|ree(ce|k)|eorgian|erman[ay]?|ilaki)|h(ayeren|"
                    r"ebrew|indi|rvatski|ungar(y|ian))|i(celandic|ndian?|"
                    r"ndonesian?|ngl[eê]se?|ngilizce|tali(ano?|en(isch)?))|"
                    r"ja(pan(ese)?|vanese)|k(a(nn?ada|zakh)|hmer|o(rean?|"
                    r"sova)|urd[iî])|l(at(in[ao]?|vi(an?|e[sš]u))|ietuvi[uų]"
                    r"|ithuanian?)|m(a[ck]edon(ian?|ski)|agyar|alay(alam?|"
                    r"sian?)?|altese|andarin|arathi|elayu|ontenegro|ongol"
                    r"(ian?)|yanmar)|n(e(d|th)erlands?|epali|orw(ay|egian)|"
                    r"orsk( bokm[aå]l)?|ynorsk)|o(landese|dia)|p(ashto|"
                    r"ersi?an?|ol(n?isc?h|ski)|or?tugu?[eê]se?(( d[eo])? "
                    r"brasil(eiro)?| ?\(brasil\))?|unjabi)|r(om[aâi]ni?[aă]n?"
                    r"|um(ano|änisch)|ussi([ao]n?|sch))|s(anskrit|erbian|"
                    r"imple english|inha?la|lov(ak(ian?)?|enš?[cč]ina|"
                    r"en(e|ij?an?)|uomi)|erbisch|pagnolo?|panisc?h|rbeska|"
                    r"rpski|venska|c?wedisc?h|hqip)|t(a(galog|mil)|elugu|"
                    r"hai(land)?|i[eế]ng vi[eệ]t|[uü]rk([cç]e|isc?h|iş|ey))|"
                    r"u(rdu|zbek)|v(alencia(no?)?|ietnamese)|welsh|(англиис|"
                    r"[kк]алмыкс|[kк]азахс|немец|[pр]усс|[yу]збекс|"
                    r"татарс)кий( язык)??|עברית|[kкқ](аза[кқ]ша|ыргызча|"
                    r"ирилл)|українськ(а|ою)|б(еларуская|"
                    r"ългарски( език)?)|ελλ[ηι]"
                    r"νικ(ά|α)|ქართული|हिन्दी|ไทย|[mм]онгол(иа)?|([cс]рп|"
                    r"[mм]акедон)ски|العربية|日本語|한국(말|어)|‌हिनद़ि|"
                    r"বাংলা|ਪੰਜਾਬੀ|मराठी|ಕನ್ನಡ|اُردُو|தமிழ்|తెలుగు|ગુજરાતી|"
                    r"فارسی|پارسی|മലയാളം|پښتو|မြန်မာဘာသာ|中文(简体|繁體)?|"
                    r"中文（(简体?|繁體)）|简体|繁體)")
LANGUAGE_RE = re.compile(LANGUAGE_REGEXES)

def process_proportion_of_langauge_added(current_item, past_item):
    current_item_res = len(re.findall(LANGUAGE_RE, str(current_item.toJSON())))
    past_item_res = len(re.findall(LANGUAGE_RE, str(past_item.toJSON())))
    return float(current_item_res - past_item_res) / \
        float(current_item_res + 1)

# AF/38
proportion_of_langauge_added = Feature(
    "proportion_of_langauge_added", process_proportion_of_langauge_added,
    returns=float, depends_on=[current_item, past_item])


def process_proportion_of_links_added(current_item, past_item):
    re_qid = re.compile(r'https?\://|wwww\.')
    current_item_res = len(re.findall(re_qid, str(current_item.toJSON())))
    past_item_res = len(re.findall(re_qid, str(past_item.toJSON())))
    return float(current_item_res - past_item_res) / \
        float(current_item_res + 1)

proportion_of_links_added = Feature(
    "proportion_of_links_added", process_proportion_of_links_added,
    returns=float, depends_on=[current_item, past_item])
