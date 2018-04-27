class Customer:
    name = ""
    userID = ""
    accountType = ""
    password = ""
    booksOut = []

    def __init__(self, nameIn, userIDIn, passwordIn):
        self.name = nameIn
        self.userID = userIDIn
        self.password = passwordIn
        self.accountType = "Member"

    def setName(self, nameIn):
        self.name = nameIn
    
    def setUserID(self, userIDIn):
        self.userID = userIDIn
    
    def setAccountType(self, accountTypeIn):
        self.accountType = accountTypeIn
    
    def setPassword(self, passwordIn):
        self.password = passwordIn
    
    def getUserID(self):
        return self.userID
    
    def getName(self):
        return self.name
    
    def getAccountType(self):
        return self.accountType
    
    def getPassword(self):
        return self.password

    def checkOut(self, bookIn):
        booksOut.append(bookIn)
        return true
    
    def toString(self):
        print(("(Customer) Name: {}, username: {}, password: {}").format(self.name, self.userID, self.password))

    def writeCustomer(self, file):
        file.write(name)
        file.write(userID)
        file.write(password)
        file.write(accountType)
    