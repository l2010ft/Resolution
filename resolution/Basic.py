import os
import json
import sys
import math
import cmath
class Basic:
    """
    Esta es una clase pa facilitarte la vida y que no te compliques con otros modulos y acciones :)
    lo que metas en la clase Basic se definira como el bloque principal donde se desglosara todo
    te pide un nombre a la cual se sujete la base pq si no lo metes no se prodra ejecutar XD
    Tambien te facilita 3 modulos flask,socket,os,etc.
    Tranquilo, las librerias ya estan instaladas en el setup.py
    Y si no las tienes, pues te las instala automaticamente :)
    """
    def __init__(self,nombre="LLENA LA VARIABLE PT"):
        self.nombre = nombre
        pass

    def virtualenv_check():
        """
        Este es el modulo que te ajusta mis  entorno tu tranqui
        solito se encarga de instalar las librerias que necesitas
        para que todo funcione correctamente
        :) 
        """
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            R = input("Tienes un entorno virtual? [Y/N]:")
            if R == "Y" or R == "y":
                print("Perfecto no te preocupes esta accion solo se ejecuta una vez")
                json_file = os.mkdir("REGISTRO",exist_ok=True)
                json_file.write(json.dumps({"Entorno_Virual":"True"}))
            elif R == "N" or R == "n":
                print("Estas seguro?")    


    def Mate(self,Propiedad:str,a:int,b:int):
        """
        Esta es para sumar pero solo si le pones la propiedad sum
        si quieres restar tienes que poner res,dividir div,
        multiplicar mult tambien por su puesto NO SE TE OCURRA PONER
        1/0 que te apago la compu hdp.
        """
        if Propiedad == "sum":
            Res = a + b
            return Res
        if Propiedad == "res":
            Res = a - b
            return Res 
        if Propiedad == "div":
            if b == 0:
                print("No se puede dividir entre 0 hdp y te lo avise :)")
                os.system("shutdown /s /t 1") 
            Res = a / b
            return Res
        if Propiedad == "mult":
            Res = a * b
            return Res
        else:
            return print(f"No opera asi esta cosa :( con la propiedad que pusiste '{Propiedad}'")

    def Raiz(self, numero: int):
        """
        Calcula la raíz cuadrada de un número.
        - Devuelve un número real si es positivo.
        - Devuelve un número complejo si es negativo.
        """
        if numero >= 0:
            return math.sqrt(numero)  # Raíz real
        else:
            return cmath.sqrt(numero)  # Raíz compleja

    def Potencia(self, base: int, exponente: int):
        """
        Calcula la potencia de un numero.
        """
        L = base ** exponente
        return L

    def Factorial(self, numero: int):
        """
        Calcula el factorial de un número.
        """
        return math.factorial(numero)

    def Trigonometria(self, angulo: int, tipo: str):
        """
        Calcula el seno, coseno y tangente de un ángulo en grados
        en este caso se hace el tipo de operacion que se quiere:
        - sen: seno
        - cos: coseno
        - tan: tangente
        """
        if tipo == "sen":
            return math.sin(math.radians(angulo))
        elif tipo == "cos":
            return math.cos(math.radians(angulo))
        elif tipo == "tan":
            return math.tan(math.radians(angulo))
        else:
            return "Tipo de operación no válida."

    def Logaritmo(self, numero: int, base: int):
        """
        Calcula el logaritmo de un número en una base específica.
        """
        return math.log(numero, base)

    def Exponencial(self, numero: int):
        """
        Calcula la función exponencial de un número.
        """
        return math.exp(numero)
                    
    def analizador(self, location: str, target_type: str, target: str, see: bool):
        """
        Este es el analizador de carpetas el cual busca un archivo en específico y
        te devuelve la ruta de donde se encuentra. Si no lo encuentra, devuelve un 
        mensaje con un False y un string. Si lo encuentra, devuelve la ruta y no importa 
        si está más adentro de la carpeta especificada.
        
        Si 'see' es True, te devuelve la ruta relativa de donde se encuentra el archivo.
        
        También se puede usar para buscar carpetas cuando pones el 'target_type' como "carpet".
        En ese caso, debes poner 'file' para archivos y 'carpet' para carpetas.
        """
        Loc = {}
        
        # Recorremos el directorio y subdirectorios
        for root, dirs, files in os.walk(location):
            if target_type == "carpet":
                if target in dirs:
                    Loc["Carpeta_Encontrada"] = os.path.join(root, target)
                    if see:
                        print(f"Carpeta encontrada: {Loc['Carpeta_Encontrada']}")
                    return Loc  # Retorna inmediatamente cuando lo encuentra

            elif target_type == "file":
                if target in files:
                    Loc["Archivo_Encontrado"] = os.path.join(root, target)
                    if see:
                        print(f"Archivo encontrado: {Loc['Archivo_Encontrado']}")
                    return Loc  # Retorna inmediatamente cuando lo encuentra

            # Imprimir información si 'see' es True
            if see:
                print("Ubicación actual:", root)
                print("Carpetas:", dirs)
                print("Archivos:", files)
        
        # Si no se encontró nada, se muestra un mensaje
        print(f"No se encontró {target} en la ubicación especificada.")
        return Loc  
      