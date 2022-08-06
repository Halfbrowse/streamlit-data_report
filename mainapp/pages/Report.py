import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title="Data Profilers", layout="wide")


def get_file_size(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb


def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in (".csv", ".xlsx"):
        return ext
    else:
        return False


with st.sidebar:

    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 200mb")
    if uploaded_file is not None:
        st.write("Modes of Operations")
        minimal = st.checkbox("Do you want a minimal report?")
        display_mode = st.radio("Display mode", options=("Primary", "Dark", "Orange"))

        if display_mode == "Dark":
            dark_mode = True
            orange_mode = False
        elif display_mode == "Orange":
            orange_mode = True
            dark_mode = False
        else:
            dark_mode = False
            orange_mode = False


if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        if ext == ".csv":
            df = pd.read_csv(uploaded_file)

        else:
            xl_file = pd.ExcelFile(uploaded_file)
            sheet_tuple = tuple(xl_file.sheet_names)
            sheet_name = st.sidebar.selectbox("Select the sheet", sheet_tuple)
            df = xl_file.parse(sheet_name)

            # generate report

            pr = ProfileReport(
                df, minimal=minimal, dark_mode=dark_mode, orange_mode=orange_mode
            )

            st_profile_report(pr, navbar=True)

    else:
        st.error("Please only upload a csv or excel file")
else:
    st.info("Please upload your data in the sidebar to generate report.")
    st.info("Please note that large files may take a long time for report to generate.")
    st.info("Please contact your co-ordinator for any issues.")
