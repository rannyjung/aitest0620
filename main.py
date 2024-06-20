import streamlit as st
from PIL import Image
import exchage_rate 

# 사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="", type="password")

if user_id =='abc'  and user_password == '1234':

    st.sidebar.header("project")
    selectbox_options = ['환율조회', '머신러닝', '데이터분석'] # 셀렉트 박스의 선택 항목
    your_option = st.sidebar.selectbox('Menu', selectbox_options) # 셀렉트박스의 항목 선택 결과
    st.sidebar.write('**당신의 선택**:', your_option)

    if your_option == "환율조회":
        st.subheader("환율조회")
        exchage_rate.ex_rate()
    elif your_option == "데이터분석":
        pass

    else:
        pass







    # # 메인(Main) 화면
    # st.subheader(your_option, divider='rainbow')

    # folder = 'img/'

    # # selectbox_options의 요소에 따라서 보여줄 이미지 파일 리스트 (selectbox_options의 요소와 순서를 일치시킴)
    # image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'klimt.jpg', 'ShinYoonbok.png'] # 이미지 파일 리스트

    # # 셀렉트박스에서 선택한 항목에 따라 이미지 표시
    # selectbox_options_index = selectbox_options.index(your_option) # selectbox_options의 리스트 인덱스 찾기
    # image_file = image_files[selectbox_options_index] # 선택한 항목에 맞는 이미지 파일 지정
    # image_local = Image.open(folder + image_file)     # PIL 라이브러리의 Image.open() 함수로 이미지 파일 열기
    # st.image(image_local, caption=your_option)        # 이미지 표시