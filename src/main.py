
from models.database import Session
from sqlalchemy import text


with Session() as session:
    rows = session.execute(text('SELECT * FROM players'))
    print(rows)