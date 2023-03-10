import json
from random import randrange

usersPath = './UserData/users.json'
adminsPath = './UserData/admins.json'

# Merge dictionaries
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

# Assigns key to account and adds to json
def addaccountmodel(acc : dict, admin = False):
    path = adminsPath if admin else usersPath
    currentFile = getaccountsmodel(admin=admin)
    # assign new key to account
    newKey = randrange(0, 999999999)
    while(newKey in currentFile.keys()):
        newKey = randrange(0, 999999999)

    newEntry = {str(newKey):dict(acc)}
    # add account to dictionary
    currentFile = MagerDicts(currentFile, newEntry)
    # write to json
    with open(path, "w") as f:
        json.dump(currentFile, f)

# Edits the user account
def editaccountmodel(acc, edits:dict, admin = False):
    path = adminsPath if admin else usersPath
    users = getaccountsmodel(admin=admin)

    for key in edits.keys():
        if key in users[acc] and edits[key] != None:
            users.get(acc)[key] = edits[key]
    
    with open(path, "w") as f:
        json.dump(users, f)
 
 # Pop account 
def deleteaccountmodel(acc : str, admin = False):
    path = adminsPath if admin else usersPath
    currentUsers = getaccountsmodel(admin=admin).pop(acc)
    # write to json
    with open(path, "w") as f:
        json.dump(currentUsers, f)
