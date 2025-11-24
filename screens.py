import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Optional QR dependency – used only if installed
try:
    import qrcode
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False


# ---------------- LOGIN SCREEN ----------------

class LoginScreen:
    """
    Simple login with demo accounts:
      Admin:       admin@sport.com / Admin@123
      Coordinator: coord@sport.com / Coord@123
      Staff:       staff@sport.com / Staff@123
    """

    DEMO_USERS = {
        "admin@sport.com": {
            "password": "Admin@123",
            "role": "Admin",
            "name": "Rohit Malhotra"
        },
        "coord@sport.com": {
            "password": "Coord@123",
            "role": "Coordinator",
            "name": "Sana Kapoor"
        },
        "staff@sport.com": {
            "password": "Staff@123",
            "role": "Staff",
            "name": "Vikram Rao"
        }
    }

    def __init__(self, root, system, login_callback):
        self.root = root
        self.system = system
        self.login_callback = login_callback

        self.root.configure(bg="#2C3E50")

        frame = tk.Frame(root, bg="#2C3E50")
        frame.pack(expand=True)

        title = tk.Label(frame,
                         text="EventMaster",
                         font=("Segoe UI", 28, "bold"),
                         bg="#2C3E50",
                         fg="#ECF0F1")
        title.pack(pady=10)

        tagline = tk.Label(frame,
                           text="Track. Prepare. Win.",
                           font=("Segoe UI", 12),
                           bg="#2C3E50",
                           fg="#ECF0F1")
        tagline.pack(pady=5)

        form = tk.Frame(frame, bg="#2C3E50")
        form.pack(pady=20)

        tk.Label(form, text="Email:", bg="#2C3E50", fg="#ECF0F1").grid(row=0, column=0, sticky="e", pady=5, padx=5)
        tk.Label(form, text="Password:", bg="#2C3E50", fg="#ECF0F1").grid(row=1, column=0, sticky="e", pady=5, padx=5)

        self.email_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        tk.Entry(form, textvariable=self.email_var, width=30).grid(row=0, column=1, pady=5)
        tk.Entry(form, textvariable=self.pass_var, show="*", width=30).grid(row=1, column=1, pady=5)

        login_btn = tk.Button(form,
                              text="Login",
                              width=20,
                              bg="#3498DB",
                              fg="white",
                              command=self.try_login)
        login_btn.grid(row=2, column=0, columnspan=2, pady=15)

        info = tk.Label(frame,
                        text="Demo:\nadmin@sport.com / Admin@123\ncoord@sport.com / Coord@123\nstaff@sport.com / Staff@123",
                        bg="#2C3E50",
                        fg="#BDC3C7",
                        font=("Segoe UI", 9))
        info.pack(pady=5)

    def try_login(self):
        email = self.email_var.get().strip()
        password = self.pass_var.get().strip()

        user = self.DEMO_USERS.get(email)
        if not user or user["password"] != password:
            messagebox.showerror("Login Failed", "Invalid email or password.")
            return

        messagebox.showinfo("Welcome", f"Logged in as {user['role']} - {user['name']}")

        user_info = {
            "email": email,
            "role": user["role"],
            "name": user["name"],
            "root": self.root
        }

        self.login_callback(user_info)


# ---------------- DASHBOARD & SCREENS ----------------

class DashboardScreen:
    def __init__(self, master, system, current_user):
        self.master = master
        self.system = system
        self.current_user = current_user

        # ----- Layout: Sidebar + Main Content -----
        self.sidebar = tk.Frame(self.master, width=200, bg="#2C3E50")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.content = tk.Frame(self.master, bg="#ECF0F1")
        self.content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ----- Sidebar Header -----
        tk.Label(self.sidebar,
                 text="EventMaster",
                 bg="#2C3E50",
                 fg="#ECF0F1",
                 font=("Segoe UI", 16, "bold")).pack(pady=10)

        tk.Label(self.sidebar,
                 text=self.current_user["role"],
                 bg="#2C3E50",
                 fg="#BDC3C7",
                 font=("Segoe UI", 10)).pack(pady=2)

        # ----- Sidebar Buttons -----
        tk.Button(self.sidebar, text="Dashboard", width=20,
                  bg="#34495E", fg="white",
                  command=self.show_dashboard).pack(pady=5)

        tk.Button(self.sidebar, text="Venues", width=20,
                  bg="#34495E", fg="white",
                  command=self.show_venues).pack(pady=5)

        tk.Button(self.sidebar, text="Volunteers", width=20,
                  bg="#34495E", fg="white",
                  command=self.show_volunteers).pack(pady=5)

        tk.Button(self.sidebar, text="Events", width=20,
                  bg="#34495E", fg="white",
                  command=self.show_events).pack(pady=5)

        tk.Button(self.sidebar, text="Reports", width=20,
                  bg="#34495E", fg="white",
                  command=self.show_reports).pack(pady=5)

        # ----- Start with dashboard -----
        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # --------- DASHBOARD ----------

    def show_dashboard(self):
        self.clear_content()
        tk.Label(self.content, text="Dashboard",
                 font=("Segoe UI", 22, "bold"), bg="#ECF0F1").pack(pady=20)

        welcome = tk.Label(self.content,
                           text=f"Welcome, {self.current_user['name']}  ({self.current_user['role']})",
                           bg="#ECF0F1",
                           font=("Segoe UI", 12))
        welcome.pack(pady=5)

        tagline = tk.Label(self.content,
                           text="Track. Prepare. Win.",
                           bg="#ECF0F1",
                           fg="#7F8C8D",
                           font=("Segoe UI", 11, "italic"))
        tagline.pack(pady=5)

        info_frame = tk.Frame(self.content, bg="#ECF0F1")
        info_frame.pack(pady=20)

        venues_count = len(self.system.get_all_venues())
        events_count = len(self.system.get_all_events())
        volunteers_count = len(self.system.get_all_volunteers())

        tk.Label(info_frame, text=f"Total Venues: {venues_count}", bg="#ECF0F1",
                 font=("Segoe UI", 11)).pack(anchor="w")
        tk.Label(info_frame, text=f"Total Events: {events_count}", bg="#ECF0F1",
                 font=("Segoe UI", 11)).pack(anchor="w")
        tk.Label(info_frame, text=f"Total Volunteers: {volunteers_count}", bg="#ECF0F1",
                 font=("Segoe UI", 11)).pack(anchor="w")

    # --------- VENUES SCREEN ----------

    def show_venues(self):
        self.clear_content()
        tk.Label(self.content, text="Venue Manager",
                 font=("Segoe UI", 18, "bold"), bg="#ECF0F1").pack(pady=10)

        form_frame = tk.Frame(self.content, bg="#ECF0F1")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", bg="#ECF0F1").grid(row=0, column=0, sticky="e")
        tk.Label(form_frame, text="Location:", bg="#ECF0F1").grid(row=1, column=0, sticky="e")
        tk.Label(form_frame, text="Capacity:", bg="#ECF0F1").grid(row=2, column=0, sticky="e")
        tk.Label(form_frame, text="Status:", bg="#ECF0F1").grid(row=3, column=0, sticky="e")

        name_var = tk.StringVar()
        loc_var = tk.StringVar()
        cap_var = tk.StringVar()
        status_var = tk.StringVar(value="In Progress")

        tk.Entry(form_frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=5, pady=2)
        tk.Entry(form_frame, textvariable=loc_var, width=30).grid(row=1, column=1, padx=5, pady=2)
        tk.Entry(form_frame, textvariable=cap_var, width=30).grid(row=2, column=1, padx=5, pady=2)
        tk.Entry(form_frame, textvariable=status_var, width=30).grid(row=3, column=1, padx=5, pady=2)

        def add_venue_action():
            name = name_var.get().strip()
            loc = loc_var.get().strip()
            cap_str = cap_var.get().strip()
            status = status_var.get().strip() or "In Progress"

            if not name or not loc or not cap_str:
                messagebox.showerror("Error", "All fields are required.")
                return
            try:
                cap = int(cap_str)
            except ValueError:
                messagebox.showerror("Error", "Capacity must be a number.")
                return

            self.system.add_venue(name, loc, cap, status)
            messagebox.showinfo("Success", "Venue added!")
            self.refresh_venue_table()

        tk.Button(form_frame, text="Add Venue",
                  bg="#3498DB", fg="white",
                  command=add_venue_action).grid(
            row=4, column=0, columnspan=2, pady=10
        )

        # Table for venues
        table_frame = tk.Frame(self.content, bg="#ECF0F1")
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ("name", "location", "capacity", "status")
        self.venue_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.venue_table.heading(col, text=col.capitalize())
        self.venue_table.pack(fill=tk.BOTH, expand=True)

        self.refresh_venue_table()

    def refresh_venue_table(self):
        for row in self.venue_table.get_children():
            self.venue_table.delete(row)

        for v in self.system.get_all_venues():
            info = v.get_info()
            self.venue_table.insert("", tk.END, values=(
                info["name"], info["location"], info["capacity"], info["status"]
            ))

    # --------- VOLUNTEERS SCREEN ----------

    def show_volunteers(self):
        self.clear_content()
        tk.Label(self.content, text="Volunteer Hub",
                 font=("Segoe UI", 18, "bold"), bg="#ECF0F1").pack(pady=10)

        form_frame = tk.Frame(self.content, bg="#ECF0F1")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", bg="#ECF0F1").grid(row=0, column=0, sticky="e")
        tk.Label(form_frame, text="Role:", bg="#ECF0F1").grid(row=1, column=0, sticky="e")
        tk.Label(form_frame, text="Contact:", bg="#ECF0F1").grid(row=2, column=0, sticky="e")

        name_var = tk.StringVar()
        role_var = tk.StringVar()
        contact_var = tk.StringVar()

        tk.Entry(form_frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=5, pady=2)
        tk.Entry(form_frame, textvariable=role_var, width=30).grid(row=1, column=1, padx=5, pady=2)
        tk.Entry(form_frame, textvariable=contact_var, width=30).grid(row=2, column=1, padx=5, pady=2)

        def add_volunteer_action():
            name = name_var.get().strip()
            role = role_var.get().strip()
            contact = contact_var.get().strip()

            if not name or not role or not contact:
                messagebox.showerror("Error", "All fields are required.")
                return

            vol = self.system.add_volunteer(name, role, contact)
            info = vol.get_info()
            messagebox.showinfo("Success",
                                f"Volunteer added!\nID: {info['id']}\nName: {info['name']}")
            self.refresh_volunteer_table()

        tk.Button(form_frame, text="Add Volunteer",
                  bg="#3498DB", fg="white",
                  command=add_volunteer_action).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        # Table for volunteers
        table_frame = tk.Frame(self.content, bg="#ECF0F1")
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ("id", "name", "role", "contact")
        self.vol_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.vol_table.heading(col, text=col.upper())
        self.vol_table.pack(fill=tk.BOTH, expand=True)

        # QR Button
        qr_frame = tk.Frame(self.content, bg="#ECF0F1")
        qr_frame.pack(pady=5)

        tk.Button(qr_frame, text="Generate QR for Selected",
                  bg="#1ABC9C", fg="white",
                  command=self.generate_qr_for_selected).pack()

        self.refresh_volunteer_table()

    def refresh_volunteer_table(self):
        for row in self.vol_table.get_children():
            self.vol_table.delete(row)

        for v in self.system.get_all_volunteers():
            info = v.get_info()
            self.vol_table.insert("", tk.END, values=(
                info["id"], info["name"], info["role"], info["contact"]
            ))

    def generate_qr_for_selected(self):
        if not QR_AVAILABLE:
            messagebox.showerror("QR Error",
                                 "QR code library not installed.\nInstall with:\npip install qrcode")
            return

        selection = self.vol_table.selection()
        if not selection:
            messagebox.showerror("Error", "Select a volunteer in the table first.")
            return

        item = self.vol_table.item(selection[0])
        vid, name, role, contact = item["values"]

        data = f"ID: {vid}\nName: {name}\nRole: {role}\nContact: {contact}"
        img = qrcode.make(data)
        filename = f"qr_{vid}.png"
        img.save(filename)

        messagebox.showinfo("QR Generated",
                            f"QR code saved as {filename} in project folder.")

    # --------- EVENTS SCREEN ----------

    def show_events(self):
        self.clear_content()
        tk.Label(self.content, text="Event Manager",
                 font=("Segoe UI", 18, "bold"), bg="#ECF0F1").pack(pady=10)

        tk.Button(self.content, text="Add Event", width=25,
                  bg="#3498DB", fg="white",
                  command=self.add_event_dialog).pack(pady=5)
        tk.Button(self.content, text="Assign Volunteer to Event", width=25,
                  bg="#3498DB", fg="white",
                  command=self.assign_volunteer_dialog).pack(pady=5)
        tk.Button(self.content, text="Add Milestone to Event", width=25,
                  bg="#3498DB", fg="white",
                  command=self.add_milestone_dialog).pack(pady=5)
        tk.Button(self.content, text="Set Event Budget", width=25,
                  bg="#3498DB", fg="white",
                  command=self.set_budget_dialog).pack(pady=5)

    def add_event_dialog(self):
        if not self.system.get_all_venues():
            messagebox.showerror("Error", "Please add a venue first.")
            return

        name = simpledialog.askstring("Event", "Enter event name:", parent=self.master)
        if not name:
            return
        date = simpledialog.askstring("Event", "Enter event date (YYYY-MM-DD):", parent=self.master)
        if not date:
            return

        venue_name = simpledialog.askstring("Event", "Enter venue name to link:", parent=self.master)
        if not venue_name:
            return

        venue = None
        for v in self.system.get_all_venues():
            if v.get_info()["name"] == venue_name:
                venue = v
                break

        if not venue:
            messagebox.showerror("Error", f"No venue found with name '{venue_name}'.")
            return

        self.system.add_event(name, venue, date)
        messagebox.showinfo("Success", "Event added successfully!")

    def assign_volunteer_dialog(self):
        if not self.system.get_all_events():
            messagebox.showerror("Error", "No events found.")
            return
        if not self.system.get_all_volunteers():
            messagebox.showerror("Error", "No volunteers found.")
            return

        event_name = simpledialog.askstring("Assign", "Enter event name:", parent=self.master)
        if not event_name:
            return

        event = None
        for e in self.system.get_all_events():
            if e.get_info()["name"] == event_name:
                event = e
                break

        if not event:
            messagebox.showerror("Error", f"No event found with name '{event_name}'.")
            return

        volunteer_name = simpledialog.askstring("Assign", "Enter volunteer name:", parent=self.master)
        if not volunteer_name:
            return

        volunteer = None
        for v in self.system.get_all_volunteers():
            if v.get_info()["name"] == volunteer_name:
                volunteer = v
                break

        if not volunteer:
            messagebox.showerror("Error", f"No volunteer found with name '{volunteer_name}'.")
            return

        self.system.assign_volunteer_to_event(event, volunteer)
        messagebox.showinfo("Success", "Volunteer assigned.")

    def add_milestone_dialog(self):
        if not self.system.get_all_events():
            messagebox.showerror("Error", "No events found.")
            return

        event_name = simpledialog.askstring("Milestone", "Enter event name:", parent=self.master)
        if not event_name:
            return

        event = None
        for e in self.system.get_all_events():
            if e.get_info()["name"] == event_name:
                event = e
                break

        if not event:
            messagebox.showerror("Error", f"No event found with name '{event_name}'.")
            return

        title = simpledialog.askstring("Milestone", "Enter milestone title:", parent=self.master)
        if not title:
            return
        deadline = simpledialog.askstring("Milestone", "Enter deadline (YYYY-MM-DD):", parent=self.master)
        if not deadline:
            return

        self.system.add_milestone_to_event(event, title, deadline)
        messagebox.showinfo("Success", "Milestone added.")

    def set_budget_dialog(self):
        if not self.system.get_all_events():
            messagebox.showerror("Error", "No events found.")
            return

        event_name = simpledialog.askstring("Budget", "Enter event name:", parent=self.master)
        if not event_name:
            return

        event = None
        for e in self.system.get_all_events():
            if e.get_info()["name"] == event_name:
                event = e
                break

        if not event:
            messagebox.showerror("Error", f"No event found with name '{event_name}'.")
            return

        total_str = simpledialog.askstring("Budget", "Enter total budget:", parent=self.master)
        if not total_str:
            return
        try:
            total = int(total_str)
        except ValueError:
            messagebox.showerror("Error", "Budget must be a number.")
            return

        budget = self.system.set_event_budget(event, total)

        add_exp = messagebox.askyesno("Budget", "Add an initial expense?")
        if add_exp:
            exp_str = simpledialog.askstring("Expense", "Enter amount:", parent=self.master)
            if exp_str:
                try:
                    amt = int(exp_str)
                    budget.add_expense(amt)
                    self.system.save_events()
                except ValueError:
                    messagebox.showerror("Error", "Expense must be a number.")

        messagebox.showinfo("Success", "Budget updated.")

    # --------- REPORTS SCREEN ----------

    def show_reports(self):
        self.clear_content()
        tk.Label(self.content, text="Reports Center",
                 font=("Segoe UI", 18, "bold"), bg="#ECF0F1").pack(pady=10)

        tk.Button(self.content, text="Show Event Report",
                  width=25, bg="#3498DB", fg="white",
                  command=self.show_event_report).pack(pady=5)
        tk.Button(self.content, text="Show Budget Report",
                  width=25, bg="#3498DB", fg="white",
                  command=self.show_budget_report).pack(pady=5)

    def show_event_report(self):
        report = self.system.generate_event_report()
        if not report.strip():
            messagebox.showinfo("Event Report", "No events found.")
        else:
            messagebox.showinfo("Event Report", report)

    def show_budget_report(self):
        report = self.system.generate_budget_report()
        if not report.strip():
            messagebox.showinfo("Budget Report", "No budget data.")
        else:
            messagebox.showinfo("Budget Report", report)
