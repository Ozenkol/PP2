import PhoneBookModule

print("Hello in PhoneBook database application!!!")
print("Select instructions you need to work: ")
print("1 - insert data from concole, (name surname phone_number format)")
print("2 - delete data from database by name surname")
print("3 - order data by name")
print("4 - to insert data from csv file")
print("5 - update data")
print("6 - exit")

isDone = False

while not isDone:
    option = int(input())
    if option == 1:
        name = input("Name: ")
        surname = input("Surname: ")
        phone_number = input("Phone number: ")
        PhoneBookModule.connect()
        PhoneBookModule.insert_data(name, surname, phone_number)

    elif option == 2:
        name = input("Name: ")
        surname = input("Surname: ")
        PhoneBookModule.delete_by_name_surname(name, surname)

    elif option == 3:
        attribute = input("Attribute: ")
        PhoneBookModule.sort_by_attribute(attribute)

    elif option == 4:
        path = input("Path: ")
        PhoneBookModule.import_from_csv(path)

    elif option == 5:
        surname = input("Enter surname: ")
        PhoneBookModule.updated_using_surname(surname)

    elif option == 6:
        isDone = True
