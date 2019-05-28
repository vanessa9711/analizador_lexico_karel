import ply.lex as lex
from lectura_archivo import *

"""ANALIZADOR LEXICO PARA KAREL"""
class Lexer:

    #Tipos de tokens para Karel (LEXICO DE PASCAL)
    tokens = [ 'LEXICO_SIMPLE', 'LEXICO_DOBLE', 'LEXICO_TRIPLE', 'LEXICO_CUADRUPLE', 'LEXICO_QUINTUPLE',
               'NUMERO', "DECLARACION_PROGRAMA", "DECLARACION_PROCEDIMIENTO", "EXPRESION",
               "EXPRESION_SI", "EXPRESION_MIENTRAS", "EXPRESION_PARA", "TERMINO",
               "CLAUSULA_Y", "CLAUSULA_NO", "CLAUSULA_ATOMICA", "EXPRESION_ENTERA",
               "FUNCION_BOOLEANA", "COMENTARIO_INICIO_LINEA", "COMENTARIO_FIN_LINEA",
               "COMENTARIO_INICIO_MULTILINEA", "COMENTARIO_FIN_MULTILINEA" , "LEXICO_SIN_RECONOCER"]

    #Tokens a ignorar
    t_ignore = '\n'' '';'
    #Comentarios
    t_COMENTARIO_INICIO_LINEA = r'{'
    t_COMENTARIO_FIN_LINEA = r'}'
    t_COMENTARIO_INICIO_MULTILINEA = r'\(\*'
    t_COMENTARIO_FIN_MULTILINEA = r'\*\)'

    #Definir un número
    def t_NUMERO(t):
        r'\d+'
        t.value = int(t.value)
        return t

    #Para instrucciones AA-AA-AA-AA-AA
    def t_LEXICO_QUINTUPLE(t):
        r'[a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*'
        if t.value == "algun-zumbador-en-la-mochila" or t.value == "ningun-zumbador-en-la-mochila": 
            t.type = "FUNCION_BOOLEANA"
        return t
    
    #Para instrucciones AA-AA-AA-AA
    def t_LEXICO_CUADRUPLE(t):
        r'[a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*'
        if t.value == "no-junto-a-zumbador": 
            t.type = "FUNCION_BOOLEANA"
        elif t.value == "no-orientado-al-norte" or t.value == "no-orientado-al-sur" or t.value == "no-orientado-al-este" or t.value == "no-orientado-al-oeste": 
            t.type = "FUNCION_BOOLEANA"
        return t

    #Para instrucciones AA-AA-AA
    def t_LEXICO_TRIPLE(t):
        r'[a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*'
        if t.value == "define-nueva-instruccion":
            t.type = "DECLARACION_PROCEDIMIENTO"
        elif t.value == "sal-de-instruccion":
            t.type = "EXPRESION"
        elif t.value == "si-es-cero":
            t.type = "CLAUSULA_ATOMICA"
        elif t.value == "junto-a-zumbador" or t.value == "orientado-al-norte" or t.value == "orientado-al-sur" or t.value == "orientado-al-este" or t.value == "orientado-al-oeste":
            t.type = "FUNCION_BOOLEANA"
        return t
    
    #Para instrucciones AA-AA
    def t_LEXICO_DOBLE(t):
        r'[a-zA-Z][a-zA-Z]*[-][a-zA-Z][a-zA-Z]*'
        if t.value == "iniciar-programa" or t.value == "inicia-ejecucion" or t.value == "termina-ejecucion" or t.value == "finalizar-programa":
            t.type = "DECLARACION_PROGRAMA"
        elif t.value == "gira-izquierda" or t.value == "coge-zumbador" or t.value == "deja-zumbador":
            t.type = "EXPRESION"
        elif t.value == "frente-libre" or t.value == "frente-bloqueado" or t.value == "izquierda-libre" or t.value == "izquierda-bloqueada":
            t.type = "FUNCION_BOOLEANA"
        elif t.value == "derecha-libre" or t.value == "derecha-bloqueada":
            t.type = "FUNCION_BOOLEANA"
        return t

    #Para instrucciones AA
    def t_LEXICO_SIMPLE(t):
        r'[a-zA-Z][a-zA-Z]*'
        if t.value == "como":
            t.type = "DECLARACION_PROCEDIMIENTO"
        elif t.value == "apagate" or t.value == "avanza" or t.value == "inicio" or t.value == "fin":
            t.type = "EXPRESION"
        elif t.value == "si" or t.value == "entonces" or t.value == "sino":
            t.type = "EXPRESION_SI"
        elif t.value == "mientras" or t.value == "hacer":
            t.type = "EXPRESION_MIENTRAS"
        elif t.value == "repetir" or t.value == "veces":
            t.type = "EXPRESION_PARA"
        elif t.value == "no":
            t.type = "CLAUSULA_NO"
        elif t.value == "si-es-cero":
            t.type = "CLAUSULA_ATOMICA"
        elif t.value == "precede" or t.value == "sucede":
            t.type = "CLAUSULA_ATOMICA"
        elif t.value == 'o':
            t.type = "TERMINO"
        elif t.value == 'y':
            t.type = "CLAUSULA_Y"
        else:
            t.type = "LEXICO_SIN_RECONOCER"
        return t
     
    # Errores
    def t_error(t):
        print("Instrucción no reconocida '%s'" % t.value[0])
        t.lexer.skip(1)

    # Construcción del lexer
    lex.lex()
    #Escribirá un archivo llamado lextab.py en el mismo directorio que el módulo que contiene la especificación lexer.
    #lex.lex(optimize=1)

    # Objeto de inicio
    inicio = Inicio()
    elementos = inicio.abrir_archivo()
    impresion =""
    linea = [" "]

    #Mientras hayan elementos en el archivo
    while linea != '':
        #Leer linea a linea del .txt
        linea = ' '.join(elementos.readline().split(' '))
        #Valor a analizar en lexer
        lex.input(linea)
        while True:
            #Devuelve
            #(tok.type, tok.value, tok.lineno, tok.lexpos)
            #(tipo, valor, value, número de línea, indice del token en la línea)
            tok = lex.token()
            #Sino hay más que leer, termine
            if not tok:
                break
            impresion += str((str(tok.type)+" - "+str(tok.value))) + '\n'
        if (linea == ['']):
            expresiones.close()
            break
    inicio.escribir_archivo(impresion)
    
lexer = Lexer()
