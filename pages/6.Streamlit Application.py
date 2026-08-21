import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Streamlit Application",
    page_icon="🔮",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* =========================
   Page Layout
========================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}


/* =========================
   Main Titles
========================= */

h1 {
    color: #b84f70 !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px;
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
   Text
========================= */

p {
    color: #51484c;
    line-height: 1.8;
}

.stMarkdown {
    color: #51484c;
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
   Caption
========================= */

[data-testid="stCaptionContainer"] {
    color: #806d74;
}


/* =========================
   Info / Success / Error
========================= */

[data-testid="stAlert"] {
    border-radius: 13px;
    border: 1px solid #f0ccd6;
    background: #fff8fa;
}


/* =========================
   Metric Cards
========================= */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #fff9fb 0%,
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
   Form
========================= */

[data-testid="stForm"] {
    background: #ffffff;

    border: 1px solid #f0d5dd;
    border-radius: 18px;

    padding: 30px;

    box-shadow:
        0 5px 20px rgba(184, 79, 112, 0.07);
}


/* =========================
   Form Section Titles
========================= */

[data-testid="stForm"] h3 {
    color: #b84f70 !important;

    padding-bottom: 8px;

    border-bottom: 1px solid #f4dce2;

    margin-top: 12px;
}


/* =========================
   Input Labels
========================= */

[data-testid="stWidgetLabel"] p {
    color: #66545b !important;
    font-weight: 500;
}


/* =========================
   Selectbox
========================= */

[data-baseweb="select"] > div {
    border-radius: 9px;
    border-color: #e8c7d0;
}

[data-baseweb="select"] > div:hover {
    border-color: #d96b8a;
}


/* =========================
   Number Input
========================= */

[data-testid="stNumberInput"] input {
    border-radius: 9px;
}


/* =========================
   Slider
========================= */

[data-testid="stSlider"] {
    padding-top: 5px;
}


/* =========================
   Button
========================= */

.stButton > button,
.stFormSubmitButton > button {
    background: #b84f70;
    color: white;

    border: none;
    border-radius: 10px;

    padding: 10px 20px;

    font-weight: 600;

    transition: all 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #a84263;
    color: white;

    box-shadow:
        0 5px 15px rgba(184, 79, 112, 0.2);

    transform: translateY(-1px);
}


/* =========================
   Prediction Result
========================= */

[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #f0d5dd;
}


/* =========================
   Expander
========================= */

[data-testid="stExpander"] {
    border: 1px solid #f0d5dd;
    border-radius: 12px;
    background: #fffafb;
}

[data-testid="stExpander"] summary {
    color: #b84f70;
    font-weight: 600;
}


/* =========================
   DataFrame
========================= */

[data-testid="stDataFrame"] {
    border: 1px solid #f0d5dd;
    border-radius: 12px;
    overflow: hidden;

    box-shadow:
        0 4px 14px rgba(184, 79, 112, 0.05);
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
    color: #b84f70 !important;
}


/* =========================
   Strong Text
========================= */

.stMarkdown strong {
    color: #b84f70;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Load Model
# =========================

@st.cache_resource
def load_model():
    return joblib.load("student_performance_svm.pkl")


try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model = None
    model_loaded = False
    model_error = str(e)


# =========================
# Title
# =========================

st.title("🎓 Student Performance Prediction")

st.caption("Machine Learning Web Application — SVM Classification")

st.divider()

st.header("5. Streamlit Application")

st.write("""
ระบบสำหรับทำนายผลการเรียนของนักเรียนโดยใช้
Support Vector Machine (SVM)
ที่ผ่านการฝึกและทดสอบจาก Dataset นักเรียน
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 📊 Dataset
    395 รายการ
    """)

with col2:
    st.info("""
    ### 🤖 Model
    SVM
    """)

with col3:
    st.info("""
    ### 🎯 Accuracy
    68.35%
    """)

# =========================
# Model Status
# =========================

if model_loaded:

    st.success(
        "✓ โหลด SVM Model สำเร็จ"
    )

else:

    st.error(
        "ไม่สามารถโหลด Model ได้"
    )

    st.code(
        model_error
    )

    st.stop()


# =========================
# Input Form
# =========================

st.subheader("📝 ข้อมูลนักเรียน")
st.caption(
    "กรุณากรอกข้อมูลให้ครบถ้วน แล้วกดปุ่ม "
    "“ทำนายผลการเรียน”"
)


with st.form("prediction_form"):

    # =====================
    # Personal Information
    # =====================

    st.markdown("### 👤 ข้อมูลทั่วไป")

    col1, col2, col3 = st.columns(3)

    with col1:

        school = st.selectbox(
            "โรงเรียน",
            ["GP", "MS"]
        )

        sex = st.selectbox(
            "เพศ",
            ["F", "M"]
        )

        age = st.number_input(
            "อายุ",
            min_value=15,
            max_value=25,
            value=17
        )

    with col2:

        address = st.selectbox(
            "ที่อยู่",
            ["U", "R"]
        )

        famsize = st.selectbox(
            "ขนาดครอบครัว",
            ["GT3", "LE3"]
        )

        Pstatus = st.selectbox(
            "สถานะผู้ปกครอง",
            ["A", "T"]
        )

    with col3:

        Medu = st.selectbox(
            "ระดับการศึกษาของแม่",
            [0, 1, 2, 3, 4]
        )

        Fedu = st.selectbox(
            "ระดับการศึกษาของพ่อ",
            [0, 1, 2, 3, 4]
        )


    # =====================
    # Family / Occupation
    # =====================

    st.markdown("### 👨‍👩‍👧‍👦 ครอบครัวและอาชีพ")

    col1, col2, col3 = st.columns(3)

    with col1:

        Mjob = st.selectbox(
            "อาชีพแม่",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

        Fjob = st.selectbox(
            "อาชีพพ่อ",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

    with col2:

        reason = st.selectbox(
            "เหตุผลที่เลือกโรงเรียน",
            [
                "home",
                "reputation",
                "course",
                "other"
            ]
        )

        guardian = st.selectbox(
            "ผู้ปกครอง",
            [
                "mother",
                "father",
                "other"
            ]
        )

    with col3:

        famrel = st.slider(
            "ความสัมพันธ์ในครอบครัว",
            1,
            5,
            4
        )


    # =====================
    # Study Information
    # =====================

    st.markdown("### 📚 ข้อมูลการเรียน")

    col1, col2, col3 = st.columns(3)

    with col1:

        traveltime = st.slider(
            "เวลาเดินทางไปโรงเรียน",
            1,
            4,
            2
        )

        studytime = st.slider(
            "เวลาในการเรียน",
            1,
            4,
            2
        )

    with col2:

        failures = st.slider(
            "จำนวนครั้งที่ตกวิชา",
            0,
            3,
            0
        )

        schoolsup = st.selectbox(
            "ได้รับการสนับสนุนด้านการเรียน",
            ["yes", "no"]
        )

    with col3:

        famsup = st.selectbox(
            "ได้รับการสนับสนุนจากครอบครัว",
            ["yes", "no"]
        )

        paid = st.selectbox(
            "เรียนพิเศษวิชาเพิ่มเติม",
            ["yes", "no"]
        )


    # =====================
    # Activities
    # =====================

    st.markdown("### 🎯 กิจกรรมและการใช้ชีวิต")

    col1, col2, col3 = st.columns(3)

    with col1:

        activities = st.selectbox(
            "ทำกิจกรรมนอกหลักสูตร",
            ["yes", "no"]
        )

        nursery = st.selectbox(
            "เคยเรียนอนุบาล",
            ["yes", "no"]
        )

    with col2:

        higher = st.selectbox(
            "ต้องการศึกษาต่อระดับสูง",
            ["yes", "no"]
        )

        internet = st.selectbox(
            "มีอินเทอร์เน็ตที่บ้าน",
            ["yes", "no"]
        )

    with col3:

        romantic = st.selectbox(
            "มีความสัมพันธ์เชิงคู่รัก",
            ["yes", "no"]
        )

        freetime = st.slider(
            "เวลาว่าง",
            1,
            5,
            3
        )


    # =====================
    # Lifestyle
    # =====================

    st.markdown("### 🧠 พฤติกรรมและสุขภาพ")

    col1, col2, col3 = st.columns(3)

    with col1:

        goout = st.slider(
            "การออกไปพบเพื่อน",
            1,
            5,
            3
        )

        Dalc = st.slider(
            "การดื่มแอลกอฮอล์วันธรรมดา",
            1,
            5,
            1
        )

    with col2:

        Walc = st.slider(
            "การดื่มแอลกอฮอล์วันหยุด",
            1,
            5,
            1
        )

        health = st.slider(
            "สุขภาพโดยรวม",
            1,
            5,
            3
        )

    with col3:

        absences = st.number_input(
            "จำนวนครั้งที่ขาดเรียน",
            min_value=0,
            max_value=100,
            value=5
        )


    # =====================
    # Submit
    # =====================

    st.divider()

    submitted = st.form_submit_button(
    "🔮 ทำนายผลการเรียน",
    use_container_width=True
)


# =========================
# Prediction
# =========================

if submitted:

    input_data = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }])


    try:

        prediction = model.predict(input_data)[0]

        # =====================
        # Result
        # =====================

        st.divider()

        st.header("📊 ผลการทำนาย")

        if prediction == 1:

            st.success(
                "🎉 ผลการทำนาย: นักเรียนมีแนวโน้ม **ผ่าน**"
            )

        else:

            st.error(
                "⚠️ ผลการทำนาย: นักเรียนมีแนวโน้ม **ไม่ผ่าน**"
            )


        # =====================
        # Probability
        # =====================

        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(
                input_data
            )[0]

            st.subheader("ความน่าจะเป็นของผลการทำนาย")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "ไม่ผ่าน",
                    f"{probability[0] * 100:.2f}%"
                )

            with col2:

                st.metric(
                    "ผ่าน",
                    f"{probability[1] * 100:.2f}%"
                )


        # =====================
        # Input Preview
        # =====================

        with st.expander("ดูข้อมูลที่ส่งให้โมเดล"):

            st.dataframe(
                input_data,
                use_container_width=True,
                hide_index=True
            )


    except Exception as e:

        st.error(
            "เกิดข้อผิดพลาดในการทำนาย"
        )

        st.code(
            str(e)
        )

        # =========================
# Model Validation
# =========================

st.divider()

st.header("🧪 ทดสอบความถูกต้องของโมเดล")

st.write("""
ส่วนนี้ใช้ตรวจสอบว่า SVM Model ที่นำมาใช้งานบนเว็บไซต์
สามารถทำนายข้อมูลจาก Testing Set ได้ตรงกับผลการทดลองใน Google Colab หรือไม่
""")


@st.cache_data
def load_test_data():

    df = pd.read_csv("student_data.csv")

    # สร้าง Target
    df["pass"] = (df["G3"] >= 10).astype(int)

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

    X = df[features]
    y = df["pass"]

    return X, y


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X, y = load_test_data()


# ใช้การแบ่งข้อมูลแบบเดียวกับ Colab
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ทำนาย Testing Set
y_pred = model.predict(X_test)


# Accuracy
test_accuracy = accuracy_score(
    y_test,
    y_pred
)


# =========================
# Display Results
# =========================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Testing Data",
        len(X_test)
    )

with col2:

    correct = int(
        (y_test.values == y_pred).sum()
    )

    st.metric(
        "ทำนายถูก",
        correct
    )

with col3:

    st.metric(
        "Accuracy",
        f"{test_accuracy * 100:.2f}%"
    )


# =========================
# Compare with Colab
# =========================

st.subheader("เปรียบเทียบกับผลจาก Google Colab")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Colab",
        "68.35%"
    )

with col2:

    st.metric(
        "Streamlit",
        f"{test_accuracy * 100:.2f}%"
    )


difference = abs(
    test_accuracy * 100 - 68.35
)


if difference < 0.01:

    st.success(
        "✅ ผลการทดสอบตรงกับ Google Colab"
    )

elif difference < 1:

    st.warning(
        f"⚠️ ผลใกล้เคียงกับ Google Colab "
        f"(ต่างกัน {difference:.2f}%)"
    )

else:

    st.error(
        f"❌ ผลแตกต่างจาก Google Colab "
        f"(ต่างกัน {difference:.2f}%)"
    )


# =========================
# Detailed Test
# =========================

with st.expander("🔍 ดูผลการทำนาย Testing Set"):

    test_result = X_test.copy()

    test_result["ผลจริง"] = y_test.values

    test_result["ผลทำนาย"] = y_pred

    test_result["สถานะ"] = [
        "✅ ถูกต้อง"
        if actual == predicted
        else "❌ ผิดพลาด"
        for actual, predicted
        in zip(y_test, y_pred)
    ]

    test_result["ผลจริง"] = test_result[
        "ผลจริง"
    ].map({
        0: "ไม่ผ่าน",
        1: "ผ่าน"
    })

    test_result["ผลทำนาย"] = test_result[
        "ผลทำนาย"
    ].map({
        0: "ไม่ผ่าน",
        1: "ผ่าน"
    })

    st.dataframe(
        test_result,
        use_container_width=True,
        hide_index=True
    )
    # =========================
# Model Validation
# =========================

st.divider()

st.header("🧪 ทดสอบความถูกต้องของโมเดล")

st.write("""
ส่วนนี้ใช้ตรวจสอบว่า SVM Model ที่นำมาใช้งานบนเว็บไซต์
สามารถทำนายข้อมูลจาก Testing Set ได้ตรงกับผลการทดลองใน Google Colab หรือไม่
""")


@st.cache_data
def load_test_data():

    df = pd.read_csv("student_data.csv")

    # สร้าง Target
    df["pass"] = (df["G3"] >= 10).astype(int)

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

    X = df[features]
    y = df["pass"]

    return X, y


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X, y = load_test_data()


# ใช้การแบ่งข้อมูลแบบเดียวกับ Colab
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ทำนาย Testing Set
y_pred = model.predict(X_test)


# Accuracy
test_accuracy = accuracy_score(
    y_test,
    y_pred
)


# =========================
# Display Results
# =========================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Testing Data",
        len(X_test)
    )

with col2:

    correct = int(
        (y_test.values == y_pred).sum()
    )

    st.metric(
        "ทำนายถูก",
        correct
    )

with col3:

    st.metric(
        "Accuracy",
        f"{test_accuracy * 100:.2f}%"
    )


# =========================
# Compare with Colab
# =========================

st.subheader("เปรียบเทียบกับผลจาก Google Colab")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Colab",
        "68.35%"
    )

with col2:

    st.metric(
        "Streamlit",
        f"{test_accuracy * 100:.2f}%"
    )


difference = abs(
    test_accuracy * 100 - 68.35
)


if difference < 0.01:

    st.success(
        "✅ ผลการทดสอบตรงกับ Google Colab"
    )

elif difference < 1:

    st.warning(
        f"⚠️ ผลใกล้เคียงกับ Google Colab "
        f"(ต่างกัน {difference:.2f}%)"
    )

else:

    st.error(
        f"❌ ผลแตกต่างจาก Google Colab "
        f"(ต่างกัน {difference:.2f}%)"
    )


# =========================
# Detailed Test
# =========================

with st.expander("🔍 ดูผลการทำนาย Testing Set"):

    test_result = X_test.copy()

    test_result["ผลจริง"] = y_test.values

    test_result["ผลทำนาย"] = y_pred

    test_result["สถานะ"] = [
        "✅ ถูกต้อง"
        if actual == predicted
        else "❌ ผิดพลาด"
        for actual, predicted
        in zip(y_test, y_pred)
    ]

    test_result["ผลจริง"] = test_result[
        "ผลจริง"
    ].map({
        0: "ไม่ผ่าน",
        1: "ผ่าน"
    })

    test_result["ผลทำนาย"] = test_result[
        "ผลทำนาย"
    ].map({
        0: "ไม่ผ่าน",
        1: "ผ่าน"
    })

    st.dataframe(
        test_result,
        use_container_width=True,
        hide_index=True
    )