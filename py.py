import streamlit as st

# Set up session state for HP values
if "hp1" not in st.session_state:
    st.session_state.hp1 = 100
if "hp2" not in st.session_state:
    st.session_state.hp2 = 100

st.title("HP Tracker")

# Display HP values
st.write(f"**HP1:** {st.session_state.hp1}")
st.write(f"**HP2:** {st.session_state.hp2}")

# Buttons to modify HP values
col1, col2 = st.columns(2)

with col1:
    if st.button("Increase HP1"):
        st.session_state.hp1 += 1
    if st.button("Decrease HP1"):
        st.session_state.hp1 -= 1

with col2:
    if st.button("Increase HP2"):
        st.session_state.hp2 += 1
    if st.button("Decrease HP2"):
        st.session_state.hp2 -= 1
