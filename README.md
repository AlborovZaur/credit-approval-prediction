# Credit Approval Prediction App

A Machine Learning project for predicting credit application approval based on financial data. The repository includes data preprocessing and model training developed in Google Colab, as well as an interactive web interface built with Streamlit.

## Project Overview
* **Task:** Binary Classification (Approved / Denied)
* **Training Environment:** Google Colab (`credit-approval-prediction.ipynb`)
* **Deployment Interface:** Streamlit (`app.py`)
* **Tech Stack:** Python, Scikit-Learn, Pandas, NumPy, Streamlit

## Repository Structure
* `credit-approval-prediction.ipynb` - Jupyter notebook with EDA, data cleaning, and model training.
* `app.py` - Streamlit application code.
* `loan_approval_model.pkl` - Trained model weights.
* `.gitignore` - Configuration file to exclude virtual environment (`venv`).

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/AlborovZaur/credit-approval-prediction
   ```
2. Install dependencies:
   ```bash
   pip install streamlit scikit-learn pandas numpy
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
