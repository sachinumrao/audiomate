import os
import time
import pathlib
import streamlit as st

# set wide laytout and other page configs
st.set_page_config(
    page_title="Audiomate",
    page_icon=":material/play_circle:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# configs
TTS_VOCIE_OPTIONS = {
    "Kokoro": ["James", "Ava"]
}

# load styles
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("./src/style.css")
load_css(file_path=css_path)

# set session state default values
if "task" not in st.session_state:
    st.session_state["task"] = None

if "tts_model" not in st.session_state:
    st.session_state["tts_model"] = None

if "voice_option" not in st.session_state:
    st.session_state["voice_option"] = None

if "speed" not in st.session_state:
    st.session_state["speed"] = 1.0


def main():
    # create title
    app_title = "Audiomate"
    st.title(app_title, width="stretch", text_alignment="center")
    st.html("<hr>")

    # create sidebar
    with st.sidebar:
        task = st.selectbox(label="Task:", options=["Text-To-Speech", "Speech-To-Text"], index=0, key="sidebar_task_label")
        st.session_state["task"] = task

        # add TTS specific settings: TTS model, Voice Options, Speed
        if task == "Text-To-Speech":
            tts_model = st.selectbox(label="Model:", options=["Kokoro"], index=0, key="sidebar_tts_model_label")
            voice_option = st.selectbox(label="Voice Options:", options=TTS_VOCIE_OPTIONS[tts_model], index=0, key="sidebar_tts_voice_label")
            speed = st.slider(label="Speed:", min_value=0.50, max_value=2.00, value=1.00, step=0.05, key="sidebar_tts_speed")

            # update params in session state
            st.session_state["tts_model"] = tts_model
            st.session_state["voice_option"] = voice_option
            st.session_state["speed"] = speed

    # create main page layout
    # input for tts
    if st.session_state["task"] == "Text-To-Speech":
        pass

    if st.session_state["task"] == "Speech-To-Text":
        # file upload
        pass





if __name__ == "__main__":
    main()
