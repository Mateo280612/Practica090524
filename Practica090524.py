
class Persona:
    def   __init__(self,name,lastname,age):
        self._name = name
        self._lastname = lastname
        self._age= age

    @property
    def age (sellf):
        return sellf._age

    @age.setter
    def age (self, newValue):
        if newValue > 0:
            self._age = newValue
        else:
            raise ValueError('Edad no valida')
    @property
    def name (self):
        return  self._name

    @name.setter
    def name (self,newValue):
        self._name = newValue.capitalize()

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, newValue):
        self._lastname = newValue.capitalize()

persona1 = Persona('Mateo','Lòpez',19)
print (persona1.age)
persona1.age = 30
print (persona1.age)
persona1.name = 'pedro'
print (persona1.name)
persona1.lastname = 'perez'
print (persona1.lastname)
persona2 = Persona('Juan','Perz','20')

class AreaRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

rectangulo1 = AreaRectangulo(9,3)


class Calculadora:
    def __init__(self,num1,num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, newValue):
        if type(newValue) != 'int' and type(newValue) != 'float':
            raise ValueError('Ingrese un numero')
        else:
            self._num1 = newValue

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, newValue):
        if type(newValue) != 'int' and type(newValue) != 'float':
            raise ValueError('Ingrese un numero')
        else:
            self._num2 = newValue
    def suma(self):
        return self._num1 + self._num2
    def resta(self):
        return  self._num1 - self._num2
    def multiplicacion(self):
        return  self._num1 * self._num2
    def division(self):
        return  self._num1 / self._num2

Calculo1 = Calculadora(9,2)
print(Calculo1.division())



//Isinstance