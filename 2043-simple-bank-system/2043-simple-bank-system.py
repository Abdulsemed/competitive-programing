class Bank:
    def __init__(self, balance: List[int]):
        self.balance=[0]
        self.balance.extend(balance)
        self.size = len(balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.size or account2 > self.size:
            return False
        else:
            if self.balance[account1] - money >= 0:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
            else:
                return False
    def deposit(self, account: int, money: int) -> bool:
        if account <= self.size:
            self.balance[account] += money
            return True
        else:
            return False
    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.size:
            if self.balance[account] - money >= 0:
                self.balance[account] -= money
                return True
            else:
                return False
        else:
            return False
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)