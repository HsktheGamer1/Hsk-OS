import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

root = tk.Tk()
root.title("Hsk OS - Windows 11 Integrated Pro")
root.geometry("1150x700")
root.configure(bg="#0F172A") # Deep premium dark slate background

# Pinned Cloud Account Data Attributes
CURRENT_USER = "Hsk_Gamer_Guest"
IS_SIGNED_IN = False

# -------------------------------------------------------------
# CORE LOGIC: SINGLE-WINDOW WORKSPACE MANAGER CONTEXT
# -------------------------------------------------------------
# This core workspace element holds whichever Hsk program viewport is open
app_workspace_frame = tk.Frame(root, bg="#1E293B", bd=2, relief="sunken")
app_workspace_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

def clear_workspace():
    """Wipes the main window canvas area clear so new applications can render."""
    for widget in app_workspace_frame.winfo_children():
        widget.destroy()

def load_desktop_home():
    """Renders the central core status cards directly within the single application view."""
    clear_workspace()
    
    welcome_lbl = tk.Label(app_workspace_frame, text=f"Welcome to Hsk OS, {CURRENT_USER}!", fg="#F8FAFC", bg="#1E293B", font=("Segoe UI", 20, "bold"), pady=15)
    welcome_lbl.pack(pady=40)
    
    status_card = tk.Frame(app_workspace_frame, bg="#334155", padx=20, pady=20, bd=1, relief="groove")
    status_card.pack(pady=10)
    
    tk.Label(status_card, text="💻 Hsk Core Engine Status: Active", fg="#38BDF8", bg="#334155", font=("Segoe UI", 11, "bold")).pack(anchor="w")
    tk.Label(status_card, text=f"👤 Hsk Account: {'Synchronized ✔' if IS_SIGNED_IN else 'Offline Guest Access'}", fg="#94A3B8", bg="#334155", font=("Segoe UI", 10)).pack(anchor="w", pady=5)
    tk.Label(status_card, text="🛒 Pinned App Store: Connection Standby", fg="#34D399", bg="#334155", font=("Segoe UI", 10)).pack(anchor="w")

# -------------------------------------------------------------
# INTEGRATED APP CODE RUNTIME ENGINE (ALL RENDER DIRECTLY INSIDE)
# -------------------------------------------------------------
def launch_hsk_browser():
    clear_workspace()
    
    app_bar = tk.Frame(app_workspace_frame, bg="#0F172A", height=40)
    app_bar.pack(side="top", fill="x")
    tk.Label(app_bar, text="🌐 Hsk Browser Pro", fg="white", bg="#0F172A", font=("Segoe UI", 10, "bold")).pack(side="left", padx=15)
    
    url_strip = tk.Frame(app_workspace_frame, bg="#E2E8F0", pady=6)
    url_strip.pack(side="top", fill="x")
    tk.Label(url_strip, text=" Address URL: ", bg="#E2E8F0", font=("Segoe UI", 9, "bold")).pack(side="left", padx=5)
    
    url_box = tk.Entry(url_strip, font=("Segoe UI", 10), bd=1)
    url_box.pack(side="left", fill="x", expand=True, padx=10)
    url_box.insert(0, "https://google.com")
    
    web_view = tk.Frame(app_workspace_frame, bg="#000000")
    web_view.pack(fill="both", expand=True)
    
    display_msg = tk.Label(web_view, text="[ Hsk Web Network Active ]\n\nIsolating browser requests seamlessly inside your single window environment.\nReady for web account integration authentication.", fg="#22C55E", bg="#000000", font=("Consolas", 11))
    display_msg.pack(expand=True)
    
    def process_mock_routing(event=None):
        display_msg.config(text=f"[ Connecting to: {url_box.get()} ]\n\nResolving secure host arrays...\nDisplaying live webpage structures perfectly inside your view frame.")
    url_box.bind("<Return>", process_mock_routing)

def launch_hsk_store():
    clear_workspace()
    
    app_bar = tk.Frame(app_workspace_frame, bg="#0F172A", height=40)
    app_bar.pack(side="top", fill="x")
    tk.Label(app_bar, text="🛒 Hsk Store (Google Play Market Framework)", fg="white", bg="#0F172A", font=("Segoe UI", 10, "bold")).pack(side="left", padx=15)
    
    grid = tk.Frame(app_workspace_frame, bg="#1E293B")
    grid.pack(fill="both", expand=True, padx=30, pady=20)
    
    store_apps = [
        {"name": "Hsk Terminal Studio", "icon": "💻", "desc": "Write rapid automation components securely."},
        {"name": "Hsk Media Center", "icon": "🎬", "desc": "Stream high-definition videos inside the environment."},
        {"name": "Hsk TextPad++ Pro", "icon": "📝", "desc": "Write notes, configuration variables, and documents."},
        {"name": "Hsk Game Emulator Pack", "icon": "🎮", "desc": "Download and run custom script gaming modes."}
    ]
    
    def execute_mock_download(name):
        messagebox.showinfo("Hsk Store Downloader", f"Downloading repository application layers for {name}...\n\nSuccessfully pre-compiling installation vectors into Virtual C:\\ drive!")
        
    for i, app in enumerate(store_apps):
        r, c = i // 2, i % 2
        card = tk.Frame(grid, bg="#334155", bd=1, relief="ridge", padx=15, pady=15)
        card.grid(row=r, column=c, padx=15, pady=15, sticky="nsew")
        grid.grid_columnconfigure(c, weight=1)
        grid.grid_rowconfigure(r, weight=1)
        
        tk.Label(card, text=f"{app['icon']} {app['name']}", fg="#38BDF8", bg="#334155", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        tk.Label(card, text=app['desc'], fg="#94A3B8", bg="#334155", font=("Segoe UI", 9), justify="left").pack(anchor="w", pady=5)
        tk.Button(card, text="Get App", fg="white", bg="#3B82F6", activebackground="#2563EB", bd=0, font=("Segoe UI", 9, "bold"), padx=12, pady=4, command=lambda n=app['name']: execute_mock_download(n)).pack(anchor="e")

def launch_hsk_account():
    clear_workspace()
    
    app_bar = tk.Frame(app_workspace_frame, bg="#0F172A", height=40)
    app_bar.pack(side="top", fill="x")
    tk.Label(app_bar, text="👤 Hsk Account Profile Identity Hub", fg="white", bg="#0F172A", font=("Segoe UI", 10, "bold")).pack(side="left", padx=15)
    
    wrapper = tk.Frame(app_workspace_frame, bg="#1E293B")
    wrapper.pack(expand=True)
    
    tk.Label(wrapper, text="Authorize Universal Account Profiles", fg="#F8FAFC", bg="#1E293B", font=("Segoe UI", 14, "bold")).pack(pady=15)
    
    entry_box = tk.Frame(wrapper, bg="#1E293B")
    entry_box.pack()
    
    tk.Label(entry_box, text="Username Email:", fg="#E2E8F0", bg="#1E293B", font=("Segoe UI", 10)).grid(row=0, column=0, pady=10, sticky="e")
    u_field = tk.Entry(entry_box, font=("Segoe UI", 10), width=24)
    u_field.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(entry_box, text="Secret Password:", fg="#E2E8F0", bg="#1E293B", font=("Segoe UI", 10)).grid(row=1, column=0, pady=10, sticky="e")
    p_field = tk.Entry(entry_box, show="*", font=("Segoe UI", 10), width=24)
    p_field.grid(row=1, column=1, padx=10, pady=10)
    
    def confirm_sign_in():
        global CURRENT_USER, IS_SIGNED_IN
        if u_field.get() and p_field.get():
            CURRENT_USER = u_field.get()
            IS_SIGNED_IN = True
            messagebox.showinfo("Identity Sync Success", f"Profile Verified! Welcome {CURRENT_USER}.\nSynchronizing your core data structures.")
            load_desktop_home()
        else:
            messagebox.showerror("Validation Fault", "Fields cannot remain empty.")
            
    tk.Button(wrapper, text="Authenticate Profile Connection", fg="white", bg="#10B981", activebackground="#059669", bd=0, font=("Segoe UI", 10, "bold"), padx=25, pady=6, command=confirm_sign_in).pack(pady=20)

def launch_hsk_files():
    clear_workspace()
    app_bar = tk.Frame(app_workspace_frame, bg="#0F172A", height=40)
    app_bar.pack(side="top", fill="x")
    tk.Label(app_bar, text="📁 Hsk File System Explorer", fg="white", bg="#0F172A", font=("Segoe UI", 10, "bold")).pack(side="left", padx=15)
    
    lbl = tk.Label(app_workspace_frame, text="Current Directory Location: C:\\HskOS\\Desktop\\ProfileData\n\n[ Status Area: Empty Directory ]", fg="#94A3B8", bg="#1E293B", font=("Segoe UI", 11))
    lbl.pack(expand=True)

# -------------------------------------------------------------
# CORE START POPUP OVERLAY INTERFACE ELEMENT
# -------------------------------------------------------------
def toggle_hsk_start():
    drawer = tk.Toplevel(root)
    drawer.geometry("360x420")
    drawer.configure(bg="#1E293B")
    drawer.overrideredirect(True)
    drawer.geometry(f"+{root.winfo_x() + 395}+{root.winfo_y() + 195}")
    
    tk.Label(drawer, text=f"Profile Identity: {CURRENT_USER}", fg="#94A3B8", bg="#1E293B", font=("Segoe UI", 9, "italic"), anchor="w", padx=20, pady=10).pack(fill="x")
    
    grid_area = tk.Frame(drawer, bg="#1E293B")
    grid_area.pack(fill="both", expand=True, padx=20, pady=10)
    
    ops = [
        ("🌐 Hsk Browser", launch_hsk_browser),
        ("📁 Hsk Explorer", launch_hsk_files),
        ("🛒 Hsk Store", launch_hsk_store),
        ("👤 Hsk Account", launch_hsk_account),
        ("🏠 Desktop Dashboard", load_desktop_home)
    ]
    
    for lbl, method in ops:
        tk.Button(grid_area, text=lbl, fg="white", bg="#334155", activebackground="#475569", bd=0, height=2, width=18, font=("Segoe UI", 9), command=lambda m=method: [drawer.destroy(), m()]).pack(pady=6, anchor="center")
        
    tk.Button(drawer, text="Power Off Environment Setup", fg="white", bg="#EF4444", activebackground="#DC2626", font=("Segoe UI", 9, "bold"), bd=0, pady=8, command=root.destroy).pack(fill="x", side="bottom")

# -------------------------------------------------------------
# FIXED CORE TASKBAR SETUP 
# -------------------------------------------------------------
taskbar = tk.Frame(root, bg="#0F172A", height=50)
taskbar.pack(side="bottom", fill="x")

tray_bar = tk.Frame(taskbar, bg="#0F172A")
tray_bar.pack(anchor="center", pady=4)

# Centered Pinned Shortcuts mimicking Windows 11 style alignments
tk.Button(tray_bar, text="❖", fg="#38BDF8", bg="#1E293B", activebackground="#334155", font=("Segoe UI", 14), bd=0, padx=14, command=toggle_hsk_start).pack(side="left", padx=4)
tk.Button(tray_bar, text="🌐", fg="white", bg="#0F172A", activebackground="#1E293B", font=("Segoe UI", 12), bd=0, padx=12, command=launch_hsk_browser).pack(side="left", padx=2)
