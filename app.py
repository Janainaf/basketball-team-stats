import constants
import random


def clean_data(constants):
    cleaned = []
    for player in constants.PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["height"] = int(player["height"].split(" ")[0])
        fixed["guardians"] = [player["guardians"].split(" and ")[0]]
        try:
            fixed["guardians"].append(player["guardians"].split(" and ")[1])
        except:
            pass
        if player["experience"] == "YES":
            fixed["experience"]  = True
        else:
            fixed["experience"]  = False
        cleaned.append(fixed)
    return cleaned


def balance_teams():
    players = clean_data(constants)
    teams = constants.TEAMS 
    num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))
    distributedTeams = []

    for team in teams:
        finalTeams = {}
        finalTeams["TEAM"] = team
        finalTeams["PLAYERS"] = random.sample(players, num_players_team )
        distributedTeams.append(finalTeams)
        
    return distributedTeams
 

# if __name__ == "__main__":
#     balance_teams()

distributedTeams = balance_teams()
print("BASKETBALL TEAM STATS TOOL")
print("---- MENU----")
print("Here are your choices:")
print("(A) Display Team Stats")
print("(B) Quit")


print("Enter an option:") 
print("(A) Panthers")
print("(B) Bandits")
print("(C) Warriors")

answer = input("Enter an option:") 
if answer == "A":
    print(f'Team: {distributedTeams[2]["TEAM"]}')
    print("--------------------")
    print(f'Total players: {len(distributedTeams[2]["PLAYERS"])}')
    print(f'Total experienced: {len(distributedTeams[2]["PLAYERS"])}')
    print(f'Total inexperienced: {len(distributedTeams[2]["PLAYERS"])}')
    print(f'Average height: {len(distributedTeams[2]["PLAYERS"])}')
    print(f'Players on Team:')
    for players in distributedTeams[2]["PLAYERS"]:
        print(players["name"], end =", ")
    print("\n")
    print(f'Guardians on Team:')
    for players in distributedTeams[2]["PLAYERS"]:      
        print(players["guardians"], end =", ")

if answer == "B":
    print(f'Team: {distributedTeams[1]["TEAM"]}')
    print("--------------------")
    print(f'Total players: {len(distributedTeams[1]["PLAYERS"])}')
    print(f'Total experienced: {len(distributedTeams[1]["PLAYERS"])}')
    print(f'Total inexperienced: {len(distributedTeams[1]["PLAYERS"])}')
    print(f'Average height: {len(distributedTeams[1]["PLAYERS"])}')
    print(f'Players on Team:')
    for players in distributedTeams[1]["PLAYERS"]:
        print(players["name"], end =", ")
    print("\n")
    print(f'Guardians on Team:')
    for players in distributedTeams[1]["PLAYERS"]:      
        print(players["guardians"], end =", ")


if answer == "C":
    print(f'Team: {distributedTeams[0]["TEAM"]}')
    print("--------------------")
    print(f'Total players: {len(distributedTeams[0]["PLAYERS"])}')
    print(f'Total experienced: {len(distributedTeams[0]["PLAYERS"])}')
    print(f'Total inexperienced: {len(distributedTeams[0]["PLAYERS"])}')
    print(f'Average height: {len(distributedTeams[0]["PLAYERS"])}')
    print(f'Players on Team:')
    for players in distributedTeams[0]["PLAYERS"]:  
        print(players["name"], end =", ")
    print("\n")
    print(f'Guardians on Team:')
    for players in distributedTeams[0]["PLAYERS"]:      
        print(players["guardians"], end =", ")



# Team: Panthers Stats
# --------------------
# Total players: 6
# Total experienced: 3
# Total inexperienced: 3
# Average height: 42.5

# Players on Team:
#   Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith

# Guardians:
#   Heather Bledsoe, David Alaska, Jamie Alaska, Thomas Helm, Eva Jones, Henrietta Dumas, Hyman Krustofski, Rachel Krustofski, Jim Smith, Jan Smith

# Press ENTER to continue...