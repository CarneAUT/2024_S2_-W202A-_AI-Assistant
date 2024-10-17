import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://ai-assistant-2a4b8-default-rtdb.asia-southeast1.firebasedatabase.app/'

})

ref = db.reference('/')

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

if __name__ == '__main__':

    ''' USER TEST 1 FAIL '''
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

    ''' USER TEST 1 PASS '''
    # # Pass: There are no in existing users in the database with the same username and email
    # result = register_user("user1", "pass1", "email1")
    # print(f"Test 1: {result}")


