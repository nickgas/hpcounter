import streamlit as st

# Initialize HP values in session state if they don't exist
if "hp1" not in st.session_state:
    st.session_state.hp1 = 100
if "hp2" not in st.session_state:
    st.session_state.hp2 = 100

# Callback functions for number inputs to overwrite HP values
def overwrite_hp1():
    try:
        st.session_state.hp1 = int(st.session_state.input_hp1)
    except ValueError:
        pass

def overwrite_hp2():
    try:
        st.session_state.hp2 = int(st.session_state.input_hp2)
    except ValueError:
        pass

# Function to update HP values using buttons
def update_hp(player, change):
    if player == "hp1":
        st.session_state.hp1 += change
    elif player == "hp2":
        st.session_state.hp2 += change

st.title("HP Tracker")

# Display current HP values
st.subheader(f"Player 1 HP: {st.session_state.hp1}")
st.subheader(f"Player 2 HP: {st.session_state.hp2}")

st.markdown("### Overwrite HP Values")

# Create two number inputs to overwrite HP values.
# They use separate keys (input_hp1 and input_hp2) and callbacks.
st.number_input("Set Player 1 HP", key="input_hp1", value=st.session_state.hp1, step=1, on_change=overwrite_hp1)
st.number_input("Set Player 2 HP", key="input_hp2", value=st.session_state.hp2, step=1, on_change=overwrite_hp2)
