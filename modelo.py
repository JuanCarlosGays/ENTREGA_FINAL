import re
import sqlite3
from tkinter import *
from datetime import date
import pandas as pd
from peewee import *

# ********************************************************
#                  MODELO
# ********************************************************
db = SqliteDatabase("elgimnasio.db")

class BaseModel(Model):
    class Meta:
        database = db

class Altas(BaseModel):
    dni = CharField(unique =True)
    apellido = CharField()
    venc_cuota = DateField()
    venc_medico = DateField()

db.connect()
db.create_tables([Altas])

class Abmc():
    #def__init__(self,): pass
    
      
    borrar = 0
    contador = 0
    activos = {}
    pasivos = {}
    ingreso = {}
    tree = {}
    x = int()
    con = int()
    

# =============================================================================
#     """
#     ACTUALIZAR TREEVIEW
#     :param mitreview: selecciona item de la tabla y actualiza el contenido
#     """
# =============================================================================

    def actualizar_treeview(self,mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
         
        for fila in Altas.select():
           
            mitreview.insert("", "end", values=(
                fila.dni, fila.apellido, fila.venc_cuota, fila.venc_medico))
    
# =============================================================================
#     """CODIGO REGEX"""
#     """:param  DNIReg : '\d{7,8}$' solo numéricos
#     :param  APELReg : '[A-Z][a-z,á,é,í,ó,ú]' inicial mayúscula resto minúsculas
#     """
# =============================================================================
    
    DNIReg = '\d{7,8}$'
    APELReg = '[A-Z][a-z,á,é,í,ó,ú]'


    def useRegexDni(self,input):
        pattern = re.compile(self.DNIReg)
        return pattern.match(input)


    def useRegexApellido(self,input):
        pattern = re.compile(self.APELReg)
        return pattern.match(input)
  

# =============================================================================
#     """ AGREGAR LINEA"""
#     """:param alta_apellido: ingresa apellido"""
#     """:param alta_dni: ingresa DNI"""
#     """:param cal1: selecciona la fecha de venc cuota"""
#     """:param cal2: selecciona la fecha de venc médico"""
#     """:param tree: actualiza treeview"""
# =============================================================================
    
    def agregar_linea_regex(self,alta_apellido,alta_dni,cal1, cal2, tree):
        while self.useRegexDni(alta_dni.get()) is None or self.useRegexApellido(alta_apellido.get()) is None:
            if self.useRegexDni(alta_dni.get()) is None:
                print("DNI mal cargado, intente nuevamente")
            if self.useRegexApellido(alta_apellido.get()) is None:
                print("Apellido mal cargado, intente nuevamente")
            break
        else:
            self.agregar_linea(alta_apellido,alta_dni,cal1, cal2, tree)


    def agregar_linea(self,alta_apellido,alta_dni,cal1, cal2, tree):
        
        altas = Altas()
        altas.apellido = alta_apellido.get()
        altas.dni = alta_dni.get()
        altas.venc_cuota = cal1.selection_get()
        altas.venc_medico = cal2.selection_get()
        altas.save()

        self.actualizar_treeview(tree)
        return

# =============================================================================
#     """
#     CHECK SOCIOS
#     
#     :param buen_dia: ingresa DNI para entrar al gimnasio, verifica si el socio está en base, y si tiene cuota y médico al dia
#     """
# =============================================================================
    def check_socio_regex(self,buen_dia):
    
        while self.useRegexDni(buen_dia.get()) is None:
            print("DNI mal cargado, intente nuevamente")
            break
        else:
            self.check_socio(buen_dia)
    


    def check_socio(self, buen_dia):
        
        ingreso = Altas.select().where(Altas.dni == buen_dia.get())
        
        y=0

        for x in ingreso:

            
            if pd.Timestamp(x.venc_cuota) >= date.today() and pd.Timestamp(x.venc_medico) >= date.today():
                print(x.apellido+" bienvenido!")
                
            else:
                if pd.Timestamp(x.venc_cuota) < date.today():
                    print(x.apellido+" actualizar cuota")
                    
                if pd.Timestamp(x.venc_medico) < date.today():
                    print(x.apellido+" actualizar apto médico")
            y=1
              
        if y == 0:
            
            print("DNI no presente en base de datos")
       
        return


    def seleccionar_elemento(self,treview,e1,e2):
        curItem = treview.focus()
        v = treview.item(curItem, 'values')
        print(v[0])
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e1.insert(0, v[1])
        e2.insert(0, v[0])

 
# =============================================================================
#     **BORRAR LINEA**
#     
#     :param tree: borra la linea seleccionada en treeview
# =============================================================================
   
    
    def borrar_linea(self,tree):
        curItem = tree.focus()
        v = tree.item(curItem, 'values')
        print(v)
        borrar=Altas.get(Altas.dni==v[0])
        borrar.delete_instance()
        self.actualizar_treeview(tree)
             
        return

# =============================================================================
#     """
#     MODIFICAR CUOTA o MEDICO
#     
#     :param tree: selecciona item para modificar fecha de vencimiento médico o cuota
#     
#     :param cal1: vencimiento médico para modificar - de ser preciso
#     
#     :param cal2: vencimiento cuota a modificar - de ser preciso
#     """
# =============================================================================

    # MODIFICAR ELEMENTO **************

    def modificar_elemento(self,alta_apellido,alta_dni,cal1, cal2, tree):
        self.borrar_linea(tree)
        self.agregar_linea_regex(alta_apellido,alta_dni,cal1, cal2, tree)

# =============================================================================
#     """
#     **LISTAR ACTIVOS vs PASIVOS**
#     
#     :param activos: lista de miembros que tienen cuota y médico al día
#     
#     :param pasivos: lista de miembros que tienen cuota y/o médico vencidos
#     """
# =============================================================================



    def imprime_listados(self):
  
        print()
        print("ACTIVOS--------------------------")
        activos = Altas.select().where((Altas.venc_cuota >=date.today())&(Altas.venc_medico >=date.today()))
       
        for x in activos:
            print(x.dni,"---",x.apellido)
        
        print()
        print("PASIVOS--------------------------")
        pasivos = Altas.select().where((Altas.venc_cuota <date.today())|(Altas.venc_medico <date.today()))
               
        for x in pasivos:
            print(x.dni,"---",x.apellido)

        return

    # CALENDARIOS***********************************
    # CAL CUOTA***********************

    def print_sel1(self,cal1):
        self.print(cal1.selection_get())

    # CAL MEDICO***********************

    def print_sel2(self,cal2):
        self.print(cal2.selection_get())