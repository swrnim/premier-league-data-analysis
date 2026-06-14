import csv
import fetch
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("plstats(1-35)2025-26.csv")

def rolescore(plrdata):
	position = plrdata["position"].item()
	if position == "D":
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
		return scores

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
		return scores
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
		return scores
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
		return scores


def roles(plrdata):
	position = plrdata["position"].item()

	cachepercentile={}

	metrics_by_pos = {
		"D": ["accurateLongBalls", "interceptions", "accurateFinalThirdPasses","totalDuelsWonPercentage", 
		"aerialDuelsWonPercentage", "dribbledPast", "clearances", "outfielderBlocks", "tacklesWonPercentage", "accurateCrossesPercentage", "successfulDribbles", 
		"keyPasses", "assists", "expectedAssists", "groundDuelsWonPercentage", "ballRecovery", "goals"],
              
        "M": ["tacklesWon", "ballRecovery", "accuratePassesPercentage", "interceptions", "groundDuelsWon", "keyPasses", "accurateLongBalls", "accurateFinalThirdPasses", "touches", "aerialDuelsWon", "groundDuelsWonPercentage", "totalShots", "assists", "successfulDribbles", "bigChancesCreated", "expectedAssists", "possessionWonAttThird", "totalDuelsWonPercentage", "accurateCrossesPercentage", "goals", "expectedGoals", "passToAssist"],
              
		"F": ["goals", "expectedGoals", "shotsOnTarget", "goalConversionPercentage", "headedGoals", "aerialDuelsWon", "keyPasses", "assists", "successfulDribbles", "touches", "totalShots", "accurateCrossesPercentage"],
              
		"G": ["goalsPrevented", "saves", "highClaims", "accuratePasses", "accurateLongBalls", "clearances", "touches"]
    }

	for metric in metrics_by_pos[position]:
		try:
			cachepercentile[metric] = fetch.percentile(plrdata, position, metric)
		except Exception:
			p[metric] = 0.0

	if position == "D":
		scores = {'Ball Playing Defender': None, 'Traditional Defender': None, 'Attacking Fullback': None, 'Defensive Fullback': None, 'Inverted Fullback': None}

		scores['Ball Playing Defender'] = (
			cachepercentile["accurateLongBalls"]*0.3 +
			cachepercentile["interceptions"]*0.05+
			cachepercentile["accurateFinalThirdPasses"]*0.2+
			cachepercentile["totalDuelsWonPercentage"]*0.05+
			cachepercentile["aerialDuelsWonPercentage"]*0.2+
			cachepercentile["dribbledPast"]*0.2
			)
		scores['Traditional Defender'] = (
			cachepercentile["clearances"]*0.2 +
			cachepercentile["aerialDuelsWonPercentage"]*0.3 +
			cachepercentile["interceptions"]*0.05+
			cachepercentile["outfielderBlocks"]*0.10+
			cachepercentile["tacklesWonPercentage"]*0.20+
			cachepercentile["dribbledPast"]*0.15
			)
		scores['Attacking Fullback'] = (
			cachepercentile["accurateCrossesPercentage"]*0.25 +
			cachepercentile["successfulDribbles"]*0.25 +
			cachepercentile["keyPasses"]*0.10+
			cachepercentile["assists"]*0.20+
			cachepercentile["expectedAssists"]*0.2
			)
		scores['Defensive Fullback'] = (
			cachepercentile["tacklesWonPercentage"]*0.30 +
			cachepercentile["interceptions"]*0.25 +
			cachepercentile["groundDuelsWonPercentage"]*0.20+
			cachepercentile["ballRecovery"]*0.25
			)
		scores['Inverted Fullback'] = (
			cachepercentile["keyPasses"]*0.1 +
			cachepercentile["interceptions"]*0.1+
			cachepercentile["accurateCrossesPercentage"]*0.2+
			cachepercentile["ballRecovery"]*0.15+
			cachepercentile["goals"]*0.15+
			cachepercentile["successfulDribbles"]*0.15-
			cachepercentile["aerialDuelsWonPercentage"]*0.15
			)

		biggestScore = max(scores, key = scores.get)
		return biggestScore

	if position == "M":
		scores = {'Ball Winning Midfielder': None, 'Deep Lying Playmaker': None, 'Anchor Man': None, 'Box to Box Midfielder': None, 'Playmaker': None, 'Hounddog Midfielder': None, 'Traditional Winger': None,'Inside Forward':None, 'Creative Winger':None}

		scores['Ball Winning Midfielder'] = (
			cachepercentile["tacklesWon"]*0.35 +
			cachepercentile["ballRecovery"]*0.1+
			cachepercentile["accuratePassesPercentage"]*0.05 +
			cachepercentile["interceptions"]*0.30+
			cachepercentile["groundDuelsWon"]*0.20
			)
		scores['Deep Lying Playmaker'] = (
			cachepercentile["keyPasses"]*0.2 +
			cachepercentile["accuratePassesPercentage"]*0.15 +
			cachepercentile["accurateLongBalls"]*0.15+
			cachepercentile["accurateFinalThirdPasses"]*0.15+
			cachepercentile["touches"]*0.10+
			cachepercentile["interceptions"]*0.05
			)
		scores['Anchor Man'] = (
			cachepercentile["accuratePassesPercentage"]*0.20 +
			cachepercentile["tacklesWon"]*0.15 +
			cachepercentile["ballRecovery"]*0.30+
			cachepercentile["interceptions"]*0.30+
			cachepercentile["aerialDuelsWon"]*0.05
			)
		scores['Box to Box Midfielder'] = (
			cachepercentile["tacklesWon"]*0.2 +
			cachepercentile["groundDuelsWonPercentage"]*0.20+
			cachepercentile["totalShots"]*0.15+
			cachepercentile["assists"]*0.10 +
			cachepercentile["accurateFinalThirdPasses"]*0.15+
			cachepercentile["keyPasses"]*0.05+
			cachepercentile["ballRecovery"]*0.10+
			cachepercentile["successfulDribbles"]*0.15
			)
		scores['Playmaker'] = (
			cachepercentile["keyPasses"]*0.3 +
			cachepercentile["bigChancesCreated"]*0.25+
			cachepercentile["assists"]*0.10+
			cachepercentile["successfulDribbles"]*0.15+
			cachepercentile["expectedAssists"]*0.20
			)
		scores['Hounddog Midfielder'] = (
			cachepercentile["possessionWonAttThird"]*0.25 +
			cachepercentile["groundDuelsWonPercentage"]*0.20+
			cachepercentile["totalDuelsWonPercentage"]*0.15+
			cachepercentile["interceptions"]*0.20+
			cachepercentile["ballRecovery"]*0.15
			)
		scores['Traditional Winger'] = (
			cachepercentile["successfulDribbles"]*0.35 +
			cachepercentile["accurateCrossesPercentage"]*0.25+
			cachepercentile["assists"]*0.20+
			cachepercentile["keyPasses"]*0.10+
			cachepercentile["totalShots"]*0.1
			)
		scores['Inside Forward'] = (
			cachepercentile["goals"]*0.35+
			cachepercentile["expectedGoals"]*0.25+
			cachepercentile["totalShots"]*0.20+
			cachepercentile["successfulDribbles"]*0.15
			)
		scores['Creative Winger'] = (
			cachepercentile["keyPasses"]*0.25+
			cachepercentile["bigChancesCreated"]*0.1+
			cachepercentile["assists"]*0.05+
			cachepercentile["expectedAssists"]*0.15+
			cachepercentile["successfulDribbles"]*0.20+
			cachepercentile["totalShots"]*0.1+
			cachepercentile["passToAssist"]*0.15
			)
		biggestScore = max(scores, key = scores.get)
		return biggestScore
	if position == "F":
		scores = {'Poacher':None, 'Target Man':None, 'False 9':None, 'Inside Forward':None, 'Traditional Winger':None}		

		scores['Poacher'] = (
			cachepercentile["goals"]*0.4+
			cachepercentile["expectedGoals"]*0.30+
			cachepercentile["shotsOnTarget"]*0.20+
			cachepercentile["goalConversionPercentage"]*0.10
		)
		scores['Target Man'] = (
			cachepercentile["goals"]*0.25+
			cachepercentile["headedGoals"]*0.3+
			cachepercentile["aerialDuelsWon"]*0.35+
			cachepercentile["goalConversionPercentage"]*0.10
		)
		scores['False 9'] = (
			cachepercentile["keyPasses"]*0.20+
			cachepercentile["assists"]*0.15+
			cachepercentile["successfulDribbles"]*0.15+
			cachepercentile["touches"]*0.10+
			cachepercentile["goals"]*0.2+
			cachepercentile["expectedGoals"]*0.2
		)
		scores['Inside Forward'] = (
			cachepercentile["goals"]*0.15+
			cachepercentile["expectedGoals"]*0.25+
			cachepercentile["totalShots"]*0.10+
			cachepercentile["successfulDribbles"]*0.25+
			cachepercentile["keyPasses"]*.1
		)
		scores['Traditional Winger'] = (
			cachepercentile["successfulDribbles"]*0.35 +
			cachepercentile["accurateCrossesPercentage"]*0.25+
			cachepercentile["assists"]*0.20+
			cachepercentile["keyPasses"]*0.10+
			cachepercentile["totalShots"]*0.1
		)

		biggestScore = max(scores, key = scores.get)
		return biggestScore
	if position == "G":
		scores = {'Shot Stopper':None, 'Sweeper Keeper':None}

		scores['Shot Stopper'] = (
			cachepercentile["goalsPrevented"]*0.35+
			cachepercentile["saves"]*0.45+
			cachepercentile["highClaims"]*0.2
		)
		scores['Sweeper Keeper'] = (
			cachepercentile["accuratePasses"]*0.25+
			cachepercentile["accurateLongBalls"]*0.30+
			cachepercentile["clearances"]*0.30+
			cachepercentile["touches"]*0.15
		)


		biggestScore = max(scores, key = scores.get)
		return biggestScore