
from datetime import datetime
import re

attempts = 1
balance = 1000.0
messageExit = "\nSaliendo del programa..."

inputName = input("Inserta nombre: ")
inputPin = input("Inserta PIN: ")

def get_submenu_option():
    while True:
        print("\n1.-Menu")
        print("2.-Salir")
        input_option_return = input("Elije el numero de opcion a realizar: ")
        if input_option_return != "1" and input_option_return != "2":
            print("Opcion no valida!\n")
        elif input_option_return == "1":
            input_option_return = 0
            break
        elif input_option_return == "2":
            input_option_return = 4
            break
    return input_option_return


while attempts < 3:
    if "1235" != inputPin:
        attempts += 1
        print("PIN invalido! \n")
        inputPin = input("Inserta nuevamente PIN: ")
    if "1235" == inputPin:
        records = []
        attempts=4
        print("\nBienvenido " + f"{inputName}" + "!")
        i=1
        inputOption=""
        while True:
            if inputOption == 4:
                print(messageExit)
                break
            print("\n1.-Consultar saldo")
            print("2.-Retirar saldo")
            print("3.-Histórico de Movimientos")
            print("4.-Salir")
            inputOption = input("Elije el numero de opcion a realizar: ")
            if inputOption != "1" and inputOption != "2" and inputOption != "3" and inputOption != "4":
                print("Opcion no valida!\n")
            else:
                if inputOption == "1":
                    print("\nSaldo actual: " + str(balance))
                    inputOption = get_submenu_option()
                elif inputOption == "2":
                    inputPick = input("\nSaldo a retirar: ")
                    pre_balance = balance
                    if re.search("^[0-9]+(.[0-9]+)?$", inputPick):
                        balance = balance - float(inputPick)
                    else:
                        print("Respuesta invalida!")
                        inputOption = get_submenu_option()
                        continue
                    if balance < 0:
                        balance = balance + float(inputPick)
                        print("no se tienen fondos suficientes!")
                    elif float(inputPick) > 0:
                        today = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                        record = {
                            "date" : today,
                            "drawout" : inputPick,
                            "prebalance" : pre_balance,
                        }
                        records.append(record)
                        print("Se retiro con exito el saldo!")
                    inputOption = get_submenu_option()
                elif inputOption == "3":
                    print("\nHistorico de movimientos: \n")
                    print("Fecha:                      Retiro:   Saldo previo: ")
                    if len(records) > 0:
                        for record in records:
                            for key,value in record.items():
                                if key == "date":
                                    print("{:<28}".format(value), end="")
                                if key == "drawout":
                                    print("{:<10}".format(value), end="")
                                if key == "prebalance":
                                    print(f"{value}", end="")
                            print("")
                        print("")
                    inputOption = get_submenu_option()
                elif inputOption == "4":
                    print(messageExit)
                    break
    elif attempts==3:
        print("PIN invalido!")

if attempts==3:
    print("Se excedío el numero de intentos!!!")