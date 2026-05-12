while True:
    classnum = int(input("Please enter number (1-30): "))

    match classnum:
        case 1:
            print("Abadejos")
        case 2:
            print("Alialy")
        case 3:
            print("Altamira")
        case 4:
            print("Arago")
        case 5:
            print("Banawan")
        case 6:
            print("Barrete")
        case 7:
            print("Buenaventura")
        case 8:
            print("Calalo")
        case 9:
            print("Custudio")
        case 10:
            print("De Chavez")
        case 11:
            print("De La Peña")
        case 12:
            print("Dela Cruz")
        case 13:
            print("Espiritu")
        case 14:
            print("Flores")
        case 15:
            print("Galido")
        case 16:
            print("Gonzales")
        case 17:
            print("Ibarra")
        case 18:
            print("Ilao")
        case 19:
            print("Magallanes")
        case 20:
            print("Manalo")
        case 21:
            print("Medroso")
        case 22:
            print("Mundo")
        case 23:
            print("Pabico")
        case 24:
            print("Promentilla")
        case 25:
            print("Razon")
        case 26:
            print("Rodriguez")
        case 27:
            print("Roxas")
        case 28:
            print("Sison")
        case 29:
            print("Torrano")
        case 30:
            print("Torres")

        case _:
            print("Invalid number. Please enter from range 1-30.")
            continue

    present = int(input("Enter number of days present: "))
    absent = int(input("Enter number of days absent: "))
    cutting = int(input("No. of times cutting classes: "))
    tardy = int(input("No. of times tardy: "))
    uniform = int(input("No. of times incomplete uniform: "))

    print(f"Days present: {present}")
    print(f"Days absent: {absent}")
    print(f"No. of times cutting: {cutting}")
    print(f"No. of times tardy: {tardy}")
    print(f"No. of times inc. uniform: {uniform}")

    again = input("\nPress Enter to continue or type 'exit' to stop: ")

    if again.lower() == "exit":
        print("Program ended.")
        break

