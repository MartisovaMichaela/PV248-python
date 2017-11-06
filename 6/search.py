#!/usr/bin/env python3

import sqlite3

def search(term):
    conn = sqlite3.connect("scorelib.dat")
    cursor = conn.cursor()
    string = term
    findings = []

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
        ss = "select * from score where id = %s" % i[0]
        score = cursor.execute(ss)
        #print(i[1])
        #print(score.fetchone())
        findings.append([i[1], score.fetchone()])
    return findings
