import bcrypt
from database import add_user, get_user


def hash_password(password):

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )


def register_user(fullname, email, password):

    if get_user(email):
        return False

    hashed = hash_password(password)

    add_user(
        fullname,
        email,
        hashed
    )

    return True


def login_user(email, password):

    user = get_user(email)

    if user is None:
        return None

    if verify_password(
        password,
        user[3]
    ):
        return user

    return None