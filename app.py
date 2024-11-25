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
      st.image('시각화1.png' ) 
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' ) 


# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 아래의 순서에 따라 내용을 작성해주세요!')

a = st.number_input(' 나이(age) 입력 ', value=0)  
b = st.number_input(' 성별 입력(sex) ',(남자:0 , 여자:1)',[0,1])
c = st.number_input(' 흉통 유형 입력(cp) ', value=0)  
d = st.number_input(' 평상시 혈압 입력(trestbps) ', value=0)  
if st.button('합불분류'):             
        input_data = [[ a,b,c,d ]]          
        p = model.predict(input_data)     
        if p[0] == 1 :
              st.success('당신의 심장병입니다!')
        else:
              st.success('당신은 심장병이 아닙니다!')

