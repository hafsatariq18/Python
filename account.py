class Account:
  def __init__(self,bal,acc):
   self.balance=bal
   self.account_no=acc


  def debit(self,amount):
    self.balance -=amount
    print("Rs,",amount,"was debited from your account")
    print("Total balance =",self.get_balance())

  def credit(self,amount):
    self.balance +=amount
    print("Rs,",amount,"was credited to your account")
    print("Total balance =",self.get_balance())

  def get_balance(self):
   return self.balance