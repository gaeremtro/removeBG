# Guía de Pruebas Manuales - RemoveBG

## 1. Verificar que el servicio está corriendo
Asegúrate de que Docker está levantado:
```powershell
docker-compose ps
```
Debe decir `Up` en el estado del servicio `remove-bg`.

## 2. Preparar tu imagen
Copia la foto que quieres probar (ej. `mi_foto.jpg`) en la carpeta del proyecto:
`C:\Users\gabri\Documents\SOM\RemoveBG`

## 3. Ejecutar la prueba
Abre una terminal en esa carpeta y ejecuta este comando (cambia `mi_foto.jpg` por el nombre de tu archivo):

```powershell
curl.exe -X POST -F "file=@mi_foto.jpg" http://localhost:8000/remove -o resultado.png
```

> **IMPORTANTE**: En Windows PowerShell debes escribir `curl.exe` y no solo `curl`, ya que `curl` es un alias de otro comando.

## 4. Ver el resultado
Revisa si se creó el archivo `resultado.png`. ¡Debería ser tu foto sin fondo!
