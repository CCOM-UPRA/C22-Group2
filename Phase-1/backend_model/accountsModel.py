import json
import os
from pathlib import Path
# Hacky fix
path = Path(__file__).parent.parent.absolute()
usersPath = str(path) + '\\UserData\\users.json'

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

# Get all accounts
def getaccountsmodel():
    with open(usersPath, "r") as f:
        data = json.load(f)
    return dict(data)


# Get the specific account requested
# In this case, we're requesting it via the key
def getaccountmodel(acc):
    with open(usersPath, "r") as f:
        data = json.load(f)
    
    for key, user in dict(data).items():
        if key == acc:
            return user

def addaccountmodel(acc : dict):
    currentFile = getaccountsmodel()
    lastKey = int(list(currentFile)[-1])
    newKey = lastKey + 1

    newEntry = {str(newKey):dict(acc)}


    currentFile = MagerDicts(currentFile, newEntry)

    with open(usersPath, "w") as f:
        json.dump(currentFile, f)
    
    return currentFile

# TODO access admin "database"
def getadmin():
    return

#print(getaccountsmodel())
#print("sus")
#print(userList)
#print(getaccountmodel('1'))
#addaccountmodel(dictUser2)