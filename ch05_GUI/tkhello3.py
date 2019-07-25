__Author__ = "noduez"
'''Label和Button控件演示'''

import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!', fg="dark green")
hello.pack()

quit = tkinter.Button(top, text='QUIT', fg='white', bg='red', command=top.quit)
quit.pack(fill=tkinter.X, expand=1)
tkinter.mainloop()