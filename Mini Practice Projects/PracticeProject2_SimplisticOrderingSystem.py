#Creating required variables
tax = 1.15
currency = 50

#Defining purchase function
def purchase_order(tax, choice, quantity):
    if choice == 1:
        pizza = 10.00 * tax
        total = (pizza * quantity)
        print(f"Your order is {quantity} pizza(s) at ${pizza} each, totaling ${total:.2f}.")
    if choice == 2:
        burger = 5.00 * tax
        total = (burger * quantity)
        print(f"Your order is {quantity} burger(s) at ${burger} each, totaling ${total:.2f}.")
    if choice == 3:
        salad = 7.50 * tax
        total = (salad * quantity)
        print(f"Your order is {quantity} salad(s) at ${salad} each, totaling ${total:.2f}.")

#Defining ordering system function
def ordering_system():
    user_ordering = True
    print("Welcome to the Simplistic Ordering System!")
    while user_ordering == True:
        try:
            choice = int(input("What would you like to order? \n1. Pizza\n2. Burger\n3. Salad\n4. Exit\n"))

            if choice == 4:
                print("Thank you for using the Simplistic Ordering System!")
                break

            elif choice not in [1, 2, 3]:
                print("Invalid selection. Please choose a valid menu option.")
                continue
        except:
            print("Invalid selection. Please choose a valid menu option. (try)")
        quantity = int(input("How many would you like to order? "))

        if quantity <= 0:
            return_to_menu = int(input("Invalid input. Would you like to return to the menu? (1 for Yes, 0 for No) "))
            if return_to_menu == 1:
                continue
            else:
                print("Thank you for using the Simplistic Ordering System!")
                user_ordering = False

        elif quantity > 5:
            return_to_menu = int(input("We do not allow orders above 5. Would you like to return to the menu or exit? (1 for Yes, 0 for No.) "))
            if return_to_menu == 1:
                continue
            else:
                print("Thank you for using the Simplistic Ordering System!")
                user_ordering = False

        else:
            item = {1: "pizza", 2: "burger", 3: "salad"}[choice]
            plural = "s" if quantity > 1 else "" # Add pluralization for items
            confirm = int(input(f"You have placed an order for {quantity} {item}{plural}. Is this correct? (1 for Yes, 0 for No.) "))
            if confirm == 1:
                purchase_order(tax, choice, quantity)
            else:
                return_to_menu = int(input("Would you like to return to the menu? (1 for Yes, 0 for No) "))
                if return_to_menu == 1:
                    continue
                else:
                    print("Thank you for using the Simplistic Ordering System!")
                    user_ordering = False

ordering_system()

