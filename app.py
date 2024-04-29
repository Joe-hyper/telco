# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for additional plots

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot(plot_type):
    if plot_type == "Scatter Plot":
        st.header('Scatter Plot')
        fig, ax = plt.subplots()
        ax.scatter(x=df['Dur. (ms)'], y=df['Avg RTT DL (ms)'])
        ax.set_xlabel('Duration (ms)')
        ax.set_ylabel('Average RTT DL (ms)')
        st.pyplot(fig)
    elif plot_type == "Boxplot":
        st.header('Boxplot')
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x='Dur. (ms)')
        ax.set_xlabel('Duration (ms)')
        st.pyplot(fig)
    elif plot_type == "Countplot":
        st.header('Countplot')
        fig, ax = plt.subplots()
# Calculate the counts of each category and select the top 10
        top_10_manufacturers = df['Handset Manufacturer'].value_counts().nlargest(10)

    # Filter the dataframe to include only the top 10 manufacturers
        filtered_df = df[df['Handset Manufacturer'].isin(top_10_manufacturers.index)]

    # Create a countplot for the filtered data
        sns.countplot(data=filtered_df, x='Handset Manufacturer', order=top_10_manufacturers.index)
        ax.set_xlabel('Handset Manufacturer')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")  # Rotate labels for better readability

        st.pyplot(fig) 
           

# Add a title and intro text
st.title('Telco Data Analysis')
st.text('This is a web app that visualizes and gives insights into telco data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing telco data')
# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Selects what you want to display:', ['Home', 'Data Summary', 'Data Header', 'EDA'])

# Plot type selection
plot_type = st.sidebar.selectbox('Select plot type:', ['Scatter Plot', 'Boxplot', 'Countplot'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'EDA':
    displayplot(plot_type)
