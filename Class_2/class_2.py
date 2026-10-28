import streamlit as st

st.Title("2nd Class")
st.caption("Helllo welcome")
st.markdown("[Link](https://originqc.com/es/blogs/dualidad-onda-particula)")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.subheader("User data")

user_data = {
    "Name ": "Margareth",
    "Age ":17,
    "Gender": "Female",
    "City": "Amates",
    "Hobbies ": "Play the violin"
}

#Usamos json para mostrarlo bonito en la pantalla
st.json(user_data)