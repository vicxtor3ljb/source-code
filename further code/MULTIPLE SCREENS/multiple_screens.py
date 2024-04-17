import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Screen 1")
# Set the size and position of the window
root.geometry("400x200+0+0") # Size: 400x200, Position: Top left corner of the primary screen

# Create a label widget inside the main window
label1 = tk.Label(root, text="Window 1")
label1.pack()

# Create a new Toplevel window (secondary window)
window2 = tk.Toplevel(root)
window2.title("Screen 2")
# Set the size and position of the secondary window
window2.geometry("400x200+800+0") # Size: 400x200, Position: Top left corner of the secondary screen

# Create a label widget inside the secondary window
label2 = tk.Label(window2, text="Window 2")
label2.pack()

# Start the Tkinter event loop
root.mainloop()

