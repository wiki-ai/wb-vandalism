SELECT
  rev_id,
  rev_user = 0 AS anon_user,
  trusted.ug_user IS NOT NULL AS trusted_user,
  user.user_editcount IS NOT NULL AND user.user_editcount >= 1000 AS trusted_edits,
  rev_comment RLIKE '/\* clientsitelink-(remove|update):' AS client_edit,
  rev_comment RLIKE '/\* wbmergeitems-(to|from):' AS merge_edit
FROM revision
LEFT JOIN user ON rev_user = user_id
LEFT JOIN user_groups trusted ON
  trusted.ug_user = rev_user AND
  trusted.ug_group IN (
    'bureaucrat', 'checkuser', 'flood', 'ipblock-excempt',
    'oversight', 'property-creator', 'rollbacker', 'steward',
    'sysop', 'translationadmin', 'wikidata-staff'
  )
LEFT JOIN user_groups bot ON
  bot.ug_user = rev_user AND
  bot.ug_group = 'bot'
WHERE
  rev_timestamp BETWEEN "2015" AND "2016" AND
  bot.ug_user IS NULL
ORDER BY RAND()
LIMIT 1000000;
