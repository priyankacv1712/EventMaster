import tkinter as tk
from ui.screens import DashboardScreen, LoginScreen


class UIFlow:
    def __init__(self, system):
        self.system = system
        self.current_user = None

    def start(self):
        root = tk.Tk()
        root.state('zoomed')  # Full window
        root.title("EventMaster - Sports Mega Event Tracker")

        # Start with login screen
        LoginScreen(root, self.system, self.on_login_success)

        root.mainloop()

    def on_login_success(self, user_info):
        # Called when login succeeds
        self.current_user = user_info
        # Clear all widgets from root and load dashboard
        for widget in user_info["root"].winfo_children():
            widget.destroy()

        DashboardScreen(user_info["root"], self.system, self.current_user)
