import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import io
from streamlit_folium import folium_static
import folium
import json
import plotly.express as px
from PIL import Image #폴더 내 이미지 보여주기


# 페이지 제목
st.title('서울시 아파트 전세가격 예측프로젝트')
# Font Awesome 라이브러리 링크 추가

# Header 적용
st.header('1. 문제정의')
st.markdown('**목표**: 서울시 내 다양한 변수(위치, 면적, 주변 시설 등)를 고려하여 아파트의 전세 가격을 예측하는 모델 개발.')
st.markdown('**배경**: 서울시 아파트 매물은 다양한 요인에 의해 전세 가격 결정, 이를 정확히 예측하는 것은 임대인과 임차인 모두에게 유익하다. 정확한 예측 모델을 통해 투자자와 정책 결정자에게도 유익한 정보를 제공할 수 있다.')

st.header('2. 기대효과')
st.markdown('전세 가격 예측 모델을 통해 임대인과 임차인이 보다 **합리적인 가격 결정**을 할 수 있도록 지원.')
st.markdown('부동산 시장의 투명성 향상 및 안정화에 기여.')
st.markdown('정책 결정자에게 시장 동향을 분석하고 예측하는 데 필요한 근거 자료 제공.')

st.header('3. 해결방안')
st.markdown('서울 열린데이터 광장, 국토교통부 사이트 등에서 서울시 아파트 관련 데이터 수집.')
st.markdown('데이터 전처리 과정을 통해 누락 데이터 처리, 이상치 제거, 외부 데이터 추가 수행.')
st.markdown('다양한 머신러닝 알고리즘(다중 선형 회귀, 그래디언트 부스팅, 랜덤 포레스트 등)을 사용하여 전세 가격 예측 모델 생성 및 성능 비교.')

st.header('4. 예측값 측정')
st.markdown('모델의 성능 평가를 위해 R-squared(결정 계수), RMSE(평균 제곱근 오차), MAE(평균 절대 오차), MSE(평균 제곱 오차) 등의 지표를 사용.')
st.markdown('그리드 서치를 이용한 하이퍼파라미터 조정.')
st.markdown('각 변수에 대한 최적의 인코딩 기법 선정')

st.header('5. 사례적용')
st.markdown('개발된 모델을 활용하여 사용자가 입력한 조건에 따른 예상 전세 가격을 제공 및 자치구별 특성에 맞춘 시장분석')
st.markdown('시간의 흐름에 따른 전세가와 여론 분석')

st.header('6. 주요 코드')
st.markdown('**판다스, 사이킷런, 플롯리, 스트림릿, 웹크롤링**')
sample_code = '''
def function():
    print('hello, world')
'''

tab1, tab2, tab3, tab4 = st.tabs(['Data', 'EDA', 'Folium', 'Web Crawling'])
tab5, tab6, tab7, tab8 = st.tabs(['모델링(1)', '모델링(2)', '모델링(3)', '모델링(4)'])


with tab1:
    df1 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_아파트_전세_17~24_결측치 수정.csv", encoding='utf-8')
    df2 = pd.read_excel("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_아파트_전세_키워드_1923.xlsx")
    df3 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/구별추가자료_완성.csv", encoding='utf-8')


    # 페이지 제목
    st.title('데이터 소개 & 수집방안')

    st.header('1. 서울시 아파트 전세 데이터')
    st.text('서울 열린 데이터 광장 - 부동산 전월세가 데이터')
    df1 =pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/진짜 최종/18-23 서울시 전세자료.csv", encoding='utf-8')
    st.dataframe(df1, use_container_width=True)

    st.header('2. 2017~2024 뉴스 키워드')
    st.text('Naver기사 웹 크롤링')
    df2 = pd.read_excel("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/키워드/Keyword1819.xlsx")
    st.dataframe(df2, use_container_width=True)
  
    st.header('3. 서울시 구별 추가자료')
    st.text('서울 열린 데이터 광장')
    df3 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시 안심이 CCTV 연계 현황(수정).csv", encoding='utf-8')
    st.dataframe(df3, use_container_width=True)


with tab2:
    Seoul_df1 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_평당가.csv", encoding='utf-8')
    Sagu_df1 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울사구_평당가.csv", encoding='utf-8')
    Seoul_df2 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_증감율.csv", encoding='utf-8')
    Sagu_df2 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울사구_증감율.csv", encoding='utf-8')
    Seoul_df3 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_표준편차.csv", encoding='utf-8')
    Sagu_df3 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울사구_표준편차.csv", encoding='utf-8')
    Seoul_df4 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울시_거래량.csv", encoding='utf-8')
    Sagu_df4 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/서울사구_거래량.csv", encoding='utf-8')
  

    st.title('EDA')
    st.header('1. 평당가 변화')
  
    fig = px.line(data_frame = Seoul_df1, x="접수년도", y="평당 전세가(만원)",
              color_discrete_sequence=["#8B4513"], template='plotly_white')
    fig.update_xaxes(tickvals=Seoul_df1["접수년도"].unique())
    fig.update_layout(title_text="서울시 평당 전세가 변화")
    st.plotly_chart(fig)
  
  

    fig = px.line(data_frame = Sagu_df1, x="접수년도", y="평당 전세가(만원)", color="서울사구",
              color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
    fig.update_xaxes(tickvals=Sagu_df1["접수년도"].unique())
    fig.update_layout(title_text="서울사구 평당 전세가 변화")
    st.plotly_chart(fig)
  
  
    st.header('2. 증감율 변화')
  
    fig = px.bar(data_frame = Seoul_df2, x="접수년도", y="평당 전세가 증감율(%)", text_auto='.0d',
              color_discrete_sequence=["#8B4513"], template='plotly_white')
    fig.update_xaxes(tickvals=Seoul_df2["접수년도"].unique())
    fig.update_layout(title_text="서울시 평당 전세가 증감율")
    st.plotly_chart(fig)
  
  
    fig = px.bar(data_frame = Sagu_df2, x="접수년도", y="증감율", barmode='group', color = '서울사구', text_auto='.0d',
              color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
    fig.update_xaxes(tickvals=Sagu_df2["접수년도"].unique())
    fig.update_yaxes(title_text="평당 전세가 증감율(%)")
    fig.update_layout(title_text="서울사구 평당 전세가 증감율")
    st.plotly_chart(fig)


  
  
    st.header('3. 평당가 표준편차')
  
    fig = px.bar(data_frame = Seoul_df3, x="접수년도", y="평당 전세가(만원)", text_auto='.0d',
              color_discrete_sequence=["#8B4513"], template='plotly_white')
    fig.update_xaxes(tickvals=Seoul_df3["접수년도"].unique())
    fig.update_layout(title_text="서울시 전세금 표준편차")
    st.plotly_chart(fig)
  
    fig = px.bar(data_frame = Sagu_df3, x="접수년도", y="평당 전세가(만원)", barmode='group', text_auto='.0d', color="서울사구",
              color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
    fig.update_xaxes(tickvals=Sagu_df3["접수년도"].unique()) 
    fig.update_layout(title_text="서울사구 전세금 표준편차")
    st.plotly_chart(fig)
  

  
    st.header('4. 거래량')
  
    fig = px.bar(data_frame = Seoul_df4, x="접수년도", y="자치구명", text_auto='.0d',
              color_discrete_sequence=["#8B4513"], template='plotly_white')
    fig.update_xaxes(tickvals=Seoul_df4["접수년도"].unique()) 
    fig.update_yaxes(title_text="거래량")
    fig.update_layout(title_text="서울시 건물 거래량")
    st.plotly_chart(fig)
  
    fig = px.bar(data_frame = Sagu_df4, x="접수년도", y="자치구명", barmode='group', text_auto='.0d', color="서울사구",
              color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
    fig.update_xaxes(tickvals=Sagu_df4["접수년도"].unique())
    fig.update_yaxes(title_text="거래량")
    fig.update_layout(title_text="서울사구 건물 거래량")
    st.plotly_chart(fig)


with tab3:
    st.title('Python과 Folium을 활용한 서울 자치구별 부동산 가격 지도 시각화')
    geo_path = "C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/seoul_municipalities_geo.json"
    geo_json = json.load(open(geo_path, encoding='utf-8'))

    add1 = pd.read_csv("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/구별추가자료_완성.csv", encoding='utf-8')
    add1 = add1.drop(['Unnamed: 0'], axis=1)


    f = folium.Figure(width=700, height=500)
    m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)
    

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    col13, col14, col15 = st.columns(3)

    with col1:
     st.header("공공안전시설_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '공공안전시설_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 공공안전시설_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)

    with col2:
     st.header("혐오시설_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '혐오시설_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 혐오시설_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col3:
     st.header("범죄발생_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '범죄발생_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 범죄발생_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col4:
     st.header("사설학원_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '사설학원_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 사설학원_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col5:
     st.header("공공체육시설_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '공공체육시설_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 공공체육시설_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col6:
     st.header("문화시설_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '문화시설_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 문화시설_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col7:
     st.header("지하철역_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '지하철역_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 지하철역_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col8:
     st.header("시내버스정류장_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '시내버스정류장_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 시내버스정류장_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col9:
     st.header("초/중/고_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '초/중/고_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 초/중/고_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col10:
     st.header("어린이집_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '어린이집_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 어린이집_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col11:
     st.header("병원_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '병원_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 병원_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col12:
     st.header("공원_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '공원_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 공원_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col13:
     st.header("관광명소_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '관광명소_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 관광명소_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
 
    with col14:
     st.header("관공서_총계")
     folium.Choropleth(
         geo_data=geo_json,
         data=add1,
         columns=['자치구명', '관공서_총계'],
         key_on='properties.name',
         fill_color='YlGnBu',
         fill_opacity=0.7,
         line_opacity=0.7,
         legend_name='서울시 구별 관공서_총계'
     ).add_to(m)

     # Streamlit에서 지도 표시
     folium_static(m)
     

with tab4:
    st.title('2017~2024 서울시 아파트 전세 뉴스 웹 크롤링')
    img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/Word.png")
    st.image(img) 

  
with tab5:
  #tab B를 누르면 표시될 내용 
  st.header('[데이터 전처리]') 
  st.subheader('(1) 결측치 처리')  
  st.write('> 건축년도: 자치구별 건축년도 최빈값 대체')
  
    # 코드 표시
  sample_code = '''
  # 자치구별 최빈값 구하기 (딕셔너리 형태) {'자치구명':'건축년도'의 최빈값}
  year_mode = s_df.groupby('자치구명')['건축년도'].agg(lambda x:x.mode()[0]).to_dict()
  '''
  st.code(sample_code, language="python")

    # 코드 표시
  sample_code = '''
  # 건축년도의 결측치 자치구별 최빈값으로 대체
  s_df['건축년도'].fillna(s_df['자치구명'].map(year_mode), inplace=True)
  '''
  st.code(sample_code, language="python")
  
  st.write('> 본번/부번: NULL인 데이터 삭제')
  
    # 코드 표시
  sample_code = '''
  # NULL이 아닌 데이터만 뽑아 새로운 데이터프레임 정의
  s_df = Seoul_df[s_df['본번'].notnull() & s_df['부번'].notnull()]
  # NULL 데이터 삭제 확인
  s_df.isna().sum()
  '''
  st.code(sample_code)
  
  
  st.markdown('---')
  
  st.header('[예측 모델]')
  st.subheader('1. 다중선형회귀')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/1차 다중선형회귀.png")
  st.image(img)
  st.subheader('▷ MAE: 11012.77 / :blue[RMSE: 16842.94] / :red[R2 SCORE: 0.69]')
  
  st.subheader('2. Gradient Boost')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/1차 Gradient Boost.png")
  st.image(img)
  st.subheader('▷ MAE: 8658.48 / :blue[RMSE: 13181.15] / :red[R2 SCORE: 0.81]')
  
  st.subheader('3. Random Forest')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/1차 Random Forest.png")
  st.image(img)
  st.subheader('▷ MAE: 5707.2 / :blue[RMSE: 10067.29] / :red[R2 SCORE: 0.89]')
  
  
  st.markdown('위 3가지 모델 中 성능이 가장 좋은 **Random Forest** 모델로 선정')
  
with tab6:
  #tab B를 누르면 표시될 내용 
  st.header('[데이터 전처리]')
  st.subheader('(1) 이상치 처리')
  st.write('> 층: 1층 ~ 40층')
  st.write('> 임대면적: 200평 이하')
  st.write('> 평당 전세가: 2000만원 이하')
  st.write('> 전세가: 30억원 이하')


      # 코드 표시
  sample_code = '''
  s_df = s_df[(s_df['층'] >= 1) & (s_df['층'] <= 40) 
  & (s_df['임대면적'] <= 150) & (s_df['평당전세가(만원)'] <= 2000
  & (s_df['전세가(만원)'] <= 300000)]
  '''  
  st.code(sample_code, language="python")  
  
  
  st.markdown('---')
  
  st.header('[예측 모델]_Random Forest')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/2차 Random Forest.png")
  st.image(img)
  st.subheader('▷ MAE: 5580.58 / :blue[RMSE: 9436.63] / R2 SCORE: 0.89')
  
  
with tab7:
  #tab B를 누르면 표시될 내용 
  st.header('[데이터 전처리]')
  st.subheader('(1) 추가 변수 투입')
  st.write('> 본번/부번 & 건물명 컬럼 추가 (Binary Encoding 처리)')
  
    # 코드 표시
  sample_code= '''
  # 본번/부번 float -> category 변환 후 인코딩
  df['본번'] = df['본번'].astype('category')
  df_encoded1 = bn_ec.fit_transform(df['본번'])
  df = pd.concat([df, df_encoded1], axis=1)

  df['부번'] = df['부번'].astype('category')
  df_encoded2 = bn_ec.fit_transform(df['부번'])
  df = pd.concat([df, df_encoded2], axis=1)

  df_encoded3 = bn_ec.fit_transform(df[['건물명']])
  df = pd.concat([df, df_encoded3], axis=1)

  '''
  st.code(sample_code, language="python")  
  
  st.markdown('---')
  
  st.header('[예측 모델]_Random_Forest')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/3차 Random Forest.png")
  st.image(img)
  st.subheader('▷  MAE:  5423.93 / :blue[RMSE:  9222.88] / R2 SCORE: 0.89')

  
with tab8:
  #tab B를 누르면 표시될 내용 
  st.header('[데이터 전처리]')
  st.subheader('(1) 외부데이터 1차 추가')
  st.write('> CCTV현황, 지하철역 포함 8개 신규 컬럼 자치구명별 그룹화하여 생성')
  
    # 코드 표시
  sample_code = '''
  Final1 = pd.merge(s_df, additional_df1, how = 'left', on = '자치구명')
  ''' 
  st.code(sample_code, language="python") 
 
  st.subheader('(2) 외부데이터 2차 추가')
  st.write('> 학교, 병원 포함 7개 신규 컬럼 자치구명별 그룹화하여 생성')
  
    # 코드 표시
  sample_code = '''
  Final2 = pd.merge(Final1, additional_df2, how = 'left', on = '자치구명')
  ''' 
  st.code(sample_code, language="python")  
  
  st.subheader('(3) Grid Search 활용한 하이퍼마라미터 튜닝')
  
    # 코드 표시
  sample_code = '''
  param_grid = {
    'n_estimators': [100, 120, 140],  # 의사 결정 나무의 개수
    'max_depth': [None, 2, 4, 6],  # 트리의 최대 깊이
    'min_samples_split': [4, 6, 8]  # 내부 노드를 분할하는데 필요한 최소 샘플 수
    }

  ''' 
  st.code(sample_code, language="python")    
  
  st.markdown('최적의 파라미터: **n_estimator: 140 / max_depth: NONE / min_samples_split: 8** 도출')
  
  st.markdown('---')
  
  st.header('[예측 모델]_Random Forest')
  st.write('> 외부데이터 1차 투입')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/4차 Random Forest (1).png")
  st.image(img)
  st.subheader('▷ MAE: 5425.27 / :blue[RMSE: 9227.96] / R2 SCORE: 0.89')
  
  st.write('> 외부데이터 2차 투입')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/4차 Random Forest (2).png")
  st.image(img)
  st.subheader('▷ MAE: 5421.16 / :blue[RMSE: 9215.95] / R2 SCORE: 0.89')
  
  st.write('> Grid Search 하이퍼마라미터 튜닝')
  img = Image.open("C:/Users/정도영/Desktop/서울시 전세 분석 프로젝트/머신러닝/4차 Random Forest (3).png")
  st.image(img)
  st.subheader('▷ MAE: 5227.06 / :blue[RMSE: 8798.74] / R2 SCORE: 0.9')
  
  import plotly.graph_objects as go

  def main():
     # feature importances
      importances = [37.48, 33.14, 10.95, 5.6, 2.65,
                   1.02, 0.07, 0.48, 0.35, 
                   0.31, 0.24, 0.24, 0.023, 0.23, 0.22]

      variables = ['법정동명te', '임대면적', '건축년도le', '접수년도le', '층',
                 '학원 및 독서실', 'cctv수', '시내버스정류장수', '범죄발생건수',
                 '병원수', '부번_8', '관공서수', '문화시설수', '관광명소수', '본번_7']

      importances, variables = zip(*sorted(zip(importances, variables), reverse=True))

      data = go.Bar(x=importances[::-1], y=variables[::-1], orientation='h')

      layout = go.Layout(title='Feature Importances',
                       xaxis=dict(title='Importance'),
                       yaxis=dict(title='Variables'))

      fig = go.Figure(data=data, layout=layout)

      st.plotly_chart(fig)

  if __name__ == "__main__":
      main()
'''
with tab9:
  col1, col2= st.columns(2)
  with col1:
    st.header("고객1. 제시 린가드")
    st.subheader('"안녕 BRO! 나 왔다 FC Seoul! 원한다 집! 조건 전세!"')
    
    st.markdown('---')
    
    st.subheader('조건')
    st.write('> 상암월드컵경기장 반경 5km 내')
    st.write('> 30-40평 대 규모 선호')
    st.write('> 젊음을 느낄 수 있고, 지하철역이 인접한 곳')
    st.write('> FC 서울에서 받는 연봉 내에서 전세금 해결')
    
    
  with col2:
    img = Image.open("C:/Users/정도영/Downloads/IMG_3440.PNG")
    st.image(img)

    
with tab10:
  col1, col2= st.columns(2)
  with col1:
    st.header("고객2. 티모시 샬라메")
    st.subheader('"영화 웡카와 듄2으로 한국활동을 시작하려고 합니다. 한국스러운 좋은 집을 찾고싶네요"')
    
    st.markdown('---')
    
    st.subheader('조건')
    st.write('> 서울 스케줄을 다니기 무리없는 위치')
    st.write('> 혼자 살 예정이어서 10-20평 대 작은 규모 선호')
    st.write('> 화려함이 아닌 옛스러움을 느낄 수 있는 지역')
    st.write('>  ')
    
    
  with col2:
    img = Image.open("C:/Users/정도영/Downloads/IMG_3443.PNG")
    st.image(img)
with tab11:
  st.title('추가예정')
    
with tab12:
  #tab B를 누르면 표시될 내용 
  st.title('프로젝트를 마무리하며...')
  st.header('한계점')
  st.write('> :blue[팀원의 이탈]로 인한 역할 배분의 어려움') 
  st.write('> 전세 매물의 :blue[구체적인 사항(방의 갯수, 인테리어 등)]을 파악하지 못함')
  
  st.header('좋았던 점')

  st.write('> SQL, Python으로 모든 과정을 직접 진행하며 스스로 :red[부족한 부분을 파악하고 많은 실력 향상]을 이루어냄')
  st.write('> :red[새로운 라이브러리들과 머신러닝]을 직접 사용해본 경험')
  st.write('> 가상의 데이터가 아닌 :red[실생활 데이터]를 이용한 경험')
  st.write('> 여러 머신러닝 모델을 실험하고 비교 분석하는 과정에서 모델 성능 평가 지표에 대한 깊은 이해를 얻음')
  st.write('> Grid Search를 샘플링을 통해 데이터 크기를 줄여 성공한 점')
  st.write('> 임정 튜터님 강의에서 배운 :red[전처리의 중요성]을 정말 뼈저리게 경험')
  ''' 