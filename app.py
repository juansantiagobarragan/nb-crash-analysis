import streamlit as st
import streamlit.components.v1 as components
st.title("Crash Analysis near Rutgers-New Brunswick Campus")
st.write("This project will be analyzing the crash data near the Rutgers University - New Brunswick area. Ultimately the goal of this project is to create a dashboard that is simple yet effective in disseminating data. Ideally this dashboard could help emergency services allocate their, at times, limited resources.")
st.header("Maps")

with open("map.html", "r") as f:
    components.html(f.read(), height=600)

st.markdown(
    "🟢 No apparent injury &nbsp; 🟡 Possible injury &nbsp; 🟠 Minor injury &nbsp;🔴 Serious injury &nbsp; ⚫ Fatal"
)
st.header("Charts")
st.image('hours.png')
st.image('days.png')