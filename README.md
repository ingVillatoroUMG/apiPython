# Lista Simple API
Esta es una API simple construida con Flask que implementa una lista simple enlazada. Permite cargar datos desde un archivo CSV, agregar registros manualmente y listar los registros en la lista.

## Endpoints
### /cargar_csv (GET)
Este endpoint carga datos desde un archivo CSV (estudiante.csv) y los agrega a la lista. Retorna la lista completa después de la carga.

### /agregar_registro (POST)
Permite agregar un registro manualmente a la lista. Se espera un cuerpo JSON con el siguiente formato:

```
{
    "id": "identificacion_del_registro"
}
```

### /listar (GET)
Este endpoint lista todos los registros en la lista.


## Postman Collection
Para validar la funcionalidad de la API, puede abrir el archivo HojaDeTrabajo.postman_collection.json en Postman. Esta colección contiene solicitudes predefinidas para probar los endpoints de la API.