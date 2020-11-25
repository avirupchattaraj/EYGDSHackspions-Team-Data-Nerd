import streamlit as st
import twint

st.title("EY-Twitter-Profile-Scraper")

st.sidebar.title("Controls")

option = st.selectbox('Choose Profile You Want To Scrape?',['EY_India','EYnews','EY_US','ey','EY_People','EY_UKI','EY_Press','EY_TMT','EY_Banking','EY_Consulting'])

st.write("You selected -",option)

st.sidebar.write("The below limit may not fully enforce for the scraping of your tweets as its based on twitter's whims and fancies.")

limit=st.sidebar.slider("Choose limit",min_value=1,max_value=3200,step=200,value=100)


if st.button("Click Me To Fetch Tweets"):
    # Twint Configuration Settings
    c=twint.Config()
    c.Username = option
    c.Limit = limit
    c.Store_csv = True
    c.Output = "output.csv"
    # Run
    twint.run.Profile(c)

    st.write("We are done getting your tweets")

if st.button("Click Me To Download CSV"):

    # Logic for handling the download

    pass





