# Coder_Playground

### URL DE LA PAGINA:
http://127.0.0.1:8000

### OBJETIVO
Crear una página que nuclée varios comercios de venta de celulares. En ella los comercios pueden indicar cuáles son las marcas con las que trabajan y los productos con los que cuentan. Los usuarios en un futuro pueden acceder y ver los productos, marcas, locales.

### FUNCIONAMIENTO
Los comercios pueden ingresar a la página, ver qué marcas tienen, ver los productos y los comercios que forman parte de estar red.

### FUNCIONALIDADES

#### MALLS
- Malls:
Se puede observar el nombre del local, la ciudad donde está, la dirección, el número de local y los días de atención.
- Add a new mall:
Esto permite generar un nuevo comercio, donde se van a indicar el nombre del mismo, la localidad, la dirección, el número de local y los horarios de atención.
- Search:
Se puede buscar un local y va a figurar la información del mismo.
Además, en la página, se puede elegir volver a la sección “Malls”


#### PRODUCTS
- Products:
En la opción de Productos se puede observar toda la información del producto y en la columna final figura si el producto tiene stock disponible, quedan pocas unidades o está agotado. Esto se generó con un if en el html de productos. El color de la palabra también sirve de indicador del nivel de stock disponible

- Add a new product:
Esto permite crear un nuevo producto, donde se va a indicar el nombre del producto, el precio, en un desplegable seleccionar la marca y el stock disponible.

#### SALESMAN
- Salesman:
Se puede observar el nombre y apellido del vendedor, así como su e-mail, fecha de nacimiento y el local donde trabaja.
- Add a new salesman:
Esto permite añadir un nuevo vendedor, donde se va a indicar el número del local en el cual trabaja, el nombre, apellido, email y fecha de nacimiento.

### NOMBRES
- En cada una de las páginas se modificó el nombre que figura en la pestaña y se modificó el ícono de la pestaña por el de un celular

### CONSIGNAS TRABAJO
- Se generó un template base. El resto de los templates heradaron la información de dicho template
- Se crearon 3 clases: Vendedores, Productos, Locales
- Se creó un formulario para cada una de las clases
- Se generó un formulario para buscar en la base de Locales
- Se trabajó todo generando el commit en GitHub
