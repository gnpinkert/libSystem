class Employee:
    name = ""
    userID = ""
    password = ""
    booksOut = []

    def __init__(self, nameIn, userIDIn, passwordIn, booksIn):
        self.name = nameIn
        self.userID = userIDIn
        self.password = passwordIn
        for i in booksIn:
            self.booksOut.append(i.rstrip())

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

    def returnBook(self, titleIn):
        self.booksOut.remove(titleIn)
    
    def displayBooks(self):
        print("Book Titles: ")
        string = ""
        for i in self.booksOut:
            string += (i + ", ")
        print(string)
    
    def toString(self):
        print(("(Employee) Name: {}, username: {}, password: {}").format(self.name, self.userID, self.password))
        
    def writeEmployee(self, file):
        file.write(name)
        file.write(userID)
        file.write(password)
        file.write(accountType)
    