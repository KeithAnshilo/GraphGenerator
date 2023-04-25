import streamlit as st
import requests

# Define the Streamlit app
def app():
    # Add a title to the app
    st.title("Graph Generator")

    # Get the graph type from the user
    graph_type = st.text_input("Graph Type:", "bar")

    # Get the data from the user
    data_input = st.text_input("Data (format: labels: [...], data: [...]):")
    try:
        data_dict = eval("{" + data_input + "}")
    except:
        st.write("Invalid data input format. Please enter the data in the correct format.")
        return

    # Generate the graph
    url = f"https://quickchart.io/{graph_type.lower()}?{'&'.join([f'{key}={value}' for key, value in data_dict.items()])}"
    response = requests.get(url)

    # Display the graph preview
    if response.status_code == 200:
        st.write(f"![Graph Preview]({response.url}) [Source]({response.url})")
    else:
        st.write("Failed to generate graph preview. Please check your input and try again.")

# Run the app
if __name__ == '__main__':
    app()
