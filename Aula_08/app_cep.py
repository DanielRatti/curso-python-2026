from altair.utils import data
import streamlit as st
import requests
import pandas as pd

URL = "https://viacep.com.br/ws/{cep}/json/"


st.title("busca CEP")

cep = st.text_input("Busque seu CEP")

if cep != "":
    
    
    try:
        resp = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data)

    except Exception as err:
        st.error("entre com um cep valido!")