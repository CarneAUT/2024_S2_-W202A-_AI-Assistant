import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def initialize_app():
    cred = credentials.Certificate('firebase-sdk.json')

    firebase_admin.initialize_app(cred, {

        'databaseURL': 'https://ai-assistant-2a4b8-default-rtdb.asia-southeast1.firebasedatabase.app/'

    })

    return db.reference('/')

ref = initialize_app()

# ref.set({
#     'Registered': {
#         'username': 'name1',
#         'password': 'pass1',
#         'email': 'email1'
#     }
# })


def register_user(username, password, email):
    existing_users = ref.get()

    if existing_users:
        for user in existing_users.values():
            if user['username'] == username:
                return "Username already exists"
            if user['email'] == email:
                return "Email already registered"

    new_user = {
        'username': username,
        'email': email,
        'password': password
    }
    ref.push(new_user)
    return "User registered successfully"


def log_in(username, password):
    existing_users = ref.get()

    if existing_users:
        for user in existing_users.values():
            if user['username'] == username and user['password'] == password:
                return True
    return False


# if __name__ == '__main__':
#     ''' USER TEST 2 FAIL '''
    # # Fail: user1 does not exist
    # result = log_in("user1", "pass2")
    # print(f"Test 1: {result}")
    #
    # # Fail: user2's password is 'pass2'
    # result = log_in("user2", "pass1")
    # print(f"Test 2: {result}")


    # ''' USER TEST 2 PASS '''
    # # Pass:
    # result = log_in("user2", "pass2")
    # print(f"Test 1: {result}")

    # ''' USER TEST 1 FAIL '''
    # # Pass: There are no in existing users in the database with the same username and email
    # result = register_user("user2", "pass2", "email2")
    # print(f"Test 1: {result}")
    #
    # # Fail: A user alr has a username named user2 in the database
    # result = register_user("user2", "pass2", "email2")
    # print(f"Test 2: {result}")
    #
    # # Fail: A user alr has an email named email2 in the database
    # result = register_user("user3", "pass2", "email2")
    # print(f"Test 3: {result}")

    # ''' USER TEST 1 PASS '''
    # # Pass: There are no in existing users in the database with the same username and email
    # result = register_user("user1", "pass1", "email1")
    # print(f"Test 1: {result}")


