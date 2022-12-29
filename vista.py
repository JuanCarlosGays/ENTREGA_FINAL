from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import modelo

#******************************************************
#***************VISTA**********************************
#******************************************************
class Panel():

  # TREE *****************************************

  #def vista_principal(root):
    def __init__(self,window):

      self.root=window          
      self.root.title("GIMNASIO LOS FANTASTICOS-MVC-POO-ORM")
    
      self.alta_dni = StringVar()
      self.alta_apellido = StringVar()
      self.buen_dia = StringVar()

      self.objeto=modelo.Abmc()
      
      """:excepciones (try-except): intenta crear base o tabla si ya no está creada"""
      
      try:
        self.objeto.crear_dbase()
      except:
        print("base creada")

      try:
        self.objeto.crear_tabla()
      except:
        print("tabla creada")

      self.e1 = Entry(self.root, textvariable = self.alta_apellido)
      self.e2 = Entry(self.root, textvariable = self.alta_dni)
      self.e3 = Entry(self.root, textvariable = self.buen_dia)
      self.e1.grid(row=2, column=0)
      self.e2.grid(row=3, column=0)
      self.e3.grid(row=2, column=1)
      
      
      self.tree= ttk.Treeview(self.root, columns =("size", "modified"))
      self.tree["columns"]=("dni","apellido","venc cuota", "venc médico")
      
      self.tree.column("apellido", width=100)
      self.tree.column("dni", width=90)
      self.tree.column("venc cuota", width=90)
      self.tree.column("venc médico", width=90)
      
      self.tree.heading("apellido", text="Apellido")
      self.tree.heading("dni", text="dni")
      self.tree.heading("venc cuota", text="Venc cuota")
      self.tree.heading("venc médico", text="Venc médico")
        
      def select_elemento(a):
          self.objeto.seleccionar_elemento(self.tree, self.e1, self.e2)
      
      self.tree.bind("<ButtonRelease 1>", select_elemento)
      
      self.apellido = Label(self.root, text="apellido")
      self.apellido.grid(row=2, column=0,sticky='w')
      self.dni = Label(self.root, text="dni")
      self.dni.grid(row=3, column=0, sticky='w')
      self.venc_cuota = Label(self.root, text="venc cuota")
      self.venc_cuota.grid(row=4, column=0)
      self.venc_medico = Label(self.root, text="venc médico")
      self.venc_medico.grid(row=4, column=1)
      self.bienvenido_dni = Label(self.root, text="Bienvenido(DNI)")
      self.bienvenido_dni.grid(row=0, column=1)
        
      
      # BOTONES##############################################
      
      
      #CALENDARIOS---------------------------------
      self.cal1 = Calendar(self.root,font="Arial 8", selectmode='day')
      self.cal1.grid(row=12,column=0)
      
      self.cal2 = Calendar(self.root,font="Arial 8", selectmode='day')
      self.cal2.grid(row=12,column=1)
      
      
      # BIENVENIDO***********************
      self.bienvenido_record = Button(self.root,text="bienvenido!", command=lambda:self.objeto.check_socio_regex(self.buen_dia))
      self.bienvenido_record.grid(row=3, column=1)
      #**********************************
      
      # AGREGAR LINEA********************
      self.agregar_record = Button(self.root,text="agrega", command=lambda:self.objeto.agregar_linea_regex(self.alta_apellido,self.alta_dni,self.cal1, self.cal2, self.tree))
      self.agregar_record.grid(row=22, column=0)
      
      #**********************************
      
      # BORRAR LINEA*********************
      self.borrar_record = Button(self.root,text="borra", command=lambda:self.objeto.borrar_linea(self.tree))
      self.borrar_record.grid(row=23, column=0)
      #**********************************
      
      # MODIFICAR LINEA*******************
      self.modificar_record = Button(self.root,text="modifica", command=lambda:self.objeto.modificar_elemento(self.alta_apellido,self.alta_dni,self.cal1, self.cal2, self.tree))
      self.modificar_record.grid(row=22, column=1)
      #**********************************
      
      # LISTAR***************************
      self.listar_dic = Button(self.root,text="listar", command=lambda:self.objeto.imprime_listados())
      self.listar_dic.grid(row=23, column=1)
      #**********************************
      
      self.tree.grid()
    
