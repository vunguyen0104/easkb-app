import streamlit as st
from PIL import Image
from src.pages.display import show_display_page
from src.pages.explore import show_explore_page

def setup_up_app():
    # Set a title and add a sidebar title
    #st.title("Your Project Dashboard")

    # Add an image to the sidebar
    image = Image.open("./images/logo.png")
    st.sidebar.image(image, use_column_width=True)

    #st.sidebar.title("Select Page")

    page = st.sidebar.selectbox("Display or Explore", ("Display", "Explore"))

    if page == "Display":
        show_display_page()
    else:
        show_explore_page()

    # ---- HIDE STREAMLIT STYLE ----
    # hide_st_style = """
    #     <style>
    #         #MainMenu {visibility: hidden;}
    #         footer {visibility: hidden;}
    #         header {visibility: hidden;}
    #     </style>
    # """
    # st.markdown(hide_st_style, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Your Project Title",  page_icon=":chart_with_upwards_trend:", layout="wide")
    setup_up_app()

if __name__ == "__main__":
    main()