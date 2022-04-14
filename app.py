import constants
import random
import statistics 


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
 

if __name__ == "__main__":
    distributedTeams = balance_teams()

    while True:
        print("BASKETBALL TEAM STATS TOOL")
        print("---- MENU----")
        print("Here are your choices:")
        print("(A) Display Team Stats")
        print("(B) Quit")
        try:
            answer1 = input("")
            if answer1 != "A" and answer1 != "B" :
                print(answer1 == "A") 
                raise NameError
        except NameError:
            print("Not a menu option, please try again")
        else:
            if answer1 == "B":
                print("see you later")
                exit()
            if answer1 == "A":
                print("Enter an option:") 
                print("(A) Panthers")
                print("(B) Bandits")
                print("(C) Warriors")
            
                try:
                    answer = input(" " )
                    print(answer)
                    if answer != "A" and answer != "B" and answer != "C":
                        raise NameError
                except NameError:
                    print("Not a menu option, please try again2")
                else:
                    if answer == "A":
                        i = 2
                    if answer == "B":
                        i = 1
                    if answer == "C":
                        i = 0
                    print(f'Team: {distributedTeams[i]["TEAM"]} Stats')
                    print("--------------------")
                    print(f'Total players: {len(distributedTeams[i]["PLAYERS"])}')
                    experience = 0
                    inexperience = 0
                    for player in distributedTeams[i]["PLAYERS"]:  
                        if player["experience"] != False:
                            experience = experience +1 
                        else:
                            inexperience = inexperience +1 
                    print(f'Total experienced: {experience}')
                    print(f'Total inexperienced: {inexperience}')
                    height = []
                    for players in distributedTeams[0]["PLAYERS"]:   
                        height.append(players["height"])
                    avegare = statistics.mean(height)
                    print(f'Average height: {avegare}')
                    print("\n")
                    print(f'Players on Team:')
                    playersNames = []
                    for players in distributedTeams[i]["PLAYERS"]:  
                        playersNames.append(players["name"])
                    print(", ".join(playersNames))    
                    print("\n")
                    print(f'Guardians on Team:')
                    guardians = []
                    for players in distributedTeams[i]["PLAYERS"]:   
                        guardians.append(players["guardians"])
                        flat_list = [item for sublist in guardians for item in sublist]
                    print(", ".join(flat_list))    
                    print("\n")

