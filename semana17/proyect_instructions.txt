# Recomendaciones

1. Investigue más sobre los elementos de `PySimpleGUI` en [la documentación oficial.](https://www.pysimplegui.org/en/latest/#elements)
2. Lea todos los requerimientos y detalles técnicos cuidadosamente.
3. Divida todos los requerimientos en tareas más pequeñas (dividir para conquistar).
4. Haga notas de aquellos requerimientos que no sepa cómo desarrollar con exactitud.
5. Divida la lógica del programa en funciones pequeñas y módulos.
6. Escriba código limpio. Use identificadores específicos y fáciles de entender.
7. Pregunte cualquier duda que tenga.

# Requerimientos

Investigue sobre la biblioteca [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) y cree un programa **con interfaz gráfica** que permita la gestión de finanzas personales. Este debe mostrar:

- Una tabla de movimientos (gastos e ingresos).
- Un botón para agregar una categoría de movimiento.
    - Este botón debe abrir otra ventana para agregar esa categoría.
    - Por ejemplo: Comida, Familia, Carro, etc.
- Un botón para agregar un gasto.
    - Este botón debe abrir otra ventana para agregar ese gasto.
    - Los gastos deben tener un titulo, un monto y una categoría.
- Un botón para agregar un ingreso.
    - Este botón debe abrir otra ventana para agregar esa ingreso.
    - Los ingresos deben tener un titulo, un monto y una categoría.

Así mismo:

- Si yo intento agregar un ingreso o un gasto, pero no hay  ninguna categoría agregada previamente, debe mostrar un error que diga “Por favor ingrese una categoría antes”.
- Cada vez que haga cambios, se debe exportar la data automáticamente en archivos.
- Cada vez que yo abra el programa, debe importar la data automáticamente (si existe).
- Toda la lógica debe ir separada en módulos y funciones.

# Proceso de descomposición

1. Hacer mockups de cada ventana.
    1. Investigar los elementos necesarios para cada ventana.
2. Diseñar como se va a guardar la data.
    1. Qué estructura tendrán a nivel de memoria.
3. Dividir funcionamientos en tareas más pequeñas.
    1. Partes “unitarias” que se puedan probar individualmente.
4. Empezar a desarrollar paso a paso.
    1. Que cada cosa funcione antes de seguir con la siguiente.
    2. No saltar a otro paso sin tener el primero listo.