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
  Function that generates a random string which is a password
  '''
  credentialFile.generate_password()

def display_credential():
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
  password_log=input()

  save_account(new_account(firstName,lastName,password_log))

  print(f"Congrast __ {firstName} __.Please Login to your fresh account...")
  print('\n')

  print("Enter firstname")
  user_name_Log=input()
  print("Enter password")
  psswd_Login=input()

  if account_exists(user_name_Log):
    account_found= find_account(user_name_Log)
    if account_found.firstName == user_name_Log and account_found.password==psswd_Login:
      print(f"Succesfully loged in as ....{user_name_Log}...")
      print('\n')    

      while True:
        print('~*~'*30)
        print(f"Welcome --- {firstName} --- to your PassWord Locker!")
        print('\n')

        print("Use this codes to navigate arround your Account.")
        print("sc --Store already existing credential")  
        print("nc --Create a new credential ")
        print("dsp --Showcase all existing credentials")
        print("dlt --Delete a credential")
        print("exit --Exit the App")
        print("Enter code-------------------------")
        code_in=input().lower()

        if code_in == 'sc':
          print("Store Your Credential")
          print("------------------------------------------------------------------")

          print("Site Name")
          site_name=input()

          print("User Name")
          user_name=input()

          print("Password")
          password=input()

          save_credential(new_credential(site_name,user_name,password))
          print('\n')
          print(f"New credential for --- {site_name} --- created.")
          print('\n')

        elif code_in == 'nc':
          print("Create a new credential")
          print("-------------------------------------------------------------------")

          print("Enter Site name")
          site_name2=input()

          print("Enter User name")
          user_name2=input()

          print("Would you want me generate a password for you?")
          print("key in_________:y --for Yes_______:n --for No")
          print("Enter y/n")
          pass_ans=input().lower()

          if pass_ans == 'y':
            
            pass_Gen = generate_password()          
            print("Here is your password......")
            print('\n')

            print(f" ____ {pass_Gen} ____")
            print('\n')  

            save_credential(new_credential(site_name2,user_name2,pass_Gen))

          elif pass_ans == 'n':  

            print("Enter your password...")
            pass_Input =input()

            save_credential(new_credential(site_name2,user_name2,pass_Input))

          else:
            print('\n')
            print("Did not get what you typed")  
            print('\n')

        elif code_in =='dsp':
          if display_credential():
            print('^'*50)
            print("Available credentials...")
            print('\n')

            for cred in display_credential():
              print(f"{cred.title}  {cred.site_username}  {cred.cred_password}")
              print('\n')
              print('^'*50)  
          else:
            print('\n')
            print("You dont have any credentials saved")      
            print('\n')
            print('^'*50)
        
        elif code_in == 'dlt':
          print("To Delete......search the credential you want to delete")
          
          if display_credential():
            print('^'*50)
            print("Available credentials...")
            print('\n')

            for cred in display_credential():
              print(f"{cred.title}  {cred.site_username}  {cred.cred_password}")
              print('\n')
              print('^'*50)  

              print("Enter the user_name for that credential to search...")  
              search=input()
              if credential_exists(search):
                search_result=find_credential(search)
                print(f"{search_result.title}  {search_result.site_username} {search_result.cred_password}")
                print("^"*50)
                print('\n')

                print("Enter y/n to delete this credential")
                yes_no=input().lower()
                if yes_no == 'y':
                  search_result.delete_credential()
                else:
                  print("Your lucky I never deleted it.")  
              else:
                print("Credential does not exist !!!")    

          else:
            print('\n')
            print("You dont have any credentials to delete!!!!")      
            print('\n')
            print('^'*50)

          
        elif code_in =='exit':
          print("It was nice hosting you here...your welcome again...")
          print('-'*100)
          break

        else:
          print("That code does not exist.Please use what I have provided!!")
    else:
      print("Incorrect Login Details......................")  

  

if __name__=='__main__':
  Interface()





  