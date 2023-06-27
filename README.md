# APICIET
Primera Api que hago y que estará dedicada a la app de CIET </br>
Van a haber muchos errores, pero de ellos se aprende y se mejora

##  Empezando 
A continuación, encontraremos las instrucciones para instalar el proyecto en nuestro equipo local o servidor.

### Prerrequisitos
Antes de instalar el proyecto tenemos que asegurarnos que en nuestro equipo este instalado los siguientes, estos programas o paquetes son necesarios para controlar las versiones:
- Instalar python https://www.python.org/downloads/

### Instalación
En la terminal, no importa donde estemos, lanzamos el siguiente comando: 
> python -m pip install fastapi

Una vez instalado, lanzaremos el siguiente comando: 
> pip install uvicorn

Para que funcione en el navegador, iremos en la terminal hasta la carpeta de nuestro proyecto y lanzaremos el comando:
> uvicorn index:app --reload
Tendremos en cuenta que index es donde se inicia el proyecto y app es el nombre de la variable donde instanciamos FastApi. 