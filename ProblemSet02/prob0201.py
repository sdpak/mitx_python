
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
minPayment = 0
unPaidBalance = 0
monthlyInterest = (annualInterestRate/12)

while month < 12:

    minPayment = balance*(monthlyPaymentRate)
    #print("min payment", minPayment)
    unPaidBalance = balance - minPayment
    #print("Unpaid balance:",unPaidBalance)
    Interest = unPaidBalance*monthlyInterest
    #print("Interest amount:", comingInterest)
    balance = unPaidBalance + Interest
    month = month + 1
    #print("Total Balance", balance)


print("Remaining balance:",str(round(balance,2)))