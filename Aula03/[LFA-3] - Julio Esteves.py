# -*- coding: cp1252 -*-
#145052 - Julio Esteves

def Exercicio1A():    
    state = 0;
    input_string = raw_input("Digite a palavra a ser reconhecida\n");
    for x in input_string:
        if (state == 0):
            if (x == '0'):
                state = 0;
            elif (x == '1'):
                state = 1;
            else:
                state = -1;
        elif (state == 1):
            if (x == '0'):
                state = 1;
            elif (x == '1'):
                state = 2;
            else:
                state = -1;
        elif (state == 2):
            if (x == '0'):
                state = 2;
            elif (x == '1'):
                state = 3;
            else:
                state == -1;

    if state == 3:
        print("Palavra Aceita\n");
    elif (state == -1):
        print("ERROR");
    else:
        print("Palavra Não Aceita\n");
        
    
def Exercicio1B():
    state = 0;
    input_string = raw_input("Digite a palavra a ser reconhecida\n");
    for x in input_string:
        if (state == 0):
            if (x == '0' or x == '1'):
                state = 1
            else:
                state = -1;
        elif (state == 1):
            if (x == '0' or x == '1'):
                state = 2;
            else:
                state = -1;
        elif (state == 2):
            if (x == '0'):
                state = 1;
            elif (x == '1'):
                state = 3;
            else:
                state == -1;
        else:
            if (x == '0' or x == '1'):
                state = 2;

    if state == 3:
        print("Palavra Aceita\n");
    elif (state == -1):
        print("ERROR");
    else:
        print("Palavra Não Aceita\n");

def Exercicio1C():
    state = 0;
    input_string = raw_input("Digite a palavra a ser reconhecida\n");
    for x in input_string:
        if (state == 0):
            if (x == '0'):
                state = 1
            elif (x == '1'):
                state = 0;
            else:
                state = -1;
        elif (state == 1):
            if (x == '0'):
                state = 1;
            elif (x == '1'):
                state = 2;
            else:
                state = -1;
        elif (state == 2):
            if (x == '0'):
                state = 3;
            elif (x == '1'):
                state = 0;
            else:
                state == -1;
        elif (state == 3):
            if (x == '0'):
                state = 1;
            elif (x == '1'):
                state = 4;
            else:
                state = -1;
        elif (state == 4):
            if (x == '0' or x == '1'):
                state = 4;
            else:
                state = -1;

    if state == 4:
        print("Palavra Aceita\n");
    elif (state == -1):
        print("ERROR");
    else:
        print("Palavra Não Aceita\n");

def Exercicio1D():
    state = 0;
    input_string = raw_input("Digite a palavra a ser reconhecida\n");
    for x in input_string:
        if (state == 0):
            if (x == '0'):
                state = 1;
            elif (x == '1'):
                state = 2;
            else:
                state = -1;
        elif (state == 1):
            if (x == '0'):
                state = 4;
            elif (x == '1'):
                state = 3;
            else:
                state = -1;
        elif (state == 2):
            if (x == '0'):
                state = 5;
            else:
                state == -1;
        elif (state == 3):
            if (x == '0'):
                state = 6;
            else:
                state = -1;
        elif (state == 4):
            if (x == '0'):
                state = 4;
            elif (x == '1'):
                state = 6;
            else:
                state = -1;
        elif (state == 5):
            if (x == '0'):
                state = 6;
            else:
                state = -1;
        elif (state == 6):
            if (x == '0'):
                state = 6;
            else:
                state = -1;

    if state == 6:
        print("Palavra Aceita\n");
    elif (state == -1):
        print("ERROR");
    else:
        print("Palavra Não Aceita\n");

def Exercicio2():
    state = 0;
    saveState = 0;
    temp_inicial = 20;
    volume_inicial = 15;

    while(1):
        if (state == 0):
            print("Você está no Menu Principal\nA - Controle de Ar Condicionado\nS - Controle de Som\nX - Sair");
        elif (state == 1):
            print("Tela de Ar Condicionado\n(+) - Aumentar Temperatura\n(-) - Diminuir Temperatura\n(V) - Voltar ao Menu Principal\n");
        elif (state == 2):
            print("Tela de Som\n(+) - Aumentar Volume\n(-) - Diminuir Volume\n(V) - Voltar ao Menu Principal\n");
        elif (state == 3):
            print("Aumentando Temperatura...");       
            temp_inicial += 1;
            print("Temperatura Atual: " + str(temp_inicial));
            state = 1;
        elif (state == 4):
            print("Diminuindo Temperatura...\n");       
            temp_inicial -= 1;
            print("Temperatura Atual: " + str(temp_inicial));
            state = 1;
        elif (state == 5):
            print("Aumentando Volume...\n");       
            volume_inicial += 1;
            print("Volume Atual: " + str(volume_inicial));
            state = 2;
        elif (state == 6):
            print("Diminuindo Volume...\n");       
            volume_inicial -= 1;
            print("Volume Atual: "+ str(volume_inicial));
            state = 2;
        elif (state == 7):
            print("Saindo...");
            break;
        else:
            state = saveState;
            print("Opção Invalida.. Digite uma opção valida\n");
            
            
        letra = raw_input().upper();
        print(letra);
        if (letra == 'A' and state == 0):
            state = 1;
        elif (letra == 'S' and state == 0):
            state = 2;
        elif (letra == '+' and (state == 1 or state == 2)):
            if (state == 1):
                state = 3;
            else:
                state = 5;
        elif (letra == '-' and (state == 1 or state == 2)):
            if (state == 1):
                state = 4;
            else:
                state = 6;
        elif (letra == 'V'):
            state = 0;
        elif (letra == 'X' and state == 0):
            state = 7;
        else:
            saveState = state;
            state = -1;

Exercicio1A();
Exercicio1B();
Exercicio1C();
Exercicio1D();
Exercicio2();
