def menu():
    print('1. print phone numbers')
    print('2. add phone number')
    print('3. remove phone number')
    print('4. search')
    print('5. update')
    print('6. quit')
    print()

numbers = {}
choice = 0
menu()
while choice != 6:
    choice = int(input("type in a number 1 to 6 : "))
    if choice == 1:
        print("telephone numbers:")
        for x in numbers.keys():
            print( x, numbers[x])
        print()
    elif choice == 2:
        print("Add Name and Number: ")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif choice == 3:
        print("Remove Name and Number: ")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif choice == 4:
        print('Search: ')
        name = input('Name: ')
        if name in numbers:
            print(name,' ',numbers[name])
        else:
            print(name, 'was not found')
    elif choice == 5:
        print('updation: ')
        name = input('Name: ')
        if name in numbers:
            phone = input('New Number: ')
            numbers[name] = phone
        else:
            print(name, 'was not found')
    elif choice != 6:
        menu()
