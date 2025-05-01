
import tkinter as tk
from tkinter import ttk, messagebox
from core.scanner_pro import scan_network, search_cve

def apply_dark_theme(style):
    style.theme_use("clam")
    style.configure(".", background="#1e1e1e", foreground="#d4d4d4", fieldbackground="#2e2e2e")
    style.configure("TLabel", background="#1e1e1e", foreground="#d4d4d4")
    style.configure("TButton", background="#3a3a3a", foreground="#d4d4d4")
    style.configure("TEntry", fieldbackground="#2e2e2e", foreground="#d4d4d4")
    style.configure("TFrame", background="#1e1e1e")
    style.configure("TNotebook", background="#1e1e1e")

def start_gui():
    root = tk.Tk()
    root.title("VulnScanner Pro")
    root.geometry("900x600")
    root.configure(bg="#1e1e1e")

    style = ttk.Style(root)
    apply_dark_theme(style)

    title = ttk.Label(root, text="VulnScanner Pro", font=("Segoe UI", 20, "bold"))
    title.pack(pady=10)

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="x")

    ip_label = ttk.Label(frame, text="IP Subnet (e.g., 192.168.1):")
    ip_label.grid(row=0, column=0, sticky="w")
    ip_entry = ttk.Entry(frame, width=30)
    ip_entry.grid(row=0, column=1, padx=5)

    cve_label = ttk.Label(frame, text="CVE Keyword (e.g., Apache):")
    cve_label.grid(row=1, column=0, sticky="w", pady=5)
    cve_entry = ttk.Entry(frame, width=30)
    cve_entry.grid(row=1, column=1, padx=5)

    text_output = tk.Text(root, bg="#252526", fg="#d4d4d4", insertbackground='white', font=("Consolas", 10))
    text_output.pack(expand=True, fill="both", padx=10, pady=10)

    status_var = tk.StringVar()
    status_bar = ttk.Label(root, textvariable=status_var, anchor="w")
    status_bar.pack(fill="x")

    def on_scan():
        subnet = ip_entry.get().strip()
        if not subnet:
            messagebox.showerror("Input Error", "Enter a valid subnet.")
            return
        status_var.set("Scanning network...")
        root.update_idletasks()
        results = scan_network(subnet)
        text_output.delete("1.0", tk.END)
        for res in results:
            text_output.insert(tk.END, f"{res}
")
        status_var.set("Network scan complete.")

    def on_search_cve():
        keyword = cve_entry.get().strip()
        if not keyword:
            messagebox.showerror("Input Error", "Enter a keyword.")
            return
        status_var.set("Fetching CVE data...")
        root.update_idletasks()
        results = search_cve(keyword)
        text_output.insert(tk.END, f"
--- CVE Results for '{keyword}' ---
")
        if "results" in results:
            for cve_id, desc, solution in results["results"]:
                text_output.insert(tk.END, f"{cve_id}: {desc}
Solution: {solution}

")
        elif "error" in results:
            text_output.insert(tk.END, f"Error: {results['error']}
")
        else:
            text_output.insert(tk.END, "No data found.
")
        status_var.set("CVE search complete.")

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=5)

    scan_btn = ttk.Button(btn_frame, text="Scan Network", command=on_scan)
    scan_btn.grid(row=0, column=0, padx=10)

    cve_btn = ttk.Button(btn_frame, text="Search CVE", command=on_search_cve)
    cve_btn.grid(row=0, column=1, padx=10)

    root.mainloop()
