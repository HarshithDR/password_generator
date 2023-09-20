import tkinter as tk

def on_submit():
    # Get the text from the entry fields
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()

    # Display the entered text
    result_label.config(text=f"You entered: {text1}, {text2}, {text3}")

# Create the main window
root = tk.Tk()
root.title("Three Text Entry Fields")

# Create a frame to hold the entry fields
entry_frame = tk.Frame(root)
entry_frame.pack()

# Create the entry fields
entry1 = tk.Entry(entry_frame)
entry2 = tk.Entry(entry_frame)
entry3 = tk.Entry(entry_frame)

# Pack the entry fields side by side
entry1.pack(side=tk.LEFT)
entry2.pack(side=tk.LEFT)
entry3.pack(side=tk.LEFT)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
