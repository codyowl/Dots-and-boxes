from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base
from game.models.games import Game

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    games_played = relationship("Game", back_populates="gamesplayed")
    level = Column(Integer,default=0)
    win_count = Column(Integer,default=0)
    total_games = Column(Integer, default=0)
    comments_received = Column(Integer, default=0)

    # helper function to get loss count
    def get_loss_count(self):
        return total_games - win_count