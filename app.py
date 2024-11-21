# 분류 모델 웹앱 만들기
import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2. 모델 설명
 st.title('심장병 여부 분류')
 st.subheader('모델 설명 ')
 st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
 st.write(' - 학습 데이터 출처 :https://www.kaggle.com/code/desalegngeb/heart-disease-predictions')
 st.write(' - 훈련    데이터 : 212건')
 st.write(' - 테스트 데이터 : 91건')
 st.write(' - 모델 정확도 : 0.89')

# 3. 데이터시각화
col1, col2,col3 = st.columns( 3 ) 
with col1:
      st.subheader('데이터시각화1')
      st.image('____________' ) 
with col2:
      st.subheader('데이터시각화2')
      st.image('____________' ) 
with col3:
      st.subheader('데이터시각화3')
      st.image('____________')    


# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

a = st.number_input(' _________ ', value=0)  
if st.button('합불분류'):             
        input_data = [[ a ]]          
        p = model._______(input_data)     
        if p[0] == 1 :
              st.success('인공지능 분류 결과는 ___입니다')
        else:
              st.success('인공지능 분류 결과를 ____입니다')

