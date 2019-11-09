import random
import string
class Credential_Sect:
  '''
  Blue print for all credentials
  '''
  credentials_list=[]

  def __init__(self,title,site_username,cred_password):
    '''
    Function to intialise the attributes of any credential.
    '''
    self.title=title
    self.site_username=site_username
    self.cred_password=cred_password

  def save_credential(self):
    '''
    Function to save any new credential
    '''
    Credential_Sect.credentials_list.append(self)

  @classmethod
  def generate_password(cls):
    '''
    Function that genetates random string
    '''
    Random_password= string.ascii_letters
    res=''.join(random.choice(Random_password) for i in range(6))
    return res
    
    

  @classmethod
  def display_credentials(cls):
    '''
    Function that shows all credentials that exist in ones account.
    '''
    return cls.credentials_list

  def delete_credential(self):
    '''
    Function that deletes an existing credential
    '''
    Credential_Sect.credentials_list.remove(self)


  @classmethod
  def find_credential(cls,site_username):
    '''
    Function to find an account based on firstname.
    '''
    for credential in cls.credentials_list:
      if credential.site_username == site_username:
        return credential

  @classmethod
  def credential_exists(cls,site_username):
    '''
    Function to check if an account exist by first name.
    '''
    for credential in cls.credentials_list:
      if credential.site_username == site_username:
        return True

    return False       


