    def  __init__ (self, master = None) :
         Frame .__ init __ (self, master)        
        self.master = master

        # widget peut prendre toutes les fenêtres
         self.pack (fill = BOTH, expand = 1 )

        # créer un bouton, le lier à clickExitButton ()
         exitButton = Button (self, text = "Exit" , command = self.clickExitButton)

        # place le bouton à (0,0)
         exitButton.place (x = 0 , y = 0 )

    def  clickExitButton (self) :
         exit ()
         root = Tk ()
         app = Window (root)
         root.wm_title ( "Tkinter button" )
         root.geometry ( "320x200" )
         root.mainloop ()
        


