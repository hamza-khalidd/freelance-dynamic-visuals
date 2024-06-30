import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #4793AF;'>Dataset Analysis</h1>", unsafe_allow_html=True)

st.write("Upload your CSV or Excel file below:")

# File upload
uploaded_file = st.file_uploader("Upload File", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            excel_data = pd.ExcelFile(uploaded_file)
            sheet_names = set(excel_data.sheet_names)
            selected_sheet = st.selectbox("Select a sheet", sheet_names, index=None, placeholder="Select Data Sheet",)
            if selected_sheet:  # Check if a sheet is selected
                data = pd.read_excel(excel_data, sheet_name=selected_sheet)
            else:
                st.warning("Please select a sheet!")
                data = None  # Set data to None if no sheet is selected
        else:
            st.warning("Invalid File Format!")
            data = None  # Set data to None for invalid file formats
    except Exception as e:
        st.error(f"Error: {e}")
        data = None  # Set data to None in case of errors
    
    try:
        st.write(data.head())
        lstViz = ['Pie', 'Bar', 'Line', 'Table']
        # -- New Update (Latest Working)
        st.divider()
        st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Dynamic Visuals</h1>", unsafe_allow_html=True)

        viz1, viz2 = st.columns(2)
        with viz1:
            with st.form("form_SelectColumn_PIE"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 1</h1>", unsafe_allow_html=True)
                selectViz1 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz1 = st.form_submit_button("SubmitViz1")
                if submitViz1:
                    if selectViz1 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz1 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz1 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz1 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)
                        
        with viz2:
            with st.form("form_SelectColumnViz2"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 2</h1>", unsafe_allow_html=True)
                selectViz2 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz2 = st.form_submit_button("SubmitViz2")
                if submitViz2:
                    if selectViz2 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz2 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz2 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz2 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)


        
        viz3, viz4 = st.columns(2)
        with viz3:
             with st.form("form_SelectColumnViz3"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 3</h1>", unsafe_allow_html=True)
                selectViz3 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz3 = st.form_submit_button("SubmitViz3")
                if submitViz3:
                    if selectViz3 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz3 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz3 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz3 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)
                        
        with viz4:
            with st.form("form_SelectColumnViz4"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 4</h1>", unsafe_allow_html=True)
                selectViz4 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz4 = st.form_submit_button("SubmitViz4")
                if submitViz4:
                    if selectViz4 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz4 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz4 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz4 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)

        viz5, viz6 = st.columns(2)
        with viz5:
             with st.form("form_SelectColumnViz5"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 5</h1>", unsafe_allow_html=True)
                selectViz5 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz5 = st.form_submit_button("SubmitViz5")
                if submitViz5:
                    if selectViz5 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz5 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz5 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz5 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)
                        
        with viz6:
            with st.form("form_SelectColumnViz6"):
                st.markdown("<h1 style='text-align: center; color: #8CB9BD;'>Viz 6</h1>", unsafe_allow_html=True)
                selectViz6 = st.selectbox("Select Visual:", lstViz, index=None, placeholder="Select Column",)
                cPIE1, cPIE2 = st.columns(2)
                with cPIE1:
                    colData_Text = st.selectbox("Select column (Text):", list(data.columns), index=None, placeholder="Select Column",)
                with cPIE2:
                    colData_Values = st.selectbox("Select column (Values):", list(data.columns), index=None, placeholder="Select Column",)

                submitViz6 = st.form_submit_button("SubmitViz4")
                if submitViz6:
                    if selectViz6 == 'Pie':
                        fig = px.pie(data, values=colData_Values, names=colData_Text, width=800)
                        st.plotly_chart(fig)
                    if selectViz6 == 'Bar':
                        fig = px.bar(data, x=colData_Text, y=colData_Values, width=800)
                        st.plotly_chart(fig)
                    if selectViz6 == 'Line':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        fig = px.line(grouped, x=colData_Text, y=colData_Values, width=800, title='Trend Line')
                        st.plotly_chart(fig)
                    if selectViz6 == 'Table':
                        grouped = data.groupby(colData_Text)[colData_Values].sum().reset_index()
                        st.write(grouped)

    except Exception as e:
        # st.error(f"Error: {e}")
        pass