import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

def ex_rate():
    def get_exchange(currency_code):
        #currency_code = 'USD'
        last_page_num=10
        df = pd.DataFrame()

        for page_no in range(1,last_page_num+1):
            url =f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{currency_code}KRW&page={page_no}"
            #dfs = pd.read_html(url, encoding='cp949')
            dfs = pd.read_html(url, header=1, encoding='cp949')  #날짜 매매기준 1페이지만 보여지게 하고 싶을 때 

            if dfs[0].empty:
                if (page_no == 1):
                    print(f"통화코드({currency_code})가 잘못 지정되었습니다")
                else:
                    print(f"{page_no}마지막 페이지 입니다.")

                break

            #print(dfs[0])
            df = pd.concat([df, dfs[0]], ignore_index=False)

        return df


    currency_name_dict = {'미국 달러':'USD', '유럽 연합 유료' : 'EUR', '일본 엔':'JPY'}
    # currency_name = st.sidebar.selectbox('통화선택', currency_name_dict.keys())
    # clicked = st.sidebar.button("환율 데이터 가져오기")
    currency_name = st.selectbox('통화선택', currency_name_dict.keys())
    clicked = st.button("환율 데이터 가져오기")

    if clicked:
        currency_code = currency_name_dict[currency_name]
        df_exchange = get_exchange(currency_code)
        #print(df_exchange)

        #원하는 열만 선택 
        df_exchange_rate = df_exchange[['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']]
        df_exchange_rate2 = df_exchange_rate.set_index('날짜')


        #날짜열의 데이터 변경 
        df_exchange_rate2.index = pd.to_datetime(df_exchange_rate2.index, format='%Y-%m-%d', errors='ignore')

        #환율 데이터 표시 
        st.subheader(f"{currency_name}환율 데이터")
        st.dataframe(df_exchange_rate2.head(20))




        #차트(선 그래프) 그리기 
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'

        ax = df_exchange_rate2['매매기준율'].plot(figsize=(15,5), grid=True)
        ax.set_title("환율 매매 기준율 그래프", fontsize=25)
        ax.set_xlabel("기간", fontsize = 10)
        ax.set_ylabel(f"원화/{currency_name}", fontsize = 10)
        plt.xticks(fontsize = 10)  #x축 눈금 값의 폰트 사이즈
        plt.yticks(fontsize = 10)  #y축 눈금 값 폰트 사이즈 
        fig = ax.get_figure()   #fig 객체 가져오기
        st.pyplot(fig)

        # df_exchange_rate2.info()

        #파일 다운로드 
        st.text("** 환율 데이터 파일 다운로드**")

        #dataframe 데이털를 csv 데이터 변환
        csv_data = df_exchange_rate.to_csv()

        #dataframe  데이터를 엑셀 데이터 변환 
        excel_data = BytesIO()  #메모리 버퍼(임시장소)에 바이너리 객체 생성 
        df_exchange_rate.to_excel(excel_data)   #엑셀 형식으로 버퍼에 쓰겠다는 의미 

        col = st.columns(2)  #2개의 세로단 생성 
        with col[0] : 
            st.download_button("CSV 파일 다운로드", csv_data, file_name='exchange_rate_data.csv')
        with col[1] : 
            st.download_button("엑셀 파일 다운로드", excel_data, file_name='exchange_rate_data.xlsx')    



    #else:
    #   pass


