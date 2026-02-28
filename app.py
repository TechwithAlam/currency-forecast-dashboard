import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime
import streamlit as st
import requests

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="AI Currency Forecast Dashboard",
    page_icon="💱",
    layout="wide"
)

st.markdown("""
# 💱 AI-Powered Currency Forecast Dashboard
### Real-Time Conversion • Trend Analysis • ML Prediction
""")
# --------------------------------
# API Config
# --------------------------------
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

CURRENCIES = ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "JPY", "AED", "KWD"]

# --------------------------------
# Session State for History
# --------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------
# Layout Columns
# --------------------------------
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Enter Amount", min_value=0.0, value=1.0)
    base_currency = st.selectbox("From", CURRENCIES)

with col2:
    target_currency = st.selectbox("To", CURRENCIES)

    if st.button("🔄 Swap Currencies"):
        base_currency, target_currency = target_currency, base_currency

# --------------------------------
# Convert Button
# --------------------------------
if st.button("Convert"):
    try:
        params = {
            "apikey": API_KEY,
            "base_currency": base_currency,
            "currencies": target_currency
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        rate = data["data"].get(target_currency)

        if rate:
            converted_amount = amount * rate

            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            st.info(f"Exchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")

            # Save history
            st.session_state.history.append(
                f"{amount} {base_currency} → {converted_amount:.2f} {target_currency}"
            )

        else:
            st.error("Currency not found.")

    except:
        st.error("Error connecting to API.")
        
st.markdown("## 🔄 Currency Conversion")
# --------------------------------
# Show Conversion History
# --------------------------------
st.markdown("---")
st.subheader("📜 Conversion History")

if st.session_state.history:
    for item in reversed(st.session_state.history[-5:]):
        st.write(item)
else:
    st.write("No conversions yet.")
    
st.markdown("## 📈 Market Trend Analysis")
# --------------------------------
# Historical Trend Graph (Working Version)
# --------------------------------
import matplotlib.pyplot as plt
import datetime

st.markdown("---")
st.subheader("📈 7-Day Exchange Rate Trend")

if st.button("Show 7-Day Trend"):
    try:
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=7)

        url = f"https://api.frankfurter.app/{start_date}..{end_date}"
        params = {
            "from": base_currency,
            "to": target_currency
        }

        response = requests.get(url, params=params)
        data = response.json()

        dates = []
        rates = []

        for date in sorted(data["rates"].keys()):
            dates.append(date)
            rates.append(data["rates"][date][target_currency])

        plt.figure()
        plt.plot(dates, rates)
        plt.xticks(rotation=45)
        plt.title(f"{base_currency} to {target_currency} (Last 7 Days)")
        plt.xlabel("Date")
        plt.ylabel("Exchange Rate")
        plt.tight_layout()

        st.pyplot(plt)

    except Exception as e:
        st.error("Could not fetch historical data.")

st.markdown("## 🤖 AI Forecasting")
# --------------------------------
# ML Prediction Section
# --------------------------------
st.markdown("---")
st.subheader("🤖 Predict Tomorrow's Exchange Rate")

if st.button("Predict Next Day Rate"):
    try:
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=7)

        url = f"https://api.frankfurter.app/{start_date}..{end_date}"
        params = {
            "to": target_currency,
            "from": base_currency
        }

        response = requests.get(url, params=params)
        data = response.json()

        rates = []
        for date in sorted(data["rates"].keys()):
            rates.append(data["rates"][date][target_currency])

        # Prepare data for ML
        X = np.array(range(len(rates))).reshape(-1, 1)
        y = np.array(rates)

        model = LinearRegression()
        model.fit(X, y)

        next_day = np.array([[len(rates)]])
        prediction = model.predict(next_day)

        st.metric(
    label="Predicted Next Day Rate",
    value=f"{prediction[0]:.4f} {target_currency}",
)

        st.caption("⚠ Prediction based on simple Linear Regression (educational purpose only)")
    except:
        st.error("Prediction failed.")
        
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
    Built with ❤️ by <b>Alam</b> <br>
    AI • Financial Analytics
    </div>
    """,
    unsafe_allow_html=True
)
