from database.get_db import Database

def get_db():
    db = Database()
    try:
        yield db
    finally:
        del db
