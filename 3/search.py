#!/usr/bin/env python3

import sys
import json
import sqlite3

if len(sys.argv) != 2:
    print("Need search string as an input!")
    sys.exit(-1)


conn = sqlite3.connect("scorelib.dat")
cursor = conn.cursor()
string = sys.argv[1]
print("searching for %s\n" % string)

s = "select person.name, score_author.score \
    from person \
    join score_author on person.id = score_author.composer \
    where person.name like \"%%%s%%\"" % string

res = cursor.execute(s)
auth_score = []
for i in res:
    score_id = i[1]
    composer = i[0]
    auth_score.append([score_id, composer])

for i in auth_score:
    print("\n", i[1])
    ss = "select * from score where id = %s" % i[0]
    score = cursor.execute(ss)
    print(score.fetchone())
