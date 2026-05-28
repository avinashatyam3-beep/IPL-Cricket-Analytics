import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

matches=pd.read_csv("data/matches.csv")
print(matches.head())
print(matches.shape)
print(matches.columns)
print(matches.info())
print(matches.isnull().sum())


#team win
teams_win=matches['winner'].value_counts()
print(teams_win)
teams_win.plot(kind='bar')
plt.title("ipl team wins")
plt.xlabel("teams")
plt.ylabel("num of wins")

plt.show()


#top player
top_playes=matches['player_of_match'].value_counts().head()
print(top_playes)
top_playes.plot(kind='bar')
plt.title("top 10 players")
plt.xlabel("players")
plt.ylabel("awards")
plt.xticks(rotation=45)
plt.show()


#toss impact analysis
matches['toss_match_win']=matches['toss_winner']==matches['winner']
print(matches[['toss_winner','winner','toss_match_win']].head())
toss_result=matches['toss_match_win'].value_counts()
print(toss_result)
toss_result.plot(kind='pie',autopct='%1.1f%%')
plt.title("toss vs match winners")
plt.ylabel("")
plt.show()

#which batsman score highest runs
deliveries=pd.read_csv("data/deliveries.csv")
print(deliveries.head())
top_batsman=deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False)
print(top_batsman.head(10))
top = top_batsman.head(10)
top.plot(kind='bar')
plt.title("top 10 ipl run scorers")
plt.xlabel("players")
plt.ylabel("runs")
plt.xticks(rotation=45)
plt.show()

#top wicket taker
print(deliveries['dismissal_kind'].unique())
wickets=deliveries[deliveries['dismissal_kind']!='run out']
top_bowlers=wickets.groupby('bowler')['player_dismissed'].count()
top_bowlers=top_bowlers.sort_values(ascending=False)
print(top_bowlers.head(10))
tops=top_bowlers.head(10)
tops.plot(kind='bar')
plt.title("top wickets")
plt.xlabel("bowlers")
plt.ylabel("wickets")
plt.xticks(rotation=45)
plt.show()


#which stadium hosted most ipl matches
print(matches['venue'].head())
venue_matches=matches['venue'].value_counts()
print(venue_matches.value_counts())
print(venue_matches.head(10))
topv=venue_matches.head(10)
topv.plot(kind='bar')
plt.title("top 10 ipl venues")
plt.xlabel("venue")
plt.ylabel("matches hosted")
plt.xticks(rotation=90)
plt.show()
plt.figure(figsize=(12,6))
sns.barplot(x=topv.values,y=topv.index)
plt.title("top ipl venues")
plt.xlabel("matches")
plt.ylabel("venues")
plt.show()


#strike rate
batsman_runs=deliveries.groupby('batter')['batsman_runs'].sum()
balls_faced=deliveries.groupby('batter')['ball'].count()
strike_rate=pd.DataFrame({
    'Runs':batsman_runs,
    'Balls':balls_faced
})
strike_rate['StrikeRate']=(strike_rate['Runs']/strike_rate['Balls'])*100
strike_rate=strike_rate[strike_rate['Balls']>=500]
topstrike=strike_rate.sort_values(by='StrikeRate',ascending=False)
print(topstrike.head(10))
plt.figure(figsize=(12,6))
sns.barplot(
    x=topstrike.head(10)['StrikeRate'],
    y=topstrike.head(10).index
)
plt.title("top 10 ipl strike rate")
plt.xlabel("strikerate")
plt.ylabel("players")
plt.show()


#economy

runs_given=deliveries.groupby('bowler')['total_runs'].sum()
balls_bowled=deliveries.groupby('bowler')['ball'].count()
economy=pd.DataFrame({
    'RunsGiven':runs_given,
    "BallsBowled":balls_bowled
})
economy['Overs']=economy['BallsBowled']/6
economy['EconomyRate']=economy['RunsGiven']/economy['Overs']
economy=economy[economy['BallsBowled']>=500]
best_economy=economy.sort_values(by='EconomyRate')
print(best_economy.head(10))
plt.figure(figsize=(12,6))
sns.barplot(
    x=best_economy.head(10)['EconomyRate'],
    y=best_economy.head(10).index
)
plt.title("best economy")
plt.xlabel("economy rate")
plt.ylabel("bowlers")
plt.show()



teams_win.to_csv("output/team_win.csv")
top.to_csv("output/top_batsmen.csv")
tops.to_csv("output/top_bowlers.csv")
topstrike.head(10).to_csv("output/strike_rate.csv")
best_economy.head(10).to_csv("output/economy_rate.csv")