import PhoneBookModule
import list_with_data

print("Hello in PhoneBook database application!!!")
print("Select instructions you need to work: ")
print("1 - insert or update data from concole, (name surname phone_number format)")
print("2 - delete data from database by name surname")
print("3 - delete data from database using phone number")
print("4 - order data by attribute")
print("5 - to insert data from csv file")
print("6 - search using patterns")
print("7 - experiment with list")
print("8 - query data using limit and offset (limit, offset input format)")
print("9 - exit")

isDone = False

while not isDone:
    option = int(input())
    if option == 1:
        name = input("Name: ")
        surname = input("Surname: ")
        phone_number = input("Phone number (+X (XXX) XXX-XX-XX format): ")
        PhoneBookModule.connect()
        PhoneBookModule.insert_data_or_update(surname, name, phone_number)

    elif option == 2:
        name = input("Name: ")
        surname = input("Surname: ")
        PhoneBookModule.delete_by_name_surname(name, surname)

    elif option == 3:
        phone_number = input("Phone number: ")
        PhoneBookModule.delete_by_phone(phone_number)

    elif option == 4:
        attribute = input("Input attribute (user_name, user_surname, phone_number): ")
        PhoneBookModule.sort_by_attribute(attribute)

    elif option == 5:
        path = input("Path: ")
        PhoneBookModule.import_from_csv(path)

    elif option == 6:
        pattern = input("Enter pattern: ")
        PhoneBookModule.sort_using_pattern(pattern)

    elif option == 7:
        PhoneBookModule.insert_data_from_list(list_with_data.my_list)

    elif option == 8:
        offset = input("Offset: ")
        limit = input("Limit: ")
        PhoneBookModule.query_data_with_limit_offset(limit, offset)

    elif option == 9:
        isDone = True




