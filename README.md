# 💱 AI-Powered Currency Forecast Dashboard

An interactive **Streamlit-based web application** that performs:

- 🌍 Real-time currency conversion  
- 📈 7-day exchange rate trend visualization  
- 🤖 AI-based next-day exchange rate prediction  

This project combines **API integration**, **data visualization**, and **machine learning** into one practical financial analytics dashboard.


## 🚀 Features

### 🔄 Real-Time Currency Conversion
- Convert between multiple currencies
- Fetches live exchange rates using an API
- Displays conversion history

### 📈 Market Trend Analysis
- 7-day historical exchange rate visualization
- Dynamic line graph using Matplotlib
- Real-time API-based data fetching

### 🤖 AI Forecasting (Machine Learning)
- Uses **Linear Regression**
- Predicts next-day exchange rate
- Educational ML implementation for financial data

---

## 🛠️ Technologies & Libraries Used

- **Python**
- **Streamlit** (Web App Framework)
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Requests**
- **Currency Exchange APIs**

---

## 📂 Project Structure

Currency-Forecast-Dashboard/
│
├── app.py # Main Streamlit application
├── README.md # Project documentation



---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/currency-forecast-dashboard.git
cd currency-forecast-dashboard

### 2️⃣ Install Required Dependencies

pip install streamlit numpy scikit-learn matplotlib requests

🔑 API Key Setup (Important)

This project uses a currency exchange API.

⚠️ You must use your own API key.
API_KEY = "YOUR_API_KEY_HERE"
Get your free API key from:

https://freecurrencyapi.com/

# ▶️ How to Run

streamlit run app.py

### 🚀 Usage Flow

Open the Streamlit application

Select base and target currencies

Enter the amount

Click Convert to see real-time exchange rate

View 7-day trend graph

Click Predict Next Day Rate for AI forecasting

### 💱 Example Usage

Enter Amount: 100
From: USD
To: INR
Click: Convert

Click: Show 7-Day Trend
Click: Predict Next Day Rate

### 📊 What You Can Do

Convert currencies in real-time

View last 7-day exchange rate trend

Predict next-day exchange rate using ML

Track recent conversion history

## 📜 License

This project is open-source and intended for learning and educational purposes only.
The forecasting model is built for academic demonstration and should not be used for real financial decisions.
