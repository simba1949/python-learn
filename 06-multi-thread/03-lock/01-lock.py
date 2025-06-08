# 锁机制
import threading


# 银行账户
class BankAccount:
	def __init__(self):
		self.balance = 1000  # 账户余额
		self.lock = threading.Lock()

	# 存款
	def deposit(self, amount):
		try:
			if self.lock.acquire():  # 加锁
				print(threading.current_thread().name, 'locked deposit', "当前账号余额为：", self.balance)
				self.balance += amount
		finally:
			self.lock.release()  # 解锁
			print(threading.current_thread().name, 'unlocked deposit', "当前账号剩余余额为：", self.balance)

	# 提现
	def withdraw(self, amount):
		try:
			if self.lock.acquire():  # 加锁
				print(threading.current_thread().name, 'locked withdraw', "当前账号余额为：", self.balance)
				self.balance -= amount
				return True
			return False
		finally:
			self.lock.release()  # 解锁
			print(threading.current_thread().name, 'unlocked withdraw', "当前账号剩余余额为：", self.balance)


# 转账
def transfer(account_from, account_to, amount):
	if account_from.withdraw(amount):
		account_to.deposit(amount)


if __name__ == '__main__':
	account_from = BankAccount()
	account_to = BankAccount()
	for i in range(100):
		t = threading.Thread(target=transfer, args=(account_from, account_to, 10), name='Thread-%s' % i)
		t.start()
		t.join()
