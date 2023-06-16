def PrintMenu():
    print("===============================================================")
    print("-----------------------Choose an option:-----------------------")
    print("===============================================================")
    print("------------------------1.Pyramid------------------------------")
    print("------------------------2.Empty_Pyramid------------------------")
    print("------------------------3.Stairs-------------------------------")
    print("------------------------4.Reflected_Stairs---------------------")
    print("------------------------5.Number_Stairs------------------------")
    print("------------------------6.Number_Stairs_Ordered----------------")
    print("===============================================================")
    print("Option:")


def Pyramid():
    print("Enter a symbol:")
    Symbol = (input())
    print("Enter a number:")
    Number_of_Symbols = int(input())
    for i in range (Number_of_Symbols):
        print(" " * (Number_of_Symbols-i-1) + Symbol * (i*2+1))

def Empty_Pyramid():
    print("Enter a symbol:")
    Symbol = (input())
    print("Enter a number:")
    Number_of_Symbols = int(input())
    print(" " * (Number_of_Symbols + 1) + Symbol)
    for i in range (Number_of_Symbols):
        print(" " + " "* (Number_of_Symbols-i-1) + Symbol + " " * (i*2+1) + Symbol)
    print(Symbol * (Number_of_Symbols * 2 + 3))

def Stairs():
   print("Enter a symbol:")
   x = (input())
   print("Enter a number:")
   y = int(input())
   for i in range(y):
        print(x * (i+1))

def Reflected_Stairs():
   print("Enter a symbol:")
   x = (input())
   print("Enter a number:")
   y = int(input())
   for i in range(y):
        print(" " * (y-i-1) + x * (i+1))

def Number_Stairs():
   print("Enter a number:")
   x = int(input())
   for i in range(1, x+1):
    for j in range (1, i+1):
        print(j, end="")
    print()

def Number_Stairs_Ordered():
   print("Enter a number:")
   x = int(input())
   current_number = 1
   for i in range(1, x+1):
    for j in range (1, i+1):
        print(current_number, end="")
        current_number += 1
    print()

while True:
    PrintMenu()
    choice = input()
    
    if choice == "1":
        Pyramid()
    elif choice == "2":
        Empty_Pyramid()
    elif choice == "3":
        Stairs()
    elif choice == "4":
        Reflected_Stairs()
    elif choice == "5":
        Number_Stairs()
    elif choice == "6":
        Number_Stairs_Ordered()
    else:
        print("Invalid option. Please choose again.")
