# Slash
Slash es un interprete para java , Slash mejora y hace amigable la sintaxis de java haciéndola entendible y fácil de utilizar


Ejemplo de codigo en Slash
Este es un Hola mundo en Slash 


class hello:
  @main(String args[]):
    print('Hola mundo')
  end
end


El interprete de slash traduce el codigo anterior a codigo Java.
La siguiente salida seria la siguiente

class hello {
  public static void main(String args[]){
    System.out.print("Hola mundo");
  }
}
