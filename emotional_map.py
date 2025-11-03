import streamlit as st
import plotly.graph_objects as go

# --------- EMOTIONAL DATABASE ---------
emotions = {
    "anger": {"inherited": 70, "learned": 30, "notes": "Quick-reacting nervous system; often triggered by learned beliefs."},
    "kindness": {"inherited": 60, "learned": 40, "notes": "Empathy wiring + valuing social goodness."},
    "sadness": {"inherited": 80, "learned": 20, "notes": "Deep emotional capacity + learned meanings."},
    "love": {"inherited": 70, "learned": 30, "notes": "Bonding chemistry + attachment patterns."},
    "fear": {"inherited": 85, "learned": 15, "notes": "Hardwired survival response + life experience."}
}

# --------- APP CONFIGURATION ---------
st.set_page_config(
    page_title="Emotional Map Explorer",
    page_icon="💫",
    layout="centered"
)

st.title("💫 Emotional Map Explorer")
st.write("Type an emotion and discover whether it is mostly inherited, learned, or a mix.")

# --------- SESSION HISTORY ---------
if "history" not in st.session_state:
    st.session_state.history = []

# --------- USER INPUT ---------
emotion_input = st.text_input("Enter an emotion:")

if emotion_input:
    key = emotion_input.lower()
    if key in emotions:
        data = emotions[key]
        
        st.subheader(f"Emotion: {emotion_input.capitalize()}")
        st.write(f"**Notes:** {data['notes']}")
        
        # Pie chart for inherited vs learned
        fig = go.Figure(data=[go.Pie(
            labels=["Inherited", "Learned"],
            values=[data['inherited'], data['learned']],
            marker=dict(colors=['#FF6F61','#6B5B95']),
            hole=0.4
        )])
        
        fig.update_layout(title_text="Inherited vs Learned Composition", title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        
        # Add to history
        st.session_state.history.append(emotion_input.capitalize())
    else:
        st.warning("Emotion not in database. Try another or expand the list.")

# --------- SHOW HISTORY ---------
if st.session_state.history:
    st.subheader("Session History")
    st.write(", ".join(st.session_state.history))
