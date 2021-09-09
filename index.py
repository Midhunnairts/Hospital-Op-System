from tkinter import *

class Application:
    def __init__(self,root):
        self.root=root
        self.root.title("PCH")
        self.root.minsize(1024, 512)
        self.root.maxsize(1024, 512)
        StartFrame=Frame(self.root, bg="black",height=512,width=1024)
        StartFrame.grid()
        self.label1=Label(StartFrame,text="PCH",font="6px",highlightcolor="red",bg="black",fg="white")
        self.label1.place(x=500,y=60)
        self.bt1=Button(StartFrame,text="Encrypt",height=20,width=38,bg="green",font="Bold")
        self.bt1.place(x=0,y=140)
        self.bt2=Button(StartFrame,text="Decrypt",height=20,width=38,bg="blue",font="Bold")
        self.bt2.place(x=340,y=140)
        self.bt3=Button(StartFrame,text="Hack",height=20,width=38,bg="red",font="Bold")
        self.bt3.place(x=680,y=140)
if __name__=='__main__':
    root = Tk()    

    app = Application(root)
    root.mainloop()

       