<div align="justify">
  
# SEMANA_9_RESTAURANTE

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - POO y Principios SOLID

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto es una aplicación desarrollada en Python que permite gestionar productos y usuarios de un restaurante mediante una interfaz de consola, facilitando el registro, consulta, actualización y eliminación de información de manera organizada y sencilla, además, el sistema mantiene una estructura modular que separa las responsabilidades de cada componente y utiliza diferentes estructuras de datos de **Python** según las necesidades de cada proceso, logrando así un código más claro, eficiente y fácil de mantener.

---

## Estructura del Proyecto

Para mantener una organización adecuada, el sistema se encuentra dividido en módulos que agrupan funciones relacionadas entre sí, permitiendo separar los modelos de datos de la lógica de negocio y de la interacción con el usuario, de esta manera, la carpeta modelos contiene las clases que representan los productos y usuarios, mientras que la carpeta servicios administra las operaciones del restaurante y finalmente, el archivo main.py funciona como punto de entrada y coordina el funcionamiento general de la aplicación.

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Responsabilidad de las Clases y Módulos

Cada componente del proyecto cumple una función específica para evitar la mezcla de responsabilidades y facilitar la comprensión del código, por lo tanto, la clase **Producto** representa la información general de cada producto mediante datos como código, nombre, categoría y precio, mientras que la clase **Usuario** administra la información de las personas registradas como identificación, nombre y correo, por otra parte, la clase **Restaurante** se encarga de gestionar las colecciones y realizar operaciones como búsqueda, inserción, actualización, eliminación y filtrado, mientras que **main.py** controla el menú y la interacción con el usuario.

---

## Uso de las Estructuras de Datos

El sistema utiliza diferentes estructuras de datos de **Python** de acuerdo con la función que debe realizar cada una, de modo que las listas permiten almacenar y modificar
las colecciones de productos y usuarios durante la ejecución, mientras que la tupla se utiliza para conservar las opciones del meúu de forma inmutable, evitando cambios accidentales, asimismo, el diccionario relaciona cada opción seleccionada con la acción que debe ejecutarse y finalmente, el conjunto permite obtener las categorías de productos sin repetir valores, facilitando así un manejo más organizado de la información.

---

## Funcionamiento del Sistema

El funcionamiento comienza desde el archivo **main.py**, donde se presenta un menú interactivo que permite al usuario seleccionar la operación que desea realizar, posteriormente, la opción seleccionada es relacionada mediante el diccionario mapa acciones con la función correspondiente y, a partir de ello, la clase **Restaurante** ejecuta la operación solicitada sobre las colecciones internas, manteniendo separada la interacción del usuario de la lógica de negocio y evitando el acceso directo a los datos internos, lo que permite conservar una estructura más segura y ordenada.

---

## Reflexión Final

La organización modular y el uso adecuado de las estructuras de datos permiten construir un sistema más claro, eficiente y fácil de mantener, ya que cada componente cumple una responsabilidad determinada y cada estructura se utiliza según la necesidad que debe resolver, de esta manera, las listas facilitan la gestión de información dinámica, las tuplas protegen datos que no deben modificarse, los diccionarios simplifican la selección de acciones y los conjuntos eliminan valores repetidos, fortaleciendo así los conocimientos de **Programación Orientada a Objetos** y proporcionando una base adecuada para ampliar el sistema en futuras versiones.

<div>
