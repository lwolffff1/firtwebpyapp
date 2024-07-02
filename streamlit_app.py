from pathlib import Path 
import json
import streamlit as st 
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

#Page configuration
st.set_page_config(page_title="Happy birthday", page_icon="🎄")

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR /".style"/"style.css"
ASSETS = THIS_DIR /".asset"
LOTTIE_ANIMATION = ASSETS /"animation.json"

#Function to Load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.youtube.com/watch?v=bYye5NkmY1c" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.facebook.com/deckdicedimension/" target="_blank">Facebook</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#Function to apply snowfall effect
def run_snow_animation():
     rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

#Function to get the name from query parameters
def get_person_name():
    query_params = st.query_params
    return query_params.get("name", ["Huyen"])[0]



#Run snowfall animation
run_snow_animation()

#Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

#Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Happy Birthday, {PERSON_NAME}! 🎄", anchor=False)

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

# Personalized holiday message
st.markdown(
    f"Dear {PERSON_NAME}, wishing you a wonderful holiday season filled with joy and peace. 🌟"
)