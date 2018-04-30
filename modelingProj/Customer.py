import time
class Customer:
    name = ""
    userID = ""
    accountType = ""
    password = ""
    booksOut = []
    count = 0

    def __init__(self, nameIn, userIDIn, passwordIn):
        self.name = nameIn
        self.userID = userIDIn
        self.password = passwordIn
        self.accountType = "Member"


    def addBook(self, bookIn):
        self.booksOut = bookIn
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
    def getBooks(self):
        return self.booksOut
    def displayBooks(self):
        print("Book Titles: ")
        string = ""
        for i in self.booksOut:
            string += (i + ", ")
        print(string)
    
    def toString(self):
        print("(Customer) Name: " + self.name + ", Account Type" + self.accountType + ", Username:  " + self.userID)

    def writeCustomer(self, file):
        file.write(name)
        file.write(userID)
        file.write(password)
        file.write(accountType)
    