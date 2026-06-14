import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("plstats(1-35)2025-26.csv")

def name(data):
	name = data["player_name"].values[0]
	return name

def goals(data):
	goals = data["goals"].values[0]
	return goals

def xg(data):
	xg = data["expectedGoals"].values[0]
	return xg


def assists(data):
	assists = data["assists"].values[0]
	return assists

def percentile(plrdata,pos,stat):
	posdata = df[df["position"]==pos]
	name = plrdata["player_name"]
	stats = posdata.groupby("player_name")[stat].mean()
	percen = stats.rank(pct=True) * 100
	plrpercen = percen[name]
	return plrpercen.item()


def chooseplr():
	plrstrarr = df["player_name"].unique()
	while  True:
		plyr = input("Choose a Player: ")
		plrdata = df[df["player_name"].str.contains(plyr, case=False, na=False)]
		for data, typed_name in [(plrdata, plyr)]:
			unique_plyr = data["player_name"].unique()
			if len(unique_plyr) == 0:
				print(f"Error: {plyr} not found. Try Again.")
			elif len(unique_plyr) > 1:
				print(f"Error: {plyr} matched multiple players: {unique_plyr.tolist()}. Be more speciffic.")
			elif len(unique_plyr) == 1:
				return plrdata
def choose1plr():
	plrstrarr = df["player_name"].unique()
	while  True:
		plyr = input("Choose 1st Player: ")
		plrdata = df[df["player_name"].str.contains(plyr, case=False, na=False)]
		for data, typed_name in [(plrdata, plyr)]:
			unique_plyr = data["player_name"].unique()
			if len(unique_plyr) == 0:
				print(f"Error: {plyr} not found. Try Again.")
			elif len(unique_plyr) > 1:
				print(f"Error: {plyr} matched multiple players: {unique_plyr.tolist()}. Be more speciffic.")
			elif len(unique_plyr) == 1:
				return plrdata

def choose2plr():
	plrstrarr = df["player_name"].unique()
	while  True:
		plyr = input("Choose 2nd Player: ")
		plrdata = df[df["player_name"].str.contains(plyr, case=False, na=False)]
		for data, typed_name in [(plrdata, plyr)]:
			unique_plyr = data["player_name"].unique()
			if len(unique_plyr) == 0:
				print(f"Error: {plyr} not found. Try Again.")
			elif len(unique_plyr) > 1:
				print(f"Error: {plyr} matched multiple players: {unique_plyr.tolist()}. Be more speciffic.")
			elif len(unique_plyr) == 1:
				return plrdata
		
def getdata(name):
	plrdata = df[df["player_name"]==name]
	return plrdata
