class ApiError(Exception):
    code = 422
    description = "Default message"

class InvalidEmailRegistrationRequestError(Exception):
    code = 400
    description = "Please provide a valid email."

class InvalidAppIdRegistrationRequestError(Exception):
    code = 400
    description = "Please provide a valid app id."

class EmailIsAlreadyRegisteredError(Exception):
    code = 409
    description = "The email was registered already."
