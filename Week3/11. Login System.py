def newusers():
    name = input('Enter your name')
def oldusers():
    pass

def login():
    result = None
    option = """
            (N)ew User Login 
            (O)ld User Login
            (E)xit """
    login_option = input(option).lower()
    if login_option == 'n':
        result = newusers()
    elif login_option == 'o':
        result = oldusers()
    elif login_option == 'e':
        print("Bye!")
    return result
if __name__ == "__main__":
    user_data = {}
    while True:
        login()