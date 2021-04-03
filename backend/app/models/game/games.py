from sqlalchemy import Boolean, Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
import enum

import datetime

class GameTypeEnum(enum.IntEnum):
	small_map = 1
	medium_map = 2
	large_map = 3

class MatchStatus(enum.IntEnum):
	win = 1
	draw = 2
	lost = 3	

class Game:
	__tablename__ = 'games'
	id = Column(Integer, primary_key=True, index=True)
	game_type = Column(Enum(GameTypeEnum))
	created_date = Column(DateTime, default=datetime.datetime.now) 
	match_status = Column(Enum(MatchStatus))
	is_active = Column(Boolean(), default=True)