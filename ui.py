import streamlit as st
import classify

st.write("""
# Phân loại động vật
         
""")

def user_input_features():
    #input tên
    user_input = st.sidebar.text_input("Tên động vật")
    #tóc
    to_bool = {'Có': 1, 'Không': 0}
    hair = st.sidebar.selectbox('Tóc', ('Có', 'Không'))
    hair_int = to_bool[hair]
    #lông
    feathers = st.sidebar.selectbox('Lông', ('Có', 'Không'))
    feathers_int = to_bool[feathers]
    #trứng
    eggs = st.sidebar.selectbox('Đẻ trứng', ('Có', 'Không'))
    eggs_int = to_bool[eggs]
    #sữa
    milk = st.sidebar.selectbox('Sữa', ('Có', 'Không'))
    milk_int = to_bool[milk]
    #trên ko
    airborne = st.sidebar.selectbox('Trên không', ('Có', 'Không'))
    airborne_int = to_bool[airborne]
    #dưới nước
    aquatic = st.sidebar.selectbox('Dưới nước', ('Có', 'Không'))
    aquatic_int = to_bool[aquatic]
    #ăn thịt
    predator = st.sidebar.selectbox('Ăn thịt', ('Có', 'Không'))
    predator_int = to_bool[predator]
    #có răng ko
    toothed = st.sidebar.selectbox('Răng', ('Có', 'Không'))
    toothed_int = to_bool[toothed]
    #xương sống
    backbone = st.sidebar.selectbox('Xương sống', ('Có', 'Không'))
    backbone_int = to_bool[backbone]
    #thở :)
    breathes = st.sidebar.selectbox('Thở', ('Có', 'Không'))
    breathes_int = to_bool[breathes]
    #có độc
    venomous = st.sidebar.selectbox('Có độc', ('Có', 'Không'))
    venomous_int = to_bool[venomous]
    #vây
    fins = st.sidebar.selectbox('Vây', ('Có', 'Không'))
    fins_int = to_bool[fins]
    #chân
    legs = st.sidebar.selectbox('Số chân', (0,2,4,8))
    #đuôi
    tail = st.sidebar.selectbox('Đuôi', ('Có', 'Không'))
    tail_int = to_bool[tail]
    #bầy đàn
    domestic = st.sidebar.selectbox('Bầy đàn', ('Có', 'Không'))
    domestic_int = to_bool[domestic]
    #kích thước
    to_bool = {'Lớn': 1, 'Nhỏ': 0}
    catsize = st.sidebar.selectbox('Kích thước', ('Lớn', 'Nhỏ'))
    catsize_int = to_bool[catsize]
    #lấy toàn bộ input được nhập trong chương trình (dữ liệu sẽ là array number(vd: 0,1,0,0...))
    data = [
        hair_int,
        feathers_int,
        eggs_int,
        milk_int,
        airborne_int,
        aquatic_int,
        predator_int,
        toothed_int,
        backbone_int,
        breathes_int,
        venomous_int,
        fins_int,
        legs,
        tail_int,
        domestic_int,
        catsize_int
    ]
    #nút bấm
    clicker = st.sidebar.button("Phân loại")
    #xử lý sự kiện khi bấm nút
    if clicker:
        if not user_input:
            st.write("Nhập tên động vật!!!")
        else:
            classification = classify.classify(data)

            animal_type = {
                1: 'Động vật có zú',
                2: 'Loài chim',
                3: 'Bò sad',
                4: 'Cá',
                5: 'Lưỡng cư',
                6: 'Côn trùng',
                7: 'Động vật không xương sống'
            }

            st.subheader('Phân loại')
            st.write(data[0], " là ", animal_type[int(classification[0])])
    return data

input_data = user_input_features()
