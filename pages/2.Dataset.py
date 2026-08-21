import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Dataset",
    page_icon="📊",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* =========================
   Page
========================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}


/* =========================
   Title
========================= */

h1 {
    color: #b84f70 !important;
    font-weight: 700 !important;
}

h2 {
    color: #b84f70 !important;
    font-weight: 650 !important;
}

h3 {
    color: #b84f70 !important;
    font-weight: 650 !important;
}


/* =========================
   Divider
========================= */

hr {
    border: none;
    border-top: 1px solid #f0d5dd;
    margin: 28px 0;
}


/* =========================
   Normal Text
========================= */

p {
    color: #51484c;
    line-height: 1.8;
}


/* =========================
   Info Box
========================= */

[data-testid="stAlert"] {
    background: linear-gradient(
        145deg,
        #fff8fa 0%,
        #fff1f5 100%
    );

    border: 1px solid #f0ccd6;
    border-radius: 14px;

    color: #5f4a52;
}


/* =========================
   Metric Cards
========================= */

[data-testid="stMetric"] {
    background: #fff8fa;

    border: 1px solid #f0ccd6;
    border-radius: 15px;

    padding: 20px 22px;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.07);

    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    border-color: #d96b8a;

    box-shadow:
        0 6px 18px rgba(184, 79, 112, 0.12);

    transform: translateY(-2px);
}

[data-testid="stMetricLabel"] {
    color: #80636d !important;
    font-weight: 500;
}

[data-testid="stMetricValue"] {
    color: #b84f70 !important;
    font-weight: 700;
}


/* =========================
   DataFrame
========================= */

[data-testid="stDataFrame"] {
    border: 1px solid #f0ccd6;
    border-radius: 12px;
    overflow: hidden;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.06);
}


/* =========================
   Table Header
========================= */

[data-testid="stDataFrame"] thead th {
    background-color: #fff1f5 !important;
    color: #b84f70 !important;
    font-weight: 600 !important;
}


/* =========================
   Chart Container
========================= */

[data-testid="stVegaLiteChart"] {
    background: #fffafb;

    border: 1px solid #f0d5dd;
    border-radius: 14px;

    padding: 12px;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.05);
}


/* =========================
   Caption
========================= */

[data-testid="stCaptionContainer"] {
    color: #806d74;
}


/* =========================
   Sidebar
========================= */

[data-testid="stSidebar"] {
    background: #fff8fa;
    border-right: 1px solid #f0d5dd;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #b84f70;
}


/* =========================
   Selection / Focus
========================= */

[data-baseweb="select"] > div {
    border-color: #e8c5cf;
    border-radius: 9px;
}

input:focus {
    border-color: #d96b8a !important;
}


/* =========================
   General
========================= */

.stMarkdown {
    color: #51484c;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Title
# =========================

st.title("📊 Dataset & การกำหนดปัญหา")

st.divider()


# =========================
# Problem Definition
# =========================

st.header("1. การกำหนดปัญหา")

st.write("""
งานนี้มีวัตถุประสงค์เพื่อศึกษาปัจจัยที่เกี่ยวข้องกับ
ผลการเรียนของนักเรียน และประยุกต์ใช้ Machine Learning
เพื่อจำแนกว่านักเรียนมีแนวโน้มที่จะ “ผ่าน” หรือ “ไม่ผ่าน”
เกณฑ์ที่กำหนด
""")


st.subheader("โจทย์ของ Machine Learning")

st.info("""
**ประเภทปัญหา:** Classification

**Target:** ผลการเรียนของนักเรียน

- คะแนน G3 ≥ 10 → ผ่าน
- คะแนน G3 < 10 → ไม่ผ่าน
""")


# =========================
# Dataset
# =========================

st.header("2. Dataset")

st.write("""
Dataset ที่ใช้ในการทดลองคือข้อมูลผลการเรียนของนักเรียน
ซึ่งประกอบด้วยข้อมูลด้านการศึกษา ครอบครัว พฤติกรรม
การใช้ชีวิต และผลการเรียน
""")


# Dataset statistics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("จำนวนข้อมูล", "395")

with col2:
    st.metric("จำนวนตัวแปร", "33")

with col3:
    st.metric("ผ่าน", "265")

with col4:
    st.metric("ไม่ผ่าน", "130")


# =========================
# Why this dataset?
# =========================

st.subheader("เหตุผลที่เลือก Dataset นี้")

st.write("""
Dataset นี้เหมาะสำหรับการทำ Machine Learning เนื่องจากมี
ข้อมูลหลายด้านที่อาจมีความสัมพันธ์กับผลการเรียน เช่น
เวลาในการเรียน จำนวนครั้งที่ตกวิชา การขาดเรียน
ความสัมพันธ์ในครอบครัว และพฤติกรรมการใช้ชีวิต

ข้อมูลเหล่านี้สามารถนำมาใช้เป็น Features เพื่อสร้างโมเดล
สำหรับจำแนกกลุ่มนักเรียนที่มีแนวโน้มผ่านหรือไม่ผ่านได้
""")


# =========================
# Dataset structure
# =========================

st.subheader("ตัวแปรที่ใช้ในการวิเคราะห์")

features = [
    "school",
    "sex",
    "age",
    "address",
    "famsize",
    "Pstatus",
    "Medu",
    "Fedu",
    "Mjob",
    "Fjob",
    "reason",
    "guardian",
    "traveltime",
    "studytime",
    "failures",
    "schoolsup",
    "famsup",
    "paid",
    "activities",
    "nursery",
    "higher",
    "internet",
    "romantic",
    "famrel",
    "freetime",
    "goout",
    "Dalc",
    "Walc",
    "health",
    "absences"
]

feature_df = pd.DataFrame({
    "ลำดับ": range(1, len(features) + 1),
    "Feature": features
})

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True
)


# =========================
# Target distribution
# =========================

st.subheader("การกระจายของข้อมูล Target")

target_data = pd.DataFrame({
    "ผลการเรียน": ["ผ่าน", "ไม่ผ่าน"],
    "จำนวน": [265, 130]
})

st.bar_chart(
    target_data.set_index("ผลการเรียน")
)


st.caption(
    "หมายเหตุ: กำหนดให้ G3 ≥ 10 เป็น 'ผ่าน' และ G3 < 10 เป็น 'ไม่ผ่าน'"
)