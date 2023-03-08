#Name:                  Dbaker4876-Assignment2.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    07-02-2023
#
#Purpose:
#This program will help Arnold take orders from customers and calculate the cost of the order
#The program will ask for what they want to order, ask them to confirm their order, and then print them a reciept 

menu = {
    1: {"food item": "Austin's Pemeal Bacon", "price": 15},
    2: {"food item": "Aaron's Poutine", "price": 10},
    3: {"food item": "Alex's Crispy Taco", "price": 11},
    4: {"food item": "Andrew's Bean Salad", "price": 5},
    5: {"food item": "Tara's Mushroom Soup", "price": 7},
    6: {"food item": "Mark's Spaghetti", "price": 9}
}
#the restaurant menu is in a dictionary for easy access

customer = {}
chosenMenu = {}
#defining the dictionaries for later use


def formatBill(data, headers, size) :               #Creating a function that will format the reciept at the end
    lines = ""
    line = ""
    i = 1
    
    for header in headers :                         #Loop creates space between headers
        line += header + "|"
        while len(line) < size * i :
            line += " "
        i += 1
        
    lines = line + "\n"                             
    lineLength = len(line)
    
    for x in range(1, lineLength):                  #Seperates headers from the body of the table
        lines += "_"
    lines += "\n"
    
    for row in data:                                #Loop through the list of lists and formats it into the table
        line = ""
        i = 1
        for element in row:
            line += element
            while len(line) < size * i :
                line += " "
            i += 1
        lines += line + "\n"
        
    return lines
#function to format the reciept at the end of the order

def getDinnerOrder():                                                                                           #Function is for asking the user which dinner they want and then
    global dinner, totalPrice, tax, grandTotal, quantity, disPrice 
    
    for item, x in menu.items():
        print("\nMenu Item: {}".format(item))
        for key in x:
            print("{0}: {1}".format(key, x[key]))
#printing out the menu for easy reading
        
    dinner = float(input("Please enter the number of the menu item you want: "))
    while dinner not in range(1, 7):
        dinner = float(input("Please enter a valid menu number: "))
        
    quantity = float(input("How many do you want?: "))
    
    chosenMenu.update({'a': menu[dinner]["food item"], 'b': menu[dinner]['price'], "Quantity": quantity}) 
    
    totalPrice = float(chosenMenu['b']) * quantity
    
    if totalPrice in range(100, 500):                      #Price calculations based on the total amount of the bill and adding the discounts
        disPrice = round(totalPrice * 0.2, 2)
    if totalPrice > 500:
        disPrice = round(totalPrice * 0.25, 2)
    if totalPrice < 100:
        disPrice = round(totalPrice * 0.15, 2)
#defining the discounted price of the order
    
    savings = totalPrice - (totalPrice + disPrice)
    grandTotal = totalPrice - disPrice
#calculating the total price of the order
    
    print('                           ')
    print(chosenMenu['a'] + " * " + str(quantity))                   #Printing the reciept to the user and asking for confirmation
    print('                             ')
    print('----------------------------')
    print('                                  ')
    print("Total $" + str(totalPrice))
    print("Discount $" + str(savings))
    print("Grand total $" + str(grandTotal))
#printing the confirmation reciept to the customer
    
    confirm = input("Is this what you want? [Y/N]: ")
    if confirm == "n":
        return True
    if confirm == "y":
        return False
#function that collects the order and quantity of the order and then calculates the total cost of the order before taxes
    
answer = input("WELCOME TO ARNOLD'S AMAZING EATS!! ARE YOU HERE TO ORDER FOOD OR WHAT? [Y/N]: ").strip().lower()  #This is the first thing the user will see, and asks if they want to order some food

while not(answer == "n" or answer == 'y'):
    answer = input('Please enter a valid answer: ')
#loop to get valid answer

if answer == 'n':
    exit()
#the program will close if they do not want to order food
    
def customerInfo():
    global specInstructions
    firstName = input("Please enter your first name: ").capitalize().strip()
    customer.update({'firstname': firstName})

    lastName = input("Please enter your last name: ").capitalize().strip()
    customer.update({'lastname': lastName})

    streetNumber = input("Please enter your street number: ").strip()                                   #Getting the user's information
    customer.update({'streetnumber': streetNumber})

    streetName = input("Please enter your street name: ").capitalize().strip()
    customer.update({'streetname': streetName})

    apartmentNum = input("Please enter your unit # if applicable: ").strip()
    customer.update({'unitnumber': apartmentNum})

    city = input("Please enter your city: ").strip().capitalize()
    customer.update({'city': city})

    province = input("Please enter your province: ").capitalize().strip()
    customer.update({'province': province})

    postalCode = input("Please enter your postal code: ").strip().upper()
    customer.update({'postalcode': postalCode})

    phoneNum = input("Please enter your phone number: ")
    customer.update({'phonenumber': phoneNum})

    specInstructions = input("Please enter any special instructions: ")
    
    confirm = input("Is this information correct? [Y/N]: ").strip().lower()
    while not(confirm == 'y' or confirm == 'n'):
        confirm = input("Please enter a valid answer: ")
        
    if confirm == 'y':
        return False
    if confirm == 'n':
        return True
#function that collects the customer info and asks them to confirm their information. It will loop if they do not confirm 

while customerInfo():
    if True:
        print("Please reenter your information.")
#calling the function to gather customer information

while getDinnerOrder():                                                                 
    if True:
        print("Please reenter your order.")
#Calling the function to determine their order
        
def addressPrint():
    print('')
    print(customer['firstname'] + ' ' + customer['lastname'])
    print(customer['streetnumber'] + ' ' + customer['streetname'] + ' ' + ' ' + customer['unitnumber'])      
    print(customer['city'] + ', ' + customer['province'] + ', ' + customer['postalcode'])
    print(customer['phonenumber'])        
    print(specInstructions)   
#function to print out the address given by the customer  
      
studentDiscount = round(grandTotal * 0.1, 2) 
studentDif = round(grandTotal - (grandTotal + studentDiscount), 3)                      
studentDis = round(grandTotal - studentDiscount, 2)
tax = totalPrice * 0.13
#Calculating the discounts if they say 'yes' to be a student

headers = ["Order", "Item Amount", "Item Price", "Total"]              
 #Setting the headers for the formatBill function
 
student = input("Are you a student? [Y/N]: ").strip().lower()               
while not(student == 'y' or student == 'n'):
    student = input("Please enter a valid answer: ").strip().lower()
#Asking if the user is a student or not

delivery = float(input("Would you like Delivery or Pick-up?: \n[1 - Delivery]\n[2 - Pick-up]\n"))
while not(delivery == 1 or delivery == 2):
    delivery = input("Please enter a valid answer: ")
#asking if the customer wants delivery or pick-up

deliveryFee = 5
if totalPrice > 30:
    deliveryFee = 0
#waiving the delivery fee on orders that are more than $30

if delivery == 1:
    tip = float(input("Please enter the tip amount: \n[1 - 10%]\n[2 - 15%]\n[3 - 20%]\n"))
    while not(tip == 1 or tip == 2 or tip == 3):
        tip = float(input("Please enter a valid value: "))
    if tip == 1:
        tip = grandTotal * 0.1
    if tip == 2:
        tip = grandTotal * 0.15
    if tip == 3:
        tip = grandTotal * 0.2
#if the customer chooses delivery, the program will ask for the tip amount and calculate the tip based on the order price
    
if student == "y":
    if delivery == 2:
        endPrice = round(tax + studentDis, 3)
        print(addressPrint())
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['10% Student Savings', '', '', '$' + str(studentDif)], ['', '', 'Sub Total', '$' + str(studentDis)], ['', '', 'Tax (13%)', '$' + str(tax)], ['', '', 'Total', '$' + str(endPrice)]
        print(formatBill(data, headers, 30))
    if delivery == 1:
        endPrice = round(tax + studentDis + deliveryFee + tip, 3)
        print(addressPrint())
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['10% Student Savings', '', '', '$' + str(studentDif)], ['', '', 'Sub Total', '$' + str(studentDis)], ['', '', 'Tip', '$' + str(tip)], ['', '', 'Tax (13%)', '$' + str(tax)], ['', '', 'Delivery', '$' + str(deliveryFee)], ['', '', 'Total', '$' + str(endPrice)]
        print(formatBill(data, headers, 25))
#printing the final order reciept to the customer based on the inputs from earlier
    
if student == "n":
    if delivery == 2:
        endPrice = round(tax + grandTotal, 3)
        print(addressPrint())
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['', '', 'Sub Total', '$' + str(grandTotal)], ['', '', 'Tax (13%)', '$' + str(tax)], ['', '', 'Total', '$' + str(endPrice)]
        print(formatBill(data, headers, 25))
    if delivery == 1:
        endPrice = round(tax + grandTotal + deliveryFee + tip, 3)
        print(addressPrint())
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['', '', 'Sub Total', '$' + str(grandTotal)], ['', '', 'Tip', '$' + str(tip)], ['', '', 'Tax (13%)', '$' + str(tax)], ['', '', 'Delivery', '$' + str(deliveryFee)], ['', '', 'Total', '$' + str(endPrice)]
        print(formatBill(data, headers, 25))
#printing the final order reciept to the customer based on the inputs from earlier