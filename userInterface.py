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
def find_account(username):
  '''
  Function to find an account based on firstname which is the username
  '''
  return UserData.find_account(username)

def account_exists(username):
  '''
  Function that checks if an account exists
  '''
  return UserData.account_exists(username)

#The userInterface
def Interface():
  print("Welcome to PASSWORD LOCKER APP") 
  print('\n')

  print("Please Create An Account...")

  print("Enter Firstname...")
  firstName=input()
  print("Enter Lastname...")
  lastName=input()
  print("Create Password...")
  password=input()

  save_account(new_account(firstName,lastName,password))

  print(f"Congrast __ {firstName} __.Please Login to your freshh account...")
  print('\n')

  print("Enter firstname")
  user_name=input()
  print("Enter password")
  psswd_Login=input()

  if account_exists(user_name):
    account_found= find_account(user_name)
    if account_found.firstName == user_name and account_found.password==psswd_Login:
      print(f"Succesfully loged in as ....{user_name}...")    

      while True:
        print("")
    else:
      print("Try again")  

  

if __name__=='__main__':
  Interface()





  