from modAccount import*

a1 = Account("Bell", 100, date(2000,7,1))

print("Account info for a1: ", a1)

#note: date not print 7/1/2016

print("Testing getters for a1: ")

bNmae= input(" ")

openBal = input(" ")

openDay = input("day: ")

openMonth = input(" ")

openDate = date(OpenYear, openMonth, openDay)

a2 = Acount(bName, openBal, openDate)

print("Info for a2 is: ", a2)

==========================================
#strftime method to format date

d1 = date(2000, 7, 1)

#jan 7, 2000

tmpStr= d1.strftime("%b %d, %Y ")

print(tmpstr)

#5 zips: modAccount.py, testAccount.py, testCheckingAcct.py, testSavings.py, menu.py
#Main Menu
#1 checkings
#2 Savings
#3 Quit

##--------------
##checking
##1) create a checking account
##2) print account info
##3) deposit
##4) withdraw: yes/no, error checking for negative number
##5)print total withdrawals
##6) print total deposits
##7) print current Balance
##8)back to main menu

##-----------------------------
##Savings
####1) create a saving account
##2) close account. (ask date, subtract date and see if they\
##                   can do that in terms of maturity date)
##3) calculate interest
##4)print account info
##5)back to main menu
