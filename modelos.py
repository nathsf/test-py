from pony.orm import *

db = Database()


class Alumno(db.Entity):
    id = PrimaryKey(int, auto=True)
    doc = Required(int)
    name = Required(str)

db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
