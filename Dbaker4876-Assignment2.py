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
customer = {}
chosenMenu = {}



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

def getDinnerOrder():                                                                                           #Function is for asking the user which dinner they want and then
    global dinner, totalPrice, tax, grandTotal, quantity  
    
    for item, x in menu.items():
        print("\nMenu Item: {}".format(item))
        for key in x:
            print("{0}: {1}".format(key, x[key]))
        
    dinner = float(input("Please enter the number of the menu item you want: "))
    while dinner not in range(1, 7):
        dinner = float(input("Please enter a valid menu number: "))
        
    quantity = float(input("How many do you want?: "))
    
    chosenMenu.update({'a': menu[dinner]["food item"], 'b': menu[dinner]['price'], "Quantity": quantity}) 
    
    
    totalPrice = float(chosenMenu['b']) * quantity
    
    print(totalPrice)
    
    if totalPrice == range(100 - 500):                      #Price calculations based on the total amount of the bill and adding the discounts
        disPrice = round(totalPrice * 0.2, 2)
    if totalPrice > 500:
        disPrice = round(totalPrice * 0.25, 2)
    if totalPrice < 100:
        disPrice = round(totalPrice * 0.15, 2)
    
    savings = totalPrice - (totalPrice + disPrice) 
    grandTotal = totalPrice - disPrice
    
    print('                           ')
    print(chosenMenu['a'] + " * " + str(quantity))                   #Printing the reciept to the user and asking for confirmation
    print('                             ')
    print('----------------------------')
    print('                                  ')
    print("Total $" + str(totalPrice))
    print("Discount $" + str(savings))
    print("Grand total $" + str(grandTotal))
    
    confirm = input("Is this what you want? [Y/N]: ")
    if confirm == "n":
        return True
    if confirm == "y":
        return False
    
answer = input("WELCOME TO ARNOLD'S AMAZING EATS!! ARE YOU HERE TO ORDER FOOD OR WHAT? [Y/N]: ").strip().lower()  #This is the first thing the user will see, and asks if they want to order some food

if answer == "n":
    exit() 

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

postalCode = input("Please enter your postal code: ").strip()
customer.update({'postalcode': postalCode})

phoneNum = input("Please enter your phone number: ")
customer.update({'phonenumber': phoneNum})

specInstructions = input("Please enter any special instructions: ")

while getDinnerOrder():                                                                 #Calling the function to determine their order
    if True:
        print("Please reenter your order.")
        
def addressPrint():
    print(firstName + ' ' + lastName)
    print(streetNumber + ' ' + streetName + ' ' + ' ' + apartmentNum)      
    print(city + ', ' + province + ', ' + postalCode)        
    print(specInstructions)
    print("")      
    return
      
studentDiscount = round(grandTotal * 0.1, 2) 
studentDif = round(grandTotal - (grandTotal + studentDiscount), 3)                      #Calculating the discounts if they say 'yes' to be a student
studentDis = round(grandTotal - studentDiscount, 2)
tax = totalPrice * 0.13

headers = ["Order", "Item Amount", "Item Price", "Total"]               #Setting the headers for the formatBill function

student = input("Are you a student? [Y/N]: ").strip().lower()               #Asking if the user is a student or not
while not(student == 'y' or student == 'n'):
    student = input("Please enter a valid answer: ").strip().lower()

delivery = float(input("Would you like Delivery or Pick-up?: \n[1 - Delivery]\n[2 - Pick-up]\n"))
while not(delivery == 1 or delivery == 2):
    delivery = input("Please enter a valid answer: ")

deliveryFee = 5
if totalPrice > 30:
    deliveryFee = 0
    
if student == "y":
    if delivery == 2:
        endPrice = round(tax + studentDis, 3)
        addressPrint()
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['10% Student Savings', '', '', str(studentDif)], ['', '', 'Sub Total', str(studentDis)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Total', str(endPrice)]
        print(formatBill(data, headers, 30))
    if delivery == 1:
        endPrice = round(tax + studentDis + deliveryFee, 3)
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['10% Student Savings', '', '', str(studentDif)], ['', '', 'Sub Total', str(studentDis)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Delivery', str(deliveryFee)], ['', '', 'Total', str(endPrice)]

    
if student == "n":
    if delivery == 2:
        endPrice = round(tax + grandTotal, 3)
        addressPrint()
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['', '', 'Sub Total', str(grandTotal)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Total', '$' + str(endPrice)]
        print(formatBill(data, headers, 25))
    if delivery == 1:
        endPrice = round(tax + grandTotal + deliveryFee, 3)
        addressPrint()
        data = [chosenMenu['a'], str(chosenMenu['Quantity']), '$' + str(chosenMenu['b']), '$' + str(grandTotal)], ['', '', 'Sub Total', str(grandTotal)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Delivery', '$' + str(deliveryFee)], ['', '', 'Total', '$' + str(endPrice)]