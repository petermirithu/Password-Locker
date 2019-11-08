#!/usr/bin/env python3.6
from userFile import UserData

def new_account(firstName,lastName,password):
  '''
  Function to create a new account
  '''
  new_account=UserData(firstName,lastName,password)
  return new_account

def save_account(userFile):
  '''
  Function that saves a new account
  '''
  userFile.save_account()

def delete_account(userFile):
  '''
  Function to delete only an existing account
  '''
  userFile.delete_account()

def account_exists(username):
  '''
  Function that checks if an account exists
  '''
  return UserData.account_exists(username)

#The userInterface
def Interface():
   


  