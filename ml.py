import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="💯 Marks Prediction", page_icon="📋 ", layout="centered")
st.title("👨🏽‍🎓 👩🏽‍🎓 Student's Mark Predictor")
st.write("👩🏽‍💻 Enter the number of **_Hours Studied_** and click **Predict** to generate result.")

# Load the model
def load_model(model):
    with open(model,"rb") as f:
        slr = pickle.load(f)
    return slr
try:
    model = load_model("SLR.pkl") # load the pkl file
except Exception as e:
    st.error("⭕️ Your pickle file not found.")
    st.exception("❗️ Failed to load file : ", e) # tells the reason of the error.
    st.stop()

hours = st.number_input("⏳ Hours Studied",
                        min_value=1.0,
                        max_value=10.0,
                        value=4.0,
                        step=0.1,
                        format="%.1f"
                        )
# Colour for the button
st.markdown("""
<style>
.stButton > button {
    background-color: #8AD9FF;
    color: white;
}
</style>
""", unsafe_allow_html=True)
if st.button("Predict"):
    try:
        x = np.array([[hours]])
        prediction = model.predict(x)
        prediction = prediction[0] # Remove the [] on the output. ❌[85] vs ✅85
        st.success(f"✅ Predicted marks : {prediction:.1f}") # Showing numbers in 1 decimal place ✅1.2 vs ❌1.23
        st.write("💢 Note : This is a ML application. **Results May Vary.**")
    except Exception as e:
        st.error(f"❗️ Prediction failed : {e}.")

