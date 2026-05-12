from models.database import Base
from enum import Flag, Enum, auto
from sqlalchemy import Enum as EnumSQL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

class TournamentStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    FINISHED = 'FINISHED'

class TournamentCategory(Flag):
    JUNIOR = auto() # 1
    SENIOR = auto() # 2
    VETERAN = auto() # 4

class Tournament(Base):
    __tablename__ = 'tournaments'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    loacation: Mapped[str] = mapped_column()
    min_players: Mapped[int] = mapped_column()
    max_players: Mapped[int] = mapped_column()
    min_elo: Mapped[int] = mapped_column()
    max_elo: Mapped[int] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    categories: Mapped[int] = mapped_column()
    status: Mapped[TournamentStatus] = mapped_column(EnumSQL(TournamentStatus, name='tournament_status'), default=TournamentStatus.PENDING)
    woman_only: Mapped[bool] = mapped_column(default=False)
    current_round: Mapped[int] = mapped_column(default=0)
