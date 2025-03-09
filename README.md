**📚 Library Management System**

🔍 Overview
The Library Management System is a Python-based application that helps manage books, users, and borrow/return transactions efficiently. It uses Pandas for data management and PySimpleGUI for a user-friendly interface.

🏗 Features
✔ User Management:

User registration and login
Change name or password
Identify user favorites based on borrowing history
✔ Book Management:

Add, search, and delete books
Search books by name, author, or topic
Track borrowed and returned books
✔ Borrow & Return System:

Borrow books with automatic due date calculation
Return books and update availability
Notify users of overdue books
✔ Admin Dashboard:

View all borrowed books
Generate reports on popular books and overdue returns
Manage users and books
🛠 Technologies Used
Python
Pandas (for data handling)
PySimpleGUI (for GUI)
Excel Files (for storing data)
📁 Project Structure
bash
Copy
Edit
📂 LibraryManagementSystem  
 ├── 📄 userClass.py   # Handles user data and authentication  
 ├── 📄 bockClass.py   # Manages book inventory and operations  
 ├── 📄 UI.py          # Implements the graphical user interface  
 ├── 📂 Data  
 │   ├── user.xlsx     # Stores user information  
 │   ├── book.xlsx     # Stores book inventory  
 │   ├── deposit.xlsx  # Tracks borrow/return transactions  
🚀 Installation & Usage
1️⃣ Install Dependencies
Make sure you have Python 3.x installed, then install the required libraries:

sh
Copy
Edit
pip install pandas openpyxl PySimpleGUI
2️⃣ Run the Application
sh
Copy
Edit
python UI.py
3️⃣ Login or Sign Up
If you don’t have an account, sign up.
Admin users have additional privileges to manage books and users.
🏆 Future Improvements
Add a database (SQLite or MySQL) instead of Excel
Implement email notifications for overdue books
Enhance the search and filtering system
