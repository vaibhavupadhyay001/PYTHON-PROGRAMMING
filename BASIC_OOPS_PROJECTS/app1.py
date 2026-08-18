import streamlit as st


# =========================
# BANKING OOP CLASSES
# =========================

class BankException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise BankException("Deposit amount must be greater than $0.")

        self.balance += amount
        return True

    def check(self, amount):
        if self.balance >= amount:
            return True
        else:
            raise BankException(
                f"Account '{self.name}' only has "
                f"${self.balance:.2f} available."
            )

    def withdraw(self, amount):
        if amount <= 0:
            raise BankException("Withdrawal amount must be greater than $0.")

        self.check(amount)
        self.balance -= amount
        return True

    def transfer(self, amount, account):
        if amount <= 0:
            raise BankException("Transfer amount must be greater than $0.")

        self.check(amount)
        self.withdraw(amount)
        account.deposit(amount)

        return True


class InterestRewardsAcc(BankAccount):

    def deposit(self, amount):
        if amount <= 0:
            raise BankException("Deposit amount must be greater than $0.")

        self.balance += amount * 1.05
        return True


class SavingsAcc(InterestRewardsAcc):

    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        if amount <= 0:
            raise BankException(
                "Withdrawal amount must be greater than $0."
            )

        self.check(amount + self.fee)

        self.balance -= amount + self.fee

        return True


# =========================
# STREAMLIT CONFIG
# =========================

st.set_page_config(
    page_title="GreenBank",
    page_icon="🏦",
    layout="wide"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f4fbf6;
    }

    /* Header */
    .main-header {
        background: linear-gradient(135deg, #0b7a3b, #16a05d);
        padding: 28px 35px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0, 120, 60, 0.15);
    }

    .main-header h1 {
        margin: 0;
        font-size: 38px;
        font-weight: 700;
    }

    .main-header p {
        margin-top: 8px;
        font-size: 16px;
        opacity: 0.9;
    }

    /* Account card */
    .account-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #dcefe2;
        box-shadow: 0 6px 20px rgba(0, 100, 50, 0.08);
        margin-bottom: 20px;
    }

    .account-name {
        color: #0b7a3b;
        font-size: 22px;
        font-weight: 700;
    }

    .balance {
        color: #111827;
        font-size: 36px;
        font-weight: 700;
        margin-top: 8px;
    }

    .account-type {
        color: #6b7280;
        font-size: 14px;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background-color: #0b7a3b;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #075d2d;
        color: white;
    }

    /* Section titles */
    .section-title {
        color: #0b7a3b;
        font-size: 24px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Transaction box */
    .transaction-box {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #dcefe2;
        box-shadow: 0 5px 15px rgba(0, 100, 50, 0.06);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #dcefe2;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# SESSION STATE
# =========================

if "accounts" not in st.session_state:

    st.session_state.accounts = {
        "Vaibhav": BankAccount(5000, "Vaibhav"),
        "Savings": SavingsAcc(10000, "Savings")
    }


accounts = st.session_state.accounts


# =========================
# HEADER
# =========================

st.markdown("""
<div class="main-header">

    <h1>🏦 GreenBank</h1>

    <p>
        Simple, secure and object-oriented banking dashboard
    </p>

</div>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🏦 GreenBank")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Deposit",
        "Withdraw",
        "Transfer",
        "Create Account"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Powered by Python + OOP + Streamlit")


# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    st.markdown(
        '<div class="section-title">Account Overview</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(len(accounts))

    for index, (name, account) in enumerate(accounts.items()):

        with cols[index]:

            account_type = type(account).__name__

            st.markdown(
                f"""
                <div class="account-card">

                    <div class="account-name">
                        {account.name}
                    </div>

                    <div class="account-type">
                        {account_type}
                    </div>

                    <div class="balance">
                        ${account.balance:,.2f}
                    </div>

                    <div class="account-type">
                        Available Balance
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    total_balance = sum(
        account.balance for account in accounts.values()
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Accounts",
            len(accounts)
        )

    with col2:
        st.metric(
            "Total Balance",
            f"${total_balance:,.2f}"
        )

    with col3:
        st.metric(
            "Bank Status",
            "Active"
        )


# =========================
# DEPOSIT
# =========================

elif menu == "Deposit":

    st.markdown(
        '<div class="section-title">💰 Deposit Money</div>',
        unsafe_allow_html=True
    )

    account_name = st.selectbox(
        "Select Account",
        list(accounts.keys())
    )

    amount = st.number_input(
        "Deposit Amount",
        min_value=1.0,
        step=100.0
    )

    if st.button("Deposit Money"):

        account = accounts[account_name]

        try:
            account.deposit(amount)

            st.success(
                f"${amount:,.2f} deposited successfully!"
            )

            st.info(
                f"New balance: ${account.balance:,.2f}"
            )

        except BankException as error:

            st.error(str(error))


# =========================
# WITHDRAW
# =========================

elif menu == "Withdraw":

    st.markdown(
        '<div class="section-title">💸 Withdraw Money</div>',
        unsafe_allow_html=True
    )

    account_name = st.selectbox(
        "Select Account",
        list(accounts.keys())
    )

    amount = st.number_input(
        "Withdrawal Amount",
        min_value=1.0,
        step=100.0
    )

    if st.button("Withdraw Money"):

        account = accounts[account_name]

        try:

            account.withdraw(amount)

            if isinstance(account, SavingsAcc):

                st.success(
                    f"${amount:,.2f} withdrawn successfully."
                )

                st.info(
                    f"Withdrawal fee: ${account.fee:.2f}"
                )

            else:

                st.success(
                    f"${amount:,.2f} withdrawn successfully."
                )

            st.info(
                f"Remaining balance: ${account.balance:,.2f}"
            )

        except BankException as error:

            st.error(str(error))


# =========================
# TRANSFER
# =========================

elif menu == "Transfer":

    st.markdown(
        '<div class="section-title">🔄 Transfer Money</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        from_account = st.selectbox(
            "From Account",
            list(accounts.keys())
        )

    with col2:

        to_options = [
            name for name in accounts.keys()
            if name != from_account
        ]

        to_account = st.selectbox(
            "To Account",
            to_options
        )

    amount = st.number_input(
        "Transfer Amount",
        min_value=1.0,
        step=100.0
    )

    if st.button("Transfer Money"):

        sender = accounts[from_account]
        receiver = accounts[to_account]

        try:

            sender.transfer(
                amount,
                receiver
            )

            st.success(
                f"${amount:,.2f} transferred successfully!"
            )

            st.info(
                f"{from_account}: "
                f"${sender.balance:,.2f}"
            )

            st.info(
                f"{to_account}: "
                f"${receiver.balance:,.2f}"
            )

        except BankException as error:

            st.error(
                f"Transfer failed: {error}"
            )


# =========================
# CREATE ACCOUNT
# =========================

elif menu == "Create Account":

    st.markdown(
        '<div class="section-title">➕ Create New Account</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Account Holder Name"
    )

    initial_amount = st.number_input(
        "Initial Deposit",
        min_value=0.0,
        step=100.0
    )

    account_type = st.selectbox(
        "Account Type",
        [
            "Regular Bank Account",
            "Savings Account"
        ]
    )

    if st.button("Create Account"):

        if not name.strip():

            st.error(
                "Please enter an account holder name."
            )

        elif name in accounts:

            st.error(
                "An account with this name already exists."
            )

        else:

            if account_type == "Savings Account":

                accounts[name] = SavingsAcc(
                    initial_amount,
                    name
                )

            else:

                accounts[name] = BankAccount(
                    initial_amount,
                    name
                )

            st.success(
                f"Account '{name}' created successfully!"
            )

            st.rerun()