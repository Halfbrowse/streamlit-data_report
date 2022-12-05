import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title="Data Profilers", layout="wide")


st.markdown(
    """
    For each column, the following information (whenever relevant for the column type) is presented in an interactive HTML report: 

    **Type inference** : detect the types of columns in a DataFrame  

    **Essentials**: type, unique values, indication of missing values  

    **Quantile statistics**: minimum value, Q1, median, Q3, maximum, range, interquartile range

    **Descriptive statistics**: mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness  

    **Most frequent and extreme values**  

    **Histograms**: categorical and numerical  

    **Correlations**: high correlation warnings, based on different correlation metrics (Spearman, Pearson, Kendall, Cramér’s V, Phik, Auto)  

    **Missing values**: through counts, matrix and heatmap  

    **Duplicate rows**: list of the most common duplicated rows  

    **Text analysis**: most common categories (uppercase, lowercase, separator), scripts (Latin, Cyrillic) and blocks (ASCII, Cyrilic)  

    **File and Image analysis**: file sizes, creation dates, dimensions, indication of truncated images and existence of EXIF metadata 
    """
)

st.info("Please note that large files may take some time to generate.")


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

try:
    if uploaded_file:
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
            if df is not None:
                button1 = st.button("Generate Report")

                if button1:

                    pr = ProfileReport(
                        df,
                        minimal=minimal,
                        dark_mode=dark_mode,
                        orange_mode=orange_mode,
                    )
                    st.download_button(
                        label="Download Report as CSV",
                        data=pr,
                        file_name="streamlit_report",
                        mime="text/csv",
                    )
                    button = st.button(st_profile_report(pr, navbar=True))

        else:
            st.error("Please only upload a csv or excel file")


except:
    TypeError("Unknown errors resolved")
