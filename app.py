import streamlit as st
import pandas as pd

st.title("Psychological Test Tool (MVP)")

st.write("Answer the questions:")

# Загружаем Excel
df = pd.read_excel("data/tests.xlsx")

answers = []

for i, row in df.iterrows():
    choice = st.radio(
        f"{row['Question']}",
        [row['Option_A'], row['Option_B']],
        key=i
    )
    answers.append(choice)

if st.button("Submit"):
    st.write("Processing results...")

    # пока просто вывод
    st.write(answers)
