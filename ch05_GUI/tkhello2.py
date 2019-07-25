__Author__ = "noduez"
'''Button控件演示'''

import tkinter as tk

top = tk.Tk()
quit = tk.Button(top, text='Hello World!',
                 command=top.quit)
quit.pack()
tk.mainloop()