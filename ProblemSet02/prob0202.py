balance = 3329
annualInterestRate = 0.2

minBlock = 0.01

monthlyInterestRate = annualInterestRate/12
unPaidBalance = 0

actualBalance = balance
balanceDiff = 0
floor = balance/12
ceiling = (balance * (1+monthlyInterestRate)**12)/12
minPayment = (floor+ceiling)/2

while abs(balance)>=minBlock:
    balance = actualBalance
    minPayment = minPayment + 10
    for month in range(0, 12):
        unPaidBalance = balance - minPayment
        Interest = unPaidBalance * monthlyInterestRate
        balance = unPaidBalance + Interest
        month += 1
    if balance > 0:
        floor = minPayment
    else:
        ceiling = minPayment
    minPayment = round (minPayment,2)

print("Lowest Payment:",minPayment)