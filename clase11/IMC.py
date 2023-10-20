class personas:
  def __init__(self):
    nombre=None
    altura=None
    peso=None

def setNombre(self,nombre:str):
    self.nombre=nombre

def setAltura(self,altura:int):
    self.altura=altura

def setPeso(self,altura:int):
    if peso>0:
       self.peso=peso
    else:
       self.peso=None
def getNombre(self):
    return self.nombre

def getAltura(self):
   

def getPeso(self):
    if self.peso==0:
            return 0
    return self.peso
   
def imc(self):
      altura=self.getAltura()
      peso=self.getPeso()
      valor_imc=(self.peso)/(self.altura/100)**2
      if valor_imc <18.5:
         return f'IMC: {valor_imc} peso por debajo.'
      elif valor_imc<24.9:
         return f'IMC: {valor_imc} peso saludable'
      elif valor_imc<29.9:
         return f'IMC: {valor_imc} peso saludable'
      elif valor_imc<34.9:
         return f'IMC: {valor_imc} peso saludable'
      elif valor_imc<39.9:
         return f'IMC: {valor_imc} peso saludable'
      return f'IMC: {valor_imc:.2f} peso obesidad[]'

def main()
    pacientes=[]
    while 1:
        usuario=personas()
        usuario.setnombre(input('nombre: '))
        usuario.setAltura(int(input('altura(cm): ')))


        pacientes.append(usuario)

        print(f'Nombre: {usuario.nombre}\n'
        f'altura: {usuario.altura} cm\n
        f'peso {usuario.altura} kg\n')
        print(usuario.imc())