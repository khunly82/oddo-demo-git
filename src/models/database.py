import os

from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

load_dotenv()

class Base(DeclarativeBase, MappedAsDataclass):
    pass

engine = create_engine(os.getenv('DB_URL'), echo=True)

registrations = Table(
    "registrations",
    Base.metadata,
    Column("tournament_id", ForeignKey("tournaments.id")),
    Column("player_id", ForeignKey("players.id")),
)

