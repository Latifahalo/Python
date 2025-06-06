budget =  int(input("Enter your budget: "))

if budget <10 :
    print('Umm save your money')
elif  budget <=100:
    print('Do you wanna buy food or clothes?')
    choose = input("Enter your choice: ")

    if choose == 'food':
       print('Buy vegetables')
    elif  choose == 'clothes':
         print("Buy coat")

elif budget >=1000:
    print('Save part of money. Enter how much  you wanna save, and than I will calculate how much youll have by the end year ')
    choose = int(input("Enter how much wanna save your money: "))
    if choose <=10:
        print('12 to 120. ummm thats a little, try to save more ')
    elif 10< choose >=100:
        print('132 to 1200. GOOD ')