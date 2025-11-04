class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 >= 1 and account1 <= self.n and account2 >= 1 and account2 <= self.n:
            if self.balance[account1-1] >= money:
                self.balance[account1-1] = self.balance[account1-1] - money
                self.balance[account2-1] = self.balance[account2-1] + money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account >= 1 and account <= self.n :
            self.balance[account-1] = self.balance[account-1] + money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account >= 1 and account <= self.n :
            if self.balance[account-1] >= money:
                self.balance[account-1] = self.balance[account-1] - money
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