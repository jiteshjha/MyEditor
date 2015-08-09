import Tkinter
import ScrolledText
root = Tkinter.Tk(className="My Editor")
textPad = ScrolledText.ScrolledText(root, width=100, height=80)
textPad.pack()
root.mainloop()
