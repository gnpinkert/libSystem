class Customer:
    name = ""
    userID = ""
    accountType = ""
    password = ""
    booksOut = []

    def __init__(self, nameIn, userIDIn, passwordIn, booksIn):
        self.name = nameIn
        self.userID = userIDIn
        self.password = passwordIn
        self.accountType = "Member"
        for i in booksIn:
            self.booksOut.append(i)

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
        self.booksOut.append(bookIn.getTitle())
        return True
    def returnBook(self, titleIn):
        self.booksOut.remove(titleIn)
    def displayBooks(self):
        print("Book Titles: ")
        for i in self.booksOut:
            print(i + ", ")
    
    def toString(self):
        print("(Customer) Name: " + self.name + "username: " + self.userID + "password: " + self.password)

    def writeCustomer(self, file):
        file.write(name)
        file.write(userID)
        file.write(password)
        file.write(accountType)
    