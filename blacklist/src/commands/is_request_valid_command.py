from ..errors.errors import InvalidAppIdRegistrationRequestError, InvalidEmailRegistrationRequestError

class IsRequesValidCommand:
    def __init__(self, request):
        self.request = request

    def execute(self):
        if (self.request.get_json().get("email") is None):
            raise InvalidEmailRegistrationRequestError
        
        if (self.request.get_json().get("app_uuid") is None):
            raise InvalidAppIdRegistrationRequestError