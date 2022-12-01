import numpy as np
import pickle
import streamlit as st
#import os

#curr_path = os.path.dirname(os.path.realpath(__file__))
#file=open(os.path.join(curr_path,'modelnew.pkl'),'rb')
file=open('modelnew.pkl','rb')
loaded_model=pickle.load(file)

#creating a function for classification

def cred_score(input_data):
    #input_data = {2, 6, 1, 7, 1169, 4, 0, 2, 67, 1}
    # changing the input to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshaping the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
        return "Good Credit Score"
    else:
        return "Bad credict Score"

def main():

    # giving title
    st.title('Cred Score Prediction App')

    # Header
    st.subheader("Find your credit score now!!!")

    #user input

    #Statusofexistingcheckingaccount= st.selectbox('Status of checking existing account')
    Statusofexistingcheckingaccount= st.selectbox("Status of checking existing account: ",['less than 0 DM', 'Between 0 and 200 DM', 'Greater than 200 DM', 'no checking amount'])
    if (Statusofexistingcheckingaccount=='less than 0 DM'):
        checkingaccount=2
    elif (Statusofexistingcheckingaccount=='Between 0 and 200 DM'):
        checkingaccount=1
    elif (Statusofexistingcheckingaccount == 'Greater than 200 DM'):
        checkingaccount=4
    else:
        checkingaccount=3
    # print the selected hobby
    Durationinmonth = st.number_input('Duration in month')
    #Credithistory= st.text_input('Credit history')
    Credithistory = st.selectbox("Credit History: ",
                                                   ['no credits taken', 'all credits paid back', 'existing credits paid back',
                                                    'delay in paying credits','critical account'])
    if (Credithistory == 'no credits taken'):
        credhist = 4
    elif (Credithistory == 'all credits paid back'):
        credhist = 0
    elif (Credithistory == 'existing credits paid back'):
        credhist = 3
    elif (Credithistory == 'delay in paying credits'):
        credhist = 2
    else:
        credhist = 1
    #Purpose= st.text_input('Purpose')
    Purpose=st.selectbox("Purpose: ",
                                 ['car(new)', 'car(used)', 'furniture/equipment',
                                  'radio/television', 'domestic appliances','repairs','education','vacation','retraining','business','others'])
    if (Purpose == 'car(new)'):
        purpos = 1
    elif (Purpose == 'car(used)'):
        purpos = 2
    elif (Purpose == 'furniture/equipment'):
        purpos = 5
    elif (Purpose == 'radio/television'):
        purpos = 7
    elif (Purpose == 'domestic appliances'):
        purpos = 3
    elif (Purpose == 'repairs'):
        purpos = 8
    elif (Purpose == 'education'):
        purpos = 4
    elif (Purpose == 'vacation'):
        purpos = 10
    elif (Purpose == 'retraining'):
        purpos = 9
    elif (Purpose == 'business'):
        purpos = 0
    else:
        purpos = 6
    Creditamount= st.number_input('Credit amount')
    #Savingsaccountandbonds = st.text_input('Savings account/bonds')
    Savingsaccountandbonds = st.selectbox("Savings account/bonds: ",
                                 ['less than 100 DM', 'between 100 to 500 DM', 'between 500 to 1000 DM',
                                  'greater than 1000 DM', 'no savings account'])
    if (Savingsaccountandbonds == 'less than 100 DM'):
        savings = 0
    elif (Savingsaccountandbonds == 'between 100 to 500 DM'):
        savings = 1
    elif (Savingsaccountandbonds == 'between 500 to 1000 DM'):
        savings = 2
    elif (Savingsaccountandbonds == 'greater than 1000 DM'):
        savings = 3
    else:
        savings = 4

    #Presentemploymentsince= st.text_input('Present employment since')
    Presentemploymentsince = st.selectbox("Present employment since: ",
                                          ['unemployed', 'less than 1 year', 'less than 4 years',
                                           'less than 7 years', 'greater than 7 years'])
    if (Presentemploymentsince == 'unemployed'):
        employement = 4
    elif (Presentemploymentsince == 'less than 1 year'):
        employement = 1
    elif (Presentemploymentsince == 'less than 4 years'):
        employement = 2
    elif (Presentemploymentsince == 'less than 7 years'):
        employement = 3
    else:
        employement = 0
    #Property = st.text_input('Property')
    Property = st.selectbox("Property: ",['real estate', 'building society savings agreement/life insurance', 'car or other',
                                                    'unknown / no property'])
    if (Property == 'real estate'):
        prop = 2
    elif (Property == 'building society savings agreement/life insurance'):
        prop = 0
    elif (Property == 'car or other'):
        prop = 1
    else:
        prop = 4

    Ageinyears = st.number_input('Age in years')

    #Housing=st.text_input('Housing')
    Housing = st.selectbox("Housing: ",
                            ['Rent', 'Own', 'For Free'])
    if (Housing == 'Rent'):
        house = 2
    elif (Housing == 'Own'):
        house = 1
    else:
        house = 0

    #code for prediction
    creditscore = ''

    #creating a button for prediction

    if st.button('Credit Score Result'):
        creditscore=cred_score([checkingaccount,Durationinmonth,credhist,purpos,Creditamount,savings,employement,prop,Ageinyears,house])

    if (creditscore=='Good Credit Score'):
        st.success(creditscore)
    else:
        st.error(creditscore)


if __name__ == "__main__":
  main()
