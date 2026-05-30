import csv
import fetch
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("plstats(1-35)2025-26.csv")


def roles(plrdata):
	position = plrdata["position"].item()
	if position == "D":
		accurlb = plrdata["accurateLongBalls"].item()
		accpasper = plrdata["accuratePassesPercentage"].item()
		clrs = plrdata["clearances"].item()
		aerialduelper = plrdata["aerialDuelsWonPercentage"].item()
		groundduelper = plrdata["groundDuelsWonPercentage"].item()
		clnshts = plrdata["cleanSheet"].item()
		driblost = plrdata["dribbledPast"].item()
		duelLost = plrdata["duelLost"].item()
		intrcpt = plrdata["interceptions"].item()
		tackleswonper = plrdata["tacklesWonPercentage"].item()
		totduelsper = plrdata["totalDuelsWonPercentage"].item()

		scores = {'Ball Playing Defender': None, 'Traditional Defender': None, 'Attacking Fullback': None, 'Defensive Fullback': None, 'Inverted Fullback': None}

		scores['Ball Playing Defender'] = (
			fetch.percentile(plrdata,"D","accurateLongBalls")*0.3 +
			fetch.percentile(plrdata,"D","interceptions")*0.05+
			fetch.percentile(plrdata,"D","accurateFinalThirdPasses")*0.2+
			fetch.percentile(plrdata,"D","totalDuelsWonPercentage")*0.05+
			fetch.percentile(plrdata,"D","aerialDuelsWonPercentage")*0.2+
			fetch.percentile(plrdata,"D","dribbledPast")*0.2
			)
		scores['Traditional Defender'] = (
			fetch.percentile(plrdata,"D","clearances")*0.2 +
			fetch.percentile(plrdata,"D","aerialDuelsWonPercentage")*0.3 +
			fetch.percentile(plrdata,"D","interceptions")*0.05+
			fetch.percentile(plrdata,"D","outfielderBlocks")*0.10+
			fetch.percentile(plrdata,"D","tacklesWonPercentage")*0.20+
			fetch.percentile(plrdata,"D","dribbledPast")*0.15
			)
		scores['Attacking Fullback'] = (
			fetch.percentile(plrdata,"D","accurateCrossesPercentage")*0.25 +
			fetch.percentile(plrdata,"D","successfulDribbles")*0.25 +
			fetch.percentile(plrdata,"D","keyPasses")*0.10+
			fetch.percentile(plrdata,"D","assists")*0.20+
			fetch.percentile(plrdata,"D","expectedAssists")*0.2
			)
		scores['Defensive Fullback'] = (
			fetch.percentile(plrdata,"D","tacklesWonPercentage")*0.30 +
			fetch.percentile(plrdata,"D","interceptions")*0.25 +
			fetch.percentile(plrdata,"D","groundDuelsWonPercentage")*0.20+
			fetch.percentile(plrdata,"D","ballRecovery")*0.25
			)
		scores['Inverted Fullback'] = (
			fetch.percentile(plrdata,"D","keyPasses")*0.1 +
			fetch.percentile(plrdata,"D","interceptions")*0.1+
			fetch.percentile(plrdata,"D","accurateCrossesPercentage")*0.2+
			fetch.percentile(plrdata,"D","ballRecovery")*0.15+
			fetch.percentile(plrdata,"D","goals")*0.15+
			fetch.percentile(plrdata,"D","successfulDribbles")*0.15-
			fetch.percentile(plrdata,"D","aerialDuelsWonPercentage")*0.15
			)

		biggestScore = max(scores, key = scores.get)
		print(plrdata["player_name"].item(),"has a profile of",biggestScore)

	if position == "M":
		scores = {'Ball Winning Midfielder': None, 'Deep Lying Playmaker': None, 'Anchor Man': None, 'Box to Box Midfielder': None, 'Playmaker': None, 'Hounddog Midfielder': None, 'Traditional Winger': None,'Inside Forward':None, 'Creative Winger':None}

		scores['Ball Winning Midfielder'] = (
			fetch.percentile(plrdata,"M","tacklesWon")*0.35 +
			fetch.percentile(plrdata,"M","ballRecovery")*0.1+
			fetch.percentile(plrdata,"M","accuratePassesPercentage")*0.05 +
			fetch.percentile(plrdata,"M","interceptions")*0.30+
			fetch.percentile(plrdata,"M","groundDuelsWon")*0.20
			)
		scores['Deep Lying Playmaker'] = (
			fetch.percentile(plrdata,"M","keyPasses")*0.2 +
			fetch.percentile(plrdata,"M","accuratePassesPercentage")*0.15 +
			fetch.percentile(plrdata,"M","accurateLongBalls")*0.15+
			fetch.percentile(plrdata,"M","accurateFinalThirdPasses")*0.15+
			fetch.percentile(plrdata,"M","touches")*0.10+
			fetch.percentile(plrdata,"M","interceptions")*0.05
			)
		scores['Anchor Man'] = (
			fetch.percentile(plrdata,"M","accuratePassesPercentage")*0.20 +
			fetch.percentile(plrdata,"M","tacklesWon")*0.15 +
			fetch.percentile(plrdata,"M","ballRecovery")*0.30+
			fetch.percentile(plrdata,"M","interceptions")*0.30+
			fetch.percentile(plrdata,"M","aerialDuelsWon")*0.05
			)
		scores['Box to Box Midfielder'] = (
			fetch.percentile(plrdata,"M","tacklesWon")*0.2 +
			fetch.percentile(plrdata,"M","groundDuelsWonPercentage")*0.20+
			fetch.percentile(plrdata,"M","totalShots")*0.15+
			fetch.percentile(plrdata,"M","assists")*0.10 +
			fetch.percentile(plrdata,"M","accurateFinalThirdPasses")*0.15+
			fetch.percentile(plrdata,"M","keyPasses")*0.05+
			fetch.percentile(plrdata,"M","ballRecovery")*0.10+
			fetch.percentile(plrdata,"M","successfulDribbles")*0.15
			)
		scores['Playmaker'] = (
			fetch.percentile(plrdata,"M","keyPasses")*0.3 +
			fetch.percentile(plrdata,"M","bigChancesCreated")*0.25+
			fetch.percentile(plrdata,"M","assists")*0.10+
			fetch.percentile(plrdata,"M","successfulDribbles")*0.15+
			fetch.percentile(plrdata,"M","expectedAssists")*0.20
			)
		scores['Hounddog Midfielder'] = (
			fetch.percentile(plrdata,"M","possessionWonAttThird")*0.25 +
			fetch.percentile(plrdata,"M","groundDuelsWonPercentage")*0.20+
			fetch.percentile(plrdata,"M","totalDuelsWonPercentage")*0.15+
			fetch.percentile(plrdata,"M","interceptions")*0.20+
			fetch.percentile(plrdata,"M","ballRecovery")*0.15
			)
		scores['Traditional Winger'] = (
			fetch.percentile(plrdata,"M","successfulDribbles")*0.35 +
			fetch.percentile(plrdata,"M","accurateCrossesPercentage")*0.25+
			fetch.percentile(plrdata,"M","assists")*0.20+
			fetch.percentile(plrdata,"M","keyPasses")*0.10+
			fetch.percentile(plrdata,"M","totalShots")*0.1
			)
		scores['Inside Forward'] = (
			fetch.percentile(plrdata,"M","goals")*0.35+
			fetch.percentile(plrdata,"M","expectedGoals")*0.25+
			fetch.percentile(plrdata,"M","totalShots")*0.20+
			fetch.percentile(plrdata,"M","successfulDribbles")*0.15
			)
		scores['Creative Winger'] = (
			fetch.percentile(plrdata,"M","keyPasses")*0.25+
			fetch.percentile(plrdata,"M","bigChancesCreated")*0.1+
			fetch.percentile(plrdata,"M","assists")*0.05+
			fetch.percentile(plrdata,"M","expectedAssists")*0.15+
			fetch.percentile(plrdata,"M","successfulDribbles")*0.20+
			fetch.percentile(plrdata,"M","totalShots")*0.1+
			fetch.percentile(plrdata,"M","passToAssist")*0.15
			)
		biggestScore = max(scores, key = scores.get)
		print(plrdata["player_name"].item(),"has a profile of",biggestScore)
	if position == "F":
		scores = {'Poacher':None, 'Target Man':None, 'False 9':None, 'Inside Forward':None, 'Traditional Winger':None}		

		scores['Poacher'] = (
			fetch.percentile(plrdata,"F","goals")*0.4+
			fetch.percentile(plrdata,"F","expectedGoals")*0.30+
			fetch.percentile(plrdata,"F","shotsOnTarget")*0.20+
			fetch.percentile(plrdata,"F","goalConversionPercentage")*0.10
		)
		scores['Target Man'] = (
			fetch.percentile(plrdata,"F","goals")*0.25+
			fetch.percentile(plrdata,"F","headedGoals")*0.3+
			fetch.percentile(plrdata,"F","aerialDuelsWon")*0.35+
			fetch.percentile(plrdata,"F","goalConversionPercentage")*0.10
		)
		scores['False 9'] = (
			fetch.percentile(plrdata,"F","keyPasses")*0.20+
			fetch.percentile(plrdata,"F","assists")*0.15+
			fetch.percentile(plrdata,"F","successfulDribbles")*0.15+
			fetch.percentile(plrdata,"F","touches")*0.10+
			fetch.percentile(plrdata,"F","goals")*0.2+
			fetch.percentile(plrdata,"F","expectedGoals")*0.2
		)
		scores['Inside Forward'] = (
			fetch.percentile(plrdata,"F","goals")*0.15+
			fetch.percentile(plrdata,"F","expectedGoals")*0.25+
			fetch.percentile(plrdata,"F","totalShots")*0.10+
			fetch.percentile(plrdata,"F","successfulDribbles")*0.25+
			fetch.percentile(plrdata,"F","keyPasses")*.1
		)
		scores['Traditional Winger'] = (
			fetch.percentile(plrdata,"F","successfulDribbles")*0.35 +
			fetch.percentile(plrdata,"F","accurateCrossesPercentage")*0.25+
			fetch.percentile(plrdata,"F","assists")*0.20+
			fetch.percentile(plrdata,"F","keyPasses")*0.10+
			fetch.percentile(plrdata,"F","totalShots")*0.1
		)

		biggestScore = max(scores, key = scores.get)
		print(plrdata["player_name"].item(),"has a profile of",biggestScore)
	if position == "G":
		scores = {'Shot Stopper':None, 'Sweeper Keeper':None}

		scores['Shot Stopper'] = (
			fetch.percentile(plrdata,"G","goalsPrevented")*0.35+
			fetch.percentile(plrdata,"G","saves")*0.45+
			fetch.percentile(plrdata,"G","highClaims")*0.2
		)
		scores['Sweeper Keeper'] = (
			fetch.percentile(plrdata,"G","accuratePasses")*0.25+
			fetch.percentile(plrdata,"G","accurateLongBalls")*0.30+
			fetch.percentile(plrdata,"G","clearances")*0.30+
			fetch.percentile(plrdata,"G","touches")*0.15
		)


		biggestScore = max(scores, key = scores.get)
		print(plrdata["player_name"].item(),"has a profile of",biggestScore)
		print()