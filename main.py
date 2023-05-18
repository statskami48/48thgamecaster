import streamlit as st
from PIL import Image
from streamlit_extras.badges import badge
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title="Statistics 48TH Game Caster", page_icon="🌟", layout="centered")
st.title("48TH Game Caster")
st.subheader("Please Like & Follow")
st.write("https://www.facebook.com/48THGameCaster")


st.markdown("🎮Weekly Schedule : 15-21 MAY 2023👾")
st.image("https://scontent.fbkk26-1.fna.fbcdn.net/v/t39.30808-6/346647020_750356016880035_5170523076902930880_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeGzNninIfmlyTYcliJtKpsnHB6CxzVRObEcHoLHNVE5sbg9Rf-lAj7fyLvbmAE44eE&_nc_ohc=d4uPaP7-o8gAX_l0M-v&_nc_ht=scontent.fbkk26-1.fna&oh=00_AfC0JRgtYS2Exb_ATVhLjjSRfMhDARqECoTv6qFSjIBZTA&oe=646A995D")


#col1, col2 = st.columns(2, gap="small")
#with col1:
    #st.subheader("ย้อนหลัง")

#with col2:


colored_header(
    label="Replay weekly 15-21/5/23",
    description=" 15-21/5/23",
    color_name="violet-70",
)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Lookked.png", width=100)
    st.subheader("Lookked CGM48 20.00-22.00")
    st.write("")
    st.write("Play : ")
    st.write("")
    st.write("")
with col2:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Jingjing.png", width=100)
    st.subheader("Jingjing CGM48 18.00-20.00")
    st.write("")
    st.write("Play : ")
    st.write("")
    st.write("")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Champoo.png", width=100)
    st.subheader("Champoo CGM48 21/5/23 15.00-17.00")
    st.write("")
    st.write("Play : ")
    st.write("")
    st.write("")
with col2:
    st.image("https://www.bnk48.com/data/Members/99/s/20230228042740cjnyz7.png", width=100)
    st.subheader("Emmy BNK48 20/5/23 21.30-23.30")
    st.write("")
    st.write("Play : ")
    st.write("")
    st.write("")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Jayda.png", width=100)
    st.subheader("Jayda CGM48 20/5/23 20.00-21.00")
    st.write("")
    st.write("Play : ")
    st.write("")
    st.write("")
with col2:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Champoo.png", width=100)
    st.subheader("Champoo CGM48 18/5/23 22.30-00.00")
    st.write("นกฮูกพร้อมยางงงง #ChampooCGM48 #CGM48")
    st.write("Play : Roblox")
    st.write("1:16:31")
    st.write("https://www.facebook.com/48THGameCaster/videos/963870701633923")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://www.bnk48.com/data/Members/86/s/20230228050544ahptx3.png", width=100)
    st.subheader("Kaofrang BNK48 18/5/23 20.00-22.00")
    st.write("#คู่หูดาวตก is back #KAOFRANGFIE วันนี้มีผู้ช่วย จะได้(ลด)กี่ดาว ไปดูกัน🥲🥲🥲 #KAOFRANGFIE")
    st.write("Play : Garena RoV Thailand")
    st.write("1:51:33")
    st.write("https://www.facebook.com/48THGameCaster/videos/576987587836064")
with col2:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Kaning.png", width=100)
    st.subheader("Kaning CGM48 18/5/23 21.30-00.00")
    st.write("เข้าครัว")
    st.write("Play : Cooking Simulator")
    st.write("2:24:42")
    st.write("https://www.facebook.com/48THGameCaster/videos/962298395216646")


col1, col2 = st.columns(2)
with col1:
    st.image("https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Marmink.png", width=100)
    st.subheader("Marmink CGM48 16/5/23 19.40-21.20")
    st.write("#MarminkCGM48 มาาาา มา")
    st.write("Play : Roblox")
    st.write("1:31:24")
    st.write("https://www.facebook.com/48THGameCaster/videos/280876511033295")
with col2:
    st.image("https://www.bnk48.com/data/Members/102/s/20230228050730lnz149.png", width=100)
    st.subheader("Marine BNK48 15/5/23 22.00-24.00")
    st.write("ซินดี้สุดสวยมาแร้วค่ะ มาต่อคับ #MarineBNK48 #BNK48")
    st.write("Play : The Bridge Curse Road to Salvation")
    st.write("2:53:06")
    st.write("https://www.facebook.com/48THGameCaster/videos/1444217676389665")



st.warning("updated : 18/5/23 22.00")

link = '[Contact us](https://twitter.com/Stats48TH)'
st.markdown(link, unsafe_allow_html=True)


badge(type="twitter", name="stats48th")
badge(type="buymeacoffee", name="stats48th")
button(username="stats48th", floating=False, width=221)