#****************************************************************************************************
#
#       Name:         Kyle McColgan
#       File name:    passwordGen.py
#       Date:         15 November 2024
#       Description:
#               This program provides a GUI based client to generate URL-friendly passwords.
#
#****************************************************************************************************

import tkinter as tk
from tkinter import messagebox, scrolledtext
import secrets
import base64

#****************************************************************************************************

class MainGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Secure Password Generator')
        self.main_window.geometry("400x300")

        # Frames for layout
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Password display
        self.result_label = tk.Label(self.top_frame, text='Generated Password:')
        self.result_label.config(fg="Green")
        self.result_text = scrolledtext.ScrolledText(self.top_frame, wrap=tk.WORD, width=40, height=3, state='disabled')

        # Password length input
        self.length_label = tk.Label(self.mid_frame, text='Password Length:')
        self.length_entry = tk.Entry(self.mid_frame, width=5)
        self.length_entry.insert(0, "64")  # Default length to 64 for strong security

        # Buttons
        self.generate_button = tk.Button(self.mid_frame, text='Generate', relief="ridge", command=self.generate_password)
        self.copy_button = tk.Button(self.bottom_frame, text='Copy', relief="ridge", command=self.copy_to_clipboard)
        self.save_button = tk.Button(self.bottom_frame, text='Save', relief="ridge", command=self.save_to_file)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', relief="ridge", command=self.main_window.quit)
        self.quit_button.config(fg="Red")

        # Pack widgets
        self.result_label.pack(side='top', pady=5)
        self.result_text.pack(side='top', padx=5, pady=5)

        self.length_label.pack(side='left', padx=5)
        self.length_entry.pack(side='left', padx=5)
        self.generate_button.pack(side='left', padx=5)

        self.copy_button.pack(side='left', padx=5)
        self.save_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        self.top_frame.pack(pady=10)
        self.mid_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)

        tk.mainloop()

    def generate_password(self):
        # Retrieve the desired password length
        try:
            length = int(self.length_entry.get())
            if length < 8 or length > 512:
                messagebox.showwarning("Warning", "Password length should be between 8 and 512 characters.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        # Generate password
        # Generate enough random bytes for the desired length
        bytes_needed = (length * 6 + 7) // 8  # Calculating required bytes for Base64 output
        random_bytes = secrets.token_bytes(bytes_needed)
        password = base64.b64encode(random_bytes).decode('utf-8')[:length]

        # Display password in text widget
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, password)
        self.result_text.config(state='disabled')

    def copy_to_clipboard(self):
        password = self.result_text.get(1.0, tk.END).strip()
        if password:
            self.main_window.clipboard_clear()
            self.main_window.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

    def save_to_file(self):
        password = self.result_text.get(1.0, tk.END).strip()
        if password:
            with open("generated_password.txt", "w") as file:
                file.write(password)
            messagebox.showinfo("Saved", "Password saved to generated_password.txt")
        else:
            messagebox.showwarning("Warning", "No password to save.")

#****************************************************************************************************

if __name__ == '__main__':
    main_gui = MainGUI()
#****************************************************************************************************