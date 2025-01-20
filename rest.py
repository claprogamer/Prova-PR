numero = int(input("Numero: "))

person = input("Sei una persona: ").capitalize()
while numero >= 18:
    if person == "Y" or person == "Yes":
        print("accettato!")