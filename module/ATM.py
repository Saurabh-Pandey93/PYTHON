import Password
import balance
import Deposit
import withdraw


print(Password.Pass)


print(balance.Amount)

print(Deposit.Deposit)
increased_balance = balance.Amount + Deposit.Deposit
print(increased_balance)

print(withdraw.withdraw_Amount)

remaining_balance = balance.Amount - withdraw.withdraw_Amount
print(remaining_balance)