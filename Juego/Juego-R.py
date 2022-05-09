import random
import os
#adadada
cono1=0
cono2=0
cono3=0
cono4=0
cono5=0
cono6=0
cono7=0
cono8=0
cono9=0
cono10=0

scoreMRAcertado = 0
scoreMRFallado = 0

scoreMOAcertado = 0
scoreMOFallado = 0


def menu():
    os.system("CLS")
    print("---------\t Multiplicaiones \t---------")
    print("1.- Multiplicar en orden.\t\t\t|")
    print("2.- Multiplicar con numeros aleatorios.\t\t|")
    print("\t\t\t\t\t\t|")
    print("3.- Score.\t\t\t\t\t|")
    print("4.- Exit.\t\t\t\t\t|")
    print("-------------------------------------------------\n")

    while True:
        try:
            op = int(input("Elija una de las opciones:1-4\n"))
            break
        except ValueError:
            print("Solo se admiten numeros del 1 al 4...\n")
            print("Pulsa Enter para volver...")
            input()
            menu()  

    if op <= 0 or op >= 5:
        print("Introduzca una opción valida!!!!!!\n")
        print("Pulsa Enter para volver...")
        input()
        menu()

    if op == 1:
        multO()
    elif op == 2:
        aleatorias()
    elif op == 3:
        score()
    elif op == 4:
        print("Hasta la proxima.")
        input()
        os.system("CLS")
        exit()
    
def multO():
    
    os.system("CLS")
    global scoreMOAcertado
    global scoreMOFallado
    
    contA = 0
    contF = 0
    
    br = 1

    print("Qué tabla/s de multiplicar quieres repasar?\n(Sí quieres añadir más tablas, solo escribe un espacio y acontinuación el la tabla que quieres añadir...)\n")
    
    while True:
        try:
            info = input("Tu tabla/s seleccionada/s --> ")
            break           
        except ValueError:
            os.system("CLS")
            print("Qué tabla/s de multiplicar quieres repasar?\n(Sí quieres añadir más tablas, solo escribe un espacio y acontinuación el la tabla que quieres añadir...)\n")

    while True:
        try:
            tab = list(map(int,info.split(" ")))
            break           
        except BaseException:
            multO()
    
    cont = len(tab)        
    pos = 0
    os.system("CLS")    
    
    while (pos < cont):
        while (br < 11):

            num2 = br
            num1 = tab[pos]
            compr = num1 * num2
            
            while True:
                try:
                    res = int(input(f'{num1} x {num2} ? '))
                    break
                except ValueError:
                    print("Solo se admiten numeros...\n")
                    print("Pulsa Enter para volver...")
                    input()
                    os.system("CLS")
            
            knowledge(res,compr,num1)
            
            if res == compr:
                print("Correcto!!!")
                contA = 1 + contA
            else:
                print(f'Incorrecto!!! --> El resultado es: {compr}')
                contF = 1 + contF
            
            br = 1 + br

        br = 0
        
        pos = 1 + pos
        
        if (pos < cont):
            os.system("CLS")
            print("-----------------\tSIGUIENTE TABLA DE MULTIPLICAR\t-----------------\n")

    print("Juego terminado!!!\n")
    
    print("******** Resultado Final ********")
    print(f'Aciertos --> {contA}\t\t\t|')
    print(f'Fallos --> {contF}\t\t\t|')
    print("*********************************")
    
    input()
    
    os.system("CLS")
    
    menu()    
          
def score():
    os.system("CLS")
    print("-------------------PUNTUACIÓN-----------------------")
    print(f'Multiplicaciones aleatorias acertadas: {scoreMRAcertado}' )
    print(f'Multiplicaciones en orden acertadas: {scoreMOAcertado}\n' )
  
    print("------------------RESULTADOS TOTALES--------------------")
    totalA = scoreMRAcertado + scoreMOAcertado
    totalF = scoreMRFallado + scoreMOFallado
    print(f"Número total de aciertos: {totalA}" )
    print(f"Número total de fallos: {totalF}\n" )
    
    print("------------------CONOCIMIENTO TOTAL--------------------")
    print("Conocimiento por tablas:")
    print(f'\t La tabla del 1 --> {cono1} de 100')
    print(f'\t La tabla del 2 --> {cono2} de 100')
    print(f'\t La tabla del 3 --> {cono3} de 100')
    print(f'\t La tabla del 4 --> {cono4} de 100')
    print(f'\t La tabla del 5 --> {cono5} de 100')
    print(f'\t La tabla del 6 --> {cono6} de 100')
    print(f'\t La tabla del 7 --> {cono7} de 100')
    print(f'\t La tabla del 8 --> {cono8} de 100')
    print(f'\t La tabla del 9 --> {cono9} de 100')
    print(f'\t La tabla del 10 --> {cono10} de 100')
    

    print("\nPulse Enter para volver...")
    input()
    
    os.system("CLS")
    
    menu()

def aleatorias():
    
    global scoreMRAcertado
    global scoreMRFallado
    
    contA = 0
    contF = 0
    
    os.system("CLS")
    resp = str(input("¿Quieres elegir las tablas que multiplicar o no? (y/n)\n"))
    
    if resp == 'n' or resp == 'N':
        os.system("CLS")
        br = 1
        while (br < 11):

            num1 = random.randint(2,10)
            num2 = random.randint(2,10)
            
            compr = num1 * num2
                
            while True:
                try:
                    res = int(input(f'{num1} x {num2} ? '))
                    break
                except ValueError:
                    print("\nSolo se admiten numeros...\n")
                    print("Pulsa Enter para volver...")
                    input()
                    os.system("CLS")

            
            knowledge(res,compr,num1)
            
            if res == compr:
                print("Correcto!!!")
                contA = 1 + contA
            else:
                print(f'Incorrecto!!! --> El resultado es: {compr}')
                contF = 1 + contF
            
            br = 1 + br
        
        print("Juego terminado!!!\n")
        
        print("******** Resultado Final ********")
        print(f'Aciertos --> {contA}\t\t\t|')
        print(f'Fallos --> {contF}\t\t\t|')
        print("*********************************")
        scoreMRAcertado = scoreMRAcertado + contA
        scoreMRFallado = scoreMRFallado + contF
        
        input()
        
        os.system("CLS")
        
        menu()
    elif resp == 'y' or resp == 'Y':
        
        br=0
        os.system("CLS")
        print("Qué tabla/s de multiplicar quieres repasar?\n(Sí quieres añadir más tablas, solo escribe un espacio y acontinuación la tabla que quieres añadir...)\n")
    
        while True:
                try:
                    info = input("Tu tabla/s seleccionada/s --> ")
                    break           
                except ValueError:
                    os.system("CLS")
                    print("Qué tabla/s de multiplicar quieres repasar?\n(Sí quieres añadir más tablas, solo escribe un espacio y acontinuación el la tabla que quieres añadir...)\n")

        while True:
                try:
                    tab = list(map(int,info.split(" ")))
                    break           
                except BaseException:
                    os.system("CLS")
                    print("Qué tabla/s de multiplicar quieres repasar?\n(Sí quieres añadir más tablas, solo escribe un espacio y acontinuación el la tabla que quieres añadir...)\n")
                    
        
        cont = len(tab)        
        pos = 0
        os.system("CLS")    
        
        while (pos < cont):
            while (br < 10):

                num2 = random.randint(1,10)
                num1 = tab[pos]
                compr = num1 * num2
                
                while True:
                    try:
                        res = int(input(f'{num1} x {num2} ? '))
                        break
                    except ValueError:
                        print("\nSolo se admiten numeros...\n")
                        print("Pulsa Enter para volver...")
                        input()
                        os.system("CLS")
                
                knowledge(res,compr,num1)
                
                if res == compr:
                    print("Correcto!!!")
                    contA = 1 + contA
                else:
                    print(f'Incorrecto!!! --> El resultado es: {compr}')
                    contF = 1 + contF
                
                br = 1 + br
                if (br == 10):
                    os.system("CLS")
                    print("-----------------\tSIGUIENTE TABLA DE MULTIPLICAR\t-----------------\n")

            br = 0
            
            pos = 1 + pos
        print("Juego terminado!!!\n")
    
        print("******** Resultado Final ********")
        print(f'Aciertos --> {contA}\t\t\t|')
        print(f'Fallos --> {contF}\t\t\t|')
        print("*********************************")
        
        scoreMRAcertado = scoreMRAcertado + contA
        scoreMRFallado = scoreMRFallado + contF
        
        input()
        
        os.system("CLS")
        
        menu()
    else:
        aleatorias()
        
def knowledge(res,comp,tab):
    
    global cono1
    global cono2
    global cono3
    global cono4
    global cono5
    global cono6
    global cono7
    global cono8
    global cono9
    global cono10
    
    if res == comp:
        if tab == 1:
            cono1 += 10
            if cono1 >= 100:
                cono1 = 100
        elif tab == 2:
            cono2 += 10
            if cono2 >= 100:
                cono2 = 100
        elif tab == 3:
            cono3 += 10
            if cono3 >= 100:
                cono3 = 100
        elif tab == 4 :
            cono4 += 10
            if cono4 >= 100:
                cono4 = 100
        elif tab == 5:
            cono5 += 10
            if cono5 >= 100:
                cono5 = 100
        elif tab == 6:
            cono6 += 10
            if cono6 >= 100:
                cono6 = 100
        elif tab == 7:
            cono7 += 10
            if cono7 >= 100:
                cono7 = 100
        elif tab == 8:
            cono8 += 10
            if cono8 >= 100:
                cono8 = 100
        elif tab == 9:
            cono9 += 10
            if cono9 >= 100:
                cono9 = 100
        elif tab == 10:
            cono10 += 10
            if cono10 >= 100:
                cono10 = 100
    elif res != comp:
        if tab == 1:
            cono1 -= 10
            if cono1 <= 0:
                cono1 = 0
        elif tab == 2:
            cono2 -= 10
            if cono2 <= 0:
                cono2 = 0
        elif tab == 3:
            cono3 -= 10
            if cono3 <= 0:
                cono3 = 0
        elif tab == 4 :
            cono4 -= 10
            if cono4 <= 0:
                cono4 = 0
        elif tab == 5:
            cono5 -= 10
            if cono5 <= 0:
                cono5 = 0
        elif tab == 6:
            cono6 -= 10
            if cono6 <= 0:
                cono6 = 0
        elif tab == 7:
            cono7 -= 10
            if cono7 <= 0:
                cono7 = 0
        elif tab == 8:
            cono8 -= 10
            if cono8 <= 0:
                cono8 = 0
        elif tab == 9:
            cono9 -= 10
            if cono9 <= 0:
                cono9 = 0
        elif tab == 10:
            cono10 -= 10
            if cono10 <= 0:
                cono10 = 0
               
def main():
    menu()

if __name__ == "__main__":
	main()