from pprint import pprint as pp
import re

f = open("scorelib.txt", "r")
db = []
tmp = []
composers = {}

for line in f:
    if line == "\n":
        db.append(tmp)
        tmp = []
    else:
        tmp.append(line)
    

for token in db:
    if len(token) == 0:
        continue
    composer = token[1].split(":")[1].strip()
    composer = re.sub(r"\([^)]*\)", "", composer) # remove stuff in "()"
    composer = composer.strip()
    if composer in composers:
        composers[composer].append(token)
    else:
        composers[composer] = [token]
pp(composers)

for c in composers:
    print(c, ":", len(c))

#s2 = "Krieger, Johann (1649--1725); Purcell, Henry (1659--1695)"
#s1 = re.sub(r"\([^)]*\)", "", s2)
