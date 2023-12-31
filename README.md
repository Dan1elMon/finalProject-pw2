# Final Project - dchuramo@unsa.edu.pe
**Author:** DANIEL WILSTON CHURA MONROY  
**Date:** 5, August 2023

## Información básica
| Asignatura                      | Programación web 2 - Teoría "C" - Labortorio "B" |
|---------------------------------|-------------------------------------------------|
| Semestre                        | III                                             |
| Alumno                          | Chura Monroy Daniel Wilston                     |
| Docentes                        |                                                 |
|                                 | Richard Smith Escobedo Quispe - rescobedoq@unsa.edu.pe |
|                                 | Anibal Sardon Paniagua - https://github.com/AnibalSardonP |

## Tools
- Django
- Github
- Git
- Vim
- Python
- JavaScript
- Html
- Css
- Vim
- Vim

### Tipo de Sistema
- Se trata de una aplicación web construida con el framework Django 4 y otras herramientas.

## Requisitos del sistema
- Esta aplicación web permite la venta de productos de moda como polos, jeans, zapatillas, gorras, y cualquier otro producto que se desee agregar.
- Esta página de ventas requiere el registro de usuarios.

## Modelo de datos
- **Product:** Almacena los datos de los productos como title (nombre), selling price (precio de venta), discounted price (precio con descuento), description (descripción del producto), composition (composición del producto), podapp (especificación del producto), categoria (categoría del producto), product image (imagen del producto).
- **Customer:** Almacena datos del usuario como user (por defecto), locality, city, mobile (teléfono), zipcode, state.
- **Cart:** Almacena los datos de usuario como user, product, quantity, total cost (costo total de los productos).
- **Payment:** Almacena estado de pago como user, amount (monto de compra), payment status (estado de pago), payment id (id de pago), paid (estado de pago realizado).
- **Order Placed:** Almacena datos del carrito de compra como user, customer (dirección), product (datos del producto), quantity, ordered date, status (estado de compra), payment (estado de pago).

## Diccionario de datos
- En la construcción de software y en el diccionario de datos sobre todo, se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

### Product model
| Attribute       | Type       | Null | Primary Key | Default | Description        |
|-----------------|------------|------|-------------|---------|--------------------|
| id              | Numeric    | No   | Yes         | None    | ID                 |
| title           | String     | No   | No          | None    | Title              |
| discounted_price | Float     | No   | No          | None    | Discounted price   |
| category        | String     | No   | No          | None    | Category           |
| product_image   | ImageField | Yes  | No          | NULL    | Product image      |

### Customer model
| Attribute       | Type          | Null | Primary Key | Default | Description        |
|-----------------|---------------|------|-------------|---------|--------------------|
| id              | Numeric       | No   | Yes         | None    | ID                 |
| user            | ForeignKey    | No   | No          | None    | User               |
| name            | String        | No   | No          | None    | Name               |
| locality        | String        | No   | No          | None    | Locality           |
| city            | String        | No   | No          | None    | City               |
| mobile          | IntegerField  | No   | No          | 0       | Phone number       |
| zipcode         | IntegerField  | No   | No          | 0       | Postal code        |
| state           | String        | No   | No          | None    | State              |

### Cart model
| Attribute       | Type                 | Null | Default | Description        |
|-----------------|----------------------|------|---------|--------------------|
| id              | Numeric              | No   | None    | ID                 |
| user            | ForeignKey           | No   | None    | User               |
| product         | ForeignKey           | No   | None    | Product            |
| quantity        | PositiveIntegerField | No   | 1       | Quantity           |
| total_cost      | FloatField           | No   | None    | Total cost         |

## Administración con Django

## CRUD - Core Business - Clientes finales
El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
1. El cliente inicia sesión.
2. El cliente selecciona la sección de productos que desea.
3. El cliente selecciona el grupo de laboratorio donde desea inscribirse.
4. El cliente selecciona los productos que desea.
5. El alumno puede ver su carrito de compras.
6. El alumno cierra sesión.


Usuario admin - qweqwe123123
Usuario DanielChura - qweqwe123123
## Operaciones asíncronas AJAX
Se utilizaron operaciones asíncronas para actualizar y crear direcciones para el usuario.

## Resultados
![Pagina inicio](img/img1.png)
Pagina inicio

![Registro Cliente](img/img2.png)
Registro Cliente

![Logeo del cliente](img/img3.png)
Logeo del cliente

![Registro de datos del cliente](img/img4.png)
Registro de datos del cliente

![Confirmacion de direccion](img/img5.png)
Confirmación de dirección

![Seleccion de productos](img/img6.png)
Selección de productos

![Vista previa y opciones de compra](img/img7.png)
Vista previa y opciones de compra

![Carrito de compras](img/img8.png)
Carrito de compras

## REFERENCIAS
- https://www.django-rest-framework.org/coreapi/
- https://github.com/Dan1elMon/finalProject-pw2
- https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/
- https://www.youtube.com/watch?v=38XWpyEK8IY
- https://www.youtube.com/playlist?list=PL5iMxK9f2ge6d9mkf3xqSBmkT4x2MsQRW
- https://www.youtube.com/watch?v=38XWpyEK8IY&t=2013s
