import streamlit as st
import time


st.header("Welcome to DataReports")

bar = st.progress(0)


def progress_bar():
    for i in range(1, 101):
        time.sleep(0.1)
        bar.progress(i)


st.subheader("The how to's and whats of DataReports.")


st.info(
    """Once ready, navigate to one of the pages on the sidebar.  \n Ensure that your media is either in .csv or .xlsx format  \n Load your data to the app and let the magic happen."""
)


progress_bar()
