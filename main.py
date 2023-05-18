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

age_inp = st.number_input("Input your age")
st.markdown(f"Your age is {age_inp}")


st.markdown("# ggg")
text_inp = st.text_input("Input")
word_tokenize = "|".join(text_inp.split())
st.markdown(f"{word_tokenize}")