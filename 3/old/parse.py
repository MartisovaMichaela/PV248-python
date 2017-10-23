from pprint import pprint as pp
import re

f = open("scorelib.txt", "r")
db = []
tmp = []
author_score = {}

for line in f:
    if line == "\n":
        db.append(tmp)
        tmp = []
    else:
        tmp.append(line)


"""
for score_info in db[7:10]: #[7:10] for testing purposes
    if len(score_info) == 0:
        continue
    composers = score_info[1].split(":")[1].strip().split(";")
    #print(composers)

    for composer in composers:
        # strip stuff in () from composer name
        #composer = re.sub(r"\([^)]*\)", "", composer) # remove stuff in "()"
        if composer in author_score:
            author_score[composer].append(score_info)
        else:
            author_score[composer] = [score_info]
"""

##pp(author_score)
pp(db)

#for c in composers:
#    print(c, ":", len(c))

#s2 = "Krieger, Johann (1649--1725); Purcell, Henry (1659--1695)"
#s1 = re.sub(r"\([^)]*\)", "", s2)
