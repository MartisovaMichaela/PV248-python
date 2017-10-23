import re # regular expressions
import sqlite3
import parse

from pprint import pprint as pp

# This is a base class for objects that represent database items. It implements
# the store() method in terms of fetch_id and do_store, which need to be
# implemented in every derived class (see Person below for an example).

class DBItem:
    def __init__( self, conn ):
        self.id = None
        self.cursor = conn.cursor()

    def store( self ):
        self.fetch_id()
        if ( self.id is None ):
            self.do_store()
            self.cursor.execute( "select last_insert_rowid()" )
            self.id = self.cursor.fetchone()[ 0 ]

# Example of a class which represents a single row of a single database table.
# This is a very simple example, since it does not contain any references to
# other objects.

class Person( DBItem ):
    def __init__( self, conn, string ):
        super().__init__( conn )
        self.born = self.died = None
        self.name = re.sub( '\([0-9/+-]+\)', '', string ).strip()
        # NB. The code below was part of the exercise (extracting years of birth & death
        # from the string).
        m = re.search( "([0-9]+)--([0-9]+)", string )
        if not m is None:
            self.born = int( m.group( 1 ) )
            self.died = int( m.group( 2 ) )

    # TODO: Update born/died if the name is already present but has null values for
    # those fields. We assume that names are unique (not entirely true in practice).
    def fetch_id( self ):
        self.cursor.execute( "select id from person where name = ?", (self.name,) )

        # NB. The below lines had a bug in the original version of
        # scorelib-import.py (which however only becomes relevant when you
        # start implementing the Score class).
        res = self.cursor.fetchone()
        if not res is None: # TODO born/died update should be done inside this if
            self.id = res[ 0 ]

    def do_store( self ):
        print ("storing '%s'" % self.name)
        # NB. Part of the exercise was adding the born/died columns to the below query.
        self.cursor.execute( "insert into person (name, born, died) values (?, ?, ?)",
                             ( self.name, self.born, self.died ) )

class Score(DBItem):
    def __init__(self, conn, genre, key, incpipit, year):
        super().__init__(conn)
        self.genre = genre
        self.key = key
        self.incipit = incipit
        self.year = year

    def fetch_id( self ):
        self.cursor.execute( "select id from score where \
                              genre = ? and key = ? and incipit = ? \
                              and year = ?", \
                              (self.genre, self.key, self.incipit, self.year,))
        res = self.cursor.fetchone()
        if not res is None:
            self.id = res[0]

    def do_store(self):
        print("storing '%s, %s, %s, %s'" % (self.genre, self.key, self.incipit,\
                                            self.year))
        self.cursor.execute("insert into score (genre, key, incipit, year) \
                             values (?, ?, ?, ?)",
                            (self.genre, self.key, self.incipit, self.year))

class ScoreAuthor(DBItem):
    def __init__(self, conn, author_id, score_id):
        super().__init__(conn)
        self.author_id = author_id
        self.score_id = score_id

    def fetch_id( self ):
        self.cursor.execute( "select id from score_author where \
                              score = ? and composer = ?", \
                              (self.score_id, self.author_id,))
        res = self.cursor.fetchone()
        if not res is None:
            self.id = res[0]

    def do_store(self):
        print("storing '%s, %s'" % (self.score_id, self.author_id, ))
        self.cursor.execute("insert into score_author (score, composer) \
                             values (?, ?)",
                            (self.score_id, self.author_id))

# NB. Everything below this line was part of the exercise.

conn = sqlite3.connect("scorelib.dat")

for entry in parse.db:
    composer = ""
    editor = ""
    genre = ""
    key = ""
    incipit = ""
    year = ""
    for line in entry:
        if line.startswith("Composer"):
            composer = line.split(":")[1].strip()
        elif line.startswith("Editor"):
            editor = line.split(":")[1].strip()
        elif line.startswith("Genre"):
            genre = line.split(":")[1].strip()
        elif line.startswith("Key"):
            key = line.split(":")[1].strip()
        elif line.startswith("Incipit"):
            incipit = line.split(":")[1].strip()
        elif line.startswith("Composition Year"):
            year = line.split(":")[1].strip()
    #print(genre, key, incipit, year)
    p = Person(conn, composer)
    p.store()
    pp(p.id)
    e = Person(conn, editor)
    e.store()
    pp(e.id)
    s = Score(conn, genre, key, incipit, year)
    s.store()
    pp(s.id)

    sa = ScoreAuthor(conn, p.id, s.id)
    sa.store()
    pp(sa.id)

conn.commit()
