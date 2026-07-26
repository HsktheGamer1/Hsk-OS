import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

root = tk.Tk()
root.title("Hsk OS - Home Desktop Workspace")
root.geometry("1100x680")
root.configure(bg="#1E3A8A")  # Classic Windows 11 Blue Desktop Wallpaper

# -------------------------------------------------------------
# CORE LOGIC: THE CENTRAL WINDOWS DESKTOP GRID AND SEARCH SYSTEM
# -------------------------------------------------------------
main_desktop = tk.Frame(root, bg="#1E3A8A")
main_desktop.pack(fill="both", expand=True)

def reset_desktop_view():
    for widget in main_desktop.winfo_children():
        widget.destroy()
    build_desktop_shortcuts()

def run_search(event=None):
    query = search_entry.get().lower()
    if "store" in query or "shop" in query:
        open_hsk_store()
    elif "game" in query or "play" in query:
        open_google_games()
    elif "file" in query or "folder" in query:
        open_hsk_files()
    else:
        messagebox.showinfo("Hsk Search", f"Searching locally for: {search_entry.get()}")

# -------------------------------------------------------------
# REAL EMBEDDED APPLICATION LAYOUT PANELS
# -------------------------------------------------------------
def open_app_frame(title_name, bg_color="#1E293B"):
    reset_desktop_view()
    # Integrated App Container with a Top Windows Titlebar
    app_container = tk.Frame(main_desktop, bg=bg_color, bd=2, relief="groove")
    app_container.pack(fill="both", expand=True, padx=40, pady=30)
    
    title_bar = tk.Frame(app_container, bg="#0F172A", height=35)
    title_bar.pack(side="top", fill="x")
    
    tk.Label(title_bar, text=title_name, fg="white", bg="#0F172A", font=("Segoe UI", 10, "bold")).pack(side="left", padx=15)
    tk.Button(title_bar, text="✕ Close Window", fg="white", bg="#EF4444", bd=0, padx=12, command=reset_desktop_view).pack(side="right", fill="y")
    return app_container

def open_hsk_store():
    frame = open_app_frame("🛒 Hsk App Store Hub")
    tk.Label(frame, text="Hsk Digital Marketplace", fg="white", bg="#1E293B", font=("Segoe UI", 16, "bold")).pack(pady=20)
    
    catalog = tk.Frame(frame, bg="#1E293B")
    catalog.pack(pady=10)
    
    # Clickable App Store Items
    tk.Label(catalog, text="🎮 Google Device Games Package", fg="#38BDF8", bg="#1E293B", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    tk.Button(catalog, text="Boot Play Mirror", bg="#10B981", fg="white", bd=0, padx=15, command=open_google_games).grid(row=0, column=1, padx=20)
    
    tk.Label(catalog, text="📁 Hsk Core File Explorer", fg="#38BDF8", bg="#1E293B", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, padx=20, pady=10, sticky="w")
    tk.Button(catalog, text="Open Folder Paths", bg="#3B82F6", fg="white", bd=0, padx=15, command=open_hsk_files).grid(row=1, column=1, padx=20)

def open_google_games():
    frame = open_app_frame("🎮 Google Device Games Engine", bg_color="#064E3B")
    tk.Label(frame, text="Google Play Device Games Hub", fg="#34D399", bg="#064E3B", font=("Segoe UI", 16, "bold")).pack(pady=20)
    
    games_grid = tk.Frame(frame, bg="#064E3B")
    games_grid.pack(pady=10)
    
    games_list = ["🕹️ Retro Snake Classic", "🚀 Space Asteroid Dash", "🏎️ Hsk Vector Racing"]
    for idx, game in enumerate(games_list):
        card = tk.Frame(games_grid, bg="#022C22", padx=15, pady=15, bd=1, relief="solid")
        card.grid(row=0, column=idx, padx=15)
        tk.Label(card, text=game, fg="white", bg="#022C22", font=("Segoe UI", 11, "bold")).pack(pady=5)
        tk.Button(card, text="Launch Game Frame", bg="#10B981", fg="white", bd=0, padx=10, pady=4, command=lambda g=game: messagebox.showinfo("Game Booter", f"Initializing {g} runtime elements.")).pack()

def open_hsk_files():
    frame = open_app_frame("📁 Hsk Storage File Explorer")
    tk.Label(frame, text="System Directory Explorer: Local C:\\ Drive", fg="white", bg="#1E293B", font=("Segoe UI", 12, "bold")).pack(pady=20)
    tk.Label(frame, text="[Directory Path: Root/User/Desktop/ - 0 Files Detected]", fg="#94A3B8", bg="#1E293B", font=("Segoe UI", 10)).pack()

# -------------------------------------------------------------
# GRAPHICAL DESKTOP SHORTCUT GRID BLOCK
# -------------------------------------------------------------
def build_desktop_shortcuts():
    shortcut_panel = tk.Frame(main_desktop, bg="#1E3A8A")
    shortcut_panel.pack(side="top", anchor="w", padx=30, pady=30)
    
    items = [
        ("🛒\nHsk Store", open_hsk_store),
        ("🎮\nGoogle Games", open_google_games),
        ("📁\nHsk Files", open_hsk_files)
    ]
    for idx, (label, action) in enumerate(items):
        btn = tk.Button(shortcut_panel, text=label, fg="white", bg="#1E3A8A", activebackground="#2563EB", font=("Segoe UI", 10), bd=0, cursor="hand2", command=action)
        btn.grid(row=idx, column=0, pady=15, padx=10, sticky="w")

# -------------------------------------------------------------
# CENTERED WINDOWS TASKBAR WITH HSK LOGO & SEARCH
# -------------------------------------------------------------
taskbar = tk.Frame(root, bg="#0F172A", height=55)
taskbar.pack(side="bottom", fill="x")

# Left Section: Pinned Hsk Identity Logo Bracket
left_branding = tk.Frame(taskbar, bg="#0F172A")
left_branding.pack(side="left", padx=15)
tk.Label(left_branding, text="[HSK]", fg="#38BDF8", bg="#0F172A", font=("Segoe UI", 12, "bold")).pack()

# Center Section: Windows 11 Taskbar App Grid
center_dock = tk.Frame(taskbar, bg="#0F172A")
center_dock.pack(anchor="center", pady=4)

# Real Functional Centered Search bar
search_entry = tk.Entry(center_dock, font=("Segoe UI", 10), width=18, bg="#1E293B", fg="white", bd=0, insertbackground="white")
search_entry.pack(side="left", padx=10, ipady=4)
search_entry.insert(0, "🔍 Search apps...")
search_entry.bind("<FocusIn>", lambda e: search_entry.delete(0, 'end') if "Search" in search_entry.get() else None)
search_entry.bind("<Return>", run_search)

# Taskbar System App Triggers
tk.Button(center_dock, text="❖", fg="#38BDF8", bg="#1E293B", font=("Segoe UI", 12), bd=0, padx=12, command=reset_desktop_view).pack(side="left", padx=3)
tk.Button(center_dock, text="🛒", fg="white", bg="#0F172A", font=("Segoe UI", 12), bd=0, padx=10, command=open_hsk_store).pack(side="left", padx=2)
tk.Button(center_dock, text="🎮", fg="white", bg="#0F172A", font=("Segoe UI", 12), bd=0, padx=10, command=open_google_games).pack(side="left", padx=2)

# Right Section: Clock Ribbon Pane
right_clock = tk.Frame(taskbar, bg="#0F172A")
right_clock.pack(side="right", padx=20)
clock_lbl = tk.Label(right_clock, fg="#94A3B8", bg="#0F172A", font=("Segoe UI", 9))
clock_lbl.pack()

def update_clock_tick():
    clock_lbl.config(text=datetime.now().strftime("%I:%M %p\n%m/%d/%Y"))
    root.after(1000, update_clock_tick)

# Boot Initialize
build_desktop_shortcuts()
update_clock_tick()
root.mainloop()
