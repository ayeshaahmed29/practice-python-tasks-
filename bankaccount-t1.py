import logging 
logging.basicConfig(filename='account.log', level=logging.INFO, format='%(asctime)s: %(message)s' )

class BankAccount:
   def __init__(self, account_holder: str, balance: float):
      self.account_holder=account_holder
      self.balance=balance
    
   def deposit(self, amount: float):
      try:
         if(amount<0):
            raise Exception
      except Exception:
         logging.error('ERROR - Deposit failed: Negative amount {} for account {}'.format(amount, self.account_holder))

      else:
         self.balance =float(self.balance + amount)
         logging.info('SUCCESS - Deposit of {} to account {} completed.'.format(amount, self.account_holder))
      

   def withdraw(self, amount: float): 
      try:
         if(amount>self.balance):
            raise Exception
      except Exception:
         logging.error('ERROR - Withdrawal failed: Insufficient balance for account {}'.format(self.account_holder))
    
      else:
         self.balance =float(self.balance + amount)
         logging.info('SUCCESS - Withdrawal of {} from account {} completed'.format(amount, self.account_holder))

   def get_balance(self):
      return self.balance
   
   
def transactions(account: BankAccount):
   account.deposit(-5.00)
   account.withdraw(1000)
   account.deposit(40)
   account.withdraw(20)

acc1= BankAccount("Ayesha",500)
print(acc1.get_balance())
print('the balance of {0.account_holder} is {0.balance}'.format(acc1))
transactions(acc1)


