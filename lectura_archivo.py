class Inicio:

    """ ABRIR ARCHIVOS """
    def abrir_archivo(self, ruta):
        #Abrir .txt con lexico a analizar
        expresiones = open(ruta)
        return expresiones

    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()   



   




       

   
