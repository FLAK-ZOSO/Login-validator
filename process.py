#!/usr/bin/python3
import json
import exceptions as e


def signUp(username: str, password: str, confirm: str) -> bool:
    # Returns True when the sign-up was successful
    # Returns False when the account was already existing
    # Raises PasswordException when the password wasn't confirmed
    if (password != confirm):
        raise e.PasswordException
    
    with open('data.json', 'r+') as data:
        new_dict = json.load(data)
        if (username in new_dict.keys()):
            return False
        new_dict[username] = {"password": password, "logged-in": False}
        json.dump(new_dict, data)
    return True


def login(username: str, password: str) -> bool:
    # Returns True when the login was successful
    # False when the account was already logged in
    # Raises an AccountException when the account doesn't exist
    # Raises a PasswordException when the password is wrong
    with open('data.json', 'r+') as data:
        new_dict = json.load(data)
        if (not username in new_dict.keys()):
            raise e.AccountException
        if (new_dict[username]["logged-in"]):
            return False
        if (password != new_dict[username]["password"]):
            raise e.PasswordException
        new_dict[username]["logged-in"] = True
        json.dump(new_dict, data)
    return True


def logout(username: str) -> None:
    with open('data.json', 'r+') as data:
        new_dict = json.load(data)
        new_dict[username]["logged-in"] = False
        json.dump(new_dict, data)