import streamlit as st

# Initialize HP values in session state if they don't exist
if "hp1" not in st.session_state:
    st.session_state.hp1 = 100
if "hp2" not in st.session_state:
    st.session_state.hp2 = 100

# Function to update HP values
def update_hp(player, change):
    if player == "hp1":
        st.session_state.hp1 += change
    elif player == "hp2":
        st.session_state.hp2 += change

# Streamlit UI
st.title("HP Tracker")

# Display HP values
st.subheader(f"Player 1 HP: {st.session_state.hp1}")
st.subheader(f"Player 2 HP: {st.session_state.hp2}")

# Buttons to modify HP values
col1, col2 = st.columns(2)

with col1:
    st.button("Increase HP1", on_click=update_hp, args=("hp1", 1))
    st.button("Decrease HP1", on_click=update_hp, args=("hp1", -1))

with col2:
    st.button("Increase HP2", on_click=update_hp, args=("hp2", 1))
    st.button("Decrease HP2", on_click=update_hp, args=("hp2", -1))
