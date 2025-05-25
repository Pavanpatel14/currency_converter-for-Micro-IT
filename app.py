import streamlit as st

st.title("Currency Converter ")

# Hardcoded exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.0,
    "GBP": 0.79,
    "JPY": 156.0,
    "CAD": 1.36,
    "AUD": 1.51,
}

currencies = list(exchange_rates.keys())

from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)
amount = st.number_input("Amount", min_value=0.0, value=1.0, step=0.01)

if st.button("Convert"):
    # Convert from source to USD, then USD to target
    usd_amount = amount / exchange_rates[from_currency]
    result = usd_amount * exchange_rates[to_currency]
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
