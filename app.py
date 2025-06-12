import streamlit as st
import joblib
import os
import pandas as pd

# --- Judul Aplikasi ---
st.title("Dropout Prediction")
st.write("Isi data di bawah ini untuk memprediksi apakah siswa akan lulus atau keluar.")

model_path = 'model/xgboost.joblib'
model = joblib.load(model_path)

st.subheader("Informasi Siswa")

# === Mapping Dictionary ===
marital_status_map = {
    "Single": 1, "Married": 2, "Widower": 3, "Divorced": 4,
    "Facto union": 5, "Legally separated": 6
}
application_mode_map = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}
course_map = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}
attendance_map = {"Daytime": 1, "Evening": 0}
qualification_map = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}
nacionality_map = {
    "Portuguese": 1, "German": 2, "Spanish": 6,
    "Italian": 11, "Dutch": 13, "English": 14,
    "Lithuanian": 17, "Angolan": 21, "Cape Verdean": 22,
    "Guinean": 24, "Mozambican": 25, "Santomean": 26,
    "Turkish": 32, "Brazilian": 41, "Romanian": 62,
    "Moldova (Republic of)": 100, "Russian": 105,
    "Cuban": 108, "Colombian": 109
}
mother_qualification_map = {
    "Secondary education - 12th Year of Schooling or Eq.": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "General commerce course": 18,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv": 19,
    "Technical-professional course": 22,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv": 37,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}
father_qualification_map = {
    "Secondary education - 12th Year of Schooling or Eq.": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "General commerce course": 18,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv": 19,
    "Technical-professional course": 22,
    "Complementary High School Course - not concluded": 25,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "General Course of Administration and Commerce": 31,
    "Supplementary Accounting and Administration": 33,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv": 37,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}
mother_occupation_map = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "Teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194
}
father_occupation_map = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Armed Forces Officers": 101,
    "Armed Forces Sergeants": 102,
    "Other Armed Forces personnel": 103,
    "Directors of administrative and commercial services": 112,
    "Hotel, catering, trade and other services directors": 114,
    "Specialists in the physical sciences, mathematics, engineering and related techniques": 121,
    "Health professionals": 122,
    "Teachers": 123,
    "Specialists in finance, accounting, administrative organization, public and commercial relations": 124,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Information and communication technology technicians": 135,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers and the like": 153,
    "Protection and security services personnel": 154,
    "Market-oriented farmers and skilled agricultural and animal production workers": 161,
    "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence": 163,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in metallurgy, metalworking and similar": 172,
    "Skilled workers in electricity and electronics": 174,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Fixed plant and machine operators": 181,
    "Assembly workers": 182,
    "Vehicle drivers and mobile equipment operators": 183,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194,
    "Street vendors (except food) and street service providers": 195
}
gender_map = {"Male": 1, "Female": 0}
yes_no_map = {"Yes": 1, "No": 0}

# === Input Form ===
input_data = {
    "Marital_status": marital_status_map[st.selectbox("Marital Status", list(marital_status_map.keys()))],
    "Application_mode": application_mode_map[st.selectbox("Application Mode", list(application_mode_map.keys()))],
    "Application_order": int(st.number_input("Application Order (0-9)", min_value=0, max_value=9)),
    "Course": course_map[st.selectbox("Course", list(course_map.keys()))],
    "Daytime_evening_attendance": attendance_map[st.selectbox("Attendance", list(attendance_map.keys()))],
    "Previous_qualification": qualification_map[st.selectbox("Previous Qualication", list(qualification_map.keys()))],
    "Previous_qualification_grade": float(st.number_input("Previous Qualification Grade (0-200)", min_value=0.0, max_value=200.0)),
    "Nacionality": nacionality_map[st.selectbox("Nationality", list(nacionality_map.keys()))],
    "Mothers_qualification": mother_qualification_map[st.selectbox("Mother's Qualification", list(mother_qualification_map.keys()))],
    "Fathers_qualification": father_qualification_map[st.selectbox("Father's Qualification", list(father_qualification_map.keys()))],
    "Mothers_occupation": mother_occupation_map[st.selectbox("Mother's Occupation", list(mother_occupation_map.keys()))],
    "Fathers_occupation": father_occupation_map[st.selectbox("Father's Occupation", list(father_occupation_map.keys()))],
    "Admission_grade": float(st.number_input("Admission Grade (0-200)", min_value=0.0, max_value=200.0)),
    "Displaced": yes_no_map[st.selectbox("Displaced", list(yes_no_map.keys()))],
    "Educational_special_needs": yes_no_map[st.selectbox("Educational Special Needs", list(yes_no_map.keys()))],
    "Debtor": yes_no_map[st.selectbox("Debtor", list(yes_no_map.keys()))],
    "Tuition_fees_up_to_date": yes_no_map[st.selectbox("Tuition Fees Up To Date", list(yes_no_map.keys()))],
    "Gender": gender_map[st.selectbox("Gender", list(gender_map.keys()))],
    "Scholarship_holder": yes_no_map[st.selectbox("Scholarship Holder", list(yes_no_map.keys()))],
    "Age_at_enrollment": int(st.number_input("Age at Enrollment", min_value=15)),
    "International": yes_no_map[st.selectbox("International Student", list(yes_no_map.keys()))],
    "Curricular_units_1st_sem_credited": int(st.number_input("1st Sem Credited Units", min_value=0)),
    "Curricular_units_1st_sem_enrolled": int(st.number_input("1st Sem Enrolled Units", min_value=0)),
    "Curricular_units_1st_sem_evaluations": int(st.number_input("1st Sem Evaluated Units", min_value=0)),
    "Curricular_units_1st_sem_approved": int(st.number_input("1st Sem Approved Units", min_value=0)),
    "Curricular_units_1st_sem_grade": float(st.number_input("1st Sem Grade", min_value=0.0)),
    "Curricular_units_1st_sem_without_evaluations": int(st.number_input("1st Sem Units Without Evaluation", min_value=0)),
    "Curricular_units_2nd_sem_credited": int(st.number_input("2nd Sem Credited Units", min_value=0)),
    "Curricular_units_2nd_sem_enrolled": int(st.number_input("2nd Sem Enrolled Units", min_value=0)),
    "Curricular_units_2nd_sem_evaluations": int(st.number_input("2nd Sem Evaluated Units", min_value=0)),
    "Curricular_units_2nd_sem_approved": int(st.number_input("2nd Sem Approved Units", min_value=0)),
    "Curricular_units_2nd_sem_grade": float(st.number_input("2nd Sem Grade", min_value=0.0)),
    "Curricular_units_2nd_sem_without_evaluations": int(st.number_input("2nd Sem Units Without Evaluation", min_value=0)),
    "Unemployment_rate": float(st.number_input("Unemployment Rate")),
    "Inflation_rate": float(st.number_input("Inflation Rate")),
    "GDP": float(st.number_input("GDP"))
}

# === Convert to DataFrame ===
input_df = pd.DataFrame([input_data])

# === Tampilkan DataFrame ===
st.write("Data yang dimasukkan:")
st.dataframe(input_df)
if st.button("Prediksi"):
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0][1] if hasattr(model, "predict_proba") else None

    if prediction == 0:
        st.error(f"Siswa diprediksi AKAN dropout. Probabilitas: {prediction_proba:.2f}" if prediction_proba else "Siswa diprediksi AKAN dropout.")
    else:
        st.success(f"Siswa diprediksi TIDAK dropout. Probabilitas: {1 - prediction_proba:.2f}" if prediction_proba else "Siswa diprediksi TIDAK dropout.")
