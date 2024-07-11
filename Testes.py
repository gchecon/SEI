import streamlit as st

st.title('Interactive Slider Example')
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected {slider_value}!')

st.title('Interactive Checkbox Example')
checkbox_value = st.checkbox('Check me')
if checkbox_value:
    st.write('Checkbox is checked!')
else:
    st.write('Checkbox is not checked.')