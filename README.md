# Slash
Slash es un interprete para java , Slash mejora y hace amigable la sintaxis de java haciéndola entendible y fácil de utilizar


Ejemplo de codigo en Slash
Este es un Hola mundo en Slash 

<br/>
class hello:<br/>
  @main(String args[]):<br/>
    print('Hola mundo')<br/>
  end<br/>
end

<br/>
<br/>

El interprete de slash traduce el codigo anterior a codigo Java.
La siguiente salida seria la siguiente

<br/>

class hello {<br/>
  public static void main(String args[]){<br/>
    System.out.print("Hola mundo");<br/>
  }<br/>
}
