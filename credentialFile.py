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

  # def generate_password(self):

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




