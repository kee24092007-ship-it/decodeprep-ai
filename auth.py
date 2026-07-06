import bcrypt
from database import create_connection


# -----------------------------
# REGISTER USER
# -----------------------------
def register_user(name, email, password):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if cursor.fetchone():

        conn.close()

        return False, "Email already exists."

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,
        (
            name,
            email,
            hashed_password
        )
    )

    conn.commit()
    conn.close()

    return True, "Account created successfully."


# -----------------------------
# LOGIN USER
# -----------------------------
def login_user(email, password):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return False, "User not found."

    stored_password = user[3]

    if bcrypt.checkpw(
        password.encode(),
        stored_password
    ):
        return True, user

    return False, "Incorrect password."


# -----------------------------
# LOGOUT
# -----------------------------
def logout():

    import streamlit as st

    st.session_state.logged_in = False

    st.session_state.user = None