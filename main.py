import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
import mysql.connector
import bcrypt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class RoleBasedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        

        self.root.geometry("1920x1080")
        self.set_background(self.root, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")  
        

        self.font = ("Arial", 14)  
        self.button_font = ("Arial", 16, "bold")  
        self.bg_color = "#4CAF50"
        self.fg_color = "#ffffff"
        self.entry_bg = "#f4f4f9"  
        self.button_hover_color = "#45a049"  
        self.button_active_color = "#3e8e41"  

        self.username_label = tk.Label(self.root, text="Username", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        
        self.username_entry = tk.Entry(self.root, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        
        self.password_label = tk.Label(self.root, text="Password", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.password_label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.password_entry = tk.Entry(self.root, show="*", font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")
        

        self.login_button = tk.Button(self.root, text="Login", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.login, relief="solid", width=20, height=2, bd=5, borderwidth=4)
        self.login_button.place(relx=0.5, rely=0.7, anchor="center")
        self.login_button.bind("<Enter>", self.on_hover)
        self.login_button.bind("<Leave>", self.on_leave)


        self.create_account_button = tk.Button(self.root, text="Create Account", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.create_account, relief="solid", width=20, height=2, bd=5, borderwidth=4)
        self.create_account_button.place(relx=0.5, rely=0.8, anchor="center")
        self.create_account_button.bind("<Enter>", self.on_hover)
        self.create_account_button.bind("<Leave>", self.on_leave)

    def set_background(self, parent, image_path):
        """Set background image with reduced opacity."""
        image = Image.open(image_path)
        image = image.resize((1920, 1080))  
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(0.7)  
        background_image = ImageTk.PhotoImage(image)
        
        label = tk.Label(parent, image=background_image)
        label.image = background_image  
        label.place(relwidth=1, relheight=1)  

    def on_hover(self, event):
        """Change the button color when the mouse hovers over it."""
        event.widget.config(bg=self.button_hover_color) 

    def on_leave(self, event):
        """Restore the button color when the mouse leaves."""
        event.widget.config(bg=self.bg_color)  

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        
        conn = mysql.connector.connect(user='root', password='1234', database='CompanyASH')
        cursor = conn.cursor()

        
        cursor.execute("SELECT username, password, role FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result is not None:
            db_username, db_password, role = result

            
            if bcrypt.checkpw(password.encode(), db_password.encode()):
             
                main_page = tk.Toplevel(self.root)
                main_page.geometry("1920x1080")
                self.set_background(main_page, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")

                welcome_message = f"Hello {db_username}, welcome to CompanyASH.\n"
                if role == "admin":
                    welcome_message += "You can view all your details here and other users' details as well."
                else:
                    welcome_message += "You can view all your details here."

                welcome_label = tk.Label(main_page, text=welcome_message, font=self.font, bg=self.bg_color, fg=self.fg_color)
                welcome_label.place(relx=0.5, rely=0.1, anchor="center")

                
                add_details_button = tk.Button(main_page, text="Add Your Details", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.add_details, relief="solid", width=20, height=2, bd=5, borderwidth=4)
                add_details_button.place(relx=0.3, rely=0.2, anchor="center")

                
                view_details_button = tk.Button(main_page, text="View Your Details", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.view_details, relief="solid", width=20, height=2, bd=5, borderwidth=4)
                view_details_button.place(relx=0.7, rely=0.2, anchor="center")

                
                if role == "admin":
                    view_user_details_button = tk.Button(main_page, text="View Details of Users", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.view_user_details, relief="solid", width=20, height=2, bd=5, borderwidth=4)
                    view_user_details_button.place(relx=0.5, rely=0.3, anchor="center")

                messagebox.showinfo("Login Success", f"Welcome, {db_username}!")
            else:
                messagebox.showerror("Error", "Incorrect password.")
        else:
            messagebox.showerror("Error", "Username not found.")

        cursor.close()
        conn.close()

    def add_details(self):
        
        details_window = tk.Toplevel(self.root)
        details_window.title("Add Your Details")
        details_window.geometry("1920x1080")
        self.set_background(details_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")

        
        self.dob_label = tk.Label(details_window, text="Date of Birth (YYYY-MM-DD):", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.dob_label.place(relx=0.5, rely=0.3, anchor="center")
        self.dob_entry = tk.Entry(details_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.dob_entry.place(relx=0.5, rely=0.35, anchor="center")

        self.department_label = tk.Label(details_window, text="Department:", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.department_label.place(relx=0.5, rely=0.4, anchor="center")
        self.department_entry = tk.Entry(details_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.department_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.location_label = tk.Label(details_window, text="Location:", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.location_label.place(relx=0.5, rely=0.5, anchor="center")
        self.location_entry = tk.Entry(details_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.location_entry.place(relx=0.5, rely=0.55, anchor="center")

        
        save_button = tk.Button(details_window, text="Save Details", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.save_details, relief="solid", width=20, height=2, bd=5, borderwidth=4)
        save_button.place(relx=0.5, rely=0.65, anchor="center")

    def save_details(self):
        
        dob = self.dob_entry.get()
        department = self.department_entry.get()
        location = self.location_entry.get()
        username = self.username_entry.get()  

        
        conn = mysql.connector.connect(user='root', password='1234', database='CompanyASH')
        cursor = conn.cursor()

        
        cursor.execute("INSERT INTO employee_data (name, dob, department, location) VALUES (%s, %s, %s, %s)", (username, dob, department, location))
        conn.commit()

        messagebox.showinfo("Success", "Your details have been saved.")
        
        cursor.close()
        conn.close()

    def view_details(self):
        
        view_window = tk.Toplevel(self.root)
        view_window.title("View Your Details")
        view_window.geometry("1920x1080")
        self.set_background(view_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")

        
        username = self.username_entry.get()  
        conn = mysql.connector.connect(user='root', password='1234', database='CompanyASH')
        cursor = conn.cursor()
        cursor.execute("SELECT dob, department, location FROM employee_data WHERE name = %s", (username,))
        result = cursor.fetchone()

        if result:
            dob, department, location = result
            details_message = f"Your Details:\nDOB: {dob}\nDepartment: {department}\nLocation: {location}"
            details_label = tk.Label(view_window, text=details_message, font=self.font, bg=self.bg_color, fg=self.fg_color)
            details_label.place(relx=0.5, rely=0.3, anchor="center")
        else:
            messagebox.showerror("Error", "No details found for this user.")

        cursor.close()
        conn.close()

    def view_user_details(self):
        
        user_view_window = tk.Toplevel(self.root)
        user_view_window.title("View Details of Users")
        user_view_window.geometry("1920x1080")
        self.set_background(user_view_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")

        
        conn = mysql.connector.connect(user='root', password='1234', database='CompanyASH')
        cursor = conn.cursor()
        cursor.execute("SELECT users.username, users.role, employee_data.dob, employee_data.department, employee_data.location FROM users INNER JOIN employee_data ON users.username = employee_data.name")

        result = cursor.fetchall()

        if result:
            for i, row in enumerate(result):
                username, role, dob, department, location = row
                user_details = f"Username: {username}\nRole: {role}\nDOB: {dob}\nDepartment: {department}\nLocation: {location}"
                details_label = tk.Label(user_view_window, text=user_details, font=self.font, bg=self.bg_color, fg=self.fg_color)
                details_label.place(relx=0.5, rely=0.1 + (i * 0.2), anchor="center")
        else:
            messagebox.showerror("Error", "No user details found.")

        cursor.close()
        conn.close()



    def create_account(self):
        self.email_check_window = tk.Toplevel(self.root)
        self.email_check_window.title("Create Account")
        self.email_check_window.geometry("1920x1080")
        
        self.set_background(self.email_check_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")  # Set background image

        self.email_label = tk.Label(self.email_check_window, text="Enter Your Email", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.email_label.place(relx=0.5, rely=0.4, anchor="center")
        
        self.email_entry = tk.Entry(self.email_check_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.email_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.next_button = tk.Button(self.email_check_window, text="Next", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.check_email, relief="solid", width=20, height=2, bd=5, borderwidth=4)
        self.next_button.place(relx=0.5, rely=0.55, anchor="center")
        self.next_button.bind("<Enter>", self.on_hover)
        self.next_button.bind("<Leave>", self.on_leave)

    def check_email(self):
        email = self.email_entry.get()
        
        if email.endswith('srmist.edu.in'):
            self.open_role_selection()
        else:
            messagebox.showerror("Error", "Invalid email domain. Please use '@srmist.edu.in'.")

    def open_role_selection(self):
        self.role_window = tk.Toplevel(self.email_check_window)
        self.role_window.title("Select Role")
        self.role_window.geometry("1920x1080")
        
        self.set_background(self.role_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")  # Set background image for role selection tab
        

        self.role_label = tk.Label(self.role_window, text="Select Role", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.role_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.role_var = tk.StringVar(value="user")
        
        self.admin_rb = tk.Radiobutton(self.role_window, text="Admin", variable=self.role_var, value="admin", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.admin_rb.place(relx=0.5, rely=0.3, anchor="center")
        
        self.user_rb = tk.Radiobutton(self.role_window, text="User", variable=self.role_var, value="user", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.user_rb.place(relx=0.5, rely=0.4, anchor="center")
        
        tk.Button(self.role_window, text="Next", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.open_email_verification, relief="solid", width=20, height=2, bd=5, borderwidth=4).place(relx=0.5, rely=0.5, anchor="center")

    def open_email_verification(self):
        role = self.role_var.get()
        email = self.email_entry.get()  
        
        if role == "admin":
            self.verification_code = random.randint(100000, 999999)
            self.send_verification_email(email, self.verification_code)

            self.verification_label = tk.Label(self.role_window, text="Enter Verification Code", font=self.font, bg=self.bg_color, fg=self.fg_color)
            self.verification_label.place(relx=0.5, rely=0.65, anchor="center")
            
            self.verification_entry = tk.Entry(self.role_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
            self.verification_entry.place(relx=0.5, rely=0.7, anchor="center")
            
            self.verify_button = tk.Button(self.role_window, text="Verify", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.verify_code, relief="solid", width=20, height=2, bd=5, borderwidth=4)
            self.verify_button.place(relx=0.5, rely=0.75, anchor="center")
        
        else:
            self.open_account_creation()

    def send_verification_email(self, email, code):
        from_email = 'ashwin2635@gmail.com'
        from_password = 'tirc mtjo kqdu aqvf'  

        subject = 'Admin Account Verification'
        text_content = f'Your verification code is: {code}'
        html_content = f'<h3>Your verification code is: {code}</h3>'
        

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = from_email
        message["To"] = email
        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        message.attach(part1)
        message.attach(part2)
        
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(from_email, from_password)
                server.sendmail(from_email, email, message.as_string())
            
            messagebox.showinfo("Success", "Verification code sent successfully to your email.")
            self.prompt_for_verification_code()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send verification email: {e}")

    def prompt_for_verification_code(self):
        # Display fields for entering the verification code after confirming email sent
        self.verification_label = tk.Label(self.role_window, text="Enter Verification Code", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.verification_label.place(relx=0.5, rely=0.65, anchor="center")
        
        self.verification_entry = tk.Entry(self.role_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.verification_entry.place(relx=0.5, rely=0.7, anchor="center")
        
        self.verify_button = tk.Button(self.role_window, text="Verify", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.verify_code, relief="solid", width=20, height=2, bd=5, borderwidth=4)
        self.verify_button.place(relx=0.5, rely=0.75, anchor="center")


    def verify_code(self):
        input_code = self.verification_entry.get()
        
        if input_code == str(self.verification_code):
            self.open_account_creation()
        else:
            messagebox.showerror("Error", "Incorrect verification code. Please try again.")

    def open_account_creation(self):
        self.account_creation_window = tk.Toplevel(self.root)
        self.account_creation_window.title("Create Account")
        self.account_creation_window.geometry("1920x1080")
        self.set_background(self.account_creation_window, "D:/Projects/CLOUD NATIVE AI/COMPANY SETUP/cl1.jpg")  # Set background image
        

        self.username_label = tk.Label(self.account_creation_window, text="Username", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        
        self.username_entry = tk.Entry(self.account_creation_window, font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        
        self.password_label = tk.Label(self.account_creation_window, text="Password", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.password_label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.password_entry = tk.Entry(self.account_creation_window, show="*", font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")
        
        self.confirm_password_label = tk.Label(self.account_creation_window, text="Confirm Password", font=self.font, bg=self.bg_color, fg=self.fg_color)
        self.confirm_password_label.place(relx=0.5, rely=0.6, anchor="center")
        
        self.confirm_password_entry = tk.Entry(self.account_creation_window, show="*", font=self.font, bd=2, relief="solid", width=30, bg=self.entry_bg, fg=self.bg_color)
        self.confirm_password_entry.place(relx=0.5, rely=0.65, anchor="center")

        self.role = self.role_var.get() 

        tk.Button(self.account_creation_window, text="Create Account", font=self.button_font, bg=self.bg_color, fg=self.fg_color, command=self.create_account_function, relief="solid", width=20, height=2, bd=5, borderwidth=4).place(relx=0.5, rely=0.75, anchor="center")

    def create_account_function(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        role = self.role  

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        conn = mysql.connector.connect(user='root', password='1234', database='CompanyASH')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (username, password, role, is_verified) VALUES (%s, %s, %s, %s)", 
                    (username, hashed_password, role, 1))  
        conn.commit()
        
        cursor.close()
        conn.close()
        
        messagebox.showinfo("Success", "Account created successfully")
        self.account_creation_window.destroy()


root = tk.Tk()
app = RoleBasedApp(root)
root.mainloop()
