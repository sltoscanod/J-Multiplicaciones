import os
import random

total_regular_correct = 0
total_regular_incorrect = 0
total_random_correct = 0
total_random_incorrect = 0

corrects = 0
mistakes = 0

knowledge = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
}

def main_menu():

    os.system("CLS")

    option = 0

    print("******************************** CALCULADORA ********************************")
    print("1.- Multiplicar en orden")
    print("2.- Multiplicar con numeros aleatorios")
    print("3.- Score")
    print("4.- Exit")

    try:
            option = int(input("Introduce opcion: "))
    except ValueError:
            option = None

    if option == 1:
            return 1
    elif option == 2:
            return 2
    elif option == 3:
            return 3
    elif option == 4:
            return 4

def regular_multiplication():

    os.system("CLS")

    global corrects
    global mistakes

    corrects = 0
    mistakes = 0

    tables = get_tables()
    for table in tables:
        for i in range(1, 11):
            correct_result = int(table) * i
            result = get_result(table, i)
            if check_result(correct_result, result, table):
                corrects += 1
            else:
                mistakes += 1

    global total_regular_correct
    global total_regular_incorrect

    total_regular_correct += corrects
    total_regular_incorrect += mistakes

def random_multiplication():

    os.system("CLS")

    global corrects
    global mistakes

    corrects = 0
    mistakes = 0

    random_tables = 0 #Variable que guarda la opcion elegida

    while (random_tables > 2 or random_tables < 1 or random_tables is None or random_tables=='' ):

        os.system("CLS")

        print("¿Quieres elegir las tablas que multiplicar?")
        print("1.- No")
        print("2.- Si")

        random_tables = int(input("Opción: "))

    if random_tables == 2:
        tables = get_tables()
        for table in tables:
            for i in range(1, 11):
                random_number = random.randint(1, 10)
                correct_result = int(table) * random_number
                result = get_result(table, random_number)

                if check_result(correct_result, result, table):
                    corrects += 1
                else:
                    mistakes += 1
    elif random_tables == 1:

        for i in range(1, 11):
            random_number1 = random.randint(1, 10)
            random_number2 = random.randint(1, 10)
            correct_result = random_number1 * random_number2
            result = get_result(random_number1, random_number2)

            if check_result(correct_result, result, random_number1):
                corrects += 1
            else:
                mistakes += 1

    global total_random_correct
    global total_random_incorrect

    total_random_correct += corrects
    total_random_incorrect += mistakes

def score():

    os.system("CLS")

    print("************PUNTUACION*************")
    print(f"ALEATORIAS ACERTADAS: {total_random_correct}")
    print(f"ALEATORIAS FALLADAS: {total_random_incorrect}")
    print(f"NORMALES ACERTADAS: {total_regular_correct}")
    print(f"NORMALES FALLADAS: {total_regular_incorrect}\n")
    print("******CONOCIMIENTO POR TABLAS******")
    for k, v in knowledge.items():
        print(f"TABLA DEL {k}: {v} de 100")

    print("\nPulsa Enter para volver...")
    input()
    os.system("CLS")

def set_knowledge(correct, table):

    table = str(table)

    if correct:
        knowledge[table] += 10
        if knowledge[table] > 100:
            knowledge[table] = 100
    else:
        knowledge[table] -= 10
        if knowledge[table] < 0:
            knowledge[table] = 0

def get_tables():

    os.system("CLS")

    value = None
    while value is None or value == '':
        try:
            os.system("CLS")
            value = input("¿Que tablas quieres multiplicar? Separalas por comas: ")
        except ValueError:
            value = None
    tables = value.strip(",").strip().split(',')
    return tables

def get_result(num1, num2):
    result = None
    while result is None:
        try:
            result = int(input(f"{num1} x {num2} = "))
        except ValueError:
            result = None
    return result

def check_result(correct_result, result, table):
    if correct_result == result:
        print("CORRECTO")
        set_knowledge(True, table)
        return True
    else:
        print(f"INCORRECTO, es {correct_result}")
        set_knowledge(False, table)
        return False

def print_results(corrects, mistakes):
    print("\n************FINAL************")
    print(F"ACIERTOS: {corrects}")
    print(F"FALLOS: {mistakes}\n")
    print("Pulsa Enter para volver...")
    input()
    os.system("CLS")

def main():

    op = None

    while op != 4 or op is None:
        op = main_menu()
        if op == 1:
            regular_multiplication()
            print_results(corrects, mistakes)
        elif op == 2:
            random_multiplication()
            print_results(corrects, mistakes)
        elif op == 3:
            score()
        elif op == 4:
            print("ADIOS")

if __name__ == '__main__':
    main()