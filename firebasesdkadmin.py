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
