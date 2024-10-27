import pickle
import streamlit as st

model = pickle.load(open("AdaBoost.pkl", "rb"))


st.title("Renal risk: Renal Health Risk Assessment")

bg = """

<style>
[data-testid="stAppViewContainer"] {
 
background-image: url("https://drgura.com/wp-content/uploads/DrGura-iStock-1125719605.jpg");
background-size: cover;
}

<style/>

"""

st.markdown(bg, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.text_input("Enter the Age")

with col2:
    bp = st.text_input("Enter the Blood Pressure")

with col1:
    sg = st.text_input("Emter the Specific Gravity")

with col2:
    al = st.text_input("Enter the Albumin value")

with col1:
    su = st.text_input("Enter Glucose level")

with col2:
    rbc = st.text_input("Enter the Red Blood Cells value in Urine")

with col1:
    pc = st.text_input("Enter the Pus Cells value")

with col2:
    pcc = st.text_input("Enter the Pus Cells Clumps value")

with col1:
    ba = st.text_input("Enter the Bacteria value")

with col2:
    bgr = st.text_input("Enter the random Blood Glucose")

with col1:
    bu = st.text_input("Enter the Blood Urea value")

with col2:
    sc = st.text_input("Enter the Serum Creatinine value")

with col1:
    sod = st.text_input("Enter the Sodium value")

with col1:
    pot = st.text_input("Enter the Potassium value")

with col2:
    hemo = st.text_input("Enter the Hemoglobin value")

with col1:
    pcv = st.text_input("Enter the Packed Cell Volume value")

with col2:
    wc = st.text_input("Enter the White Blood Cells count in blood")

with col1:
    rc = st.text_input("Enter the Reb Blood Cells in the blood")

with col2:
    htn = st.text_input("Enter whether the patient has Hypertension or not")

with col1:
    dm = st.text_input("Enter whether the patient has Diabetes or not")

with col2:
    cad = st.text_input("Enter whether the patient has Heart Disease or not")

with col1:
    appet = st.text_input(
        "Enter Enter whether the patient has Appetite or not")

with col2:
    pe = st.text_input("Enter whether the patient has Pedal Edema or not")

with col1:
    ane = st.text_input("Enter whether the patient has Anemia or not")


diagnosis = ""

if st.button("Renal Test Result"):
    try:
        age = int(age)
        bp = float(bp)
        sg = float(sg)
        al = float(al)
        su = float(su)
        rbc = int(rbc)
        pc = int(pc)
        pcc = int(pcc)
        ba = int(ba)
        bgr = float(bgr)
        bu = float(bu)
        sc = float(sc)
        sod = float(sod)
        pot = float(pot)
        hemo = float(hemo)
        pcv = int(pcv)
        wc = int(wc)
        rc = float(rc)
        htn = int(htn)
        dm = int(dm)
        cad = int(cad)
        appet = int(appet)
        pe = int(pe)
        ane = int(ane)

        # prediction

        prediction = model.predict([[age,
                                     bp,
                                     sg,
                                     al,
                                     su,
                                     rbc,
                                     pc,
                                     pcc,
                                     ba,
                                     bgr,
                                     bu,
                                     sc,
                                     sod,
                                     pot,
                                     hemo,
                                     pcv,
                                     wc,
                                     rc,
                                     htn,
                                     dm,
                                     cad,
                                     appet,
                                     pe,
                                     ane]])
        if prediction[0] == 0:
            diagnosis = "Congratulations you are healthy"
        else:
            diagnosis = "Sorry you have Kidney disease. Please refer to a medical professional"
    except ValueError as e:
        st.error(f"Invalid input: {e}")

st.success(diagnosis)
