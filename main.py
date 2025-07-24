from user import User, Admin
def login_admin():
	password = input("Enter admin password")
	admin = Admin()
	return admin.admin_login(password)
def admin_add():
	name = input("Enter user name")
	pin = input("Enter user secret pin")
	role = input("Enter user role")
	admin.add_user(name, pin, role)
def admin_unlock():
	name = input("Enter locked user name")
	admin.unlock_user(name)
def register_user():
	name = input("Enter your name")
	role = input('Enter your role')
	pin = input("Enter your four digit pin")
	result = user.User.verify_pin(name, role, pin)
	if not result:
		print("Invalid pin enter exactly four digit pin that follow our standards")
		return 
	print("Pin is valid registration processing ")
	new_user = user.User(name, role, pin)
	new_user.register()
def login():
		name = input("Enter your name")
		pin = input("Enter your pin")
		role = input("Enter your role")
		result = user.User.check_lock(name, pin, role)
		if not result:
			print("You are among the locked users list login failed")
			return
			
		trials = 3
		while trials > 0:
		    login_result = user.User.login(name, pin, role)
		    if not login_result:
		      trials -= 1
		      if trials == 0:
		          print("Login failed trials used up")
		          user.User.lock_user(name, pin, role)
		          return
		      else:
		           print(f"Login failed {trials} trials left")
		           pin = input("Enter a valid pin now")
		    else:
		        print("Login succesfully")
		        return 
		        
		print("Login failed trials used up contact admin for solution")
		          


while True:
    print("Welcome to Multiuser platform")
    print("How may we help you")
    print("Are you an user or an admin")
    choice = input("Enter who you are")
    
    if choice.lower() == "exit":
        print("Goodbye")
        break
    elif choice.lower() == "admin":
                      if login_admin():
                          print("Woiyou like to add user or unlock user")
                          help = input("what would you like to do")
                          if help.lower() == "add":
                              admin_add()
                          elif help.lower() == "unlock":
                              admin_unlock()
                          else:
                              print("invalid option")
    elif choice.lower() == "user":
          print("Hey user how may we help you")
          print("Do you want to register or login")
          choose = input("Let us know how we can help you")
          if choose.lower() == "register":
              register_user()
          elif choose.lower() == "login":
              login()
          else:
              print("invalid option")
    else:
        print("invalid option")
		
	
	