import json
import os
import pickle

from nose.tools import eq_
from revscoring.dependencies import solve
from wb_vandalism.feature_lists import wikidata
from wb_vandalism.datasources.revision import comment


def test_comment_features():
    # /* wbmergeitems-to:0||Q928543 */ The Distributed Game #1: Merge items
    # Undid revision 1448592 by [[Special:Contributions/Sk!dbot|Sk!dbot]] ([[User talk:Sk!dbot|talk]])
    #
    merge_to_comment = "/* wbmergeitems-to:0||Q928543 */ "
    merge_from_comment = "/* wbmergeitems-from:0||Q928543 */ "
    client_delete_comment = "/* clientsitelink-remove:1||enwiki */ Boris Kok"
    client_move_comment = "/* clientsitelink-update:0|uk|uk:A|uk:B *"
    rollback_comment = "Undid revision 1448592 by [[Special:Contributions/"
    restore_comment = "Restored revision 123456"
    revert_comment = "Reverted edits by [[Special:Contributions/"
    item_creation_comment = "/* wbeditentity-create:0| */"

    eq_(solve(wikidata.is_merge_into,
              cache={comment: merge_to_comment}), True)
    eq_(solve(wikidata.is_merge_into,
              cache={comment: merge_from_comment}), False)

    eq_(solve(wikidata.is_merge_from,
              cache={comment: merge_from_comment}), True)
    eq_(solve(wikidata.is_merge_from,
              cache={comment: merge_to_comment}), False)

    eq_(solve(wikidata.is_client_delete,
              cache={comment: client_delete_comment}), True)
    eq_(solve(wikidata.is_client_delete,
              cache={comment: client_move_comment}), False)

    eq_(solve(wikidata.is_client_move,
              cache={comment: client_move_comment}), True)
    eq_(solve(wikidata.is_client_move,
              cache={comment: client_delete_comment}), False)

    eq_(solve(wikidata.is_revert, cache={comment: revert_comment}), True)
    eq_(solve(wikidata.is_revert, cache={comment: rollback_comment}), False)

    eq_(solve(wikidata.is_rollback, cache={comment: rollback_comment}), True)
    eq_(solve(wikidata.is_rollback, cache={comment: revert_comment}), False)

    eq_(solve(wikidata.is_restore, cache={comment: restore_comment}), True)
    eq_(solve(wikidata.is_restore,
              cache={comment: item_creation_comment}), False)

    eq_(solve(wikidata.is_item_creation,
              cache={comment: item_creation_comment}), True)
    eq_(solve(wikidata.is_item_creation,
              cache={comment: revert_comment}), False)
