import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://ai-assistant-2a4b8-default-rtdb.asia-southeast1.firebasedatabase.app/'

})

ref = db.reference('/')
ref.set({
    'Test_Entry':
        {
            'test':{
                'name':'Philip',
                'lname':'Jin'
            },
            'asd':{
                'name':'asdasd'
            }
        }
})