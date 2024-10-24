# User API Documentation

## `get_all_users_router`

Consulta todos los usuarios de forma asíncrona.

**Flujo:**
1. Llama a `get_all_users_router()`.
2. `get_all_users_service()` procesa la solicitud.
3. `UserMethods.fetch_all_users()` ejecuta la consulta.

**Returns:** 
Lista de usuarios de la base de datos.

## Response Codes

- **200**: Operación exitosa.
- **500**: Error en la consulta.
