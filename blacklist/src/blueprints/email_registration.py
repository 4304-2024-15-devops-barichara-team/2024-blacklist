from flask import Blueprint, request, jsonify
import os
from ..commands.register_email_command import RegisterEmail
from ..commands.is_email_bannered_command import IsEmailBanneredCommand
from ..commands.is_request_valid_command import IsRequesValidCommand
from ..errors.errors import ApiError, InvalidAppIdFormatRegistrationRequestError, InvalidAppIdRegistrationRequestError, InvalidEmailRegistrationRequestError, EmailIsAlreadyRegisteredError

from ..utils.constants import EMAIL_REGISTERED
import logging
import traceback

email_registration_blueprint = Blueprint('email_registration', __name__, url_prefix='/blacklists')

@email_registration_blueprint.route('', methods=['POST'])
def register_email():
    json = request.get_json()

    try:
        token = request.headers.get('Authorization')
        if token != f"Bearer {os.environ.get('STATIC_TOKEN')}":
            logging.warning("Unauthorized access attempt with token: %s", token)
            return jsonify({"msg": "Unauthorized"}), 401

        email = json.get("email")
        app_uuid = json.get("app_uuid")
        blocked_reason = json.get("blocked_reason")
        ip_address = request.environ['REMOTE_ADDR']

        IsRequesValidCommand(request).execute()
        IsEmailBanneredCommand(email=email).execute()
        RegisterEmail(email=email, app_uuid=app_uuid,blocked_reason=blocked_reason, ip_address=ip_address).execute()

        logging.info("Successfully registered email: %s", email)
        return {"msg": EMAIL_REGISTERED}, 201

    except InvalidAppIdFormatRegistrationRequestError:
        logging.error("Invalid app ID format for request: %s", json)
        logging.debug(traceback.format_exc())
        return {"msg": InvalidAppIdFormatRegistrationRequestError.description}, InvalidAppIdFormatRegistrationRequestError.code
    except EmailIsAlreadyRegisteredError:
        logging.error("Email is already registered: %s", json.get("email"))
        logging.debug(traceback.format_exc())
        return {"msg": EmailIsAlreadyRegisteredError.description}, EmailIsAlreadyRegisteredError.code
    except InvalidEmailRegistrationRequestError:
        logging.error("Invalid email registration request: %s", json)
        logging.debug(traceback.format_exc())
        return {"msg": InvalidEmailRegistrationRequestError.description}, InvalidEmailRegistrationRequestError.code
    except InvalidAppIdRegistrationRequestError:
        logging.error("Invalid app ID for registration request: %s", json)
        logging.debug(traceback.format_exc())
        return {"msg": InvalidAppIdRegistrationRequestError.description}, InvalidAppIdRegistrationRequestError.code
    except Exception:
        logging.error("Unexpected error occurred: %s", str(e))
        logging.debug(traceback.format_exc())
        return {"msg": ApiError.description}, ApiError.code