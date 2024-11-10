# CLOUD-NATIVE-AI-PROJECT-COMPANYASH

A GUI-based company employee management system for a domain like SRMIST developed with Python's Tkinter library, providing role-based access control for Admin and User roles. Admins have privileges to view and manage employee data, while regular users can only view their own details. The system ensures secure account creation with email verification for SRMIST-affiliated accounts.

## Features

- **Login Authentication**: Secure login with role-based access control.
- **Account Creation with Email Verification**: Create accounts only for SRMIST-affiliated emails, with additional verification for admin roles.
- **User Details Management**: Add and view personal details (DOB, department, location) for each user.
- **Admin Dashboard**: View and manage details of all users with admin privileges.
- **Interactive UI**: User-friendly GUI with responsive button hover effects and custom background.

## Prerequisites

- Python 3.x
- `tkinter` (usually pre-installed with Python)
- `PIL` (Pillow) for image processing
- SQLite3 (comes with Python)
- `smtplib` for email verification

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/EmployeeManagementSystem.git
   cd EmployeeManagementSystem
   ```

2. Install dependencies:
   ```bash
   pip install pillow
   ```

3. Set up the SQLite database:
   - Open the SQLite shell and create the required tables for users and employee data, or run a SQL script (if provided).

## Usage

1. Run the `EmployeeManagementSystem.py` file:
   ```bash
   python EmployeeManagementSystem.py
   ```

2. **Login**: Enter your credentials. Admin users will have additional privileges.
3. **Create Account**: 
   - Enter an SRMIST-affiliated email (`@srmist.edu.in`).
   - Choose your role:
      - **Admin**: Additional email verification required (email must not contain numbers).
      - **User**: Proceed without email verification.
4. **Add/View Details**: Enter details like DOB, department, and location. Admins can view all users' details.

## Code Overview

### Function Descriptions

- **`login()`**: Authenticates user credentials and grants access based on role.
- **`set_background()`**: Sets a customized background for the GUI.
- **`on_hover()` & `on_leave()`**: Changes button color on hover for improved user experience.
- **`add_details()`**: Opens a form for entering personal details.
- **`save_details()`**: Saves the entered personal details to the database.
- **`view_details()`**: Displays the logged-in user's details.
- **`view_user_details()`**: Allows admins to view details of all users.
- **`create_account()`**: Initiates the account creation process with email validation.
- **`check_email()`**: Validates SRMIST email format before account creation.
- **`open_role_selection()`**: Displays role options for account creation.
- **`open_email_verification()`**: Sends a verification code for admin role creation.
- **`send_verification_email()`**: Sends an email with a unique code for admin verification.
- **`verify_code()`**: Confirms the verification code for admin access.


## Notes

- **Email Requirements**: Admin emails must not contain numbers and must end with `@srmist.edu.in`.
- **Email Verification**: Admin accounts require code verification via email.

