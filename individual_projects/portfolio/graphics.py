#graphs and graphics

import tkinter

#create class menu
class Menu:
    #create function init, get options'
    def __init__(self,options):
        #create window with boxes for every option
        self.options=options

    #create function use
    def use(self):
        #show window
        while True:
            root=tkinter.Tk()
            root.title('Personal Portfolio')
            root.configure(background='red')
            root.minsize(500,500)
            root.maxsize(1000,1000)
            root.geometry('700x700+1300+500')
            self.out=tkinter.StringVar()
            #return option clicked
            def push(name):
                self.out=name
                root.destroy()
            #check for box click
            buttons=[]
            for v in self.options:
                buttons.append(tkinter.Button(root,text=v,command=lambda v=v: push(v)))
            for v,i in enumerate(buttons):
                i.pack()
                i.place(x=100,y=700/len(self.options)*(v+0.42))
            root.mainloop()
            try:
                return self.out
            except:
                pass
        

#create function inputs, get question and wrong
def inputs(question,wrong=False):
    while True:
        #create window, show question and text box
        root=tkinter.Tk()
        root.title('Personal Finance')
        root.configure(background='black')
        root.minsize(500,500)
        root.maxsize(1000,1000)
        root.geometry('700x700+1300+500')
        out=tkinter.StringVar()
        enter=tkinter.Entry(root,width=50,textvariable=out)
        enter.pack()
        enter.place(x=200,y=350)
        q=tkinter.Label(root,text=question)
        q.pack()
        q.place(x=250,y=300)
        #return text box entry
        def end():
            root.destroy()
        #if wrong is true, also show invalid input, try again
        if wrong:
            error=tkinter.Label(root,text='Invalid input. Try again.')
            error.pack()
            error.place(x=270,y=250)
        button=tkinter.Button(root,text='Enter',command=end)
        button.pack()
        button.place(x=300,y=370)
        root.mainloop()
        if out.get()!="":
            return out.get()

#create function show, get stuff
def show(stuff):
    #create window and display stuff
    root=tkinter.Tk()
    root.title('Personal Finance')
    root.configure(background='black')
    root.minsize(500,500)
    root.maxsize(1000,1000)
    root.geometry('700x700+1300+500')
    tkinter.Message(root,text=stuff,width=700).pack()
    def end():
        root.destroy()
    button=tkinter.Button(root,text='Continue',command=end)
    button.pack()
    button.place(x=300,y=500)
    root.mainloop()

#need to test everything except inputs