import csv
import fetch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("plstats(1-35)2025-26.csv")

def compare(plr1data, plr2data, stat):
	plr1 = fetch.name(plr1data)
	p1stat1 = plr1data[stat].item()

	plr2 = fetch.name(plr2data)
	p2stat1 = plr2data[stat].item()

	fig, ax = plt.subplots(figsize=(6, 5))
	bars = ax.bar([plr1, plr2], [p1stat1, p2stat1], color=['#1f77b4', '#ff7f0e'])
    
	ax.bar_label(bars, fmt='%.2f', padding=3)

	ax.set_xlabel("Player")
	ax.set_ylabel(stat)
    
	ax.set_title(f"{stat} Comparison")
    
	plt.tight_layout()
	plt.show()


def outliers(stat1, stat2):
	plrstrarr = df["player_name"].unique()
	player_stats = df.groupby("player_name")[[stat1, stat2]].mean()
	player_stats["pct1"] = player_stats[stat1].rank(pct=True) * 100
	player_stats["pct2"] = player_stats[stat2].rank(pct=True) * 100

	is_outlier = (player_stats["pct1"] >= 99) | (player_stats["pct2"] >= 99)
	outliers_df = player_stats[is_outlier]
	regular_df = player_stats[~is_outlier]

	fig, ax = plt.subplots(figsize=(10, 7))
	ax.scatter(regular_df[stat2], regular_df[stat1], color="gray", alpha=0.4, label="Others")
	ax.scatter(outliers_df[stat2], outliers_df[stat1], color="blue", edgecolors="black", s=60, label="Outliers")

	x_mean = player_stats[stat2].mean()
	y_mean = player_stats[stat1].mean()

	ax.axvline(x=x_mean, color='black', linestyle='--', alpha=0.3, linewidth=1.5)
	ax.axhline(y=y_mean, color='black', linestyle='--', alpha=0.3, linewidth=1.5)

	x_max, x_min = player_stats[stat2].max(), player_stats[stat2].min()
	y_max, y_min = player_stats[stat1].max(), player_stats[stat1].min()

	ax.text(x_max, y_max, "Elite Both", alpha=0.5, fontsize=10, ha='right', va='top', color='green', weight='bold')
	ax.text(x_min, y_max, f"High {stat1}", alpha=0.5, fontsize=10, ha='right', va='top', color='green', weight='bold')
	ax.text(x_max, y_min, f"High {stat2}", alpha=0.5, fontsize=10, ha='right', va='top', color='green', weight='bold')

	coordinate_counts = {}

	for name, row in outliers_df.iterrows():
		x_val = row[stat2]
		y_val = row[stat1]

		coord_key = (round(x_val, 2), round(y_val, 2))

		if coord_key in coordinate_counts:
			coordinate_counts[coord_key] += 1
		else:
			coordinate_counts[coord_key] = 0

		y_offset = 5+ (coordinate_counts[coord_key] * 12)

		ax.annotate(
			name,
			(x_val, y_val),
			textcoords="offset points",
			xytext =(5, y_offset),
			ha ="left",
			va="bottom",
			fontsize=9,
			weight='semibold'
		)

	ax.set_xlabel(stat2)
	ax.set_ylabel(stat1)
	ax.legend(loc='upper left')

	plt.tight_layout()
	plt.show()
	

def spidergraph(plrdata1, plrdata2, statlist):
	p1name = plrdata1["player_name"]
	p2name = plrdata2["player_name"]

	p1_values = [plrdata1[stat] for stat in statlist]
	p2_values = [plrdata2[stat] for stat in statlist]

	num_stat = len(statlist)

	angles = np.linspace(0, 2 * np.pi, num_stat, endpoint=False).tolist()
	
	angles += angles[:1]
	p1_values += p1_values[:1]
	p2_values += p2_values[:1]

	fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
	plt.xticks(angles[:-1], statlist, color="dimgray", size=10)

	ax.plot(angles, p1_values, linewidth=2, linestyle='solid', label=p1name, color='#1f77b4')
	ax.fill(angles, p1_values, color='#1f77b4', alpha=0.25)

	ax.plot(angles, p2_values, linewidth=2, linestyle='solid', label=p2name, color='#ff7f0e')
	ax.fill(angles, p2_values, color='#ff7f0e', alpha=0.25)

	ax.set_title(f"Profile Overlay: {p1name} vs {p2name}", y=1.1, fontsize=12, fontweight='bold')
	ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
	
	ax.set_ylim(0,100)

	plt.show()


def leaguebenchmark(plrdata, stat1):
	plrstrarr = df["player_name"].unique()
	plr_pos = plrdata["position"].item()
	positiongrp = df[df["position"]==plr_pos]

	mean = positiongrp[stat1].mean()

	plr1 = fetch.name(plrdata)
	p1stat1 = plrdata[stat1].item()

	fig, ax = plt.subplots(figsize=(6, 5))
	bars = ax.bar([plr1, "League Average"], [p1stat1, mean], color=['#1f77b4', '#ff7f0e'])
    
	ax.bar_label(bars, fmt='%.2f', padding=3)
    
	ax.set_title(f"{plr1} {stat1} vs Position Average")
    
	plt.tight_layout()
	plt.show()