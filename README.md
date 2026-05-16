# Credit Approval Prediction System 💰🤖

An end-to-end Machine Learning project that predicts credit application approval based on user financial metrics. The project covers the full pipeline: from exploratory data analysis (EDA) and model training in Google Colab to deploying an interactive web application using Streamlit.

## 🚀 Project Overview
* **Task:** Binary Classification (Approved / Denied)
* **Research & Training:** Google Colab (`credit-approval-prediction.ipynb`)
* **Web Interface:** Streamlit app (`app.py`)
* **Core Stack:** Python, Scikit-Learn, Pandas, NumPy, Streamlit

## 📂 Repository Structure
* `credit-approval-prediction.ipynb` - Jupyter notebook containing data cleaning, visualization, feature engineering, and model training.
* `app.py` - Core Streamlit application code for the interactive user interface.
* `loan_approval_model.pkl` - Serialized file of the best-performing trained ML model.
* `.gitignore` - Configuration file to exclude local virtual environments (`venv`) from tracking.

## 🛠️ How to Run the App Locally

1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd credit-approval-prediction
   ```
3. Install required libraries:
   ```bash
   pip install streamlit scikit-learn pandas numpy
   ```
4. Launch the Streamlit web application:
   ```bash
   streamlit run app.py
   ```
