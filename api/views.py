from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'name': 'Angie', 'age': 25}
    print(request.data['prueba'])
    error = 'Error log'
    if request.data['prueba'] == 1290:
        return Response(person)
    return Response(error)