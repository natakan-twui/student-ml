import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Data Preprocessing",
    page_icon="⚙️",
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
   Headings
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
   Metric Cards
========================= */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #fff8fa 0%,
        #fff1f5 100%
    );

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
   Success Alert
========================= */

[data-testid="stAlert"] {
    border-radius: 13px;
}

[data-testid="stAlert"][kind="success"] {
    background: #fff7f9;
    border: 1px solid #e9c2cd;
    color: #665057;
}


/* =========================
   Error Alert
========================= */

[data-testid="stAlert"][kind="error"] {
    background: #fff5f7;
    border: 1px solid #e5b7c3;
}


/* =========================
   Info Alert
========================= */

[data-testid="stAlert"][kind="info"] {
    background: #fff7f9;
    border: 1px solid #f0ccd6;
    color: #624d55;
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
   Table
========================= */

[data-testid="stTable"] {
    border: 1px solid #f0ccd6;
    border-radius: 12px;
    overflow: hidden;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.05);
}


/* =========================
   Code Block
========================= */

[data-testid="stCodeBlock"] {
    border: 1px solid #f0d5dd;
    border-radius: 12px;
}


/* =========================
   Code Text
========================= */

code {
    font-family: Consolas, monospace;
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
   Caption
========================= */

[data-testid="stCaptionContainer"] {
    color: #806d74;
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

st.title("⚙️ Data Preprocessing")

st.divider()


# =========================
# Introduction
# =========================

st.header("2. Data Preprocessing")

st.write("""
ก่อนนำข้อมูลเข้าสู่กระบวนการสร้าง Machine Learning Model
จำเป็นต้องตรวจสอบและเตรียมข้อมูลให้อยู่ในรูปแบบที่เหมาะสม
เพื่อให้โมเดลสามารถเรียนรู้ข้อมูลได้อย่างมีประสิทธิภาพ
""")


# =========================
# Data Quality
# =========================

st.subheader("1. ตรวจสอบคุณภาพของข้อมูล")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "จำนวนข้อมูล",
        "395"
    )

with col2:
    st.metric(
        "จำนวน Features",
        "33"
    )

with col3:
    st.metric(
        "Missing Values",
        "0"
    )

with col4:
    st.metric(
        "ข้อมูลซ้ำ",
        "0"
    )


st.success(
    "✓ ไม่พบ Missing Values และไม่พบข้อมูลซ้ำ "
    "จึงไม่จำเป็นต้องลบหรือเติมข้อมูล"
)


# =========================
# Target Creation
# =========================

st.subheader("2. การกำหนด Target")

st.write("""
กำหนดตัวแปรเป้าหมายจากคะแนน G3 ซึ่งเป็นคะแนนสุดท้าย
ของนักเรียน โดยแบ่งออกเป็น 2 กลุ่ม
""")

target_df = pd.DataFrame({
    "เงื่อนไข G3": [
        "G3 ≥ 10",
        "G3 < 10"
    ],
    "Target": [
        "ผ่าน (1)",
        "ไม่ผ่าน (0)"
    ],
    "จำนวน": [
        265,
        130
    ],
    "สัดส่วน": [
        "67.09%",
        "32.91%"
    ]
})

st.table(target_df)


# =========================
# Remove G1 G2 G3
# =========================

st.subheader("3. การเลือก Features")

st.write("""
ในการสร้างโมเดล เราไม่นำ G1, G2 และ G3 มาใช้เป็น Features

โดย G3 ถูกใช้ในการสร้าง Target และ G1 กับ G2 ถูกตัดออก
เพื่อป้องกันไม่ให้คะแนนก่อนหน้าถูกนำมาใช้โดยตรงในการทำนาย
""")


col1, col2 = st.columns(2)

with col1:
    st.markdown("### ❌ ไม่ใช้เป็น Features")

    st.error("""
    G1 — คะแนนช่วงประเมินครั้งที่ 1

    G2 — คะแนนช่วงประเมินครั้งที่ 2

    G3 — คะแนนสุดท้าย
    """)

with col2:
    st.markdown("### ✅ Features ที่ใช้")

    st.success("""
    ข้อมูลด้านประชากร

    ข้อมูลครอบครัว

    ข้อมูลการศึกษา

    พฤติกรรมการเรียน

    พฤติกรรมการใช้ชีวิต

    สุขภาพและการขาดเรียน
    """)


st.info(
    "หลังจากตัด G1, G2 และ G3 ออก "
    "เหลือ Features สำหรับโมเดลทั้งหมด 30 ตัว"
)


# =========================
# Categorical Encoding
# =========================

st.subheader("4. การแปลงข้อมูลประเภทข้อความ")

st.write("""
ข้อมูลบางส่วนเป็นข้อมูลประเภทข้อความ เช่น เพศ อาชีพ
สถานะ และการตอบแบบ Yes/No ซึ่ง Machine Learning
ไม่สามารถนำไปประมวลผลโดยตรงได้

จึงใช้ One-Hot Encoding เพื่อแปลงข้อมูลประเภทหมวดหมู่
ให้อยู่ในรูปแบบตัวเลข
""")


categorical = [
    "school",
    "sex",
    "address",
    "famsize",
    "Pstatus",
    "Mjob",
    "Fjob",
    "reason",
    "guardian",
    "schoolsup",
    "famsup",
    "paid",
    "activities",
    "nursery",
    "higher",
    "internet",
    "romantic"
]

cat_df = pd.DataFrame({
    "ประเภทข้อมูล": categorical
})

st.dataframe(
    cat_df,
    use_container_width=True,
    hide_index=True
)


st.code(
'''ตัวอย่าง

sex

F
M

↓

One-Hot Encoding

sex_F    sex_M
   1        0
   0        1
''',
    language="text"
)


# =========================
# Numerical Scaling
# =========================

st.subheader("5. การปรับมาตรฐานข้อมูลตัวเลข")

st.write("""
ข้อมูลประเภทตัวเลขมีช่วงค่าที่แตกต่างกัน เช่น อายุ
จำนวนครั้งที่ขาดเรียน และเวลาในการเรียน

จึงใช้ StandardScaler เพื่อปรับข้อมูลให้อยู่ในมาตรฐานเดียวกัน
โดยเฉพาะโมเดล KNN และ SVM ที่มีความไวต่อ Scale ของข้อมูล
""")


numerical = [
    "age",
    "Medu",
    "Fedu",
    "traveltime",
    "studytime",
    "failures",
    "famrel",
    "freetime",
    "goout",
    "Dalc",
    "Walc",
    "health",
    "absences"
]

num_df = pd.DataFrame({
    "ประเภทข้อมูล": numerical
})

st.dataframe(
    num_df,
    use_container_width=True,
    hide_index=True
)


st.code(
'''StandardScaler

X_scaled = (X - mean) / standard deviation
''',
    language="text"
)


# =========================
# Train Test Split
# =========================

st.subheader("6. แบ่งข้อมูลสำหรับ Training และ Testing")

st.write("""
หลังจากเตรียมข้อมูลแล้ว จะแบ่งข้อมูลออกเป็น 2 ส่วน
เพื่อใช้สร้างและประเมินโมเดล
""")


col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Training Set",
        "316 records",
        "80%"
    )

with col2:

    st.metric(
        "Testing Set",
        "79 records",
        "20%"
    )


st.code(
'''train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)''',
    language="python"
)


# =========================
# Summary
# =========================

st.subheader("สรุป Data Preprocessing")

summary = pd.DataFrame({
    "ขั้นตอน": [
        "ตรวจสอบ Missing Values",
        "ตรวจสอบข้อมูลซ้ำ",
        "สร้าง Target",
        "ตัด G1, G2, G3 ออกจาก Features",
        "One-Hot Encoding",
        "StandardScaler",
        "Train/Test Split"
    ],
    "ผลลัพธ์": [
        "ไม่พบข้อมูลที่หายไป",
        "ไม่พบข้อมูลซ้ำ",
        "ผ่าน / ไม่ผ่าน",
        "เหลือ 30 Features",
        "แปลงข้อมูล Categorical",
        "ปรับมาตรฐานข้อมูลตัวเลข",
        "80% / 20%"
    ]
})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)


st.success(
    "✓ ข้อมูลผ่านกระบวนการ Preprocessing "
    "และพร้อมสำหรับการสร้าง Machine Learning Model"
)