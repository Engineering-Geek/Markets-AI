import pandas as pd
import numpy as np
import json
from datetime import datetime
from typing import List


class MarketUnit:
	# A Market Unit is a company, ForEx listing, commodity, etc. Specifically companies in this case, may change later
	def __init__(self, symbol: str, name: str, date_range: List[datetime]):
		self.symbol = symbol
		self.name = name


class MarketUnits:
	# Collection of MarketUnits
	def __init__(self, start_date: datetime, end_date: datetime):
		symbols, names = pd.read_csv("/src/data/data/nasdaq.csv")[["Symbol", "Name"]].to_numpy()

		# Collection of Market Units
		self.markets = [MarketUnit(symbol, name, [start_date, end_date]) for symbol, name in zip(symbols, names)]




