import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="การประเมินโมเดล",
    page_icon="📈",
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
   Alert / Highlight
========================= */

[data-testid="stAlert"] {
    border-radius: 13px;
    border: 1px solid #f0ccd6;
    background: #fff7f9;
    color: #5f4d54;
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
   Charts
========================= */

[data-testid="stArrowVegaLiteChart"],
[data-testid="stVegaLiteChart"],
[data-testid="stPyplot"] {
    background: #ffffff;
    border: 1px solid #f0d5dd;
    border-radius: 14px;

    padding: 12px;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.05);
}


/* =========================
   Selectbox
========================= */

[data-testid="stSelectbox"] {
    margin-bottom: 10px;
}

[data-testid="stSelectbox"] label {
    color: #80636d !important;
    font-weight: 600;
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
   Strong Text
========================= */

.stMarkdown strong {
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

st.title("📈 การประเมินและเปรียบเทียบโมเดล")

st.divider()


# =========================
# Introduction
# =========================

st.header("4. การประเมินและเปรียบเทียบโมเดล")

st.write("""
หลังจากสร้าง Machine Learning ทั้ง 4 โมเดลแล้ว
จึงนำโมเดลมาทดสอบกับ Testing Set จำนวน 79 รายการ
และประเมินประสิทธิภาพด้วย Accuracy, Precision,
Recall และ F1-Score
""")


# =========================
# Model Results
# =========================

results = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "KNN",
        "SVM",
        "Random Forest"
    ],
    "Accuracy": [
        65.82,
        58.23,
        68.35,
        62.03
    ],
    "Precision": [
        70.31,
        66.13,
        70.59,
        67.16
    ],
    "Recall": [
        84.91,
        77.36,
        90.57,
        84.91
    ],
    "F1-Score": [
        76.92,
        71.30,
        79.34,
        75.00
    ]
})


# =========================
# Best Model
# =========================

best_model = results.loc[
    results["Accuracy"].idxmax()
]


st.success(
    f"🏆 โมเดลที่มี Accuracy สูงที่สุดคือ "
    f"**{best_model['Model']}** "
    f"ด้วย Accuracy **{best_model['Accuracy']:.2f}%**"
)


# =========================
# Metrics
# =========================

st.subheader("ผลการประเมินโมเดล")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Decision Tree",
        "65.82%"
    )

with col2:
    st.metric(
        "KNN",
        "58.23%"
    )

with col3:
    st.metric(
        "SVM",
        "68.35%"
    )

with col4:
    st.metric(
        "Random Forest",
        "62.03%"
    )


# =========================
# Comparison Table
# =========================

st.subheader("ตารางเปรียบเทียบประสิทธิภาพ")


display_results = results.copy()

for column in [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-Score"
]:
    display_results[column] = (
        display_results[column].map(
            lambda x: f"{x:.2f}%"
        )
    )


st.dataframe(
    display_results,
    use_container_width=True,
    hide_index=True
)


# =========================
# Chart
# =========================

st.subheader("กราฟเปรียบเทียบประสิทธิภาพของโมเดล")


metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-Score"
]


x = range(len(results["Model"]))

fig, ax = plt.subplots(figsize=(12, 6))

width = 0.18

for i, metric in enumerate(metrics):

    values = results[metric]

    positions = [
        pos + (i - 1.5) * width
        for pos in x
    ]

    ax.bar(
        positions,
        values,
        width,
        label=metric
    )


ax.set_xlabel("Model")
ax.set_ylabel("Score (%)")

ax.set_title(
    "Comparison of Machine Learning Models"
)

ax.set_xticks(list(x))
ax.set_xticklabels(
    results["Model"]
)

ax.set_ylim(0, 100)

ax.legend()

ax.grid(
    axis="y",
    alpha=0.2
)

st.pyplot(fig)


# =========================
# Individual Metrics
# =========================

st.subheader("เปรียบเทียบแต่ละ Metric")


metric_choice = st.selectbox(
    "เลือก Metric",
    metrics
)


metric_df = results[
    ["Model", metric_choice]
].set_index("Model")


st.bar_chart(
    metric_df
)


# =========================
# SVM Highlight
# =========================

st.divider()

st.header("🏆 ผลลัพธ์ของ SVM")

st.write("""
จากผลการทดลองพบว่า SVM ให้ประสิทธิภาพโดยรวมดีที่สุด
เมื่อเปรียบเทียบกับโมเดลอื่นที่นำมาทดลอง
""")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "68.35%"
    )

with col2:
    st.metric(
        "Precision",
        "70.59%"
    )

with col3:
    st.metric(
        "Recall",
        "90.57%"
    )

with col4:
    st.metric(
        "F1-Score",
        "79.34%"
    )


# =========================
# Analysis
# =========================

st.subheader("วิเคราะห์ผลการทดลอง")

st.write("""
SVM มี Accuracy สูงที่สุดที่ 68.35% และมี F1-Score
สูงที่สุดที่ 79.34% เมื่อเทียบกับโมเดลทั้ง 4 แบบ

นอกจากนี้ SVM ยังมี Recall สูงถึง 90.57% ซึ่งหมายความว่า
โมเดลสามารถตรวจจับนักเรียนที่อยู่ในกลุ่ม “ผ่าน” ได้ในสัดส่วนสูง

เมื่อพิจารณา Accuracy, Recall และ F1-Score ร่วมกัน
จึงเลือก SVM เป็นโมเดลที่เหมาะสมที่สุดสำหรับระบบนี้
""")


# =========================
# Ranking
# =========================

st.subheader("อันดับประสิทธิภาพตาม Accuracy")


ranking = results.sort_values(
    "Accuracy",
    ascending=False
).reset_index(drop=True)

ranking.insert(
    0,
    "อันดับ",
    range(1, len(ranking) + 1)
)


ranking_display = ranking.copy()

for column in [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-Score"
]:
    ranking_display[column] = (
        ranking_display[column].map(
            lambda x: f"{x:.2f}%"
        )
    )


st.dataframe(
    ranking_display,
    use_container_width=True,
    hide_index=True
)


st.info("""
สรุป:

🥇 SVM — 68.35%

🥈 Decision Tree — 65.82%

🥉 Random Forest — 62.03%

4️⃣ KNN — 58.23%
""")