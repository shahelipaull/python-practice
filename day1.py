def hellofn(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

#print(hellofn('hi', 'Shalu'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses=['math','science','history'] #this is a list
info={'name':'Shalu','age':'18'} #this is a dictionary

#student_info(*courses,**info) #unpacking of the arguments


month_days=['0','31','28','31','30','31','30','31','31','30','31','30','31']

def is_leap(year):
    return year%4==0 and (year%100 !=0 or year%400==0)


def days_in_month(year,month):
    if not 1<=month<=12:
        return 'Invalid Month'
    
    if month==2 and is_leap(year):
        return '29'
    
    return month_days[month]

#print(days_in_month(2020,0))

def price_average(*args):
    return sum(args)/len(args)

#print(price_average(20,40,60,70.45))

def build_profile(**kwargs):
    return kwargs

profile= build_profile(firstname='Shaheli',lastname='Paul', weight='45')
#print(profile)


def apply(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

"""print(apply(double, 5))   # 10
print(apply(square, 4))   # 16
print(apply(is_leap, 2020))  # True


- Create an account with an owner name and starting balance
- Deposit money
- Withdraw money (but block it if balance is too low)
- Show transaction history
- Transfer money to another account"""

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


account1 = BankAccount("Shaheli", 2000)
account2 = BankAccount("Supratik", 1000)

account1.deposit(500)
account1.withdraw(200)
account1.transfer(300, account2)

#print(account1.get_history())
#print(account2.get_history())

class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        maxprofit=0
        for price in prices
            if price<min:
                min=price
            elif maxprofit<price-min:
                maxprofit=price-min

        return maxprofit
        