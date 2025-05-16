import streamlit as st
import helper
import pickle

# Page config
st.set_page_config(
    page_title="Duplicate Question Detector",
    page_icon="🔍",
    layout="centered"
)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background-color: #F8FAFC;
        }

        .title {
            font-size: 2.5rem;
            font-weight: 600;
            color: #1E293B;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #475569;
            margin-bottom: 30px;
        }

        .stButton>button {
            background: linear-gradient(90deg, #6366F1, #3B82F6);
            color: white;
            font-weight: bold;
            padding: 0.6rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #3B82F6, #2563EB);
        }

        .result-box {
            padding: 20px;
            border-radius: 10px;
            background-color: #E0F2FE;
            color: #0C4A6E;
            font-weight: 600;
            font-size: 18px;
        }

        .not-duplicate {
            background-color: #FEE2E2;
            color: #991B1B;
        }

        .footer {
            margin-top: 60px;
            text-align: center;
            font-size: 13px;
            color: #94A3B8;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="title">🔁 Duplicate Question Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check whether two questions convey the same meaning using deep learning.</div>', unsafe_allow_html=True)

# Form
with st.form(key="question_form"):
    q1 = st.text_input("📝 Question 1")
    q2 = st.text_input("📝 Question 2")
    submit = st.form_submit_button("Detect")

# Result Display
if submit:
    if not q1.strip() or not q2.strip():
        st.warning("⚠️ Please fill in both questions.")
    else:
        try:
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

            st.markdown("---")
            if result:
                st.markdown('<div class="result-box">✅ These questions are <strong>Duplicate</strong>.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-box not-duplicate">❌ These questions are <strong>Not Duplicate</strong>.</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")

