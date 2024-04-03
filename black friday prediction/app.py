# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda
from ml_app import run_ml

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Black Friday Prediction App</h1>
		
		</div>
		"""

def main():
	stc.html(html_temp)
	menu = ["EDA","ML"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "EDA":
		run_eda()
		pass
	elif choice == "ML":
		run_ml()
	


if __name__ == '__main__':
	main()