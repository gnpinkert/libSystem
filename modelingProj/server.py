import Administrator
import Customer
import Employee
import Book



class Server:
	
	userObjects = []
	bookObjects = []
	ebookObjects = []
	adminObjects = []
	employeeObjects = []
	allEmployees = []

	def __init__(self):
		self.loadCustomer()
		self.loadBooks()
		self.loadEbook()
		self.loadAdmin()
		self.loadEmployee()
		allEmployees = adminObjects + employeeObjects

	def writeAll(self):
		self.writeEmployee(employeeObjects)
		self.writeCustomer(customerObjects)
		self.writeAdmin(adminObjects)
		self.writeBook(bookObjects)
		self.writeEBook(ebookObjects)


	def searchBook(self, titleIn):
		for i in ebookObjects:
			if i.title = titleIn:
				found = i
				ebookObjects.remove(i)
				return found, "EBook"
		for i in bookObjects:
			if i.title = titleIn
				found = i
				bookObjects.remove(i)
				return found, "Physical Book"
		else:
			return None

	def checkOutBook(self, bookIn):
		if bookIn.decCopies() == False:
			return False

	def checkInBook(self, bookIn):
		bookIn.incCopies()
		return True
	
	def login(self, usernameIn, passwordIn):
		for i in userObjects:
			if i.username == usernameIn && i.password = passwordIn
				return True
		return False

	def bookInfo(self, book):
		print book.toString()
		return True
	
	def addBook(self, bookIn, typeIn):
		if typeIn = 1:
			ebookObjects.append(bookIn)
		else:
			ebookObjects.append(bookIn)
		return True

	def addCustomer(self, customerIn):
		customerObjects.append(customerIn)

	def addEmployee(self, employeeIn):
		employeeObjects.append(employeeIn)
	
	def addAdmin(self, adminIn):
		adminObjects.append(adminIn)

	def loadCustomer():
		i = 0
		j = 0
		users = []
		with open("customer.txt", "r"):
			for line in f:
				users[i] = line
				count++
		while i < len(users):
			user = Customer(i, i + 1, i + 2, i + 3)
			i = i + 4
			userObjects[j] = user
		return userObjects

	def loadBooks()
		i = 0
		j = 0
		books = []
		with open("book.txt", "r"):
			for line in f:
				books[i] = line
				count++
		while i < len(books):
			if books[i + 7] == 1:
				book = Book.PhysicalBook(i, i + 1, i+2, i+3, i+4,i+5,i+6,i+7)
				bookObjects[j] = book
			i = i + 8

	def loadEbook()
		i = 0
		j = 0
		books = []
		with open("ebook.txt", "r"):
			for line in f:
				books[i] = line
				count++
		while i < len(books):
			if books[i + 7] == 1:
				ebook = Book.eBook(i, i + 1, i+2, i+3, i+4,i+5,i+6,i+7)
				ebookObjects[j] = ebook
			i = i + 8
	def loadAdmin()
		i = 0
		j = 0
		admins = []
		with open("admin.txt", "r"):
			for line in f:
				admins[i] = line
				count++
		while i < len(admins):
			if admins[i + 7] == 1:
				admin = Administrator.admin(i, i + 1, i+2, i+3, i+4,i+5,i+6,i+7,i+8)
				adminObjects[j] = admin
			i = i + 9

	def loadEmployee():
		i = 0
		j = 0
		admins = []
		with open("admin.txt", "r"):
			for line in f:
				admins[i] = line
				count++
		while i < len(admins):
			if admins[i + 7] == 1:
				admin = Employee.Employee(i, i + 1, i+2, i+3, i+4,i+5,i+6,i+7,i+8)
				employeeObjects[j] = admin
			i = i + 9

	def writeEmployee(employees):
		file = open("employee.txt", "w")
		for obj in employees:
			obj.writeEmployee(file)
		file.close()

	def writeCustomer(customers):
		file = open("customer.txt", "w")
		for obj in customers:
			obj.writeCustomer()
		file.close()

	def writeAdmin(admins):
		file = open("admin.txt", "w")
		for obj in admins:
			obj.writeCustomer()
		file.close()

	def writeBook(books):
		file = open("book.txt", "w")
		for obj in books:
			obj.writeCustomer()
		file.close()

	def writeEBook(ebooks):
		file = open("ebook.txt", "w")
		for obj in admins:
			obj.writeCustomer()
		file.close()





