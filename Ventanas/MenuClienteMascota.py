# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:06:21 2015

@author: Win7Ultimate
"""

import wx

def create(parent):
    return MenuClienteMascota(parent)

[wxID_MENUCLIENTEMASCOTA, wxID_MENUCLIENTEMASCOTABUTTON1, 
 wxID_MENUCLIENTEMASCOTABUTTON2, wxID_MENUCLIENTEMASCOTACOMBOBOX1, 
 wxID_MENUCLIENTEMASCOTANOTEBOOK1, wxID_MENUCLIENTEMASCOTAPANEL1, 
 wxID_MENUCLIENTEMASCOTAPANEL2, wxID_MENUCLIENTEMASCOTAPANEL3, 
 wxID_MENUCLIENTEMASCOTASEARCHCTRL1, wxID_MENUCLIENTEMASCOTASTATICBOX1, 
 wxID_MENUCLIENTEMASCOTASTATICBOX2, wxID_MENUCLIENTEMASCOTASTATICBOX3, 
 wxID_MENUCLIENTEMASCOTASTATICBOX4, wxID_MENUCLIENTEMASCOTASTATICTEXT1, 
 wxID_MENUCLIENTEMASCOTASTATICTEXT10, wxID_MENUCLIENTEMASCOTASTATICTEXT2, 
 wxID_MENUCLIENTEMASCOTASTATICTEXT3, wxID_MENUCLIENTEMASCOTASTATICTEXT4, 
 wxID_MENUCLIENTEMASCOTASTATICTEXT5, wxID_MENUCLIENTEMASCOTASTATICTEXT6, 
 wxID_MENUCLIENTEMASCOTASTATICTEXT7, wxID_MENUCLIENTEMASCOTASTATICTEXT8, 
 wxID_MENUCLIENTEMASCOTASTATICTEXT9, wxID_MENUCLIENTEMASCOTATEXTCTRL1, 
 wxID_MENUCLIENTEMASCOTATEXTCTRL2, wxID_MENUCLIENTEMASCOTATEXTCTRL3, 
 wxID_MENUCLIENTEMASCOTATEXTCTRL4, wxID_MENUCLIENTEMASCOTATEXTCTRL5, 
 wxID_MENUCLIENTEMASCOTATEXTCTRL6, wxID_MENUCLIENTEMASCOTATEXTCTRL8, 
 wxID_MENUCLIENTEMASCOTATEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(31)]

class MenuClienteMascota(wx.Dialog):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False, text='Altas')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text='Modificar')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MENUCLIENTEMASCOTA,
              name=u'MenuClienteMascota', parent=prnt, pos=wx.Point(419, 205),
              size=wx.Size(713, 485), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Cliente')
        self.SetClientSize(wx.Size(697, 447))

        self.notebook1 = wx.Notebook(id=wxID_MENUCLIENTEMASCOTANOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(697, 447), style=0)
        self.notebook1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.panel1 = wx.Panel(id=wxID_MENUCLIENTEMASCOTAPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 421),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_MENUCLIENTEMASCOTAPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 421),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOX1,
              label=u'Alta Cliente', name='boxAltaC', parent=self.panel1,
              pos=wx.Point(6, 8), size=wx.Size(306, 328), style=0)
        self.staticBox1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.staticText1 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT1,
              label=u'Documento', name='labelDoc', parent=self.panel1,
              pos=wx.Point(30, 50), size=wx.Size(55, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT2,
              label=u'Nombre', name='labelNombre', parent=self.panel1,
              pos=wx.Point(30, 100), size=wx.Size(38, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT3,
              label=u'Apellido', name='labelApe', parent=self.panel1,
              pos=wx.Point(30, 150), size=wx.Size(38, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT4,
              label=u'Direccion', name='labelDirec', parent=self.panel1,
              pos=wx.Point(30, 200), size=wx.Size(44, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT5,
              label=u'Telefono', name='labelTel', parent=self.panel1,
              pos=wx.Point(30, 250), size=wx.Size(43, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL1,
              name='textDoc', parent=self.panel1, pos=wx.Point(88, 100),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL2,
              name='textNombre', parent=self.panel1, pos=wx.Point(88, 50),
              size=wx.Size(104, 21), style=0, value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL3,
              name='textApe', parent=self.panel1, pos=wx.Point(88, 150),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL4,
              name='textDirec', parent=self.panel1, pos=wx.Point(88, 200),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL5,
              name='textTel', parent=self.panel1, pos=wx.Point(88, 250),
              size=wx.Size(136, 21), style=0, value=u'')

        self.staticBox2 = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOX2,
              label=u'Alta Mascota', name='boxAltaM', parent=self.panel1,
              pos=wx.Point(352, 8), size=wx.Size(328, 328), style=0)
        self.staticBox2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.staticText6 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT6,
              label=u'Nombre', name='labelNombre', parent=self.panel1,
              pos=wx.Point(368, 50), size=wx.Size(38, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT7,
              label=u'Raza', name='labelRaza', parent=self.panel1,
              pos=wx.Point(368, 100), size=wx.Size(25, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT8,
              label=u'Peso', name='labelPeso', parent=self.panel1,
              pos=wx.Point(368, 150), size=wx.Size(24, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT9,
              label=u'Codigo', name='labelCodigo', parent=self.panel1,
              pos=wx.Point(368, 200), size=wx.Size(34, 13), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL6,
              name='textNombre', parent=self.panel1, pos=wx.Point(432, 50),
              size=wx.Size(160, 21), style=0, value=u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL8,
              name='textPeso', parent=self.panel1, pos=wx.Point(432, 150),
              size=wx.Size(56, 21), style=0, value=u'')

        self.textCtrl9 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL9,
              name='textCodigo', parent=self.panel1, pos=wx.Point(432, 200),
              size=wx.Size(128, 21), style=0, value=u'')
        self.textCtrl9.SetEditable(False)

        self.button1 = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTON1,
              label=u'Guardar', name='botonGuardar', parent=self.panel1,
              pos=wx.Point(568, 288), size=wx.Size(99, 31), style=0)

        self.button2 = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTON2,
              label=u'Atras', name='botonAtras', parent=self.panel1,
              pos=wx.Point(8, 384), size=wx.Size(88, 31), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_MENUCLIENTEMASCOTABUTTON2)

        self.comboBox1 = wx.ComboBox(choices=["Pointer", "Bulldog",
              "Bull Terrie", "Boxer", "Collie", "Dalmata", "Dogo", "Doberman",
              "Fox Terrier", "Golden", "Pastor Aleman", "Rottweiler", "Setter",
              "Pit bull","Pichichen" ], id=wxID_MENUCLIENTEMASCOTACOMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(432, 104),
              size=wx.Size(160, 21), style=0, value=u'Seleccione la raza..')
        self.comboBox1.SetLabel(u'Seleccione la raza..')
        self.comboBox1.Bind(wx.EVT_COMBOBOX, self.OnComboBox1Combobox,
              id=wxID_MENUCLIENTEMASCOTACOMBOBOX1)

        self.staticBox4 = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOX4,
              label=u'Modificar Mascota', name='staticBox4', parent=self.panel2,
              pos=wx.Point(344, 16), size=wx.Size(312, 320), style=0)
        self.staticBox4.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticBox3 = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOX3,
              label=u'Modificar Cliente', name='staticBox3', parent=self.panel2,
              pos=wx.Point(16, 16), size=wx.Size(304, 320), style=0)
        self.staticBox3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.panel3 = wx.Panel(id=wxID_MENUCLIENTEMASCOTAPANEL3, name='panel3',
              parent=self.panel2, pos=wx.Point(112, 48), size=wx.Size(176, 32),
              style=wx.TAB_TRAVERSAL)

        self.searchCtrl1 = wx.SearchCtrl(id=wxID_MENUCLIENTEMASCOTASEARCHCTRL1,
              name='searchCtrl1', parent=self.panel3, pos=wx.Point(0, 0),
              size=wx.Size(176, 32), style=0, value=u'Buscar..')

        self.staticText10 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT10,
              label=u'Documento', name='staticText10', parent=self.panel2,
              pos=wx.Point(32, 56), size=wx.Size(55, 13), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)
        
    def OnButton2Button(self, event):
       self.Close(True)

    def OnComboBox1Combobox(self, event):
        event.Skip()    
    
    def __init__(self, parent):
        self._init_ctrls(parent)