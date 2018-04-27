import Server
import Book
import Customer
import Employee
import Administrator
import time
import datetime

def addBook():
	
	title = raw_input("Input title of the book: ")
	author = raw_input("Input author: ")
	subject = raw_input("Input subject: ")
	isbn = raw_input("Input ISBN number: ")
	date_added = time.strftime("%d/%m/%Y")
	time_added = datetime.datetime.now().strftime("%H:%M:%S")
	numCopies = raw_input("Input number of copies: ")
	which = int(raw_input("Enter 1 for eBook or 2 for a physical book: "))
	
	if(which == 2):
		inputBook = Book.PhysicalBook(title, author, subject, isbn, date_added, numCopies, time_added, "Never checked Out", 0)
	else:
		inputBook = Book.eBook(title, author, subject, isbn, date_added, numCopies, time_added, "Never checked Out",1)

	return inputBook,which

def customerMenu(customerObj):
	print("\n\nHello, " +   customerObj.getName() + "\n\n\tHere are your options:\n")
	print("\t\tView Status (1)\n\t\tSearch Book Info (2)\n\t\tCheckout Book (3)\n\t\tReturn Book(4)\n\t\tCheckout (5)")
	choice = int(raw_input())
	return choice

def employeeMenu(employeeObj):
	print("\n\nHello, " +   employeeObj.getName() + "\n\n\tHere are your options:\n")
	print("\t\tAdd Book (1)\n\t\tDelete Book (2)\n\t\tEdit Book (3)\n\t\tView Customer (4)\n\t\tDelete Customer (5)\n\t\tAdd Customer (6)\n\t\tView Book(7)\n\t\tLog Off (8)")
	choice = int(input())
	return choice
def adminMenu(adminObj):
	print("\n\nHello, " +   adminObj.getName() + "\n\n\tHere are your options:\n")
	print("\t\tAdd Book (1)\n\t\tDelete Book (2)\n\t\tEdit Book (3)\n\t\tView Customer (4)\n\t\tDelete Customer (5)\n\t\tAdd Customer (6)\n\t\tView Book(7)" +
		"\n\t\tAdd Employee (8) \n\t\tRemove Employee (9)\n\t\tAdd Administrator (10)\n\t\tRemove Administrator (11)\n\t\tLog Off (12)")
	choice = int(input())
	return choice
def loginMenu():
	print("Hello, Welcome to the Argonauts Library Management System!\n")
	choice = int(raw_input("Press 1 to login or 2 to turn the system off\n"))
	if choice == 1:
		return True
	return False
def login():
	username = raw_input("Username: ")
	password = raw_input("\nPassword: ")
	return username, password

def main():
	on = True
	server = Server.Server()
	while (on):
		on = loginMenu()
		if on:
			username = 	raw_input("Please Input username: ")
			password = raw_input("\nPlease Input password: ")
			user, typeIn = server.searchUser(username, password)
			loggedIn = True
			if typeIn == 0:
				while (loggedIn):
					choice = customerMenu(user)
					if choice == 1:
						user.toString()
					if choice == 2:
						titleIn = raw_input("Enter book title: ")
						book, typeI = server.searchBook(titleIn)
						print(book.toString())
						if book == None:
							print("Book does not exist in the system\n")
						else:
							book.toString()
						server.addBook(book, book.getType())
					if choice == 3:
						titleIn = raw_input("Enter book title: ")
						book, typeI = server.searchBook(titleIn)
						if book == None:
							print("Book does not exist in the system\n")
						else:
							var = book.decCopies()
							if var == False:
								print("No Copies left\n")
							else:
								#TODO: Need to add book to customer
								print("Book successfully checked out!\n")
						server.addBook(book, book.getType())
					if choice == 4:
						customer.printBooks()
						var = raw_input("Enter which book you would like to check back in (use the number", 
							" use the number next to the book")
						book = customer.removeBook(var)
						book = server.searchBook(book.getTitle())
						book.decCopies()
						server.addBook(book)
					if choice == 5:
						loggedIn = False
				server.addCustomer(user)
			if typeIn == 1:
				while(loggedIn):
					choice = adminMenu(user)
					if choice == 1:
						book,typeasf = addBook()
						server.addBook(book, typeasf)
						print("Book Added!\n")
					if choice == 2:
						title = raw_input("Enter the title of the book you would like to remove")
						book = server.searchBook(title)
						if book == None:
							print("Book does not exist!")
						else:
							print("Book successfully deleted!")
					if choice == 3:
						title = raw_input("Enter the title of the book you wish to edit: ")
						book, typeF = server.searchBook(title)
						if book == None:
							print("Book does not exist")
						else:
							print("Current Information:\n")
							print(book.toString())
							print("\nEnter new info:")
							book,typeF = addBook()
							server.addBook(book,typeF)
					if choice == 5:
						title = raw_input("Enter name of customer to delete: ")
						userI = server.searchCustomer(title)
						if userI == None:
							print("User does not exist!\n")
						else:
							print("Customer deleted from server!")
					if choice == 6:
						name = raw_input("Name of customer: ")
						username = raw_input("\nUsername of customer: ")
						password = raw_input("\nPassword for customer: ")
						cust = Customer.Customer(name, username, password)
						server.addCustomer(cust)
					if choice == 4:
						name = raw_input("Name of customer to view: ")
						cust = server.searchCustomer(name)
						if cust == None:
							print("Customer does not exist!\n")
						else:
							cust.toString()
							server.addCustomer(cust)
					if choice == 12:
						loggedIn = False
					if choice == 7:
						titleIn = raw_input("Enter book title: ")
						book, typeI = server.searchBook(titleIn)
						print(book.toString())
						if book == None:
							print("Book does not exist in the system\n")
						else:
							book.toString()
						server.addBook(book, book.getType())
					if choice == 8:
						name = raw_input("Name of employee: ")
						username = raw_input("\nUsername of employee: ")
						password = raw_input("\nPassword for employee: ")
						employee = Employee.Employee(name, username, password)
						server.addEmployee(employee)
					if choice == 9:
						title = raw_input("Enter name of employee to delete: ")
						userI = server.searchEmployee(title)
						if userI == None:
							print("User does not exist!\n")
						else:
							print("User deleted from server!")
					if choice == 10:
						name = raw_input("Name of admin: ")
						username = raw_input("\nUsername of admin: ")
						password = raw_input("\nPassword for admin: ")
						employee = Administrator.Administrator(name, username, password)
						server.addAdmin(employee)
					if choice == 11:
						title = raw_input("Enter name of admin to delete: ")
						userI = server.searchAdmin(title)
						if userI == None:
							print("Admin does not exist!\n")
						else:
							print("Admin deleted from server!")
				server.addAdmin(user)
			if typeIn == 2:
				while(loggedIn):
					choice = employeeMenu(user)
					if choice == 1:
						book,typeasf = addBook()
						server.addBook(book, book.getType())
						print("Book Added!\n")
					if choice == 2:
						title = raw_input("Enter the tintle of the book you would like to remove")
						book,afaf = server.searchBook(title)
						if book == None:
							print("Book does not exist!")
						else:
							print("Book successfully deleted!")
					if choice == 3:
						title = raw_input("Enter the title of the book you wish to edit: ")
						book,typeF = server.searchBook(title)
						if book == None:
							print("Book does not exist")
						else:
							print("Current Information:\n")
							print(book.toString())
							print("\nEnter new info:")
							book,typeF = addBook()
							server.addBook(book,typeF)
					if choice == 5:
						title = raw_input("Enter name of customer to delete: ")
						user = server.searchCustomer(title)
						if user == None:
							print("User does not exist!\n")
						else:
							print("Customer deleted from server!")
					if choice == 6:
						name = raw_input("Name of customer: ")
						username = raw_input("\nUsername of customer: ")
						password = raw_input("\nPassword for customer: ")
						cust = Customer.Customer(name, username, password)
						server.addCustomer(cust)
					if choice == 4:
						name = raw_input("Name of customer to view: ")
						cust = server.searchCustomer()
						if cust == None:
							print("Customer does not exist")
						else:
							cust.toString()
							server.addCustomer(cust)
					if choice == 8:
						loggedIn = False
					if choice == 7:
						titleIn = raw_input("Enter book title: ")
						book, typeI = server.searchBook(titleIn)
						print(book.toString())
						if book == None:
							print("Book does not exist in the system\n")
						else:
							book.toString()
						server.addBook(book, book.getType())
				server.addEmployee(user)
	server.writeEverything()
					




			

		



if __name__ == '__main__':
	main()