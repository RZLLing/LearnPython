import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('500x300')

# # 讲
# var = tk.StringVar()
#
# label = tk.Label(window,textvariable=var, bg='green', font=('Arial',12), width=30, height=2)
# label.pack()
#
#
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
#
#
# button1 = tk.Button(window,text='hit me',font=('Arial',12),width=10,height=1,command=hit_me)
# button1.pack()

# entry 的用法
# e1 = tk.Entry(window, show='*',font=('Arial',14))
# e2 = tk.Entry(window,show=None,font=('Arial',14))
# e1.pack()
# e2.pack()

# e = tk.Entry(window, show=None)
# e.pack()
#
#
# def insert_point():
#     var = e.get()
#     t.insert('insert',var)
# def insert_end():
#     var = e.get()
#     t.insert('end',var)
#
# b1 = tk.Button(window,text= 'insert point',width =10, height = 2,command = insert_point)
# b1.pack()
# b2 = tk.Button(window,text='insert end', width=10, height=2, command=insert_end)
# b2.pack()
#
# t = tk.Text(window,height=3)
# t.pack()

var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window,listvariable=var2)
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()
window.mainloop()
