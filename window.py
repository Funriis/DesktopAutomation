import tkinter as tk
from clickBtn import clicked

#Todo: Learn more about tkinter grids
#Todo: Think of something you can automate with a window/buttons
#*imp: Don't let that younger kid get better (Texas tho)
#*imp: Udemy course on data visulization

#Git init                         (Initialize git)
#rm -rf .git                      (Remove git)
#Git add .                        (Add all files)
#Git commit -m "Commit desc"      (Commit)

window = tk.Tk()
window.geometry("800x500+150+150")

Button_1 = tk.Button(window, text="Open Google chrome", bg="#545454", command=clicked)
Button_1.pack(side=tk.LEFT)

window.mainloop()