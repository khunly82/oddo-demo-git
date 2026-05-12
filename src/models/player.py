from models.database import Base
from sqlalchemy import Enum as EnumSQL
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from enum import Enum

class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    birth_date: Mapped[date] = mapped_column()
    elo: Mapped[int] = mapped_column(default=1200)
    gender: Mapped[Gender] = mapped_column(EnumSQL(Gender, name='gender'), nullable=True, default=None)
