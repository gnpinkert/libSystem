# coding: utf-8

from __future__ import print_function
import Server
import Book
import Customer
import Employee
import Administrator
import time
import datetime
from random import randint
import sys

server = Server.Server()
def addBook():
	
	title = raw_input("Input title of the book: ")
	author = raw_input("Input author: ")
	subject = raw_input("Input subject: ")
	isbn = raw_input("Input ISBN number: ")
	date_added = time.strftime("%d/%m/%Y")
	time_added = datetime.datetime.now().strftime("%H:%M:%S")
	numCopies = raw_input("Input number of copies: ")
	which = int(raw_input("Enter 1 for eBook or 2 for a physical book: "))
	if server.searchIsbn(isbn):
		if(which == 2):
			inputBook = Book.PhysicalBook(title, author, subject, isbn, date_added, numCopies, time_added, "Never checked Out", 0)
		else:
			inputBook = Book.eBook(title, author, subject, isbn, date_added, numCopies, time_added, "Never checked Out",1)
		print("Book Added!")
		return inputBook,which
	else:
		print("Duplicate ISBN number, cannot add")
	return None, None

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
		"\n\t\tAdd Employee (8) \n\t\tRemove Employee (9)\n\t\tAdd Administrator (10)\n\t\tRemove Administrator (11)\n\t\tLog Off (12)\n\t\tUpdate System (13)")
	choice = int(input())
	return choice
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end =	 '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
def updateSytem():
	num = randint(0,10)
	if(num < 3):
		items = list(range(0,57))
		l = len(items)
		print("Update found, starting download process")
		printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
		for i, item in enumerate(items):
			time.sleep(0.1)
			printProgressBar(i+1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
		print("Done!")
	else:
		print("No Update Found")
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

def searchBook():
	titleIn = raw_input("Enter book title: ")
	book, typeI = server.searchBook(titleIn)
	if book == None:
		print("Book does not exist in the system\n")
	else:
		book.toString()
		server.addBook(book, book.getType())
def checkoutBook():
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

def checkinBook():
	customer.printBooks()
	var = raw_input("Enter which book you would like to check back in (use the number", 
		" use the number next to the book")
	book = customer.removeBook(var)
	book,asd = server.searchBook(book.getTitle())
	if book == None:
		print("Book does not exist")
	else:
		book.decCopies()
		server.addBook(book)

def removeBook():
	title = raw_input("Enter the title of the book you would like to remove")
	book = server.searchBook(title)
	if book == None:
		print("Book does not exist!")
	else:
		print("Book successfully deleted!")
def editBook():
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
def deleteCustomer():
	title = raw_input("Enter name of customer to delete: ")
	userI = server.searchCustomer(title)
	if userI == None:
		print("User does not exist!\n")
	else:
		print("Customer deleted from server!")

def addCustomer():
	name = raw_input("Name of customer: ")
	username = raw_input("\nUsername of customer: ")
	password = raw_input("\nPassword for customer: ")
	cust = Customer.Customer(name, username, password)
	server.addCustomer(cust)
def viewCustomer():
	name = raw_input("Name of customer to view: ")
	cust = server.searchCustomer(name)
	if cust == None:
		print("Customer does not exist!\n")
	else:
		cust.toString()
		server.addCustomer(cust)
def addEmployee():
	name = raw_input("Name of customer to view: ")
	cust = server.searchCustomer(name)
	if cust == None:
		print("Customer does not exist!\n")
	else:
		cust.toString()
		server.addCustomer(cust)
def deleteEmployee():
	title = raw_input("Enter name of employee to delete: ")
	userI = server.searchEmployee(title)
	if userI == None:
		print("User does not exist!\n")
	else:
		print("User deleted from server!")
def addAdmin():
	name = raw_input("Name of admin: ")
	username = raw_input("\nUsername of admin: ")
	password = raw_input("\nPassword for admin: ")
	employee = Administrator.Administrator(name, username, password)
	server.addAdmin(employee)
def deleteAdmin():
	title = raw_input("Enter name of admin to delete: ")
	userI = server.searchAdmin(title)
	if userI == None:
		print("Admin does not exist!\n")
	else:
		print("Admin deleted from server!")


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
						searchBook()
					if choice == 3:
						checkoutBook()
					if choice == 4:
						checkinBook()
					if choice == 5:
						loggedIn = False
				server.addCustomer(user)
			if typeIn == 1:
				while(loggedIn):
					choice = adminMenu(user)
					if choice == 1:
						book,typeasf = addBook()
						if book != None:
							server.addBook(book, typeasf)
					if choice == 2:
						removeBook()
					if choice == 3:
						editBook()
					if choice == 5:
						deleteCustomer()
					if choice == 6:
						addCustomer()
					if choice == 4:
						viewCustomer()
					if choice == 12:
						loggedIn = False
					if choice == 7:
						searchBook()
					if choice == 8:
						addEmployee()
					if choice == 9:
						deleteCustomer()
					if choice == 10:
						addAdmin()
					if choice == 11:
						deleteAdmin()
					if choice == 13:
						updateSytem()
				server.addAdmin(user)
			if typeIn == 2:
				while(loggedIn):
					choice = employeeMenu(user)
					if choice == 1:
						book,typeasf = addBook()
						if book != None:
							server.addBook(book, book.getType())
					if choice == 2:
						removeBook()
					if choice == 3:
						editBook()
					if choice == 5:
						deleteCustomer()
					if choice == 6:
						addCustomer()
					if choice == 4:
						viewCustomer()
					if choice == 8:
						loggedIn = False
					if choice == 7:
						searchBook()
				server.addEmployee(user)
	server.writeEverything()
					




			

		



if __name__ == '__main__':
	main()