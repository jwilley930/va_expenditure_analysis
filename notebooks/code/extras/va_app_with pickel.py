from pyexpat import model
import streamlit as st
import numpy as np
import plotly.express as px
import pickle
import time
import pandas as pd
from sklearn.preprocessing import StandardScaler

st.set_page_config(layout='wide')

st.title('VA Expenditure per County Predictor')
st.header('Adjust options to predict changes to VA spending')

col1, col2, col3 = st.columns(3)
st.write('')
st.write('')
col4,col5,col6 = st.columns(3)
st.write('')
st.write('')
col7,col8,col9 = st.columns(3)
st.write('')
st.write('')
col10,col11,col12 = st.columns(3)
st.write('')
st.write('')
col13, col14,col15 = st.columns(3)
st.write('')
st.write('')
col16,col17,col18, col19 = st.columns(4)
st.write('')
st.write('')


with col1:
    state= st.selectbox('State',['Alabama','Alaska','Arizona','Arkansas','California',
    'Colorado','Connecticut','Delaware', 'District of Columbia', 'Florida','Georgia',
    'Hawaii','Idaho','Illinois','Indiana','Iowa',
    'Kansas','Kentucky','Louisiana','Maine','Maryland',
    'Massachusetts','Michigan','Minnesota','Mississippi',
    'Missouri','Montana','Nebraska','Nevada','New Hampshire',
    'New Jersey','New Mexico','New York','North Carolina',
    'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','South Dakota','Tennessee',
    'Texas','Utah','Vermont','Virginia','Washington',
    'West Virginia','Wisconsin','Wyoming'])
with col2:
    county_pop= st.slider('County Population', 0, 10_000_000)
with col3:
    vet_pop= st.slider('Veteran Population', 0, 300_000)
    
with col4:
    age_under18_pct= st.slider('Pop.% Under 18', 0, 100) 
with col5:
    age_over65_pct= st.slider('Pop.% Over 65', 0, 100)
with col6:
    rural_pct= st.slider('Pop.% in Rural Area', 0, 100)
    
with col7:
    median_income= st.slider('Median Income', 20_000, 200_000)
with col8:
    unemployment_pct= st.slider('Unemployent Rate', 0, 100)
with col9:
    poverty_pct= st.slider('% in Poverty', 0, 100)
with col10:
    severe_housing_problems_pct= st.slider('% of Households with severe housing problem', 0, 100)
with col11:
    food_insecure_pct=st.slider('Pop.% who lack adequate access to food', 0, 100)
    
with col12:
    hs_grad_pct= st.slider('Pop.% with high school diploma', 0, 100)
with col13:
    clg_grad_pct= st.slider('Pop.% with college degree', 0, 100)

with col14:
    smokers_pct= st.slider('% of adults who are smokers', 0, 100)
with col15:
    obesity_pct= st.slider('% of adults who are obese', 0, 100)
with col16:
    inactive_pct= st.slider('% of adults who are physically inactive', 0, 100)
with col17:
    excess_alcohol_pct= st.slider('% of adults who report excessive drinking ', 0, 100)
with col18:
    diabetes_pct= st.slider('% of adults who have diabetes ', 0, 100)
with col19:
    state_va_fac= st.slider('Number of statewide VA facilities', 0, 110)

# user_input = np.array([[state, county_pop, vet_pop, age_under18_pct, age_over65_pct, rural_pct, median_income, unemployment_pct, poverty_pct, severe_housing_problems_pct, food_insecure_pct, hs_grad_pct, clg_grad_pct, smokers_pct, obesity_pct, inactive_pct, excess_alcohol_pct, diabetes_pct, state_va_fac]])

user_input = np.array([[state, county_pop, vet_pop, state_va_fac, hs_grad_pct, clg_grad_pct,
       median_income, poverty_pct, unemployment_pct,
       severe_housing_problems_pct, smokers_pct, obesity_pct,
       inactive_pct, excess_alcohol_pct, diabetes_pct,
       food_insecure_pct, age_under18_pct, age_over65_pct, rural_pct]])
   

 
    # asdf

user_input_code = pd.DataFrame()

user_input_code['county_pop'] = [float(county_pop)]
user_input_code['vet_pop'] = [float(vet_pop)]
user_input_code['age_under18_pct'] = [float(age_under18_pct)]
user_input_code['age_over65_pct'] = [float(age_over65_pct)]
user_input_code['rural_pct'] = [float(rural_pct)]
user_input_code['median_income'] = [float(median_income)]
user_input_code['unemployment_pct'] = [float(unemployment_pct)]
user_input_code['poverty_pct'] = [float(poverty_pct)]
user_input_code['severe_housing_problems_pct'] = [float(severe_housing_problems_pct)]
user_input_code['food_insecure_pct'] = [float(food_insecure_pct)]
user_input_code['hs_grad_pct'] = [float(hs_grad_pct)]
user_input_code['clg_grad_pct'] = [float(clg_grad_pct)]
user_input_code['smokers_pct'] = [float(smokers_pct)]
user_input_code['obesity_pct'] = [float(obesity_pct)]
user_input_code['inactive_pct'] = [float(inactive_pct)]
user_input_code['excess_alcohol_pct'] = [float(excess_alcohol_pct)]
user_input_code['diabetes_pct'] = [float(diabetes_pct)]
user_input_code['state_va_fac'] = [float(state_va_fac)]

if state == 'Alabama':
    user_input_code['state_al'] = [1]
else:
    user_input_code['state_al'] = [0]
if state == 'Alaska':
    user_input_code['state_ak'] = [1]
else:
    user_input_code['state_ak'] = [0]
if state == 'Arizona':
    user_input_code['state_az'] = [1]
else:
    user_input_code['state_az'] = [0]
if state == 'Arkansas':
    user_input_code['state_ar'] = [1]
else:
    user_input_code['state_ar'] = [0]
if state == 'California':
    user_input_code['state_ca'] = [1]
else:
    user_input_code['state_ca'] = [0]
if state == 'Colorado':
    user_input_code['state_co'] = [1]
else:
    user_input_code['state_co'] = [0]
if state == 'Connecticut':
    user_input_code['state_ct'] = [1]
else:
    user_input_code['state_ct'] = [0]
if state == 'Delaware':
    user_input_code['state_de'] = [1]
else:
    user_input_code['state_de'] = [0]
if state == 'District of Columbia':
    user_input_code['state_dc'] = [1]   
else:
    user_input_code['state_dc'] = [0]
if state == 'Florida':
    user_input_code['state_fl'] = [1]
else:
    user_input_code['state_fl'] = [0]
if state == 'Georgia':
    user_input_code['state_ga'] = [1]
else:
    user_input_code['state_ga'] = [0]
if state == 'Hawaii':
    user_input_code['state_hi'] = [1]
else:
    user_input_code['state_hi'] = [0]
if state == 'Idaho':
    user_input_code['state_id'] = [1]
else:
    user_input_code['state_id'] = [0]
if state == 'Illinois':
    user_input_code['state_il'] = [1]
else:
    user_input_code['state_il'] = [0]
if state == 'Indiana':
    user_input_code['state_in'] = [1]
else:
    user_input_code['state_in'] = [0]
if state == 'Iowa':
    user_input_code['state_ia'] = [1]
else:
    user_input_code['state_ia'] = [0]
if state == 'Kansas':
    user_input_code['state_ks'] = [1]
else:
    user_input_code['state_ks'] = [0]
if state == 'Kentucky':
    user_input_code['state_ky'] = [1]
else:
    user_input_code['state_ky'] = [0]
if state == 'Louisiana':
    user_input_code['state_la'] = [1]
else:
    user_input_code['state_la'] = [0]
if state == 'Maine':
    user_input_code['state_me'] = [1]
else:
    user_input_code['state_me'] = [0]
if state == 'Maryland':
    user_input_code['state_md'] = [1]
else:
    user_input_code['state_md'] = [0]
if state == 'Massachusetts':
    user_input_code['state_ma'] = [1]
else:
    user_input_code['state_ma'] = [0]
if state == 'Michigan':
    user_input_code['state_mi'] = [1]
else:
    user_input_code['state_mi'] = [0]
if state == 'Minnesota':
    user_input_code['state_mn'] = [1]
else:
    user_input_code['state_mn'] = [0]
if state == 'Mississippi':
    user_input_code['state_ms'] = [1]
else:
    user_input_code['state_ms'] = [0]
if state == 'Missouri':
    user_input_code['state_mo'] = [1]
else:
    user_input_code['state_mo'] = [0]
if state == 'Montana':
    user_input_code['state_mt'] = [1]
else:
    user_input_code['state_mt'] = [0]
if state == 'Nebraska':
    user_input_code['state_ne'] = [1]
else:
    user_input_code['state_ne'] = [0]
if state == 'Nevada':
    user_input_code['state_nv'] = [1]
else:
    user_input_code['state_nv'] = [0]
if state == 'New Hampshire':
    user_input_code['state_nh'] = [1]
else:
    user_input_code['state_nh'] = [0]
if state == 'New Jersey':
    user_input_code['state_nj'] = [1]
else:
    user_input_code['state_nj'] = [0]
if state == 'New Mexico':
    user_input_code['state_nm'] = [1]
else:
    user_input_code['state_nm'] = [0]
if state == 'New York':
    user_input_code['state_ny'] = [1]
else:
    user_input_code['state_ny'] = [0]
if state == 'North Carolina':
    user_input_code['state_nc'] = [1]
else:
    user_input_code['state_nc'] = [0]
if state == 'North Dakota':
    user_input_code['state_nd'] = [1]
else:
    user_input_code['state_nd'] = [0]
if state == 'Ohio':
    user_input_code['state_oh'] = [1]
else:
    user_input_code['state_oh'] = [0]
if state == 'Oklahoma':
    user_input_code['state_ok'] = [1]
else:
    user_input_code['state_ok'] = [0]
if state == 'Oregon':
    user_input_code['state_or'] = [1]
else:
    user_input_code['state_or'] = [0]
if state == 'Pennsylvania':
    user_input_code['state_pa'] = [1]
else:
    user_input_code['state_pa'] = [0]
if state == 'Rhode Island':
    user_input_code['state_ri'] = [1]
else:
    user_input_code['state_ri'] = [0]
if state == 'South Carolina':
    user_input_code['state_sc'] = [1]
else:
    user_input_code['state_sc'] = [0]
if state == 'South Dakota':
    user_input_code['state_sd'] = [1]
else:
    user_input_code['state_sd'] = [0]
if state == 'Tennessee':
    user_input_code['state_tn'] = [1]
else:
    user_input_code['state_tn'] = [0]
if state == 'Texas':
    user_input_code['state_tx'] = [1]
else:
    user_input_code['state_tx'] = [0]
if state == 'Utah':
    user_input_code['state_ut'] = [1]
else:
    user_input_code['state_ut'] = [0]
if state == 'Vermont':
    user_input_code['state_vt'] = [1]
else:
    user_input_code['state_vt'] = [0]
if state == 'Virginia':
    user_input_code['state_va'] = [1]
else:
    user_input_code['state_va'] = [0]
if state == 'Washington':
    user_input_code['state_wa'] = [1]
else:
    user_input_code['state_wa'] = [0]
if state == 'West Virginia':
    user_input_code['state_wv'] = [1]
else:
    user_input_code['state_wv'] = [0]
if state == 'Wisconsin':
    user_input_code['state_wi'] = [1]
else:
    user_input_code['state_wi'] = [0]
if state == 'Wyoming':
    user_input_code['state_wy'] = [1]
else:
    user_input_code['state_wy'] = [0]

user_input_code = user_input_code[['county_pop', 'vet_pop', 'state_va_fac', 'hs_grad_pct', 'clg_grad_pct',
       'median_income', 'poverty_pct', 'unemployment_pct',
       'severe_housing_problems_pct', 'smokers_pct', 'obesity_pct',
       'inactive_pct', 'excess_alcohol_pct', 'diabetes_pct',
       'food_insecure_pct', 'age_under18_pct', 'age_over65_pct', 'rural_pct',
       'state_ak', 'state_al', 'state_ar', 'state_az', 'state_ca', 'state_co',
       'state_ct', 'state_dc', 'state_de', 'state_fl', 'state_ga', 'state_hi',
       'state_ia', 'state_id', 'state_il', 'state_in', 'state_ks', 'state_ky',
       'state_la', 'state_ma', 'state_md', 'state_me', 'state_mi', 'state_mn',
       'state_mo', 'state_ms', 'state_mt', 'state_nc', 'state_nd', 'state_ne',
       'state_nh', 'state_nj', 'state_nm', 'state_nv', 'state_ny', 'state_oh',
       'state_ok', 'state_or', 'state_pa', 'state_ri', 'state_sc', 'state_sd',
       'state_tn', 'state_tx', 'state_ut', 'state_va', 'state_vt', 'state_wa',
       'state_wi', 'state_wv', 'state_wy']]



ss = StandardScaler()
user_input_code_ss = pd.DataFrame(ss.fit_transform(user_input_code))

with open('saved_lasso_model.pkl', 'rb') as f:
    gs = pickle.load(f)
    
def predictor(pred_model, user_input):
      
    model_pred = pred_model.predict(user_input)
    # if model_pred < 0:
    #     return float(np.round((model_pred), 1))
    # if model_pred > 0:
    #     return float(np.round((model_pred), 1))
    return model_pred
    #return user_input_code

with st.spinner('Predicting...'):
    time.sleep(2)
    prediction = predictor(gs, user_input_code_ss)
# st.title('The predicted VA expenditure for this county is $'+str(prediction)+'000')
    st.title(prediction)