import csv
import pandas as pd
import matplotlib.pyplot as plt
import graph
import roles
import fetch
import simmilar

df = pd.read_csv("plstats(1-35)2025-26.csv")

class player:
	def __init__(self, name,goals,assists):
		self.name = name
		self.goals = goals
		self.assists = assists

def stats():
	maxgoals = df["goals"].max()
	topgoalscrrdata = df[df["goals"]==maxgoals]
	p1 = player(fetch.name(topgoalscrrdata), fetch.goals(topgoalscrrdata), fetch.assists(topgoalscrrdata))
	print(p1.name)
	print(p1.goals)
	print(p1.assists)

while True:
	print("\n=== Premier League Analytics ===")
	print("1. Role Classifier")
	print("2. Compare 2 Players")
	print("3. Find League Outliers")
	print("4. Find Similar Players")
	print("5. Exit")

	choice = int(input("Choose one of the above Options:"))
	print()

	if choice == 1:
		plrdata = fetch.chooseplr()
		roles.roles(plrdata)
	elif choice == 2:
		plr1data = fetch.choose1plr()
		plr2data = fetch.choose2plr()
		while True:
			print("1. Compare Goals and Assists")
			print("2. Compare Dribbles")
			print("3. Compare Big Chances Created")
			print("4. Compare Duels Won")

			choice = int(input("Choose one of the above Options:"))
			if choice == 1:
				graph.compare(plr1data,plr2data,"goalsAssistsSum")
				break
			elif choice == 2:
				graph.compare(plr1data,plr2data,"successfulDribbles")
				break
			elif choice == 3:
				graph.compare(plr1data,plr2data,"bigChancesCreated")
				break
			elif choice == 4:
				graph.compare(plr1data,plr2data,"totalDuelsWon")
				break
			else:
				print("Choose a valid option.")
				print()
	elif choice == 3:
		while True:
			print("1. League Stats of Goal Conversion Percentage and Goals")
			print("2. League Stats of Big Chances Created and Dribbles")
			print("3. League Stats of Duels Won and Interceptions")
			choice = int(input("Choose one of the above Options:"))
			print()
			if choice == 1: 
				graph.outliers("goalConversionPercentage","goals")
				break
			elif choice == 2:
				graph.outliers("bigChancesCreated","successfulDribbles")
				break
			elif choice == 3:
				graph.outliers("totalDuelsWon","interceptions")
				break
			else:
				print("Choose a valid option.")
				print()
		break
	elif choice == 4:
		plrdata = fetch.chooseplr()
		simmilar.sim(plrdata)
	elif choice == 5:
		print("Exiting program.")
		break
	else:
		print("Choose a valid option.")
		print()





