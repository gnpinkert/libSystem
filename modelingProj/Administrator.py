#Inherited from Employee

class Administrator():
	name = ""
	userID = ""
	password = ""

	def __init__(self, nameIn, userIDIn, passwordIn):
	    self.name = nameIn
	    self.userID = userIDIn
	    self.password = passwordIn

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
    
	def toString(self):
		print(("(Admin) Name: {}, username: {}, password: {}").format(self.name, self.userID, self.password))

	def writeAdministrator(self, file):
	    file.write(name)
	    file.write(userID)
	    file.write(password)
	    file.write(accountType)
