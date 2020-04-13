# Celcius to fahrenheit => (celcius x 9/5) + 32
# Fanrenheit to celcius => (fahrenheit - 32) * 5/9

print("========================================")
print("For Celcius to Fahrenheit Conversion, Press 1.")
print("For Fahrenheit to Celcius Conversion, Press 2.")

choice = input("\nMake Your Choice: ")

def cel_to_fahr():
    celcius = input("Enter Temperature in Celcius: ")
    if (celcius.isalpha()):
        print("Input Must Be Numeric...!")
        exit()
    else:
        try:
            celcius = float(celcius)
            conv = (celcius * 9/5) + 32
            conv = format(conv, ".2f")       
            print (f"{celcius} in Celcius is equal to {conv} in Fahrenheit.")
            return
        except:
            print("There's Something Wrong With Your Input...!")

def fahr_to_cel():
    fahr = input("Enter Temperature in Fahrenheit: ")
    if (fahr.isalpha()):
        print("Input Must Be Numeric...!")
    else:
        try:
            fahr = float(fahr)
            conv = (fahr - 32) * 5/9
            conv = format(conv, ".2f")  
            print (f"{fahr} in Fahrenheit is equal to {conv} in Celcius.")
            return
        except:
            print("There's Something Wrong With Your Input...!")

if (choice == "1"):
    cel_to_fahr()
elif (choice == "2"):
    fahr_to_cel()
else:
    print("Input Cannot Be Recognised...!")
    exit()

# print("9.9".isalpha())