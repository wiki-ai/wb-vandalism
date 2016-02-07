from . import wikibase, wikidata

general = wikibase.general
general_and_context = wikibase.general + wikidata.context
general_context_and_type = wikibase.general + wikidata.context + \
                           wikidata.edit_type

general_and_user = wikibase.general + wikibase.user_rights + \
                   wikibase.protected_user

# All features
all = wikibase.general + wikidata.context + wikidata.edit_type + \
      wikibase.user_rights + wikibase.protected_user
