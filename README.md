🔐 Multi-Tier Secure Access Manager

This is a secure multi-user access system built in Python. It simulates login validation for users with different access levels and enforces strict password rules for security.

💡 Features

- Role-based users (Admin, Editor, Viewer)
- 4-digit password with six security rules:
  - All digits must be unique
  - Not a palindrome
  - First + last digit = second + third digit
  - Sum divisible by 3
  - No two consecutive even digits
- 3 login attempts before user lockout
- Admin features:
  - View all users
  - Unlock locked users
  - Add new users

📁 File Structure

- `main.py`: App entry point (user/admin interface)
- `user.py`: Core logic for User and Admin handling
- `Secret Users/`: Stores registered user data
- `Locked Users/`: Stores locked out users

🧠 Skills Practiced

- File I/O with JSON
- Object-Oriented Programming
- Error Handling
- Input Validation
- Modular Code Design


📌 This project demonstrates practical real-world user authentication systems with clear validation logic and secure access control.
