import streamlit as st


st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
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
   Info / Success Box
========================= */

[data-testid="stAlert"] {
    border-radius: 13px;
    border: 1px solid #f0ccd6;
    background: #fff7f9;
    color: #5f4d54;
}

[data-testid="stAlert"][kind="success"] {
    background: #fff7f9;
    border-color: #e9c2cd;
}


/* =========================
   Model Overview Cards
========================= */

.model-card {
    background: linear-gradient(
        145deg,
        #fff8fa 0%,
        #fff1f5 100%
    );

    border: 1px solid #f0ccd6;
    border-radius: 15px;

    padding: 22px 20px;

    min-height: 155px;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.07);

    transition: all 0.2s ease;
}

.model-card:hover {
    border-color: #d96b8a;

    box-shadow:
        0 7px 20px rgba(184, 79, 112, 0.12);

    transform: translateY(-2px);
}


/* =========================
   Code Blocks
========================= */

[data-testid="stCodeBlock"] {
    border: 1px solid #f0d5dd;
    border-radius: 12px;

    box-shadow:
        0 3px 10px rgba(184, 79, 112, 0.04);
}


/* =========================
   Metrics
========================= */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #fff8fa 0%,
        #fff1f5 100%
    );

    border: 1px solid #f0ccd6;
    border-radius: 15px;

    padding: 20px;

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
   Comparison Text
========================= */

.stMarkdown strong {
    color: #b84f70;
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

st.title("🤖 Machine Learning Models")

st.divider()


# =========================
# Introduction
# =========================

st.header("3. การสร้างโมเดล Machine Learning")

st.write("""
หลังจากผ่านขั้นตอน Data Preprocessing แล้ว
ข้อมูลถูกนำมาใช้สร้างและเปรียบเทียบ Machine Learning
จำนวน 4 โมเดล ได้แก่ Decision Tree, K-Nearest Neighbor,
Support Vector Machine และ Random Forest
""")


st.info("""
**ประเภทของปัญหา:** Classification

**เป้าหมาย:** จำแนกนักเรียนออกเป็น 2 กลุ่ม

• ผ่าน (1)

• ไม่ผ่าน (0)
""")


# =========================
# Model Overview
# =========================

st.subheader("โมเดลที่ใช้ในการทดลอง")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    ### 🌳
    **Decision Tree**

    สร้างโครงสร้างต้นไม้
    เพื่อแบ่งข้อมูลออกเป็นกลุ่ม
    """)

with col2:
    st.markdown("""
    ### 📍
    **KNN**

    จำแนกข้อมูลจาก
    เพื่อนบ้านที่อยู่ใกล้ที่สุด
    """)

with col3:
    st.markdown("""
    ### ⚡
    **SVM**

    หาขอบเขตที่เหมาะสมที่สุด
    สำหรับแยกกลุ่มข้อมูล
    """)

with col4:
    st.markdown("""
    ### 🌲
    **Random Forest**

    รวม Decision Tree
    หลายต้นเพื่อเพิ่มความแม่นยำ
    """)


st.divider()


# =========================
# Decision Tree
# =========================

st.header("🌳 1. Decision Tree")

st.write("""
Decision Tree เป็นอัลกอริทึมที่มีโครงสร้างคล้ายต้นไม้
โดยเริ่มจาก Root Node และแบ่งข้อมูลออกเป็นกลุ่มย่อย
ตามคุณลักษณะที่มีความเหมาะสมในการแบ่งข้อมูลมากที่สุด
จนกระทั่งได้ผลลัพธ์ที่ Leaf Node
""")


st.subheader("หลักการทำงาน")

st.markdown("""
1. เริ่มต้นจากข้อมูลทั้งหมดที่ Root Node
2. เลือก Feature ที่สามารถแบ่งข้อมูลได้ดีที่สุด
3. แบ่งข้อมูลออกเป็นกลุ่มย่อย
4. ทำขั้นตอนเดิมซ้ำกับแต่ละกลุ่ม
5. หยุดเมื่อถึงเงื่อนไขที่กำหนด
6. ใช้ Leaf Node เป็นผลลัพธ์ในการจำแนก
""")


st.code(
"""ตัวอย่างแนวคิด

จำนวนครั้งที่ตกวิชา
        │
   ┌────┴────┐
   │         │
  0 ครั้ง   > 0 ครั้ง
   │         │
  ผ่าน      ไม่ผ่าน
""",
    language="text"
)


st.info("""
**ข้อดี:** เข้าใจง่ายและสามารถอธิบายเส้นทางการตัดสินใจได้

**ข้อจำกัด:** หากต้นไม้ซับซ้อนเกินไปอาจเกิด Overfitting
""")


# =========================
# KNN
# =========================

st.header("📍 2. K-Nearest Neighbor (KNN)")

st.write("""
KNN เป็นอัลกอริทึมที่ใช้ระยะห่างระหว่างข้อมูล
ในการจำแนกประเภท โดยจะค้นหาข้อมูลที่อยู่ใกล้กับ
ข้อมูลใหม่จำนวน K ตัว แล้วใช้กลุ่มของเพื่อนบ้าน
ส่วนใหญ่เป็นตัวกำหนดผลลัพธ์
""")


st.subheader("หลักการทำงาน")

st.markdown("""
1. กำหนดค่า K
2. คำนวณระยะห่างระหว่างข้อมูลใหม่กับข้อมูล Training
3. เลือกข้อมูลที่อยู่ใกล้ที่สุดจำนวน K ตัว
4. นับว่ากลุ่มใดมีจำนวนมากที่สุด
5. กำหนดกลุ่มนั้นเป็นผลการทำนาย
""")


st.code(
"""ตัวอย่าง

K = 5

เพื่อนบ้าน:
ผ่าน     ผ่าน     ไม่ผ่าน     ผ่าน     ผ่าน

ผลลัพธ์ → ผ่าน
""",
    language="text"
)


st.info("""
**ข้อดี:** หลักการทำงานง่ายและไม่ต้องสร้างสมการของโมเดลที่ซับซ้อน

**ข้อจำกัด:** ประสิทธิภาพอาจลดลงเมื่อข้อมูลมีจำนวนมาก
หรือ Features มีมิติสูง
""")


# =========================
# SVM
# =========================

st.header("⚡ 3. Support Vector Machine (SVM)")

st.write("""
SVM เป็นอัลกอริทึมที่พยายามหาเส้นหรือ Hyperplane
ที่สามารถแบ่งข้อมูลแต่ละกลุ่มออกจากกันได้ดีที่สุด
โดยพยายามทำให้ระยะห่างระหว่างขอบเขตและข้อมูล
ที่อยู่ใกล้ที่สุดมีค่ามากที่สุด
""")


st.subheader("หลักการทำงาน")

st.markdown("""
1. นำข้อมูลเข้าสู่พื้นที่ Feature Space
2. ค้นหา Hyperplane ที่ใช้แบ่งกลุ่มข้อมูล
3. พิจารณาข้อมูลที่อยู่ใกล้เส้นแบ่งมากที่สุด
4. ขยาย Margin ระหว่างกลุ่มข้อมูล
5. ใช้ Hyperplane ที่ได้สำหรับจำแนกข้อมูลใหม่
""")


st.code(
"""ข้อมูล

ไม่ผ่าน  ● ● ●

              │
              │  Hyperplane
              │
ผ่าน     ● ● ●

←────── Margin ──────→
""",
    language="text"
)


st.info("""
**ข้อดี:** มีประสิทธิภาพกับข้อมูลที่มี Features หลายตัว
และสามารถสร้างขอบเขตการแบ่งกลุ่มที่ซับซ้อนได้

**ข้อจำกัด:** ต้องปรับ Parameter ให้เหมาะสม
และมีความไวต่อ Scale ของข้อมูล
""")


st.success("""
ในงานนี้ SVM ใช้ Kernel แบบ RBF และมีการใช้
StandardScaler ในขั้นตอน Preprocessing
เพื่อให้ข้อมูลอยู่ใน Scale ที่เหมาะสม
""")


# =========================
# Random Forest
# =========================

st.header("🌲 4. Random Forest")

st.write("""
Random Forest เป็น Ensemble Learning ที่รวม
Decision Tree หลายต้นเข้าด้วยกัน โดยแต่ละต้น
จะเรียนรู้จากข้อมูลและ Features ที่แตกต่างกัน
จากนั้นนำผลลัพธ์ของต้นไม้ทั้งหมดมารวมกัน
เพื่อหาผลการทำนายสุดท้าย
""")


st.subheader("หลักการทำงาน")

st.markdown("""
1. สร้าง Decision Tree หลายต้น
2. แต่ละต้นเรียนรู้จากข้อมูลที่สุ่มเลือก
3. แต่ละต้นทำการทำนาย
4. รวมผลการทำนายของทุกต้น
5. ใช้ผลโหวตส่วนใหญ่เป็นคำตอบสุดท้าย
""")


st.code(
"""Decision Tree 1 → ผ่าน
Decision Tree 2 → ผ่าน
Decision Tree 3 → ไม่ผ่าน
Decision Tree 4 → ผ่าน
Decision Tree 5 → ผ่าน

        ↓

ผลโหวตส่วนใหญ่

        ↓

      ผ่าน
""",
    language="text"
)


st.info("""
**ข้อดี:** ลดโอกาสเกิด Overfitting เมื่อเทียบกับ
Decision Tree เพียงต้นเดียว และมีความสามารถ
ในการจัดการ Features หลายประเภท

**ข้อจำกัด:** อธิบายการตัดสินใจได้ยากกว่า Decision Tree
""")


# =========================
# Why Compare These Models?
# =========================

st.divider()

st.header("เหตุผลที่เลือกโมเดลทั้ง 4 แบบ")

st.write("""
โมเดลทั้ง 4 แบบมีแนวคิดในการเรียนรู้ที่แตกต่างกัน
จึงสามารถนำมาเปรียบเทียบประสิทธิภาพในการจำแนก
นักเรียนที่ผ่านและไม่ผ่านได้
""")


comparison = {
    "Decision Tree": "โครงสร้างต้นไม้และกฎการตัดสินใจ",
    "KNN": "ระยะห่างระหว่างข้อมูล",
    "SVM": "Hyperplane และ Margin",
    "Random Forest": "การรวมผลจาก Decision Tree หลายต้น"
}


for model_name, concept in comparison.items():
    st.write(f"**{model_name}** — {concept}")


st.divider()


# =========================
# Experimental Setup
# =========================

st.header("การตั้งค่าการทดลอง")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Training Data",
        "316"
    )

with col2:
    st.metric(
        "Testing Data",
        "79"
    )

with col3:
    st.metric(
        "Models",
        "4"
    )


st.write("""
ทุกโมเดลใช้ Training Set และ Testing Set ชุดเดียวกัน
เพื่อให้สามารถเปรียบเทียบประสิทธิภาพได้อย่างยุติธรรม
""")


st.success(
    "ขั้นตอนถัดไปคือการประเมินและเปรียบเทียบผลลัพธ์ของโมเดล"
)