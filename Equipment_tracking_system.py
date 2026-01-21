equipment_list = []

def add_equipment():
    name = input("Enter equipment name: ")
    status = input("Enter status (Available/In Use): ")
    equipment_list.append({"name": name, "status": status})
    print("Equipment added")

def view_equipment():
    if not equipment_list:
        print("No equipment available")
    else:
        for eq in equipment_list:
            print(eq["name"], "- Status:", eq["status"])

def main():
    while True:
        print("1. Add Equipment")
        print("2. View Equipment")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            view_equipment()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
