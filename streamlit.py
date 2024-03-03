import streamlit as st 
import numpy as np 
import joblib,time




st.title("Parkinson Disease Detection")

st.subheader("Enter the Deteails correctly")

# name,MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,
# MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE,status

# input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)


name = st.text_input(
        "Enter Your Name:")

age = st.text_input(
        "Enter Your Age:")

sex = st.text_input(
        "Enter Your Sex:")

if sex.lower()== 'male':
    sex = 1
elif sex.lower() == 'female':
    sex=0
else:
    sex=3

f1 = st.text_input(
        "Enter Your MDVP_Fo(Hz) value:")

f2 = st.text_input(
        "Enter Your MDVP_Fhi(Hz) value:")

f3 = st.text_input(
        "Enter Your MDVP_Flo(Hz) Value:")

f4 = st.text_input(
        "Enter Your MDVP_Jitter(%) VALUE:")

f5 = st.text_input(
        "Enter Your MDVP_Jitter(Abs) value:")

f6 = st.text_input(
        "Enter Your MDVP_RAP value:")

f7 = st.text_input(
        "Enter Your MDVP_PPQ value:")

f8 = st.text_input(
        "Enter Your Jitter_DDP value:")

f9 = st.text_input(
        "Enter Your MDVP_Shimmer value:")

f10 = st.text_input(
        "Enter Your MDVP_Shimmer(dB) value:")

f11 = st.text_input(
        "Enter Your Shimmer_APQ3 Value:")


f12 = st.text_input(
        "Enter Your Shimmer_APQ5 Value:")


f13 = st.text_input(
        "Enter Your MDVP_APQ Value:")


f14 = st.text_input(
        "Enter Your Shimmer_DDA Value:")

# NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE


f15 = st.text_input(
        "Enter Your NHR Value:")

f16 = st.text_input(
        "Enter Your HNR Value:")

f17 = st.text_input(
        "Enter Your RPDE Value:")

f18 = st.text_input(
        "Enter Your DFA Value:")

f19 = st.text_input(
        "Enter Your Spread-1 Value:")

f20 = st.text_input(
        "Enter Your spread-2 Value:")

f21 = st.text_input(
        "Enter Your D2 Value:")

f22 = st.text_input(
        "Enter Your PPE Value:")

x = st.button("submit")
if x:
    if x:
        model = joblib.load('model.pkl')
        p = model.predict(np.array((float(f1),float(f2),float(f3),float(f4),float(f5),float(f6),float(f7)
                                     ,float(f8),float(f9),float(f10),float(f11),float(f12),float(f13),float(f14),float(f15),float(f16)
                                     ,float(f17),float(f18),float(f19),float(f20),float(f21),float(f22))).reshape(1,-1))
        print("streamlit predictions",p[0])
        x = model.predict(np.array((197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,
                                 0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)).reshape(1,-1))
        print(x)
    with st.spinner('Processing your data...'):
        time.sleep(5)
    st.success('Done!')
    st.title("Status:")    
    if p[0] == 0:
        
        st.success("you are perfectly alright....")
    else:                
        st.error("Disease confirmed")
