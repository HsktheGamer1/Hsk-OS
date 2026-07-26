import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Standard operational variables
APP_VERSION = "1.2.0-SafeEdition"
ACTIVE_PROFILE = "Hsk_Local_User"

root = tk.Tk()
root.title(f"Hsk OS Environment - {APP_VERSION}")
root.geometry("1100x650")
root.configure(bg="#0F172A")

# Main interface panel
display_panel = tk.Frame(root, bg="#1E293B", bd=1, relief="solid")
display_panel.pack(side="top", fill="both", expand=True, padx=20, pady=20)

def reset_display():
    for widget in display_panel.winfo_children():
        widget.destroy()

def show_home():
    reset_display()
    tk.Label(display_panel, text=f"Welcome to Hsk OS Dashboard", fg="#F8FAFC", bg="#1E293B", font=("Segoe UI", 18, "bold")).pack(pady=30)
    
    info_card = tk.Frame(display_panel, bg="#334155", padx=15, pady=15)
    info_card.pack(pady=10)
    tk.Label(info_card, text=f"User Session: {ACTIVE_PROFILE}", fg="#38BDF8", bg="#334155", font=("Segoe UI", 10, "bold")).pack(anchor="w")
    tk.Label(info_card, text="Security Status: Verified Clean Execution Loop", fg="#34D399", bg="#334155", font=("Segoe UI", 9)).pack(anchor="w", pady=5)

def launch_browser():
    reset_display()
    tk.Label(display_panel, text="🌐 Hsk Browser Module", fg="white", bg="#1E293B", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=10)
    frame = tk.Frame(display_panel, bg="#000000")
    frame.pack(fill="both", expand=True, padx=15, pady=10)
    tk.Label(frame, text="Local network stack verified. Visual placeholder framework active.", fg="#22C55E", bg="#000000", font=("Consolas", 10)).pack(expand=True)

def launch_store():
    reset_display()
    tk.Label(display_panel, text="🛒 Hsk Store Catalog", fg="white", bg="#1E293B", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=10)
    
    catalog_frame = tk.Frame(display_panel, bg="#1E293B")
    catalog_frame.pack(fill="both", expand=True, padx=15, pady=10)
    
    app_items = ["Hsk Notepad Companion", "Hsk Diagnostic Tool", "Hsk System Calculator"]
    for item in app_items:
        card = tk.Frame(catalog_frame, bg="#334155", padx=10, pady=10)
        card.pack(fill="x", pady=5)
        tk.Label(card, text=item, fg="white", bg="#334155", font=("Segoe UI", 10, "bold")).pack(side="left")
        tk.Button(card, text="Initialize App Setup", bg="#3B82F6", fg="white", bd=0, padx=10, command=lambda n=item: messagebox.showinfo("Local Installer", f"Setting up localized paths for {n}.")).pack(side="right")

# Bottom control ribbon
taskbar = tk.Frame(root, bg="#0F172A", height=50)
taskbar.pack(side="bottom", fill="x")

tray = tk.Frame(taskbar, bg="#0F172A")
tray.pack(anchor="center", pady=5)

tk.Button(tray, text="❖", fg="#38BDF8", bg="#1E293B", font=("Segoe UI", 12, "bold"), bd=0, padx=12, command=show_home).pack(side="left", padx=4)
tk.Button(tray, text="🌐", fg="white", bg="#0F172A", font=("Segoe UI", 12), bd=0, padx=12, command=launch_browser).pack(side="left", padx=2)
tk.Button(tray, text="🛒", fg="white", bg="#0F172A", font=("Segoe UI", 12), bd=0, padx=12, command=launch_store).pack(side="left", padx=2)

show_home()
root.mainloop()
