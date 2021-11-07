import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Hello world")
        panel=MyPanel(self)
        self.Show()

class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        button = wx.Button(self, label="Press me")

if __name__ =="__main__":
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()