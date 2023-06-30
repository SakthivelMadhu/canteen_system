# Step 1: Create an empty inventory dictionary
inventory = {}

# Step 2: Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the snack available? (yes/no): ")
    
    # Add snack details to the inventory dictionary
    inventory[snack_id] = {
        'snack_name': snack_name,
        'price': price,
        'availability': availability.lower() == 'yes'
    }
    print("Snack added to inventory.")

# Step 3: Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")
    
    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from inventory.")
    else:
        print("Snack not found in inventory.")

# Step 4: Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter the snack ID to update availability: ")
    
    if snack_id in inventory:
        availability = input("Is the snack available? (yes/no): ")
        inventory[snack_id]['availability'] = availability.lower() == 'yes'
        print("Snack availability updated.")
    else:
        print("Snack not found in inventory.")

# Step 5: Function to display the snack inventory
def display_inventory():
    print("Snack Inventory:")
    print("ID\tSnack Name\tPrice\tAvailability")
    
    for snack_id, details in inventory.items():
        availability = "Yes" if details['availability'] else "No"
        print(f"{snack_id}\t{details['snack_name']}\t\t{details['price']}\t{availability}")

# Step 6: Function to record a snack sale and update the inventory
def record_sale():
    snack_id = input("Enter the snack ID sold: ")
    
    if snack_id in inventory:
        if inventory[snack_id]['availability']:
            inventory[snack_id]['availability'] = False
            print("Snack sale recorded. Inventory updated.")
        else:
            print("Snack not available for sale.")
    else:
        print("Snack not found in inventory.")

# Step 7: Implement error handling
def handle_invalid_input():
    print("Invalid input. Please try again.")

# Main program loop
while True:
    print("\n==== Mumbai Munchies Canteen System ====")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Display snack inventory")
    print("5. Record a snack sale")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_snack()
    elif choice == '2':
        remove_snack()
    elif choice == '3':
        update_availability()
    elif choice == '4':
        display_inventory()
    elif choice == '5':
        record_sale()
    elif choice == '0':
        print("Exiting program.")
        break
    else:
        handle_invalid_input()
