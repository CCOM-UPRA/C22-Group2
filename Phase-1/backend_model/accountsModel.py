import json
#import os
#from pathlib import Path
# Hacky fix
# path = Path(__file__).parent.parent.absolute()
usersPath = './UserData/users.json'
adminsPath = './UserData/admins.json'

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

# Get all accounts
def getaccountsmodel(admin = False):
    path = adminsPath if admin else usersPath
    with open(path, "r") as f:
        data = json.load(f)
    return dict(data)


# Get the specific account requested
# In this case, we're requesting it via the key
def getaccountmodel(acc, admin = False):
    path = adminsPath if admin else usersPath
    with open(path, "r") as f:
        data = json.load(f)
    
    for key, user in dict(data).items():
        if key == acc:
            return user

def addaccountmodel(acc : dict, admin = False):
    path = adminsPath if admin else usersPath
    currentFile = getaccountsmodel(admin=admin)
    # assign new key to account
    lastKey = int(list(currentFile)[-1])
    newKey = lastKey + 1

    newEntry = {str(newKey):dict(acc)}
    # add account to dictionary
    currentFile = MagerDicts(currentFile, newEntry)
    # write to json
    with open(path, "w") as f:
        json.dump(currentFile, f)

# Edits the user account
def editaccountmodel(acc, edits:dict, admin = False):
    currentUser = getaccountmodel(acc, admin=admin)

    for key in dict(currentUser).keys():
        if key in edits.keys():
            dict(currentUser)[key] = edits[key]

    deleteaccountmodel(currentUser)
    addaccountmodel(currentUser)
    
        
def deleteaccountmodel(acc, admin = False):
    path = adminsPath if admin else usersPath
    currentUsers = getaccountsmodel(admin=admin)
    currentUsers.pop(acc)
    # write to json
    with open(path, "w") as f:
        json.dump(currentUsers, f)




