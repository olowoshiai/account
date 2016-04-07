class Account:
    _lastAcctNumUsed = 100

    def __init__(self, tmpBankName, tmpOpenBal,tmpDateOpened):
        self._AcctNumber = Account._lastAcctNumUsed
        Account._lastAcctNumUsed += 1
        self._BankName = tmpBankName
        self._acctType = "general"
        self._openingBalance = tmpOpenBal
        self._CurrentBalance =  tmpOpenBal
        self._DateOpened = tmpDateOpened


    def toString(self):
        tmp = "Bank Name: " + str(self._tmpBankName) + "\n"\
               "Account Type: " + str(self._tmpAcctType) + "\n" \
               "Opening Balance: " + str(self._tmpOpenBal) + "\n"\
               "Current Balance: " + str(self._tmpCurBal) + "\n"\
               "Date Opened: " +str(self._DateOPened)
        return tmp

    def getAcctNumber(self):
        return self._AcctNumber
    def getBankName(self):
        return self._BankName
    def getacctType(self):
        return self._RoomHeight

##
##    def setRoomLenght(self, tmplength):
##        self._Roomlength = tmplenght
##
##    def setRoomWidth(self, tmpWidth):
##       self._RoomWidth = tmpWidth
##
##    def setRoomHeight(self, tmpheight):
##        self._RoomHeight = tmpheight
##
