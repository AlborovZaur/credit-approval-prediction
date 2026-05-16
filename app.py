import streamlit as st
import pandas as pd
import joblib
import os 

model_path="loan_approval_model.pkl"
final_model = joblib.load(model_path)

st.title('Проверка одобрения кредита')

person_age = st.sidebar.number_input('Возраст', min_value=18, max_value=100, value=30)
person_income = st.sidebar.number_input('Годовой доход', min_value=10000, max_value=10000000, value=50000, step=100)
person_emp_exp = st.sidebar.number_input('Опыт работы в годах', min_value=1, max_value=50, value=5)
loan_amnt = st.sidebar.number_input('Сумма кредита', min_value=10000, max_value=10000000, value=100000, step=1000)
loan_int_rate = st.sidebar.number_input('Процентная ставка по кредиту', min_value=5.0, max_value=30.0, value=11.0, step=0.01)
loan_percent_income = st.sidebar.number_input('Сумма кредита в процентах от годового дохода', min_value=0.01, max_value=5.0, value=0.50, step=0.01)
cb_person_cred_hist_length = st.sidebar.number_input('Длительность кредитной истории в годах', min_value=1.0, max_value=50.0, value=5.0,step=0.1)
credit_score = st.sidebar.number_input('Кредитный рейтинг', min_value=10, max_value=1000, value=500) 

person_gender = st.sidebar.selectbox('Укажите Ващ пол', ['male', 'female'])
person_education = st.sidebar.selectbox('Укажите образование',['Bachelor', 'Master', 'High School', 'Associate'])
person_home_ownership = st.sidebar.selectbox('Владение жильем', ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
loan_intent = st.sidebar.selectbox('Цель кредита',['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'])
previous_loan_defaults_on_file = st.sidebar.selectbox('Наличие дефолта', ['Yes', 'No'])

if st.button('Рассчитать статус кредита'):
    user_data = {
        'person_age': [person_age],
        'person_income': [person_income],
        'person_emp_exp': [person_emp_exp],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_cred_hist_length': [cb_person_cred_hist_length],
        'credit_score': [credit_score],
        'person_gender': [person_gender],
        'person_education': [person_education],
        'person_home_ownership': [person_home_ownership],
        'loan_intent': [loan_intent],
        'previous_loan_defaults_on_file': [previous_loan_defaults_on_file]
    }
    
    input_df = pd.DataFrame(user_data)
    
    prediction = final_model.predict(input_df)
    prediction_proba = final_model.predict_proba(input_df)[0] * 100

    st.subheader('Результат предсказания:')
    
    if prediction == 1:
        st.success('Кредит **одобрен**!')
        st.write(f"Вероятность одобрения: **{prediction_proba[1]:.2f}%**")
        st.progress(float(prediction_proba[1] / 100))
    else:
        st.error('В кредите **отказано**.')
        st.write(f"Вероятность отказа: **{prediction_proba[0]:.2f}%**")
        st.progress(float(prediction_proba[0] / 100))