import csv
import fetch
import graph
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

df = pd.read_csv("plstats(1-35)2025-26.csv")

stats = [
	"keyPasses",
	"tacklesWon",
	"successfulDribbles",
	"expectedGoals",
	"expectedAssists",
	"bigChancesCreated",
	"possessionWonAttThird",
	"accurateFinalThirdPasses",
	"accurateLongBalls",
	"aerialDuelsWon",
	"groundDuelsWon",
	"totalShots",
	"ballRecovery",
	"headedGoals",
	"accuratePasses",
	"interceptions",
	"touches",
	"totalOppositionHalfPasses",
	"totalOwnHalfPasses",
	"accurateCrosses",
	"clearances",
	"totalDuelsWon",
	"goalsPrevented",
	"saves"
]

statF = [
	"keyPasses",
	"successfulDribbles",
	"expectedGoals",
	"bigChancesCreated",
	"accurateFinalThirdPasses",
	"accurateLongBalls",
	"aerialDuelsWon",
	"groundDuelsWon",
	"totalShots",
	"accuratePasses",
	"headedGoals",
	"touches",
	"accurateCrosses",
	"totalDuelsWon"
]

statM = [
	"keyPasses",
	"tacklesWon",
	"successfulDribbles",
	"expectedGoals",
	"expectedAssists",
	"bigChancesCreated",
	"possessionWonAttThird",
	"accurateFinalThirdPasses",
	"accurateLongBalls",
	"aerialDuelsWon",
	"groundDuelsWon",
	"totalShots",
	"ballRecovery",
	"accuratePasses",
	"interceptions",
	"touches",
	"totalOppositionHalfPasses",
	"totalOwnHalfPasses",
	"accurateCrosses",
	"totalDuelsWon"
]

statD = [
	"keyPasses",
	"tacklesWon",
	"successfulDribbles",
	"bigChancesCreated",
	"accurateFinalThirdPasses",
	"accurateLongBalls",
	"aerialDuelsWon",
	"groundDuelsWon",
	"ballRecovery",
	"accuratePasses",
	"headedGoals",
	"interceptions",
	"clearances",
	"touches",
	"totalOppositionHalfPasses",
	"totalOwnHalfPasses",
	"accurateCrosses",
	"totalDuelsWon"
]

statG = [
	"goalsPrevented",
	"accuratePasses",
	"clearances",
	"touches",
	"totalOwnHalfPasses",
	"accurateLongBalls",
	"saves"
]


percentile_columns = (
	df.groupby('position')[stats].rank(pct=True).multiply(100).round(1)
	)

percentile_columns = percentile_columns.add_suffix('_percentile')
profiles_df = pd.concat([df[['player_name', 'position']], percentile_columns], axis=1)

percentile_colsF = [
	"keyPasses_percentile",
	"successfulDribbles_percentile",
	"expectedGoals_percentile",
	"bigChancesCreated_percentile",
	"accurateFinalThirdPasses_percentile",
	"accurateLongBalls_percentile",
	"aerialDuelsWon_percentile",
	"groundDuelsWon_percentile",
	"totalShots_percentile",
	"accuratePasses_percentile",
	"headedGoals_percentile",
	"touches_percentile",
	"accurateCrosses_percentile",
	"totalDuelsWon_percentile"
]

percentile_colsM = [
	"keyPasses_percentile",
	"tacklesWon_percentile",
	"successfulDribbles_percentile",
	"expectedGoals_percentile",
	"expectedAssists_percentile",
	"bigChancesCreated_percentile",
	"possessionWonAttThird_percentile",
	"accurateFinalThirdPasses_percentile",
	"accurateLongBalls_percentile",
	"aerialDuelsWon_percentile",
	"groundDuelsWon_percentile",
	"totalShots_percentile",
	"ballRecovery_percentile",
	"accuratePasses_percentile",
	"interceptions_percentile",
	"touches_percentile",
	"totalOppositionHalfPasses_percentile",
	"totalOwnHalfPasses_percentile",
	"accurateCrosses_percentile",
	"totalDuelsWon_percentile"
]

percentile_colsD = [
	"keyPasses_percentile",
	"tacklesWon_percentile",
	"successfulDribbles_percentile",
	"bigChancesCreated_percentile",
	"accurateFinalThirdPasses_percentile",
	"accurateLongBalls_percentile",
	"aerialDuelsWon_percentile",
	"groundDuelsWon_percentile",
	"ballRecovery_percentile",
	"accuratePasses_percentile",
	"headedGoals_percentile",
	"interceptions_percentile",
	"clearances_percentile",
	"touches_percentile",
	"totalOppositionHalfPasses_percentile",
	"totalOwnHalfPasses_percentile",
	"accurateCrosses_percentile",
	"totalDuelsWon_percentile"
]

percentile_colsG = [
	"goalsPrevented_percentile",
	"accuratePasses_percentile",
	"clearances_percentile",
	"touches_percentile",
	"totalOwnHalfPasses_percentile",
	"accurateLongBalls_percentile",
	"saves_percentile"
]

def sim(plrdata):
	chplyr = get_profile(plrdata)

	similarities = []

	for _, row in profiles_df.iterrows():
		stat_similarities = []
		
		if row["player_name"] == chplyr["player_name"]:
			continue

		if row["position"] != chplyr["position"]:
			continue

		distance = 0

		if row["position"] == "F":
			for stat in percentile_colsF:
				distance += (
					chplyr[stat] - row[stat]
				) **2 
				if chplyr[stat] != 0:
					diff = abs(chplyr[stat] - row[stat])
				else:
					continue
				stat_sim_pct = 100.0 - diff
				stat_similarities.append((stat, stat_sim_pct))
			distance = distance **0.5
		
		elif row["position"] == "M":
			for stat in percentile_colsM:
				distance += (
					chplyr[stat] - row[stat]
				) **2 
				if chplyr[stat] != 0:
					diff = abs(chplyr[stat] - row[stat])
				else:
					continue
				stat_sim_pct = 100.0 - diff
				stat_similarities.append((stat, stat_sim_pct))
			distance = distance **0.5

		elif row["position"] == "D":
			for stat in percentile_colsD:
				distance += (
					chplyr[stat] - row[stat]
				) **2 
				if chplyr[stat] != 0:
					diff = abs(chplyr[stat] - row[stat])
				else:
					continue
				stat_sim_pct = 100.0 - diff
				stat_similarities.append((stat, stat_sim_pct))
			distance = distance **0.5

		elif row["position"] == "G":
			for stat in percentile_colsG:
				distance += (
					chplyr[stat] - row[stat]
				) **2 
				diff = abs(chplyr[stat] - row[stat])
				stat_sim_pct = 100.0 - diff
				stat_similarities.append((stat, stat_sim_pct))
			distance = distance **0.5

		stat_similarities.sort(key=lambda x: x[1], reverse = True)
		similarities.append((row["player_name"],distance, stat_similarities))
	similarities.sort(key=lambda x: x[1])
	maxdistance = max(distance for _, distance, _ in similarities)

	results = {
		'target_player_profile': chplyr,
		'matches':[]
	}

	for player, distance, stat_similarities in similarities[:3]:
		simper = (
			1 - distance/maxdistance
		) * 100

		top_stats = []
		for stat, stat_sim_pct in stat_similarities[:8]:
			clean_stat = stat.replace("_percentile", "")
			top_stats.append({
				"stat_raw_name": stat,
				"stat_clean_name": clean_stat,
				"percentage": round(stat_sim_pct, 2)
			})

		results["matches"].append({
			"player_name": player,
			"similarity_score": round(simper, 2),
			"top_similar_stats": top_stats,
			"matched_player_profile": get_profile(profiles_df[profiles_df["player_name"]==player])
		})

		return results

def get_profile(plrdata):
	plyrRow = profiles_df[profiles_df["player_name"] == fetch.name(plrdata)]
	return plyrRow.iloc[0].to_dict()
