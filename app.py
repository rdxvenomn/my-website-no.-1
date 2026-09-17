import streamlit as st

st.title("YOUR CONDOM MAKER APP IS HERE!!!")

if st.button("Make your own condom") :
    st.success("your condom is on the way")

addflavour = st.checkbox("Add your own flavour")

if addflavour:
    st.write("Flavour is added")

condomtype = st.radio("Pick your condom flavour and customize it by yourself : ",
                      ["Chocolate ", "Strawberry",])

st. write(f"Selected condoms flavour {condomtype}")  

Add_customize_flavour =st.selectbox("chosee extra flavour : ", ["kesar","tulsi","monty special surprise"])
st.write(f"Selected Flavour {Add_customize_flavour}")

flavourcontrast = st.slider("flavourcontrast",0,100,50)

NoOfCondoms= st.number_input("How many condoms u need in a pack" , min_value=1,max_value=10)
st.write(f"NO. of condoms{NoOfCondoms}")

name = st.text_input("Enter your Name")
if name:
    st.write(f"BKL Welcome, {name} 💦💦! Your condom is on the way , patience will save u from unwanted pregnancy")

st.title("condom flavour preferences")

col1 , col2 = st.columns(2)

with col1:
    st.header("Chocolate")
    vote1 = st.button("Vote Chocolate")
    

with col2 :
    st.header("Strawberry")
    vote2 = st.button("Vote Strawberry")

if vote1:
    st.success("ACHA BKL Choclate pasand hai Madarchod")
elif vote2:
    st.success("ACHA BKL Strawberry pasand hai Madarchod")

Age = st.sidebar.text_input("Enter your age :")
st.write(f"YOUR AGE IS {Age} , Are u sure about that")


with st.expander("Show me instruction how to use it"):
    st.write("""
    1. First find a girl it can maybe your gf or prostitute
    2. Ask them what kind of flavours they want
    3. Stay hard and fuck her

 """)

Phone = st.text_input("Enter your gf no. will talk to her directly ",   max_chars= 10)
if Phone:
    st.success(f"OOPs! your gf is someone else, This is her No. +91  9824712194 call her she will make u crazy 🫦🫦")











