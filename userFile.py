class UserData:
  '''
  A class to that has everything to do with users data such new account and login
  '''
  users=[]

  def __init__(self,firstName,lastName,password):
    self.firstName = firstName
    self.lastName = lastName
    self.password = password