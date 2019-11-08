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
    




