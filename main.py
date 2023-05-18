import streamlit as st

st.title("Test")
st.write("Progressing")

st.markdown("## my markdown")
code = '''def hello():
    print("hello")'''

st.code(code, language='python')

show_btn = st.button("Show code")
if show_btn:
    st.code("Button has already clicked")