# -*- coding: utf-8 -*-

import wx


def create(parent):
    return MenuPrincipal(parent)

[wxID_MENUPRINCIPAL, wxID_MENUPRINCIPALBOTONCLIENTE, 
 wxID_MENUPRINCIPALBOTONCONSULTAS, wxID_MENUPRINCIPALBOTONPASEADOR, 
 wxID_MENUPRINCIPALBOTONSALIR, wxID_MENUPRINCIPALCOPYRIGHT, 
 wxID_MENUPRINCIPALPANEL1, wxID_MENUPRINCIPALSTATICBITMAP1, 
 wxID_MENUPRINCIPALTITULOPRINCIPAL, 
] = [wx.NewId() for _init_ctrls in range(9)]

class MenuPrincipal(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MENUPRINCIPAL, name=u'MenuPrincipal',
              parent=prnt, pos=wx.Point(341, 91), size=wx.Size(750, 550),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Menu Principal')
        self.SetClientSize(wx.Size(742, 519)) 
        self.SetIcon(wx.Icon(u'C:/Users/Win7Ultimate/Documents/Python Scripts/Trabajo-Phyton-Mendieta-Nunez-Perez/Imagenes/pie_Icono.ico',wx.BITMAP_TYPE_ICO))
                            
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Verdana'))

        self.panel1 = wx.Panel(id=wxID_MENUPRINCIPALPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(742, 519),
              style=wx.TAB_TRAVERSAL)

        self.BotonCliente = wx.Button(id=wxID_MENUPRINCIPALBOTONCLIENTE,
              label=u'Cliente/Mascotas', name=u'BotonCliente', parent=self.panel1,
              pos=wx.Point(488, 104), size=wx.Size(144, 64), style=0)
        self.BotonCliente.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Verdana'))
        self.BotonCliente.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.BotonCliente.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.BotonCliente.Bind(wx.EVT_BUTTON, self.OnBotonClienteButton,
              id=wxID_MENUPRINCIPALBOTONCLIENTE)

        self.BotonPaseador = wx.Button(id=wxID_MENUPRINCIPALBOTONPASEADOR,
              label=u'Paseador', name=u'BotonPaseador', parent=self.panel1,
              pos=wx.Point(488, 224), size=wx.Size(144, 64), style=0)
        self.BotonPaseador.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Verdana'))
        self.BotonPaseador.Bind(wx.EVT_BUTTON, self.OnBotonPaseadorButton,
              id=wxID_MENUPRINCIPALBOTONPASEADOR)

        self.BotonConsultas = wx.Button(id=wxID_MENUPRINCIPALBOTONCONSULTAS,
              label=u'Consultas', name=u'BotonConsultas', parent=self.panel1,
              pos=wx.Point(488, 344), size=wx.Size(144, 64), style=0)
        self.BotonConsultas.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Verdana'))

        self.BotonSalir = wx.Button(id=wxID_MENUPRINCIPALBOTONSALIR,
              label=u'Salir', name=u'BotonSalir', parent=self.panel1,
              pos=wx.Point(648, 480), size=wx.Size(75, 23), style=0)
        self.BotonSalir.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Verdana'))

        self.TituloPrincipal = wx.StaticText(id=wxID_MENUPRINCIPALTITULOPRINCIPAL,
              label=u'AGENCIA DE PASEO DE MASCOTAS', name=u'TituloPrincipal',
              parent=self.panel1, pos=wx.Point(104, 24), size=wx.Size(524, 32),
              style=0)
        self.TituloPrincipal.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Verdana'))

        self.Copyright = wx.StaticText(id=wxID_MENUPRINCIPALCOPYRIGHT,
              label=u'Copyright by Mendieta - Nu\xf1ez - Perez',
              name=u'Copyright', parent=self.panel1, pos=wx.Point(16, 496),
              size=wx.Size(216, 13), style=0)
        self.Copyright.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        
        '--IMAGEN DEL PASEADOR---'
        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Win7Ultimate/Documents/Python Scripts/Trabajo-Phyton-Mendieta-Nunez-Perez/Imagenes/Paseador-de-perros.png',
              wx.BITMAP_TYPE_PNG), id=wxID_MENUPRINCIPALSTATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(24, 80),
              size=wx.Size(386, 400), style=0)
        self.staticBitmap1.SetToolTipString(u'staticBitmap1')
        self.staticBitmap1.Enable(False)
        self.staticBitmap1.SetAutoLayout(False)

    def __init__(self, parent):
        print 'aca'
        self._init_ctrls(parent)

    def OnBotonClienteButton(self, event):
      event.Skip()

    def OnBotonPaseadorButton(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()

