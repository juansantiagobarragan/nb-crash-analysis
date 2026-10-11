import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Safer Roads: New Brunswick",layout="wide",page_icon="🚙")
st.title("Safer Roads: New Brunswick",text_alignment="center")
st.caption("Analyzing Crashes in the City of New Brunswick to help Emergency Services allocate resources",text_alignment="center")
st.write("This project will be analyzing the crash data near the Rutgers University - New Brunswick area. Ultimately the goal of this project is to create a dashboard that is simple yet effective in disseminating data. Ideally this dashboard could help emergency services allocate their, at times, limited resources.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Crashes",2391)
c2.metric("Worst Intersection","Route 18 & Route 1")
c3.metric("Peak Hour","5pm")
c4.metric("Pedestrian Crashes",87)

st.header("Which intersections have the most crashes?",text_alignment="center")
st.write("The intersection with the most crashes is Route 18 and Route 1. With the amount of cars that pass by there everyday, it is expected for there to be more crashes on the highway.")
with open("map.html", "r") as f:
    components.html(f.read(), height=600)

st.markdown(
    "🟢 No apparent injury &nbsp; 🟡 Possible injury &nbsp; 🟠 Minor injury &nbsp;🔴 Serious injury &nbsp; ⚫ Fatal"
)

st.header("Where are pedestrians most getting struck by cars?",text_alignment="center")
st.write("The street with the most pedestrians struck is Easton Ave, which is right near the College Avenue Campus. Being able to visualize where pedestrians are most struck at may help local government decide which street needs their pedestrian infrastructure upgraded.")

st.header("What time and day have the most crashes?",text_alignment="center")
st.write("5pm is when most crashes happened in 2025 and Tuesday had the most crashes. With everyone trying to get back home after a long day at work, 5pm is peak rush hour which is why there so many crashes at that time. ")

col1,col2 = st.columns(2)
col1.image('hours.png')
col2.image('days.png')

st.divider()
st.caption("Reported Crashes Only")
st.markdown("[New Jersey Department of Transportation Crash Data Dashboard](https://njdot.aashtowaresafety.net/njdot-crash-data-dashboard#/)")
st.caption("Github")
st.markdown("[View the code on GitHub](https://github.com/juansantiagobarragan/nb-crash-analysis)")