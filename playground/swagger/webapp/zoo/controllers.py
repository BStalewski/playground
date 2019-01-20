import json

from pyramid.response import Response
from pyramid.view import view_config

from .models import Dog


@view_config(
    route_name='get_dog',
    request_method='GET',
)
def get_dog(request):
    dog_id = int(request.matchdict['id'])
    dog = Dog(id=dog_id, name='dog-{}'.format(dog_id), age=dog_id * 7)
    return Response(serialize_dog(dog))


@view_config(
    route_name='create_dog',
    request_method='POST',
    renderer='json',
)
def create_dog(request):
    payload = request.json
    dog = Dog(
        id=payload['id'],
        name=payload['name'],
        age=payload['age'],
    )
    # return Response('Created dog: {}'.format(serialize_dog(dog)))
    return serialize_dog(dog)


def serialize_dog(dog):
    dog_json = {
        'id': dog.id,
        'name': dog.name,
        'age': dog.age,
    }
    return json.dumps(dog_json)
