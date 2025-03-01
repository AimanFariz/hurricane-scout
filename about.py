import streamlit as st
import gdown

# page_bg_img='''
# <style>
# [data-testid="stAppViewContainer"] {
# background-image: url('https://cdn.freebiesupply.com/logos/large/2x/tulsa-golden-hurricane-2-logo-png-transparent.png');
# background-size: 50% 50%;
# background-repeat:
# }
# </style>
# '''
# st.markdown (page_bg_img, unsafe_allow_html=True)



def about_page():
    file_id = "1Qag0gA0G5pbAZqUQonBeXg6myC2_hDMT"
    url = f"https://drive.google.com/uc?id={file_id}"

    # Download the XLSX file
    output = "data.xlsx"
    gdown.download(url, output, quiet=False)

    df = pd.read_excel(output, engine="openpyxl")  # Use "openpyxl" for Excel files

# Display the dataframe in Streamlit
st.write(df)
    st.title("About Hurricane Scout")
    st.write("The main purpose of this app is to assist the TU Men Soccer coaches to scout future potential players. This app stores all the data for NCAA D1 from Wyscout, and NCAA D2, NAIA, NJCAA stats as scraped from their respective websites.")
    
    st.header("The Moneyball Thesis")
    st.html(
        "<ul><li>The term “Moneyball” could be credited to Michael Lewis, from his book “Moneyball: The Art of Winning an Unfair Game”, published in 2003.</li><li>The main theme of Moneyball was leveraging data to find the best players for the least amount of money.</li><li>This app is my initiative to help implement our own version of Moneyball.</li></ul>"
    )
    
    st.header("How this app was built")
    st.write("This app was built using Streamlit and hosted using Streamlit Community Cloud.")
    
    st.header("Limitations")
    st.write("Compared to NCAA D1, all NAIA, NJCAA, and even NCAA D2 stats were much more restricted to goals and assists.")
    
    st.header("Future Improvements")
    st.write("Connect the scraper to this app through Flask. Will need more time and knowledge (read documentations) for that.")
    st.write("Deploy on a secure DNS (discuss with IT Team at Zink Hall)")
    
    st.header("Credit")
    st.write("This app was made by Aiman Fariz, BS in CS and French @ Utulsa '27 | Pathway to Sports Academy - Men's Soccer Data Analytics")