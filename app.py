import streamlit as st
from auth import register_user, login_user

st.set_page_config(
    page_title="DecodePrep AI",
    page_icon="💼",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "login"

st.title("DecodePrep AI")
st.caption("Practice Smarter. Interview Better.")

# -----------------------
# LOGIN PAGE
# -----------------------

if st.session_state.page == "login":

    st.subheader("Sign In")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Continue"):

        success, result = login_user(
            email,
            password
        )

        if success:

            st.success("Login Successful!")

            st.switch_page(
                "pages/dashboard.py"
            )

        else:

            st.error(result)

    st.write("")

    if st.button("Create Account"):

        st.session_state.page = "signup"

        st.rerun()

# -----------------------
# SIGNUP PAGE
# -----------------------

else:

    st.subheader("Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        success, message = register_user(
            name,
            email,
            password
        )

        if success:

            st.success(message)

            st.session_state.page = "login"

            st.rerun()

        else:

            st.error(message)

    st.write("")

    if st.button("Back to Login"):

        st.session_state.page = "login"

        st.rerun()