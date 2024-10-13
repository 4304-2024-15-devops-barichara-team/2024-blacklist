from ..database import db
from ..models.blacklist import Blacklist


def get_blacklist_by_email(email):
    record = db.session.query(Blacklist).filter(Blacklist.email == email).first()
    return record


def check_if_user_is_verified(user):
    if not user.status == Status.VERIFICADO:
        raise UserNotVerified
    return user
