def sign_up():
    user_login = input("enter a user name: ")
    user_login = input("create a password: ")
    return user_login

def sign_in():
    user_login  = input("enter your username: ")
    user_login  = input("enter your password: ")
    return user_login

def main():
    orignal_login = sign_up()
    attempt_login = sign_in()

    if orignal_login == attempt_login:
        print("login sucessfull ")
    else:
        print("login failed! username or password does not match")
 

main()
  