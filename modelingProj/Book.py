import datetime

class Book:
	#local variables
	title = "notSet"
	author = "notSet"
	subjectArea = "notSet"
	ISBN_Number = 0
	dateAdded = "notSet"
	numberOfCopies = 0
	reserve = False

	#Initializer
	def __init__(self, titleIn, authorIn, subjectIn, ISBN_In, dateIn, copiesIn):
		self.title = titleIn
		self.author = authorIn
		self.subjectArea = subjectIn
		self.ISBN_Number = ISBN_In
		self.dateAdded = dateIn
		self.numberOfCopies = int(copiesIn)

	#Setters
	def setTitle(self, titleIn):
		self.title = titleIn
	def setReserved(self):
		self.reserve = True
	def setNotReserved(self):
		self.reserve = False
	def setAuthor(self, authorIn):
		self.author = authorIn

	def setSubject(self, subjectIn):
		self.subjectArea = subjectIn

	def setISBN(self, ISBN_In):
		self.ISBN_Number = ISBN_In

	def setDateAdded(self, dateIn):
		self.dateAdded = dateIn

	def setNumCopies(self, copiesIn):
		self.numberOfCopies = copiesIn
	def incCopies(self):
		self.numberOfCopies += 1
	def decCopies(self):
		if self.numberOfCopies == 0:
			return False
		self.numberOfCopies -= 1
		return True

	#Getters
	def getTitle(self):
		return self.title

	def getAuthor(self):
		return self.author

	def getReseveStatus(self):
		if (reserve):
			return "Reserved"
		else:
			return "Not Reserved"

	def getSubject(self):
		return self.subjectArea

	def getISBN(self):
		return self.ISBN_Number

	def getDateAdded(self):
		return self.dateAdded

	def getNumCopies(self):
		return self.numberOfCopies
	

#Inherited Classes

class PhysicalBook(Book):
	#local variables
	numberOfTimesIssued = 0
	lastIssueDateTime = "notSet"
	typeB = None
	#Initializer
	def __init__(self, titleIn, authorIn, subjectIn, ISBN_In, dateIn, copiesIn,
					timesIssuedIn, lastIssueDateIn, typeIn):
		Book.__init__(self, titleIn, authorIn, subjectIn, ISBN_In, dateIn, copiesIn)
		self.numberOfTimesIssued = timesIssuedIn
		self.lastIssueDateTime = lastIssueDateIn
		self.typeB = typeIn

	#Setters
	def setTimesIssued(self, issueTimesIn):
		self.numberOfTimesIssued = issueTimesIn

	def setLastIssueDate(self, lastIssueDateIn):
		self.lastIssueDateTime = lastIssueDateIn

	#Getters
	def getTimesIssued(self):
		return self.numberOfTimesIssued

	def getLastIssueDate(self):
		return self.lastIssueDateTime

	def toString(self):
		return ("Author: " + self.author + " Title: " + self.title + " Copies Available: " + str(self.numberOfCopies))
	
	def getType(self):
		return self.typeB


class eBook(Book):
	#local variables
	numberOfTimesIssued = 0
	lastIssueDateTime = "notSet"
	typeB = None

	#Initializer
	def __init__(self, titleIn, authorIn, subjectIn, ISBN_In, dateIn, copiesIn,
					timesIssuedIn, lastIssueDateIn, typeIn):
		Book.__init__(self, titleIn, authorIn, subjectIn, ISBN_In, dateIn, copiesIn)
		self.numberOfTimesIssued = timesIssuedIn
		self.lastIssueDateTime = lastIssueDateIn
		self.typeB = typeIn
	#Setters
	def setTimesIssued(self, issueTimesIn):
		self.numberOfTimesIssued = issueTimesIn

	def setLastIssueDate(self, lastIssueDateIn):
		self.lastIssueDateTime = lastIssueDateIn

	#Getters
	def getTimesIssued(self):
		return self.numberOfTimesIssued

	def getLastIssueDate(self):
		return self.lastIssueDateTime

	def toString(self):
		return ("(eBook) Author: " + self.author + " Title: " + self.title + " Copies Available: " + str(self.numberOfCopies))
	def getType(self):
		return self.typeB