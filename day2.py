#day 2 - june 8
#OOP part 2 -  inheritance
#starting 9am
"""
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            # Checking a set takes O(1) time
            if num in seen:
                return True
            seen.add(num)
            
        return False

"""
"""

#idk what
from collections import Counter

def findMinOperations(centers):
    n= len(centers)

    freq=Counter(centers)
    mx=max(freq.value())

    if n-mx<mx:
        return mx
    
    return n+1//2

"""

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transactions=[]


    def deposit(self,dmoney):
        self.balance+=dmoney
        self.transactions.append(('deposit',dmoney))
        return self.balance

    def withdraw(self, wmoney):
        if self.balance - wmoney < 500:
            return 'Cannot go below minimum balance of 500'
    
        if wmoney>self.balance:
            return 'Insufficient Balance'
        
        self.balance-=wmoney
        self.transactions.append(('withdraw',wmoney))
        return self.balance
    
    def get_history(self):
        return self.transactions
    

    """Transferring 500 from account A to account B is just two things — 
    withdraw 500 from A, deposit 500 into B. 
    You already have both those methods. 
    So transfer is literally just calling them."""
    def transfer(self,amount, other_account):
        self.withdraw(amount)
        other_account.deposit(amount)

class SavingsAccount(BankAccount):

    
    def __init__(self, name, balance, interestRate=0.05):
        super().__init__(name, balance)
        self.interestRate= interestRate

    def apply_interest(self):
        interest = int(self.balance * self.interestRate)
        self.deposit(interest)
        return interest



# account1 = SavingsAccount("Shaheli", 2000)
# print(account1.apply_interest())
# print(account1.balance)      # should show 2100.0 after interest
# print(account1.get_history()) # should show the interest deposit in history
# account2 = BankAccount("Supratik", 1000)

# # account1.deposit(500)
# account1.withdraw(200)
# account1.transfer(300, account2)

#print(account1.get_history())
#print(account2.get_history())

class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit= overdraft_limit

    def withdraw(self, wmoney):
        if self.balance - wmoney < self.overdraft_limit:
            return f'Cannot go below overdraft limit of {self.overdraft_limit}'   
        
        self.balance-=wmoney
        self.transactions.append(('withdraw',wmoney))
        return self.balance
    
acc1 = SavingsAccount("Shaheli", 2000)
acc2 = CurrentAccount("Rahul", 1000, -500)
acc3 = BankAccount("Supratik", 3000)

acc1.apply_interest()
acc2.withdraw(1400)  # should work, stays above -500
acc2.withdraw(200)   # should block, would go below -500

print(acc1.get_history())
print(acc2.get_history())
