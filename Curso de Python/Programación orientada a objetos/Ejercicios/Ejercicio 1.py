'''
    Preguntas Conceptuales y Análisis

    * Sobre Encapsulamiento: ¿Por qué el atributo _saldo se escribe con doble guion bajo (_) al principio? ¿Qué intenta prevenir el programador al hacer esto?

    * Métodos "Getters": ¿Cuál es el propósito del método get_saldo()? Si ya tenemos el atributo __saldo, ¿por qué no lo leemos directamente desde fuera de la clase?

    * Lógica de Validación: En el método _init, ¿por qué se utiliza self.depositar(saldo_inicial) en lugar de asignar directamente self._saldo = saldo_inicial? ¿Qué ventaja nos da hacerlo de esa manera?

    * Predicción de Errores: Si intentas ejecutar el siguiente código, ¿qué mensaje se imprimirá en la pantalla y por qué?
        mi_cuenta_nueva = CuentaBancaria("Juan Pérez")
    mi_cuenta_nueva.retirar(100)

    * Análisis de Flujo: ¿Qué valor tendría el saldo final si se ejecutan estas tres operaciones en orden sobre una cuenta que empieza con $500?
        * depositar(200)
        * retirar(800)
        * retirar(700)
'''

print('se usa el doble guión bajo en el atributo __saldo para indicar que se convierta en privado, previniendo el acceso o modificación directa desde fuera creando un encapsulamiento')
print('el método get_saldo() sirve para proteger y controlar el acceso al atributo privado, por eso, no se debe leer directamente el atributo privado desde fuera de la clase')
print('usar self.depositar(saldo_inicial) en el constructor aplica automáticamente todas las validaciones del método, evita duplicar lógica y asegura que el objeto se inicializa correctamente y en un estado válido')
print('se imprime un mensaje de error porque el constructor espera que el saldo inicial sea un número, sin embargo, se le está pasando una cadena de texto')
print('el saldo final sería $0, suponiendo que la clase no permite retiros superiores al saldo disponible')

'''
    Ejercicios Prácticos de Código

    * Crear y Usar un Objeto:

    * Crea una instancia de CuentaBancaria para un titular llamado "Carlos Gómez" con un saldo inicial de $2,500.
    
    * Realiza un depósito de $500.

    * Intenta realizar un retiro de $3,500.

    * Realiza un retiro válido de $1,200.

    * Al final, llama al método mostrar_informacion() para ver el estado final de la cuenta.

    * Modificar la Clase (Desafío):

    * Añade un nuevo atributo "privado" a la clase llamado __numero_transacciones, que comenzará en 0.

    * Modifica los métodos depositar y retirar para que cada vez que se realice una operación exitosa, este contador se incremente en 1.

    * Modifica el método mostrar_informacion() para que también muestre el total de transacciones realizadas.
'''

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = 0
        self.__numero_transacciones = 0
        self.depositar(saldo_inicial)
    
    def depositar(self, monto):
        if monto <= 0:
            print("El depósito debe ser mayor que cero.")
            return
        self.__saldo += monto
        self.__numero_transacciones += 1

    def retirar(self, monto):
        if monto <= 0:
            print("El retiro debe ser mayor que cero.")
            return
        if monto > self.__saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return
        self.__saldo -= monto
        self.__numero_transacciones += 1

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo}")
        print(f"Total de transacciones: {self.__numero_transacciones}")

cuenta = CuentaBancaria("Carloz Gómez", 2500)
cuenta.depositar(500)
cuenta.retirar(3500)
cuenta.retirar(1200)
cuenta.mostrar_informacion()

'''
    Preguntas Conceptuales y de Análisis

    * Atributos Públicos vs. Privados: En la clase Producto, el nombre es un atributo público, pero __precio y __stock son privados. ¿Cuál crees que es la razón de esta diferencia de diseño?
 
    * Métodos "Setters": ¿Cuál es la función principal del método set_precio()? ¿Qué problema podría ocurrir si el precio se pudiera cambiar directamente sin este método?
 
    * Lógica Unificada: El método actualizar_stock() sirve tanto para añadir como para quitar unidades. ¿Cómo sabe el método si debe aumentar o disminuir el stock basándose en el número que recibe?
 
    * Predicción de Estado: Si creas un producto así: mi_producto = Producto("Lámpara", -20, 5), ¿cuál será el precio real del producto según el código y por qué?
 
    * Análisis de Flujo: Un producto tiene un stock inicial de 15. ¿Cuál será el stock final después de ejecutar estas dos operaciones en orden? Explica por qué.
        * actualizar_stock(-10)
        * actualizar_stock(-10)
'''

print('El nombre del producto es público porque es un dato que puede ser leído y modificado libremente sin afectar la integridad del objeto. Por el contrario, __precio y __stock son privados para proteger la información sensible y evitar modificaciones directas')
print('La función principal de set__precio es permitir modificar el precio del producto de forma controlada, si se pudiera cambiar el precio directamente, se le podría asignar valores inválidos, el setter previene esos problemas aplicando reglas antes de realizar la asignación')
print('El método suele recibir un parámetro numérico, si es positivo, aumenta el stock; si es negativo, lo disminuye')
print('El precio real será 0 o un valor por defecto, porque el código debería evitar precios negativos y corregirlos automáticamente')
print('El stock final es -5, cada llamada resta 10 unidades al stock, después de la segunda operación, el stock es negativo, ésto sucede porque no hay  una validación')

'''
    Ejercicios Prácticos de Código

    * Crear y Gestionar un Producto:

    * Crea una instancia de la clase Producto para un "Teclado Mecánico", con un precio de $95 y un stock inicial de 30 unidades.

    * Simula la venta de 5 teclados.

    * El proveedor envía 10 teclados más. Actualiza el stock para reflejar su llegada.

    * Debido a una oferta, actualiza el precio del teclado a $89.99.

    * Muestra el detalle final del producto.

    * Modificar la Clase (Desafío):

    * Añade un método llamado vender(cantidad). Este método debe ser una forma más intuitiva de disminuir el stock. Internamente, deberá llamar a actualizar_stock() con el número correcto (es decir, un número negativo).

    * El método vender debe imprimir un mensaje específico como "Venta realizada: Se vendieron X unidades." si la venta es exitosa. Si no hay stock, debe indicarlo.
'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio if precio > 0 else 0
        self.__stock = stock if stock >= 0 else 0

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    def get_stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad):
        if self.__stock + cantidad < 0:
            print("No hay suficientes unidades en stock para realizar la operación.")
            return False
        self.__stock += cantidad
        return True

    def mostrar_detalle(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Stock disponible: {self.__stock}")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            return
        if self.actualizar_stock(-cantidad):
            print(f"Venta realizada: Se vendieron {cantidad} unidades.")
        else:
            print("Venta no realizada: No hay suficiente stock.")

teclado = Producto("Teclado Mecánico", 95, 30)
teclado.vender(5)
teclado.actualizar_stock(10)
teclado.set_precio(89.99)
teclado.mostrar_detalle()