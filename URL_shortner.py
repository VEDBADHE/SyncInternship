import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    original_url = entry_url.get()
    curtailed_url = pyshorteners.Shortener()
    short_url = curtailed_url.tinyurl.short(original_url)
    label_shortened.config(text="The Shortened URL is: " + short_url)
    copied_url.set(short_url)  # Update the URL in the copied_url StringVar

def copy_url_to_clipboard():
    short_url = copied_url.get()
    pyperclip.copy(short_url)  # Copy the shortened URL to the clipboard

# Create the main application window
app = tk.Tk()
app.title("URL Shortener")
app.configure(bg="lightgray")  # Set background color for the main window

# Create and place widgets
label_instructions = tk.Label(app, text="Enter the URL to be shortened:", bg="yellow")
label_instructions.pack(pady=10)

entry_url = tk.Entry(app, width=40, bg="white")
entry_url.pack(pady=5)

button_shorten = tk.Button(app, text="Shorten URL", command=shorten_url, bg="blue", fg="white")
button_shorten.pack(pady=10)

label_shortened = tk.Label(app, text="", bg="lightgray")
label_shortened.pack()

# StringVar to store the copied URL
copied_url = tk.StringVar()

# Create a label to display the copied URL
label_copied_url = tk.Label(app, textvariable=copied_url, bg="lightgray")
label_copied_url.pack()

# Create a button to copy the URL to the clipboard
button_copy_url = tk.Button(app, text="Copy URL", command=copy_url_to_clipboard)
button_copy_url.pack(pady=5)

# Start the main event loop
app.mainloop()
