# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:06:21 2015

@author: Win7Ultimate
"""

import wx

def create(parent):
    return VClienteMascota(parent)

[wxID_VCLIENTEMASCOTA, wxID_VCLIENTEMASCOTABUTTON1, 
 wxID_VCLIENTEMASCOTABUTTON2, wxID_VCLIENTEMASCOTANOTEBOOK1, 
 wxID_VCLIENTEMASCOTAPANEL1, wxID_VCLIENTEMASCOTAPANEL2, 
 wxID_VCLIENTEMASCOTASTATICBOX1, wxID_VCLIENTEMASCOTASTATICBOX2, 
 wxID_VCLIENTEMASCOTASTATICTEXT1, wxID_VCLIENTEMASCOTASTATICTEXT2, 
 wxID_VCLIENTEMASCOTASTATICTEXT3, wxID_VCLIENTEMASCOTASTATICTEXT4, 
 wxID_VCLIENTEMASCOTASTATICTEXT5, wxID_VCLIENTEMASCOTASTATICTEXT6, 
 wxID_VCLIENTEMASCOTASTATICTEXT7, wxID_VCLIENTEMASCOTASTATICTEXT8, 
 wxID_VCLIENTEMASCOTASTATICTEXT9, wxID_VCLIENTEMASCOTATEXTCTRL1, 
 wxID_VCLIENTEMASCOTATEXTCTRL2, wxID_VCLIENTEMASCOTATEXTCTRL3, 
 wxID_VCLIENTEMASCOTATEXTCTRL4, wxID_VCLIENTEMASCOTATEXTCTRL5, 
 wxID_VCLIENTEMASCOTATEXTCTRL6, wxID_VCLIENTEMASCOTATEXTCTRL7, 
 wxID_VCLIENTEMASCOTATEXTCTRL8, wxID_VCLIENTEMASCOTATEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(26)]

class VClienteMascota(wx.Dialog):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True, text='Altas')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text='Modificar')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_VCLIENTEMASCOTA,
              name=u'VClienteMascota', parent=prnt, pos=wx.Point(433, 160),
              size=wx.Size(713, 485), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Cliente')
        self.SetClientSize(wx.Size(697, 447))

        self.notebook1 = wx.Notebook(id=wxID_VCLIENTEMASCOTANOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(697, 447), style=0)

        self.panel1 = wx.Panel(id=wxID_VCLIENTEMASCOTAPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 421),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_VCLIENTEMASCOTAPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 421),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_VCLIENTEMASCOTASTATICBOX1,
              label=u'Alta Cliente', name='boxAltaC', parent=self.panel1,
              pos=wx.Point(6, 8), size=wx.Size(306, 328), style=0)
        self.staticBox1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.staticText1 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT1,
              label=u'Documento', name='labelDoc', parent=self.panel1,
              pos=wx.Point(30, 50), size=wx.Size(55, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT2,
              label=u'Nombre', name='labelNombre', parent=self.panel1,
              pos=wx.Point(30, 100), size=wx.Size(38, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT3,
              label=u'Apellido', name='labelApe', parent=self.panel1,
              pos=wx.Point(30, 150), size=wx.Size(38, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT4,
              label=u'Direccion', name='labelDirec', parent=self.panel1,
              pos=wx.Point(30, 200), size=wx.Size(44, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT5,
              label=u'Telefono', name='labelTel', parent=self.panel1,
              pos=wx.Point(30, 250), size=wx.Size(43, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL1,
              name='textDoc', parent=self.panel1, pos=wx.Point(88, 100),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL2,
              name='textNombre', parent=self.panel1, pos=wx.Point(88, 50),
              size=wx.Size(104, 21), style=0, value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL3,
              name='textApe', parent=self.panel1, pos=wx.Point(88, 150),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL4,
              name='textDirec', parent=self.panel1, pos=wx.Point(88, 200),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL5,
              name='textTel', parent=self.panel1, pos=wx.Point(88, 250),
              size=wx.Size(136, 21), style=0, value=u'')

        self.staticBox2 = wx.StaticBox(id=wxID_VCLIENTEMASCOTASTATICBOX2,
              label=u'Alta Mascota', name='boxAltaM', parent=self.panel1,
              pos=wx.Point(352, 8), size=wx.Size(328, 328), style=0)
        self.staticBox2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.staticText6 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT6,
              label=u'Nombre', name='labelNombre', parent=self.panel1,
              pos=wx.Point(368, 50), size=wx.Size(38, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT7,
              label=u'Raza', name='labelRaza', parent=self.panel1,
              pos=wx.Point(368, 100), size=wx.Size(25, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT8,
              label=u'Peso', name='labelPeso', parent=self.panel1,
              pos=wx.Point(368, 150), size=wx.Size(24, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_VCLIENTEMASCOTASTATICTEXT9,
              label=u'Codigo', name='labelCodigo', parent=self.panel1,
              pos=wx.Point(368, 200), size=wx.Size(34, 13), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL6,
              name='textNombre', parent=self.panel1, pos=wx.Point(432, 50),
              size=wx.Size(160, 21), style=0, value=u'')

        self.textCtrl7 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL7,
              name='textRaza', parent=self.panel1, pos=wx.Point(432, 100),
              size=wx.Size(160, 21), style=0, value=u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL8,
              name='textPeso', parent=self.panel1, pos=wx.Point(432, 150),
              size=wx.Size(56, 21), style=0, value=u'')

        self.textCtrl9 = wx.TextCtrl(id=wxID_VCLIENTEMASCOTATEXTCTRL9,
              name='textCodigo', parent=self.panel1, pos=wx.Point(432, 200),
              size=wx.Size(128, 21), style=0, value=u'')
        self.textCtrl9.SetEditable(False)

        self.button1 = wx.Button(id=wxID_VCLIENTEMASCOTABUTTON1,
              label=u'Guardar', name='botonGuardar', parent=self.panel1,
              pos=wx.Point(568, 288), size=wx.Size(99, 31), style=0)

        self.button2 = wx.Button(id=wxID_VCLIENTEMASCOTABUTTON2, label=u'Atras',
              name='botonAtras', parent=self.panel1, pos=wx.Point(8, 384),
              size=wx.Size(88, 31), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_VCLIENTEMASCOTABUTTON2)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)