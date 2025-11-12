import streamlit as st
class Atm:
    bank_name = "IDFC"
    def __init__(self, username, panno, add):
        self.username = username
        self.panno = panno
        self.add = add
        self.balance = 0
        st.success(f"Welcome to {self.bank_name} Bank, {self.username}! Your account has been created successfully.")

    def deposit(self, amount):
        self.balance += amount
        st.info(f"Your deposit of ₹{amount} was successful!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            st.warning(f"Your withdrawal of ₹{amount} was successful!")
        else:
            st.error("Insufficient funds!")

    def check_balance(self):
        st.write(f"💰 Your Account Balance: ₹{self.balance}")


# --- Streamlit GUI wrapper ---
st.title("🏦 ATM Simulator (IDFC Bank)")
st.write("A simple ATM simulation using OOP + Streamlit")

# Step 1: Create account
st.subheader("Create Your Account")
username = st.text_input("Enter your Name:")
panno = st.text_input("Enter your PAN number:")
add = st.text_area("Enter your Address:")

if "atm" not in st.session_state:
    st.session_state.atm = None

if st.button("Create Account"):
    if username and panno and add:
        st.session_state.atm = Atm(username, panno, add)
    else:
        st.error("Please fill all the details!")

# Step 2: Banking operations
if st.session_state.atm:
    st.divider()
    st.subheader("Banking Operations")

    option = st.radio("Choose an operation:", ["Deposit", "Withdraw", "Check Balance"])

    if option == "Deposit":
        amount = st.number_input("Enter deposit amount:", min_value=1, step=100)
        if st.button("Deposit"):
            st.session_state.atm.deposit(amount)

    elif option == "Withdraw":
        amount = st.number_input("Enter withdrawal amount:", min_value=1, step=100)
        if st.button("Withdraw"):
            st.session_state.atm.withdraw(amount)

    elif option == "Check Balance":
        if st.button("Show Balance"):
            st.session_state.atm.check_balance()
