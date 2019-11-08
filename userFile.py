class UserData:
  '''
  A class to that has everything to do with users data such new account and login
  '''
  users=[]

  def __init__(self,firstName,lastName,password):
    '''
    A function that initialise the attributes of a new account in Passwordlocker.
    '''
    self.firstName = firstName
    self.lastName = lastName
    self.password = password

  def save_account(self):
    '''
    Function that saves a new account to the password locker app
    '''
    UserData.users.append(self)    