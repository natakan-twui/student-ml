import streamlit as st


st.set_page_config(
    page_title="ข้อมูลผู้พัฒนา",
    page_icon="👤",
    layout="wide"
)

# =========================
# CSS
# =========================

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* =========================
   Main Title
========================= */

h1 {
    color: #b84f70 !important;
    font-weight: 700 !important;
}

h2 {
    color: #b84f70 !important;
    font-weight: 700 !important;
}

h3 {
    color: #b84f70 !important;
    font-weight: 600 !important;
}


/* =========================
   General Text
========================= */

p {
    color: #4f474a;
    line-height: 1.7;
}


/* =========================
   Divider
========================= */

hr {
    border: none !important;
    border-top: 1px solid #ead5dc !important;
}


/* =========================
   Info Box
========================= */

[data-testid="stAlert"] {
    background-color: #fff7f9 !important;
    border: 1px solid #edcbd5 !important;
    border-radius: 12px !important;
}

[data-testid="stAlert"] p {
    color: #554b4f !important;
}


/* =========================
   Sidebar
========================= */

[data-testid="stSidebar"] {
    background-color: #fff8fa !important;
    border-right: 1px solid #ead5dc !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #b84f70 !important;
}


/* =========================
   Buttons
========================= */

.stButton > button,
.stFormSubmitButton > button {
    background-color: #b84f70 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #a64061 !important;
}


/* =========================
   Metric
========================= */

[data-testid="stMetric"] {
    border: 1px solid #ead5dc;
    border-radius: 12px;
}

[data-testid="stMetricLabel"] {
    color: #80656d !important;
}

[data-testid="stMetricValue"] {
    color: #b84f70 !important;
}


/* =========================
   Dataframe
========================= */

[data-testid="stDataFrame"] {
    border: 1px solid #ead5dc;
    border-radius: 10px;
    overflow: hidden;
}


/* =========================
   Selectbox / Input
========================= */

div[data-baseweb="select"] > div {
    border-color: #e5c5ce !important;
}

div[data-baseweb="select"] > div:focus-within {
    border-color: #b84f70 !important;
    box-shadow: 0 0 0 1px #b84f70 !important;
}

input:focus {
    border-color: #b84f70 !important;
}


/* =========================
   Slider
========================= */

[data-baseweb="slider"] [role="slider"] {
    background-color: #b84f70 !important;
}


/* =========================
   Success / Warning / Error
========================= */

[data-testid="stAlert"][kind="success"] {
    background-color: #fff7f9 !important;
    border-color: #d9bcc5 !important;
}

[data-testid="stAlert"][kind="warning"] {
    background-color: #fffaf3 !important;
    border-color: #ead9bd !important;
}

[data-testid="stAlert"][kind="error"] {
    background-color: #fff5f6 !important;
    border-color: #e6c2c8 !important;
}

</style>
""", unsafe_allow_html=True)

st.title("👤 ข้อมูลผู้พัฒนา")

st.divider()


col1, col2 = st.columns([1, 4], gap="small")


with col1:
    st.image(
        "pages/images/profile.jpg",
        width=220
    )


with col2:
    st.subheader("ข้อมูลผู้พัฒนา")

    st.write("ชื่อ - นามสกุล: นางสาวณฐกาญจน์ โพธิ์ทอง")
    st.write("รหัสนักศึกษา: 664245006")
    st.write("หมู่เรียน: 66/43")


st.divider()


st.subheader("รายละเอียดงาน")

st.write("""
งานนี้เป็นการประยุกต์ใช้ Machine Learning
เพื่อวิเคราะห์ข้อมูลผลการเรียนของนักเรียน
และสร้างระบบสำหรับทำนายว่านักเรียนมีแนวโน้ม
ที่จะผ่านหรือไม่ผ่านเกณฑ์ที่กำหนด
""")