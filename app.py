import streamlit as st


st.set_page_config(
    page_title="Student Performance ML",
    page_icon="🎓",
    layout="wide"
)


# =========================
# CSS
# =========================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #b84f70;
    margin-top: 50px;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #6f6267;
    margin-bottom: 40px;
    font-weight: 400;
}

.info-card {
    padding: 28px 25px;
    border-radius: 16px;
    background: linear-gradient(
        145deg,
        #fff8fa 0%,
        #fff1f5 100%
    );
    border: 1px solid #f0ccd6;
    margin-bottom: 20px;
    min-height: 150px;
    box-shadow: 0 4px 14px rgba(184, 79, 112, 0.08);
    transition: all 0.2s ease;
}

.info-card:hover {
    border-color: #d96b8a;
    box-shadow: 0 6px 18px rgba(184, 79, 112, 0.13);
    transform: translateY(-2px);
}

.info-card h3 {
    color: #b84f70;
    font-size: 21px;
    font-weight: 650;
    margin-bottom: 12px;
}

.info-card p {
    color: #5f5559;
    font-size: 16px;
    line-height: 1.7;
    margin: 0;
}


/* =========================
   Divider
========================= */

hr {
    border: none;
    border-top: 1px solid #f0d5dd;
    margin: 25px 0;
}


/* =========================
   Streamlit Info Box
========================= */

[data-testid="stAlert"] {
    background-color: #fff5f8;
    border: 1px solid #f0ccd6;
    color: #704b58;
    border-radius: 12px;
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
   General Text
========================= */

.stMarkdown {
    color: #3f373a;
}


/* =========================
   Button
========================= */

.stButton > button {
    border: 1px solid #d96b8a;
    border-radius: 10px;
    background-color: #ffffff;
    color: #b84f70;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #d96b8a;
    color: white;
    border-color: #d96b8a;
}


/* =========================
   Metric
========================= */

[data-testid="stMetric"] {
    background: #fff7f9;
    border: 1px solid #f0d5dd;
    border-radius: 12px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #765d65;
}

[data-testid="stMetricValue"] {
    color: #b84f70;
}


/* =========================
   Selectbox / Input
========================= */

[data-baseweb="select"] > div {
    border-radius: 9px;
    border-color: #e8c5cf;
}

input {
    border-radius: 9px !important;
}


/* =========================
   Expander
========================= */

[data-testid="stExpander"] {
    border: 1px solid #f0ccd6;
    border-radius: 12px;
    background: #fffafb;
}

[data-testid="stExpander"] summary {
    color: #b84f70;
    font-weight: 600;
}


/* =========================
   Success
========================= */

[data-testid="stAlert"][kind="success"] {
    border-left-color: #c45d7c;
}


/* =========================
   Page spacing
========================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Home
# =========================

st.markdown(
    '<div class="main-title">🎓 Student Performance ML</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'ระบบวิเคราะห์และทำนายผลการเรียนของนักเรียนด้วย Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


st.divider()


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📊 Dataset</h3>
        <p>
        วิเคราะห์ข้อมูลนักเรียนจำนวน 395 รายการ
        และ 33 ตัวแปร
        </p>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 Machine Learning</h3>
        <p>
        เปรียบเทียบ Decision Tree, KNN,
        SVM และ Random Forest
        </p>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🔮 Prediction</h3>
        <p>
        ทำนายว่านักเรียนมีแนวโน้ม
        ผ่านหรือไม่ผ่าน
        </p>
    </div>
    """, unsafe_allow_html=True)


# st.markdown("### 📌 วัตถุประสงค์ของโครงงาน")

# st.write("""
# โครงงานนี้มีวัตถุประสงค์เพื่อศึกษาการประยุกต์ใช้
# Machine Learning ในการวิเคราะห์ปัจจัยที่เกี่ยวข้องกับ
# ผลการเรียนของนักเรียน และสร้างระบบสำหรับทำนายว่า
# นักเรียนมีแนวโน้มที่จะผ่านหรือไม่ผ่านเกณฑ์ที่กำหนด
# """)


st.info(
    "💡 สามารถเลือกหัวข้อต่าง ๆ ได้จากเมนูด้านซ้าย"
)