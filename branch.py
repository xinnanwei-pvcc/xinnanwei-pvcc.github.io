#Name: Xinnan Wei
# Prog Purpose: This program finds the cost for adults and childeren at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

##############  define global variables ##############
# define tax rate, service fee, and prices
SERVICE_FEE = 0.10
SALES_TAX_RATE = 0.062
PR_ADULT_MEAL = 19.95
PR_CHILD_MEAL = 11.95

# define global variables
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
service_fee = 0
sales_tax = 0
total = 0

##############  define program functions ##############
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals
    num_adult_meals = int(input("Number of adult meals: "))
    global num_child_meals
    num_child_meals = int(input("Number of child meals: "))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total
    subtotal = num_adult_meals * PR_ADULT_MEAL + num_child_meals * PR_CHILD_MEAL
    service_fee = subtotal * SERVICE_FEE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    print('------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('------------------------------')
    print('Adult Meals  $ ' + format(num_adult_meals * PR_ADULT_MEAL,'8,.2f'))
    print('Child Meals  $ ' + format(num_child_meals * PR_CHILD_MEAL,'8,.2f'))
    print('Subtotal     $ ' + format(subtotal,'8,.2f'))
    print('Service Fee  $ ' + format(service_fee,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))


##########  call on main program to execute ##########
main()
