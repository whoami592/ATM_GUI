import tkinter as tk
from tkinter import messagebox

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("400x500")
        self.users = {
            "03409777222": {"pin": "5678", "balance": 10000}
        }
        self.current_user = None

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to ATM", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Account Number").pack()
        self.acc_entry = tk.Entry(self.root)
        self.acc_entry.pack(pady=5)
        tk.Label(self.root, text="PIN").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.validate_login).pack(pady=20)

    def validate_login(self):
        acc = self.acc_entry.get()
        pin = self.pin_entry.get()
        if acc in self.users and self.users[acc]["pin"] == pin:
            self.current_user = acc
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN")

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="ATM Menu", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).pack(pady=10)
        tk.Button(self.root, text="Deposit", command=self.create_deposit_screen).pack(pady=10)
        tk.Button(self.root, text="Withdraw", command=self.create_withdraw_screen).pack(pady=10)
        tk.Button(self.root, text="Change PIN", command=self.create_pin_change_screen).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack(pady=10)

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        messagebox.showinfo("Balance", f"Your balance is: ${balance:.2f}")

    def create_deposit_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Deposit Amount", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Enter amount").pack()
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack(pady=5)
        tk.Button(self.root, text="Confirm", command=self.process_deposit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def process_deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount > 0:
                self.users[self.current_user]["balance"] += amount
                messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "Amount must be positive")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def create_withdraw_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Withdraw Amount", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Enter amount").pack()
        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack(pady=5)
        tk.Button(self.root, text="Confirm", command=self.process_withdrawal).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def process_withdrawal(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount > 0:
                if amount <= self.users[self.current_user]["balance"]:
                    self.users[self.current_user]["balance"] -= amount
                    messagebox.showinfo("Success", f"Withdrawn ${amount:.2f}")
                    self.create_main_menu()
                else:
                    messagebox.showerror("Error", "Insufficient balance")
            else:
                messagebox.showerror("Error", "Amount must be positive")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def create_pin_change_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Change PIN", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="New PIN").pack()
        self.new_pin_entry = tk.Entry(self.root, show="*")
        self.new_pin_entry.pack(pady=5)
        tk.Button(self.root, text="Confirm", command=self.process_pin_change).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def process_pin_change(self):
        new_pin = self.new_pin_entry.get()
        if len(new_pin) == 4 and new_pin.isdigit():
            self.users[self.current_user]["pin"] = new_pin
            messagebox.showinfo("Success", "PIN changed successfully")
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "PIN must be a 4-digit number")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()