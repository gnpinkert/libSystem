import Administrator
import Customer
import Employee
import Book

userObjects = []
bookObjects = []
ebookObjects = []
adminObjects = []
employeeObjects = []
allEmployees = []
customerObjects = []
name = None
class Server:
	
	

	def __init__(self, nameIn):
		self.name = nameIn
	def load(self):
		self.loadCustomer()
		self.loadBooks()
		self.loadEbook()
		self.loadAdmin()
		self.loadEmployee()


	def searchIsbn(self, isbnIn):
		for i in ebookObjects:
			if i.getISBN == isbnIn:
				return False
		return True

	def searchBook(self, titleIn):
		for i in ebookObjects:
			if i.getTitle() == titleIn:
				found = i
				ebookObjects.remove(i)
				return found, "EBook"
		for i in bookObjects:
			if i.getTitle() == titleIn:
				found = i
				bookObjects.remove(i)
				return found, "Physical Book"
		else:
			return None, None

	def searchUser(self, usernameIn, passwordIn):
		for i in customerObjects:
			if (i.getUserID() == usernameIn and i.getPassword() == passwordIn):
				found = i
				customerObjects.remove(i)
				return found, 0
		
		for i in adminObjects:
			if i.getUserID() == usernameIn and i.password == passwordIn:
				found = i
				print("Length of admin objects before remove: " + str(len(adminObjects)))
				adminObjects.remove(i)
				print("Length of admin objects after remove: " + str(len(adminObjects)))
				return found,1
		
		for i in employeeObjects:
			if i.getUserID() == usernameIn and i.password == passwordIn:
				found = i
				employeeObjects.remove(i)
				return found,2
		return None, None
	
	def searchEmployee(self, nameIn):
		for i in employeeObjects:
			if i.getName() == nameIn:
				found = i
				employeeObjects.remove(i)
				return found
	
	def searchAdmin(self, nameIn):
		for i in adminObjects:
			if i.getName() == nameIn:
				found = i
				adminObjects.remove(i)
				return found

				
	def searchCustomer(self, nameIn):
		for i in customerObjects:
			if i.getName() == nameIn:
				found = i
				customerObjects.remove(i)
				return found
		return None

	def checkOutBook(self, bookIn):
		if bookIn.decCopies() == False:
			return False

	def checkInBook(self, bookIn):
		bookIn.incCopies()
		return True
	
	def login(self, usernameIn, passwordIn):
		for i in userObjects:
			if i.username == usernameIn and i.password == passwordIn:
				return True
		return False

	def bookInfo(self, book):
		print book.toString()
		return True
	
	def addBook(self, bookIn, typeIn):
		if typeIn == 1:
			ebookObjects.append(bookIn)
		else:
			bookObjects.append(bookIn)
		return True

	def addCustomer(self, customerIn):
		customerObjects.append(customerIn)

	def addEmployee(self, employeeIn):
		employeeObjects.append(employeeIn)
	
	def addAdmin(self, adminIn):
		adminObjects.append(adminIn)

	def loadCustomer(self):
		i = 0
		users = []
		with open("customer.txt", "r") as f:
			mylist = f.read().splitlines()
			for line in mylist:
				users.append(line)
		if len(users) == 3:
			users.append("")
		while i < len(users):
			booksout = users[i+3].split(",")
			user = Customer.Customer(users[i], users[i + 1], users[i + 2], booksout)
			i = i + 4
			customerObjects.append(user)
		return customerObjects

	def loadBooks(self):
		i = 0
		books = []
		with open("book.txt", "r") as f:
			mylist = f.read().splitlines()
			for line in mylist:
				line.strip()
				books.append(line)
		while i < len(books):
			book = Book.PhysicalBook(books[i], books[i + 1], books[i+2], books[i+3], books[i+4],books[i+5],books[i+6],books[i+7],0)
			bookObjects.append(book)
			i = i + 8

	def loadEbook(self):
		i = 0
		books = []
		with open("ebook.txt", "r") as f:
			mylist = f.read().splitlines()
			for line in mylist:
				books.append(line)
		while i < len(books):
			ebook = Book.eBook(books[i], books[i + 1], books[i+2], books[i+3], books[i+4],books[i+5],books[i+6],books[i+7],1)

			ebookObjects.append(ebook)
			i = i + 8
	def loadAdmin(self):
		i = 0
		admins = []
		with open("admin.txt", "r") as f:
			mylist = f.read().splitlines()
			for line in mylist:
				admins.append(line)
		print("Length of admins before creating all objects: " + str(len(admins)))
		while i < len(admins):
			admin = Administrator.Administrator(admins[i], admins[i + 1], admins[i + 2])
			adminObjects.append(admin)
			i = i + 3

	def loadEmployee(self):
		i = 0
		j = 0
		admins = []
		with open("employee.txt", "r") as f:
			mylist = f.read().splitlines()
			for line in mylist:
				admins.append(line)
		while i < len(admins):
			booksout = admins[i+3].split(",")
			admin = Employee.Employee(admins[i], admins[i + 1], admins[i + 2], booksout)
			employeeObjects.append(admin)
			i = i + 4

	def writeEmployee(self):
		file = open("employee.txt", "w")
		file.seek(0)
		file.truncate()
		for obj in employeeObjects:
			file.write(obj.getName()+"\n")
			file.write(obj.getUserID()+"\n")
			file.write(obj.getPassword()+"\n")
			for i in obj.booksOut:
				file.write(i + ",")
			file.write("\n")
		file.close()

	def writeCustomer(self):
		file = open("customer.txt", "w")
		file.seek(0)
		file.truncate()
		for obj in customerObjects:
			file.write(obj.getName()+"\n")
			file.write(obj.getUserID()+"\n")
			file.write(obj.getPassword()+"\n")
			for i in obj.booksOut:
				file.write(i + ",")
			file.write("\n")
		file.close()

	def writeAdmin(self):
		file = open("admin.txt", "w")
		file.seek(0)
		file.truncate()
		file.close()
		print(len(adminObjects))
		file = open("admin.txt", "w")
		for obj in adminObjects:
			file.write(obj.getName()+"\n")
			file.write(obj.getUserID()+"\n")
			file.write(obj.getPassword()+"\n")
		file.close()

	def writeBook(self):
		file = open("book.txt", "w")
		file.seek(0)
		file.truncate()
		file.close()
		file = open("book.txt", "w")
		for obj in bookObjects:
			file.write(obj.getTitle()+"\n")
			file.write(obj.getAuthor()+"\n")
			file.write(obj.getSubject()+"\n")
			file.write(str(obj.getISBN())+"\n")
			file.write(obj.getDateAdded()+"\n")
			file.write(str(obj.getNumCopies())+"\n")
			file.write(obj.getTimesIssued()+"\n")
			file.write(obj.getLastIssueDate()+"\n")
		file.close()

	def writeEBook(self):
		file = open("ebook.txt", "w")
		file.seek(0)
		file.truncate()
		for obj in ebookObjects:
			file.write(obj.getTitle()+"\n")
			file.write(obj.getAuthor()+"\n")
			file.write(obj.getSubject()+"\n")
			file.write(str(obj.getISBN())+"\n")
			file.write(obj.getDateAdded()+"\n")
			file.write(str(obj.getNumCopies())+"\n")
			file.write(obj.getTimesIssued()+"\n")
			file.write(obj.getLastIssueDate()+"\n")
		file.close()

	def writeEverything(self):
		self.writeEBook()
		self.writeCustomer()
		self.writeAdmin()
		self.writeEmployee()
		self.writeBook()

	




