DELETE
FROM person p1 USING Person p2
WHERE p1.email = p2.email
  AND p1.id > p2.id; -- we can't use p1.id != p2.id because it would delete both rows.