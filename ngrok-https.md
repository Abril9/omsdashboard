Ngrok para exponer peticiones https con Django 


1. Instalar ngrok

	1.1. Crearse una  cuenta en https://ngrok.com/
	Esto generará un token de autentificación (authtoken)

	1.2. Dentro de la vps instalar ngrok usando snap

2. Usar el token para vincularme
Correr el comando de configuracion usando el authtoken:

ngrok config add-authtoken 2NQdT1dUWBiKJLMZECpbyL8mJ8z_63CXe5Q4qkasMtZCViDGv

##3. Iniciar el servicio ngrok
Indicando el puerto y el ip correctos, correr el comando:

ngrok http 186.65.87.251:8000


##4. Modificar el settings.py del proyecto
Agregar el dominio que ngrok generó a los ALLOWED_HOSTS de Django y reiniciar volver a levantar el servicio con gunicorn.

__________________________________________________________________________________

    • Aplicar configuraciones a ngrok

sudo ngrok service install –config=/home/julio/snap/ngrok/89/.config/ngrok/ngrok.yml

    • NO HUB
Para que el servicio de ngrok quede corriendo en el fondo correr:

nohup ngrok http 186.65.87.251:8000
