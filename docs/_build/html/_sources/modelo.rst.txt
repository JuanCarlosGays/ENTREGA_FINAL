modelo module
=============

**AGREGAR LINEA**

def agregar_linea(self,alta_apellido,alta_dni,cal1, cal2, tree)

	:alta_apellido: ingresa apellido
	:alta_dni: ingresa DNI
	:cal1: selecciona la fecha de venc cuota
	:cal2: selecciona la fecha de venc medico
	:tree: actualiza treeview

**BORRAR LINEA**

def borrar_linea(self,tree):
    
	:tree: borra la linea seleccionada en treeview

**MODIFICAR ELEMENTO (CUOTA Y/O MEDICO)**

def modificar_elemento(self,alta_apellido,alta_dni,cal1, cal2, tree):
    
	self.borrar_linea(tree)
    
	self.agregar_linea_regex(alta_apellido,alta_dni,cal1, cal2, tree)  
  
	:tree: selecciona item para modificar fecha de vencimiento medico o cuota
	:cal1: vencimiento medico para modificar - de ser preciso
	:cal2: vencimiento cuota a modificar - de ser preciso

**CHECK SOCIOS**

def check_socio_regex(self,buen_dia):

	:buen_dia: ingresa DNI para entrar al gimnasio, verifica si el socio esta en base, y si tiene cuota y medico al dia

**LISTAR ACTIVOS vs PASIVOS**

def imprime_listados(self):

	:activos: lista de miembros que tienen cuota y medico al dia
	:pasivos: lista de miembros que tienen cuota y/o medico vencidos
  
.. automodule:: modelo
   :members:
   :undoc-members:
   :show-inheritance:

