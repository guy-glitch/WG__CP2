import tkinter as tk
root = tk.Tk()

root.title("Testing")
root.configure(background="green")
root.minsize(300,300)
root.maxsize(1000,1000)
root.geometry("300x300+200+100")
label = tk.Label(root, text="This is currently working!", font=("Times New Roman",20,))
label.config(fg="pink", background="green")
image = tk.PhotoImage(file="Notes/MasmCodeSnippet.gif")
tk.Label(root,image=image)
#Stuff about button
root.count = 0
def add():
    root.count += 1
    num["text"] = root.count
btn=tk.Button(root,text="ADD", command=add)
btn.pack()
num=tk.Label(root,text='0')
num.pack
label.pack()
root.mainloop()
