import csv
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

import graph
import roles
import fetch
import simmilar

df = pd.read_csv("plstats(1-35)2025-26.csv")

class PlApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Premier League Analytics")
		self.root.geometry("1200x750")
		
		self.bg_dark = "#0B0F19"
		self.bg_card = "#1A2236"
		self.accent = "#00E676"
		self.hovercolor = "#25314D"
		self.hoverfore="#00B0FF"
		self.text_body = "#F4F6FA"

		self.mainstyle = ttk.Style()
		self.mainstyle.theme_use("clam")
		self.mainstyle.configure('main.TFrame', background=self.bg_dark)

		self.root.configure(bg=self.bg_dark)

		self.main_container = ttk.Frame(self.root, padding="20", style='main.TFrame')
		self.main_container.pack(fill=tk.BOTH, expand=True)


		self.show_main_menu()

	def clear(self):
		for widget in self.main_container.winfo_children():
			widget.destroy()

	def show_main_menu(self):
		self.clear()

		title = ttk.Label(self.main_container, text="Premier League Analytics", font=("Lexend", 18, "bold"), foreground=self.accent,background=self.bg_dark)
		title.pack(pady=20)

		self.mainstyle.configure("TLabel", background=self.bg_dark, foreground=self.text_body)

		self.mainstyle.configure("TCombobox", fieldbackground=self.bg_card,background=self.bg_card, foreground=self.accent)

		self.mainstyle.configure("TButton", font=("Lexend", 10), background=self.bg_card,foreground=self.text_body)
		self.mainstyle.map('TButton',
			background=[('active', self.hovercolor)],
			foreground=[('active', self.hoverfore)]
		)

		ttk.Button(self.main_container, text="Role Classifier",width=30, command=self.handleroles).pack(pady=10)
		ttk.Button(self.main_container, text="Compare 2 Players",width=30, command=self.handlecomparision).pack(pady=10)
		ttk.Button(self.main_container, text="Find League Outliers", width=30, command=self.handleoutliers).pack(pady=10)
		ttk.Button(self.main_container, text="Find Similar Players", width=30, command=self.handlesimmilarity).pack(pady=10)
		ttk.Button(self.main_container, text="Compare to Position Benchmark", width=30, command=self.handlebenchmark).pack(pady=10)
		ttk.Button(self.main_container, text="Check Squad Roles", width=30, command=self.handleteamprofile).pack(pady=10)

		ttk.Separator(self.main_container, orient='horizontal').pack(fill='x', pady=15)
		ttk.Button(self.main_container, text="Exit", width=15, command=self.root.quit).pack()

	def handleroles(self):
		self.clear()

		ttk.Label(self.main_container, text="Role Classifier", font=("Lexend", 14, "bold"), foreground=self.accent).pack(pady=10)

		ttk.Label(self.main_container, text="Select Player: ").pack(pady=5)
		self.plr_option = df["player_name"].unique().tolist()
		self.plr_dropdown = ttk.Combobox(self.main_container, values=self.plr_option)
		self.plr_dropdown.pack(pady=5)
		self.plr_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.plr_option, self.plr_dropdown))

		self.results_frame = ttk.Frame(self.main_container, style='main.TFrame')
		self.results_frame.pack(pady=10)

		def launchroles():
			for widget in self.results_frame.winfo_children():
				widget.destroy()

			pname = self.plr_dropdown.get()

			if not pname:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return

			plrdata = fetch.getdata(pname)

			if plrdata is None or plrdata.empty:
				messagebox.showerror("Error", "Choose a valid player.")
				return

			scores = roles.rolescore(plrdata)
			preferedrole = max(scores, key=scores.get)

			result_text = f"{pname} has the profile of: {preferedrole}"
			result_text2 = "Profile Scores:"
			result_text3 = ""

			sorted_roles = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
			for role, score in sorted_roles.items():
				result_text3 += f"{role}, Score: {round(score, 2)}\n"


			ttk.Label(self.results_frame, text=result_text, justify=tk.LEFT, font=("Comfortaa", 14)).pack(pady=5)
			ttk.Label(self.results_frame, text=result_text2, justify=tk.LEFT, font=("Comfortaa", 12)).pack(pady=2)
			ttk.Label(self.results_frame, text=result_text3, justify=tk.LEFT, font=("Comfortaa", 10)).pack(pady=2)

		ttk.Button(self.main_container, text="Clasify", width=30, command=launchroles).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)


	def handlecomparision(self):
		self.clear()

		ttk.Label(self.main_container, text="Compare 2 Players", font=("Lexend", 14, "bold")).pack(pady=10)


		ttk.Label(self.main_container, text="Select Player 1: ").pack(pady=5)
		self.plr_option = df["player_name"].unique().tolist()
		self.plr_dropdown = ttk.Combobox(self.main_container, values=self.plr_option)
		self.plr_dropdown.pack(pady=5)
		self.plr_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.plr_option, self.plr_dropdown))


		ttk.Label(self.main_container, text="Select Player 2: ").pack(pady=5)
		self.plr_dropdown2 = ttk.Combobox(self.main_container, values=self.plr_option)
		self.plr_dropdown2.pack(pady=5)
		self.plr_dropdown2.bind("<KeyRelease>", lambda event: self.filter_options(event, self.plr_option, self.plr_dropdown2))

		ttk.Label(self.main_container, text="Choose Metric to Compare: ").pack(pady=5)
		self.stat_option = list(df.select_dtypes(include='number'))
		self.stats_dropdown = ttk.Combobox(self.main_container, values=self.stat_option)
		self.stats_dropdown.pack(pady=5)
		self.stats_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.stat_option, self.stats_dropdown))

		def launchcompare():
			p1_name = self.plr_dropdown.get()
			p2_name = self.plr_dropdown2.get()
			metric = self.stats_dropdown.get()

			if not p1_name or not p2_name or not metric:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return

			plr1data = fetch.getdata(p1_name)
			plr2data = fetch.getdata(p2_name)

			if plr1data.empty or plr2data.empty:
				messagebox.showerror("Error", "One or both players could not be found. Please choose from the list.")
				return

			graph.compare(plr1data, plr2data, metric)
		
		ttk.Button(self.main_container, text="Compare", width=30, command=launchcompare).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)


	def filter_options(self, event, list, dropdown):
		if event.keysym in ["Up", "Down", "Return", "Left", "Right", "Escape"]:
			return

		typed_text = dropdown.get()
		cursor_pos = dropdown.index(tk.INSERT)

		if typed_text == "":
			filtered_data = list
		else:
			filtered_data = [opt for opt in list if typed_text.lower() in opt.lower()]

		dropdown['values'] = filtered_data
		dropdown.set(typed_text)
		dropdown.icursor(cursor_pos)

	def handleoutliers(self):
		self.clear()

		ttk.Label(self.main_container, text="Find Outliers", font=("Lexend", 14, "bold")).pack(pady=10)

		ttk.Label(self.main_container, text="Choose 1st Metric: ").pack(pady=5)
		self.stat_option = list(df.select_dtypes(include='number'))
		self.stats_dropdown = ttk.Combobox(self.main_container, values=self.stat_option)
		self.stats_dropdown.pack(pady=5)
		self.stats_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.stat_option, self.stats_dropdown))

		ttk.Label(self.main_container, text="Choose 2nd Metric: ").pack(pady=5)
		self.stats_dropdown2 = ttk.Combobox(self.main_container, values=self.stat_option)
		self.stats_dropdown2.pack(pady=5)
		self.stats_dropdown2.bind("<KeyRelease>", lambda event: self.filter_options(event, self.stat_option, self.stats_dropdown2))

		def launchoutlier():
			stat1 = self.stats_dropdown.get()
			stat2 = self.stats_dropdown2.get()

			if not stat1 or not stat2:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return
			
			graph.outliers(stat1, stat2)

		ttk.Button(self.main_container, text="Find", width=30, command=launchoutlier).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)

	def handlesimmilarity(self):
		self.clear()

		ttk.Label(self.main_container, text="Find Similar Player", font=("Lexend", 14, "bold")).pack(pady=10)

		ttk.Label(self.main_container, text="Select Player: ").pack(pady=5)
		self.plr_option = df["player_name"].unique().tolist()
		self.plr_dropdown = ttk.Combobox(self.main_container, values=self.plr_option)
		self.plr_dropdown.pack(pady=5)
		self.plr_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.plr_option, self.plr_dropdown))

		def launchsimilarity():
			pname = self.plr_dropdown.get()
			if not pname:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return

			plrdata = fetch.getdata(pname)

			if plrdata is None or plrdata.empty:
				messagebox.showerror("Error", "Choose a valid player.")
				return


			similarityinfo = simmilar.sim(plrdata)

			self.clear()

			bestmatch = similarityinfo["matches"][0]

			result_text = f"Most Similar Player: {bestmatch['player_name']} ({bestmatch['similarity_score']}% match)"
			result_text2 = "Top Overlapping Attributes:"
			result_text3 = ""

			statname = []
			for stat in bestmatch["top_similar_stats"]:
				result_text3 += f"- {stat['stat_clean_name']}: {stat['percentage']}% similar\n"
				statname.append(stat['stat_raw_name'])

			def showgraph():
				graph.spidergraph(
					similarityinfo['target_player_profile'],
					bestmatch['matched_player_profile'],
					statname
				)

			ttk.Label(self.main_container, text=result_text, font=("Comfortaa", 14, "bold")).pack(pady=10)
			ttk.Label(self.main_container, text=result_text2, justify=tk.LEFT, font=("Comfortaa", 12)).pack(pady=10)
			ttk.Label(self.main_container, text=result_text3, justify=tk.LEFT, font=("Comfortaa", 10)).pack(pady=10)
			ttk.Button(self.main_container, text="View Spider Graph Comparision Chart", command=showgraph).pack(pady=10)
			ttk.Button(self.main_container, text="Back", width=30, command=self.handlesimmilarity).pack(pady=5)

		ttk.Button(self.main_container, text="Find", width=30, command=launchsimilarity).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)

	def handlebenchmark(self):
		self.clear()

		ttk.Label(self.main_container, text="Find Similar Player", font=("Lexend", 14, "bold")).pack(pady=10)

		ttk.Label(self.main_container, text="Select Player: ").pack(pady=5)
		self.plr_option = df["player_name"].unique().tolist()
		self.plr_dropdown = ttk.Combobox(self.main_container, values=self.plr_option)
		self.plr_dropdown.pack(pady=5)
		self.plr_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.plr_option, self.plr_dropdown))

		ttk.Label(self.main_container, text="Choose a Metric: ").pack(pady=5)
		self.stat_option = list(df.select_dtypes(include='number'))
		self.stats_dropdown = ttk.Combobox(self.main_container, values=self.stat_option)
		self.stats_dropdown.pack(pady=5)
		self.stats_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.stat_option, self.stats_dropdown))

		def launchbenchmark():
			stat = self.stats_dropdown.get()
			pname = self.plr_dropdown.get()

			if not pname:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return

			plrdata = fetch.getdata(pname)

			if plrdata is None or plrdata.empty:
				messagebox.showerror("Error", "Choose a valid player.")
				return

			if not stat:
				messagebox.showerror("Error", "Please fill in all dropdown fields")
				return

			graph.leaguebenchmark(plrdata, stat)


		ttk.Button(self.main_container, text="Compare", width=30, command=launchbenchmark).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)


	def handleteamprofile(self):
		self.clear()

		ttk.Label(self.main_container, text="Get Roles of An Entire Team", font=("Lexend", 14, "bold")).pack(pady=10)

		ttk.Label(self.main_container, text="Select Team: ").pack(pady=5)
		self.team_option = df["team_name"].unique().tolist()
		self.team_dropdown = ttk.Combobox(self.main_container, values=self.team_option)
		self.team_dropdown.pack(pady=5)
		self.team_dropdown.bind("<KeyRelease>", lambda event: self.filter_options(event, self.team_option, self.team_dropdown))

		self.profiles = ttk.Frame(self.main_container, style='main.TFrame')
		self.profiles.pack(pady=10)

		def launchteamprofile():
			for widget in self.profiles.winfo_children():
				widget.destroy()
			team = self.team_dropdown.get()

			if not team:
				messagebox.showerror("Error", "Choose a valid team")
				return
			
			teamgrp = df[df['team_name']==team]

			if teamgrp is None or teamgrp.empty:
				messagebox.showerror("Error", "Choose a valid team")
				return

			position_mapping = {
				"F": "Forwards / Attackers",
				"M": "Midfielders",
				"D": "Defenders",
				"G": "Goalkeepers"
			}

			result_text = f"Roles Of Players in {team}: "
			ttk.Label(self.profiles, text=result_text, font=("Comfortaa", 14, "bold")).pack(pady=10)

			column_container = ttk.Frame(self.profiles, style='main.TFrame')
			column_container.pack(fill='x', expand=True, padx=10)

			left_column_positions = [("G", "Goalkeepers"),("D", "Defenders")]
			right_column_positions = [("F", "Forwards / Attackers"), ("M", "Midfielders")]

			left_frame = ttk.Frame(column_container, style='main.TFrame')
			left_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=20, anchor='n')

			for pos_code, pos_name in right_column_positions:
				pos_df = teamgrp[teamgrp["position"]==pos_code]

				if pos_df.empty:
					continue

				result_text2 = ""
        		
				ttk.Label(left_frame, text=f"\n --{pos_name}--", font=("Comfortaa", 12, "bold"), foreground="#1f77b4").pack(pady=5, anchor='w')

				for name in pos_df["player_name"].unique():
					data = fetch.getdata(name)
					score = roles.roles(data)
					result_text2 += f"- {name}: {score}\n"

				ttk.Label(left_frame, text=result_text2.strip(), justify=tk.LEFT, font=("Comfortaa", 12)).pack(pady=2, anchor='w')

			right_frame = ttk.Frame(column_container, style='main.TFrame')
			right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=20, anchor='n')

			for pos_code, pos_name in left_column_positions:
				pos_df = teamgrp[teamgrp["position"]==pos_code]

				if pos_df.empty:
					continue

				result_text2 = ""
        		
				ttk.Label(right_frame, text=f"\n --{pos_name}--", font=("Comfortaa", 12, "bold"), foreground="#1f77b4").pack(pady=5, anchor='w')

				for name in pos_df["player_name"].unique():
					data = fetch.getdata(name)
					score = roles.roles(data)
					result_text2 += f"- {name}: {score}\n"

				ttk.Label(right_frame, text=result_text2.strip(), justify=tk.LEFT, font=("Comfortaa", 12)).pack(pady=2, anchor='w')


		ttk.Button(self.main_container, text="Get Roles", width=30, command=launchteamprofile).pack(pady=10)
		ttk.Button(self.main_container, text="Back To Main Menu", width=30, command=self.show_main_menu).pack(pady=5)


if __name__ == "__main__":
	root = tk.Tk()
	app = PlApp(root)
	root.mainloop()

