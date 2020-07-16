class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
    
class Checking(Account):
    """This class generates checking accounts objects"""
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount, transfer_to):
        self.balance = self.balance - amount - self.fee
        transfer_to.deposit(amount)

    


checking_acc1 = Checking(r"Exercises\Section 24\account\acc1.txt", 1)
checking_acc2 = Checking(r"Exercises\Section 24\account\acc2.txt", 1)

print("Account 1 " + str(checking_acc1.balance))
print("Account 2 " + str(checking_acc2.balance))
checking_acc1.transfer(20, checking_acc2)
print("Account 1: " + str(checking_acc1.balance))
print("Account 2: " + str(checking_acc2.balance))
checking_acc1.commit()
checking_acc2.commit()
