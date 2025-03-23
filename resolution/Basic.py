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

    def Mate(self,Propiedad:str,a:int,b:int):
        """
        Esta es para sumar pero solo si le pones la propiedad sum
        si quieres restar tienes que poner res,dividir div,
        multiplicar mult tambien por su puesto NO SE TE OCURRA PONER
        1/0 que te apago la compu hdp.
        """
        import os
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
        import os
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
    def Flask(self,Type_app:str,host:str,port:int,index:list):
        """
        Este es el modulo de flask, el cual te permite hacer una app web con python
        solo tienes que poner el tipo de app que quieres hacer, si es una api o una app web
        y el host y el puerto donde se va a alojar la app tambien el index o el app route de inicio
        por ejemplo si quieres que tu app inicie en homte debes agregarlo en la lista como el 
        primer elemento de la lista.

        [index principal,index_secundario,etc]
        """
        from flask import Flask
        app = Flask(__name__)
        if Type_app == "api":
            @app.route('/')
            def hello_world():
                return 'Hello, World!'
        if Type_app == "web":
            @app.route('/')
            def hello_world():
                return 'Hello, World!'
        app.run(host=host,port=port,debug=True)