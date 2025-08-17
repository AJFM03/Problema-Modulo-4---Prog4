# Problema-Modulo-4---Prog4

🎯 Objetivo
Modificar la aplicación de línea de comandos previamente desarrollada para reemplazar el uso de bases de datos relacionales por una base de datos no relacional, utilizando MongoDB y el cliente oficial pymongo.

📝 Contexto
El propósito de esta tarea es que los estudiantes comprendan las diferencias entre bases de datos relacionales y no relacionales. Para ello, transformarán su aplicación de biblioteca personal para trabajar con documentos JSON en MongoDB en lugar de registros en tablas relacionales.

Cada libro será representado como un documento en una colección de MongoDB.

📌 Requisitos funcionales
La aplicación debe seguir ofreciendo todas las funcionalidades mínimas del sistema original:

Agregar nuevo libro
➤ Añadir libros con título, autor, género y estado de lectura.

Actualizar información de un libro
➤ Permitir modificar cualquier campo del libro, incluyendo su estado de lectura.

Eliminar libro existente
➤ Eliminar un documento de la colección.

Ver listado de libros
➤ Mostrar todos los libros registrados en MongoDB.

Buscar libros
➤ Permitir búsquedas por título, autor o género utilizando filtros.

Salir
➤ Terminar el programa correctamente.

🔄 Cambios y objetivos clave
Reemplazar el uso de bases de datos relacionales con MongoDB.

Almacenar cada libro como un documento dentro de una colección en MongoDB.

Utilizar pymongo para interactuar con la base de datos.

Adaptar todas las operaciones a una estructura basada en documentos JSON.

Configurar la conexión a MongoDB, ya sea local o remota (por ejemplo, MongoDB Atlas).

Documentar claramente cómo instalar y configurar MongoDB en el entorno de desarrollo.

💡 Consideraciones técnicas
Utilizar pymongo para conexión y manipulación de datos.

Incluir un archivo requirements.txt con las dependencias necesarias.

El README.md debe incluir:

Instrucciones para instalar MongoDB (local o Atlas)

Configuración de la cadena de conexión

Comando para ejecutar la aplicación

Ejemplos de entradas válidas y estructura esperada del documento

Incluir validaciones para errores comunes como:

Error de conexión

Documentos mal estructurados

Búsquedas sin resultados
