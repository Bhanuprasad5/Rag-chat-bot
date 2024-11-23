# Import necessary libraries
import streamlit as st

# Set the title of the web app
st.title("My First Streamlit App 🎉")

# Add a text input
user_name = st.text_input("What's your name?", "")

# Add a slider
age = st.slider("How old are you?", 0, 100, 25)

# Display output based on user input
if user_name:
    st.write(f"Hello, {user_name}! 🎈")
    st.write(f"Wow, you're {age} years young! 🎂")

# Add a button
if st.button("Click Me!"):
    st.success("You clicked the button! 🚀")

# Add an image (optional)
st.image("https://placekitten.com/400/300", caption="Here's a cute kitten!")

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar where you can add extra content.")
