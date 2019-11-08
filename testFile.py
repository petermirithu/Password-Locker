import unittest 
from userFile import UserData
from credentialFile import Credential_Sect

class TestAccount(unittest.TestCase):
  '''
  Test class that checks if test cases for each function are correct and accurate.
  '''
  def setUp(self):
    '''
    The method runs before each test to provide an existing account for our testing benefit.
    '''
    self.new_account = UserData("Pyra","Myra","Lexus007")
    self.new_credential= Credential_Sect("Twitter","pyra_myra","BMW2019")

  def test_init(self):
    '''
    Test case to see if the an object is initialized in a proper manner.
    '''
    #initialization for accounts in password locker
    self.assertEqual(self.new_account.firstName,"Pyra")
    self.assertEqual(self.new_account.lastName,"Myra")
    self.assertEqual(self.new_account.password,"Lexus007")
    
    #initilization for credetials
    self.assertEqual(self.new_credential.title,"Twitter")
    self.assertEqual(self.new_credential.site_username,"pyra_myra")
    self.assertEqual(self.new_credential.cred_password,"BMW2019")

  def test_save_account(self):
    '''
    Test case to check if we can save a new account in (user) list.
    '''
    self.new_account.save_account()
    self.assertEqual(len(UserData.users),1)

  def tearDown(self):
    '''
    Cleans up the (user) list which stores accounts
    '''
    UserData.users=[]

  def test_delete_account(self):
    '''
    Test case to check if we can delete our already existing account.
    '''
    self.new_account.save_account()

    another_account = UserData("Maxy","Jerry","Gery420")
    another_account.save_account()

    self.new_account.delete_account()
    self.assertEqual(len(UserData.users),1)

  def test_find_account(self):
    '''
    Test case to check if we can find an account in our user list by firstname.
    '''
    self.new_account.save_account()

    another_account = UserData("Maxy","Jerry","Gery420")
    another_account.save_account()

    found_account=UserData.find_account("Maxy")
    self.assertEqual(found_account.firstName,another_account.firstName)



  def test_account_exists(self):
    '''
    Test case to check if an account exits .
    '''
    self.new_account.save_account()

    another_account = UserData("Maxy","Jerry","Gery420")
    another_account.save_account()

    account_exists= UserData.account_exists("Maxy")
    self.assertTrue(account_exists)


    
    
if __name__ == '__main__':
  unittest.main()