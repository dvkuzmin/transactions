from functools import wraps


import jwt

SECRET = "DFSDDF2345msf23asdfs"


def auth(func):

    @wraps(func)
    def wrapper(controller, request, response, *args):
        if request.get_header('Authorization'):
            method, token = request.get_header('Authorization').split()
            if method in ('Bearer', 'JWT'):
                data = jwt.decode(token, SECRET, algorithms=["HS256"])
                if data['user_id']:
                    request.context = data
                    func(controller, request, response, *args)
                else:
                    raise errors.AuthError
            else:
                raise errors.AuthError
        else:
            raise errors.AuthError
    return wrapper
