'''
    File Name: test_useraccount.py
    Project Name: SimplePark
    Author: Colin Robbins
    Student Number: 400353539
    Date: 12/02/2020
    Class: SFWRTECH 3RQ3
    Professor: Sean Watson
    Purpose: used to run tests on the useraccount.py class
'''

from simplepark.useraccount import UserAccount

'''
Requirement 3.1.3: Saving a Username and Password
Testing: valid to invalid usernames and passswords, 
         they require:
         Username: Between 8 and 20 characters
         Password: >8 characters, special character, a capital
'''
#-----------------------------------------------------------
def test_username():
    valid_usernames = [
        "colinrobbins",
        "testuser01",
        "sfwrtech3rq3",
        "RagingBananaMonkey"
    ]

    userdefine = UserAccount()
    for username in valid_usernames:
        assert userdefine.verify_username(username) == True, "These usernames are all valid and work to the requirements"

def test_username_invalid():
    invalid_usernames = [
        "colinrobbinscoolboy3000justbecause",
        "hello",
        123,
        None
    ]
    
    userdefine = UserAccount()
    for username in invalid_usernames:
        assert userdefine.verify_username(username) == False, "the usernames do not follow between 8 and 20 characters, or does not exist"

def test_password():
    valid_passwords = [
        "Hello43!",
        "DoY0uEv3nTry?",
        "Wh@t$OneM0re?"
    ]
    
    userdefine = UserAccount()
    for password in valid_passwords:
        assert userdefine.verify_password(password) == True, "The password works perfectly for the requirements given"
        
def test_password_invalid():
    invalid_passwords = [
        "hello",
        "WhatDoIWantInLife",
        "????",
        "1234",
        None
    ]
    
    userdefine = UserAccount()
    for password in invalid_passwords:
        assert userdefine.verify_password(password) == True, "The password does not follow correct requirements for password creation."
#-----------------------------------------------------------