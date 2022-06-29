from rest_framework.response import Response
from rest_framework.decorators import api_view
from urllib.parse import quote

import pyrebase
import json
import random
import string

firebaseConfig ={"apiKey": "AIzaSyCRvKDk0ixXieZataevh6h__eWN0xhEwII",
  "authDomain": "bamdata-4bf86.firebaseapp.com",
  "databaseURL":"https://bamdata-4bf86-default-rtdb.firebaseio.com/",
  "projectId": "bamdata-4bf86",
  "storageBucket": "bamdata-4bf86.appspot.com",
  "messagingSenderId": "178450080103",
  "appId": "1:178450080103:web:9e0eea97d0a37d91b10fc2"}

@api_view(['GET'])
def getData(request):

    pyrebase.pyrebase.quote = lambda s, safe=None: s
    def get_url(self, token=None):
        path = self.path
        self.path = None
        if path.startswith('/'):
            path = path[1:]
        if token:
            return "{0}/o/{1}?alt=media&token={2}".format(self.storage_bucket, quote(path, safe=''), token)
        return "{0}/o/{1}?alt=media".format(self.storage_bucket, quote(path, safe=''))

    pyrebase.pyrebase.Storage.get_url = lambda self, token=None: \
    get_url(self, token)

    cliente = request.data['cliente']
    valor = {"documento":'documento'}
    documento = valor["documento"]
    val = "0"
    print(cliente)

    firebase = pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()
    print("va")

    result = db.child("Clientes").order_by_child(documento).equal_to(cliente).get()
    print("--->", result.val())

    error = 'Error log'
   
    return Response(result.val())