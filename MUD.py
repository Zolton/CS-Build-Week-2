import requests
from secrets import token

token = token()
#print(token)


def init():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"

    HEADERS = {"Authorization": f"Token {token}"}
    response = requests.get(url = URL, headers = HEADERS)
    #print(response)
    data = response.json()
    return data
    

def move(direction):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"direction":f"{direction}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data
    #print("cooldown--- ", data["cooldown"])

#init()
# move("w")
# move("e")

def fastMove(direction, nextRoomNumber):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"direction":f"{direction}", "next_room_id": f"{nextRoomNumber}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    print("cooldown for movement is:    ", data["cooldown"])
    for i in data["exits"]:
        print("exit is: ", i)
    return data
    #print("exits are:    ", data["exits"][0][1][2][3][4])
#init()
#fastMove("w", "1")

def pickUpTreasure(treasureName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{treasureName}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    # print("response from sesrsver: ", data)
    return data

def dropTreasure(treasureName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{treasureName}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def offerTreasureForSale(treasureName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{treasureName}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def sellTreasure(treasureName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{treasureName}", "confirm":"yes"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def checkInventory():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/status/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)
    return data

def examine(playerChoice):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{playerChoice}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def equipItem(equipItem):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{equipItem}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def unequipItem(unequipItem):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/undress/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{unequipItem}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def changeName(newName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{newName}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    data = response.json()
    return data

def confirmName(newName):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{newName}", "confirm":"aye"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    #print(response)
    data = response.json()
    #print(data)
    return data

def pray():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)
    return data

def fly(direction):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"direction":f"{direction}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def dash():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"direction":"n", "num_rooms":"5", "next_room_ids":"10,19,20,63,72"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def giveToGhost(ghostGiveItem):
    # Holds 1 item ONLY - heaviest item
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"name":f"{ghostGiveItem}"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def takeFromGhost():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)
    return data

def mine(newProof):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/"
    HEADERS = {"Authorization": f"Token {token}", "Content-Type": "application/json"
    }
    DATA = {"proof":newProof}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)
    return data

def lastProof():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/"
    HEADERS = {"Authorization": f"Token {token}"}
    response = requests.get(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)
    return data

def lambdaCoinBalance():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/"
    HEADERS = {"Authorization": f"Token {token}"}
    response = requests.get(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)
    return data