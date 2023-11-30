#
class Persona:
    pais = "Peru"
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido =apellido
        self.edad = edad
    def obtener(self):
      print(f"Para obtener el atributo del objeto: {getattr(self,'edad')}")
    def existencia(self):
        print(f"Sabes que el atributo si existe: {hasattr(Persona,'pais')}")
    def asignar(self):
        setattr(Persona,'pais','Cuba')
        print(self.edad)
    def eliminaratrr(self):
        delattr(Persona,'pais')
doctor = Persona("Miguel","Mallqui",21)
doctor.obtener()
#doctor.existencia()
#doctor.eliminaratrr()
#doctor.asignar()
class Hijo(Persona):
    def __init__(self,grado,nombre,apellido):
        Persona.__init__(self,nombre,apellido,20)
        self.grado = grado

    
H = Hijo("Miguel","Torres","Secundario")
H.obtener()

class Calculadora:
    def __init__(self,n):
        self.n = n
        self.datos = [0 for i in range(self.n)] 
    def ingresardatos(self):
        self.datos =  [int(input("Ingresar datos:" + str(i+1) + ":")) for i in range(self.n)]
class Operacion(Calculadora):
    def __init__(self):
        super().__init__(2)
        #Calculadora.__init__(self,2)
    def s(self):
        a,b = self.datos
        print(f"Suma: {a+b}")
Op = Operacion()
print(isinstance(Op,Operacion))
# Verificar o revisar el tema de la herencia de clase
print(issubclass(Operacion,Calculadora))
# Multiple
class Telefono:
    alambrico = True;
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        if(self.alambrico):
            self.comunicacion = 'Alambrico'
        else:
            self.comunicacion = 'Inalambrico' 
    def llamar(self):
        return print('<p>Riing Riing!!!</p>');
    def obtener_informacion(self):
        return print(f'Marca: {self.marca}\nModelo: {self.modelo}\nComunicacion: {self.comunicacion}')
           
class Grabadora:
    encendido = False;
    def __init__(self) :
        pass

    def GetEncendido(self):
        return self.encendido
    def SetEncendido(self):
        self.encendido = True

class SmarthPhone(Telefono,Grabadora):
    def __init__(self,marca,modelo,color):
        Telefono.__init__(self,marca,modelo)
        Grabadora.__init__(self)
        self.color = color
        
    def obtener(self):
        print(self.comunicacion)

    """def __str__(self):
        return f"====Informacion====\nMarca: {self.marca}\nModelo: {self.modelo}\nTipo: {self.comunicacion}"""
    """def __repr__(self):
        return f"====Informacion====\nMarca: {self.marca}\nModelo: {self.modelo}\nTipo: {self.comunicacion}"""
   
    # De la manera independiente estos valores solo pertenece a esta clase
    """@classmethod
    def Smartphone_11(cls):
        return cls(['Huawai','A11',['camara','memoria','pixeles']])"""
    @classmethod
    def Smartphone_12(cls):
        cls.pixeles = 12
        return cls.alambrico
    @classmethod
    def SaberPixeles(cls):
        print(f"Pixeles: {cls.pixeles}")
movil = SmarthPhone('Apple','X0111',"Marron")
movil.obtener_informacion()
print(movil.comunicacion)
print(movil.GetEncendido())
movil.obtener()
print(f"{movil !r}")
print(SmarthPhone.Smartphone_12())
print(movil.Smartphone_12())
SmarthPhone.SaberPixeles()
#print(dir(movil))
# Metodo de clase @classmethod Este metodo puede ser llamado sin crear una instancia de la clase 
# Metodo de clase @staticmethod pueden ser llamados sin tener una instancia de la clase, ademas este
# tipo de metodo no tienen acceso al exterior,por lo cual no puede acceder a ningun otro atributo o llamar a
# ninguna otra funcion dentro de la clase
import math
class Pastel:
    def __init__(self,ing,tamano):
        self.ing = ing
        self.__tamano = tamano
    def __repr__(self):
        return (f'Pastel({self.ing}, 'f'{self.__tamano})')
    def area(self):
        return self.__tamano_area(self.__tamano)
    def __setTamano(self,ta):
        self.__tamano = ta

    @staticmethod
    def __tamano_area(A):
        return A ** 2 * math.pi
    def __getTamano(self):
        return self.__tamano
    def __setTamano(self,ta):
        self.__tamano = ta

    def __deltamano(self):
        del self.__tamano
    tamano = property(fget=__getTamano,fset= __setTamano,fdel=__deltamano,
                      doc="soy la propiedad del tamano")
    


class Chocolate(Pastel):
    pass
Chocolate = Chocolate(['Harina',"Azucar","Leche",'Crema'],10)
print(Chocolate._Pastel__tamano_area(10))
Chocolate.tamano = 30
print(Chocolate.tamano)
nuevo_pastel = Pastel(['Harina',"Azucar","Leche",'Crema'],15)
nuevo_pastel.tamano = 20
print(nuevo_pastel.tamano)
help(nuevo_pastel)

#print(nuevo_pastel.GetTamano())
print(nuevo_pastel._Pastel__tamano)
print(nuevo_pastel._Pastel__tamano_area(10))
print(f'{nuevo_pastel !r}')
print(nuevo_pastel.area())
#print(nuevo_pastel.tamano_area__(10))
#print(Pastel.tamano_area(4))
class Mamifero:
    def __init__(self,nombre):
        print(nombre,'Padre')
class Leon(Mamifero):
    def __init__(self):
        print("Hijo")
        #super().__init__('Miguel')
        Mamifero.__init__(self,'Miguel')
leon = Leon()

