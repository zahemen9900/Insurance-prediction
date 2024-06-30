import streamlit as st
import joblib
import pandas as pd

# Load the pretrained model
model = joblib.load(os.path.join(os.getcwd(), 'insurance_model.pkl'))

st.markdown("# Insurance Predictions")

# Sidebar for user input
st.sidebar.header('User Input Features')

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    occupation = st.sidebar.selectbox('Occupation', ('NURSE', 'TEACHER', 'PHOTOGRAPHER', 'SECURITY', 'COOK',
       'LIBRARIAN', 'CONTRACTOR', 'MIDWIFE', 'RESOURCE GUARD', 'COCOBOD',
       'AGRIC EXTENSION', 'STENOGRAPHER', 'SALES OFFICER', 'GENERAL LAB',
       'SANITARY ARTISAN', 'CIVIL SERVANT', 'ADMINISTRATOR',
       'ANESTHESIOLOGIST', 'NBSSI', 'TELECOM AGENT', 'PLUMBING',
       'WELDING', 'CLERK', 'ENGINEER', 'ACCOUNTANT', 'SECURITY GUARD',
       'SEAMSTRESS', 'GARDENER', 'OPTICAL TECHNICIAN', 'LECTURER',
       'OFFICER', 'CHEF', 'MATRON', 'TRADING'))
    
    plan = st.sidebar.selectbox('Plan', ('FAMILY SECURITY PLAN', 'EDUCATION', 'FLEXI CHILD EDUCATION', 'ULTIMATE LIFE'))
    proposals = st.sidebar.date_input('Date of Proposal')
    policy_value = st.sidebar.slider('Policy Value', 0.0, 1000000.0, 100000.0)
    paid_premium = st.sidebar.slider('Paid Premium', 0.0, 1000000.0, 50000.0)
    premium = st.sidebar.slider('Premium', 0, 100000, 10000)
    total_premium = st.sidebar.slider('Total Premium', 0.0, 1000000.0, 150000.0)
    policy_duration_years = st.sidebar.slider('Policy Duration (Years)', 0.0, 50.0, 5.0)
    
    data = {
        'gender': gender,
        'occupation': occupation,
        'plan': plan,
        'proposals': proposals,
        'policy_value': policy_value,
        'paid_premium': paid_premium,
        'premium': premium,
        'total_premium': total_premium,
        'policy_duration_years': policy_duration_years
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Display user input
st.subheader('User Input features')
st.write(df)
# Add any other necessary preprocessing steps here

# Prediction
#prediction = model.predict(df)

# Display prediction
st.subheader('Prediction')
st.write(f'The predicted insurance cost is: ${prediction[0]:.2f}')

# Run the app
if __name__ == '__main__':
    st.run()
