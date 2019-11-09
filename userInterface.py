#!/usr/bin/env python3.6
from userFile import UserData
from credentialFile import Credential_Sect

#User account section--------------------------------------------------------------------
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


#credential section---------------------------------------------------------------------
def new_credential(title,site_username,cred_password):
  '''
  Function to that create a new credential
  '''
  new_credential=Credential_Sect(title,site_username,cred_password)
  return new_credential

def save_credential(credentialFile):
  '''
  Function that saves a credential
  '''
  credentialFile.save_credential()

def generate_password(credentialFile):
  '''
  Function that generates a randow=m string which is a password
  '''
  credentialFile.generate_password()

def display_credentials():
  '''
  Function that displays all credentials existing
  '''
  return Credential_Sect.display_credentials()

def delete_credential(credentialFile):
  '''
  Function that deletes existing credential
  '''
  credentialFile.delete_credential()

def find_credential(site_username):
  '''
  Function that find a credential
  '''
  return Credential_Sect.find_credential(site_username)

def credential_exists(site_username):
  '''
  Function that checks if a credential exists
  '''
  return Credential_Sect.credential_exists(site_username)

  
#The userInterface--------------------------------------------------------------------
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

  print(f"Congrast __ {firstName} __.Please Login to your fresh account...")
  print('\n')

  print("Enter firstname")
  user_name=input()
  print("Enter password")
  psswd_Login=input()

  if account_exists(user_name):
    account_found= find_account(user_name)
    if account_found.firstName == user_name and account_found.password==psswd_Login:
      print(f"Succesfully loged in as ....{user_name}...")
      print('\n')    

      while True:
        print(f"Welcome --- {user_name} --- to your PassWord Locker!")
        print('\n')

        print("Use this codes to navigate arround your Account.")
        print("sc --Store already existing credential __")  
        print("nc --Create a new credential __")
        print("dsp --Showcase all existing credentials __")
        print("dlt --Delete a credential __")
        print("exit --Exit the App __")
        print("Enter code-------------------------")
        code_in=input().lower()

        if code == 'sc':
          print("Store Your Credential")
          print("------------------------------------------------------------------")

          print("Site Name")
          site_name=input()

          print("User Name")
          user_name=input()

          print("Password")
          password=input()

          save_credential(new_credential(site_username,user_name,password))
          print('\n')
          print(f"New credential for --- {site_name} --- created.")
          print('\n')

        elif code == 'nc':
          print("Create a new credential")
          print("-------------------------------------------------------------------")

          print("Enter Site name")
          site_name=input()

          print("Enter User name")
          user_name=input()

          print("Would you want me generate a password for you?")
          print("key in_________:y --for Yes_______:n --for No")
          print("Enter y/n")
          pass_ans=input().lower()

          if pass_ans == 'y':
            
            passGen=generate_password()          
            print("Here is your password......")
            print('\n')

            print(f" ____ {pass_ans} ____")



          if 


        else:
          print("That code does not exist.Please use what I have provided!!")
    else:
      print("Try again")  

  

if __name__=='__main__':
  Interface()





  