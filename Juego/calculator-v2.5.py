import os,random

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

    option = 0

    print("******************************** CALCULADORA ********************************")
    print("1.- Multiplicar en orden")
    print("2.- Multiplicar con numeros aleatorios")
    print("3.- Score")
    print("4.- Exit")

    try:
        option = int(input("Introduce opcion: ").strip())
    except ValueError:
        option = 0

    if option <= 4 and option >= 1:
            return option

def multiplication(op):

    global total_regular_correct    #Hay que indicar que estamos usando las variables que inicializamos fuera de la función
    global total_regular_incorrect  #ya que, si no ponemos el 'global', Python las reconoce como variables locales no inicializadas
    global total_random_correct
    global total_random_incorrect
    global corrects
    global mistakes

    corrects = 0 #Reseteo de corrects y mistakes
    mistakes = 0

    if op == 1: #El usuario ha elegido hacer multiplicaciones en orden
        tables = get_tables()
        for table in tables:
            for i in range(1, 11):
                correct_result = int(table) * i
                result = get_result(table, i)
                check_result(correct_result, result, table)

        total_regular_correct += corrects
        total_regular_incorrect += mistakes

    elif op == 2: #El usuario ha elegido hacer multiplicaciones con numeros aleatorios

        choose_random = 0 #Variable que guarda la opcion elegida

        while (choose_random > 2 or choose_random < 1 ):

            os.system("CLS")

            print("¿Quieres elegir las tablas que multiplicar?")
            print("1.- No")
            print("2.- Si")

            try:
                choose_random = int(input("Opción: ").strip())
            except ValueError:
                choose_random = 0

        if choose_random == 2: #Elige la tabla que quiere multiplicar
            tables = get_tables()
            for table in tables:
                for i in range(1, 11):
                    random_number = random.randint(1, 10)
                    correct_result = int(table) * random_number
                    result = get_result(table, random_number)

                    check_result(correct_result, result, table)

        elif choose_random == 1: #Elige que salga tablas aleatorias a multiplicar

            for i in range(1, 11):
                random_number1 = random.randint(1, 10)
                random_number2 = random.randint(1, 10)
                correct_result = random_number1 * random_number2
                result = get_result(random_number1, random_number2)

                check_result(correct_result, result, random_number1)

        total_random_correct += corrects
        total_random_incorrect += mistakes

def score():

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

    global corrects
    global mistakes

    if correct_result == result:
        corrects += 1
        print("CORRECTO")
        set_knowledge(True, table)
    else:
        mistakes += 1
        print(f"INCORRECTO, es {correct_result}")
        set_knowledge(False, table)

def print_results(corrects, mistakes):
    print("\n************FINAL************")
    print(F"ACIERTOS: {corrects}")
    print(F"FALLOS: {mistakes}\n")
    print("Pulsa Enter para volver...")
    input()

def main():

    op = None

    while op != 4:
        os.system("CLS")
        op = main_menu()
        if op == 1:
            os.system("CLS")
            multiplication(op)
            print_results(corrects, mistakes)
        elif op == 2:
            os.system("CLS")
            multiplication(op)
            print_results(corrects, mistakes)
        elif op == 3:
            os.system("CLS")
            score()
            os.system("CLS")
        elif op == 4:
            print("Hasta la proxima!!!")

if __name__ == '__main__':
    main()