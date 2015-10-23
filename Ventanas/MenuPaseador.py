#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(550, 181), size=wx.Size(400, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(384, 447))

        self.panel1 = wx.Panel(id=wxID_DIALOG1PANEL1, name='panel1',
              parent=self, pos=wx.Point(112, 72), size=wx.Size(200, 100),
              style=wx.TAB_TRAVERSAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
