import tkinter as tk
from tkinter import messagebox

# 1. Initialize the Main Hsk OS Desktop Window
root = tk.Tk()
root.title("Hsk OS Desktop Environment - Version 1.0.0-Beta")
root.geometry("1024x600")
root.configure(bg="#1e1e1e")  # Matches your Dark Mode theme configuration

# 2. Add an Interactive Click Event for Desktop Apps
def launch_app(app_name):
    messagebox.showinfo("Hsk OS Launcher", f"Launching {app_name} inside Hsk OS...")

# 3. Create Desktop Icon Grid Systems
icon_frame = tk.Frame(root, bg="#1e1e1e")
icon_frame.pack(side="top", anchor="w", padx=20, pady=20)

btn_browser = tk.Button(icon_frame, text="🌐\nWeb Browser", fg="white", bg="#2d2d2d", 
                        font=("Arial", 10), bd=0, padx=10, pady=10, command=lambda: launch_app("Secure Web Browser"))
btn_browser.grid(row=0, column=0, padx=10)

btn_docs = tk.Button(icon_frame, text="📁\nMy Files", fg="white", bg="#2d2d2d", 
                     font=("Arial", 10), bd=0, padx=10, pady=10, command=lambda: launch_app("File Explorer"))
btn_docs.grid(row=0, column=1, padx=10)

# 4. Create the Centered Windows-style Taskbar
taskbar = tk.Frame(root, bg="#101010", height=50)
taskbar.pack(side="bottom", fill="x")

# Center Container inside the Taskbar
centered_menu = tk.Frame(taskbar, bg="#101010")
centered_menu.pack(side="top", anchor="center", pady=5)

# Centered Buttons (Start Menu, Search, Actions)
btn_start = tk.Button(centered_menu, text="❖ Start", fg="#0078d4", bg="#202020", font=("Arial", 10, "bold"), bd=0, padx=15, command=lambda: launch_app("Start Menu"))
btn_start.pack(side="left", padx=5)

btn_search = tk.Button(centered_menu, text="🔍 Search", fg="white", bg="#202020", font=("Arial", 10), bd=0, padx=10, command=lambda: launch_app("Search Index"))
btn_search.pack(side="left", padx=5)

# Keep the interactive layout window open running on your computer
root.mainloop()
