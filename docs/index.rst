.. Gym_Fantasticos documentation master file, created by
   sphinx-quickstart on Mon May 30 16:44:46 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Gym Fantasticos's documentation!
===========================================

Este programa cumple las siguientes funciones para un gimnasio, grabando la informacion en base *Sqlite3*: 

*alta:* para dar de alta un nuevo socio con apellido, dni, fecha de vencimiento cuota y fecha de vencimiento medico

*borrar:* para borrar un socio de la base de datos

*modificar:* para modificar el vencimiento de cuota o medico en socios que tuviesen restringida la entrada por estos motivos

*listar:* lista los socios *activos* (aquellos con cuota y medico al dia) y los *pasivos* (aquellos con alguno o ambos parametros antes mencionados vencidos)

y finalmente:

*bienvenidos:* se ingresa DNI de socio que viene a ejercitar. Si esta en base de datos y no tiene vencidos da mensaje de bienvenida, sino alerta sobre vencimiento para modificar. Si no estuviese en base de datos alerta como DNI inexistente.


.. note::

   **REGEX:** Es obligatorio cargar el apellido con Mayuscula en la primera y luego minusculas, y el DNI debe tener 7 u 8 digitos.


.. toctree::
   :maxdepth: 4
   :caption: Contenido:

   controlador
   vista
   modelo
   


