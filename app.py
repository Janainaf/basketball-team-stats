import constants

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
            continue
        if player["experience"] == "YES":
            fixed["experience"]  = True
        else:
            fixed["experience"]  = False


        cleaned.append(fixed)

    print(cleaned)


if __name__ == "__main__":
    clean_data(constants)
   