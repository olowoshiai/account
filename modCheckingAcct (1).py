class CheckingAcct(Account):
    _totalDeposits = 0
    _totalWithdrawals = 0
    def __init__(self, tmpBankName, tmpOpenBal,tmpDateOpened):
        Account.__init__(self, tmpBankName, tmpOpenBal,tmpDateOpened)
        self._acctType = "checking"
        CheckingAcct._totalDeposits += 1
        CheckingAcct._totalWithdrwals +=1
    def deposit(self, amount):
        
        
        
