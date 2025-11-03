import streamlit as st
import plotly.graph_objects as go

# Initialize session state for database and history
if "emotions" not in st.session_state:
    st.session_state.emotions = {
        "anger": {"inherited": 70, "learned": 30, "notes": "Quick-reacting nervous system; often triggered by learned beliefs."},
        "kindness": {"inherited": 60, "learned": 40, "notes": "Empathy wiring + valuing social goodness."},
        "sadness": {"inherited": 80, "learned": 20, "notes": "Deep emotional capacity + learned meanings."},
        "love": {"inherited": 70, "learned": 30, "notes": "Bonding chemistry + attachment patterns."},
        "fear": {"inherited": 85, "learned": 15, "notes": "Hardwired survival response + life experience."}
    }

if "history" not in st.session_state:
    st.session_state.history = []

# --- App Configuration ---
st.set_page_config(page_title="Emotional Map Explorer", page_icon="💫", layout="centered")
st.title("💫 Emotional Map Explorer")
st.write("Explore emotions and see whether they are inherited, learned, or a mix. You can also add new emotions!")

# --- Section: Add New Emotion ---
st.subheader("Add a New Emotion")
with st.form(key="add_emotion_form"):
    new_emotion = st.text_input("Emotion Name:")
    inherited = st.slider("Inherited (%)", 0, 100, 50)
    learned = st.slider("Learned (%)", 0, 100, 50)
    notes = st.text_area("Notes / Description:")
    submit = st.form_submit_button("Add Emotion")

if submit:
    if new_emotion.strip() == "":
        st.warning("Please enter an emotion name.")
    else:
        st.session_state.emotions[new_emotion.lower()] = {
            "inherited": inherited,
            "learned": learned,
            "notes": notes
        }
        st.success(f"Emotion '{new_emotion}' added successfully!")

# --- Section: Explore Emotion ---
st.subheader("Explore an Emotion")
emotion_input = st.text_input("Enter an emotion to explore:")

if emotion_input:
    key = emotion_input.lower()
    if key in st.session_state.emotions:
        data = st.session_state.emotions[key]
        st.subheader(f"Emotion: {emotion_input.capitalize()}")
        st.write(f"**Notes:** {data['notes']}")
        
        fig = go.Figure(data=[go.Pie(
            labels=["Inherited", "Learned"],
            values=[data['inherited'], data['learned']],
            marker=dict(colors=['#FF6F61','#6B5B95']),
            hole=0.4
        )])
        fig.update_layout(title_text="Inherited vs Learned Composition", title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        
        st.session_state.history.append(emotion_input.capitalize())
    else:
        st.warning("Emotion not found. You can add it above!")

# --- Section: Show History ---
if st.session_state.history:
    st.subheader("Session History")
    st.write(", ".join(st.session_state.history))
