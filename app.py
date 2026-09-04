import streamlit as st

st.set_page_config(page_title="Pitch Checker", page_icon="🎤", layout="centered")

st.title("CREO Pitch Checker")
st.caption("Paste your 6-minute pitch. Get told whether it will actually fit.")

WORDS_PER_MINUTE = 130  # a calm presenting pace

text = st.text_area(
    "Your pitch script",
    height=200,
    placeholder="We built this for Ananya, a second-year student who...",
)

if st.button("Check it", type="primary"):
    if not text.strip():
        st.warning("Paste something first.")
    else:
        words = len(text.split())
        seconds = words / WORDS_PER_MINUTE * 60
        minutes = int(seconds // 60)
        rest = int(seconds % 60)

        col1, col2 = st.columns(2)
        col1.metric("Words", words)
        col2.metric("Spoken length", f"{minutes}:{rest:02d}")

        if seconds > 360:
            over = int(seconds - 360)
            st.error(f"You are {over} seconds over. Cut roughly {int(over / 60 * WORDS_PER_MINUTE)} words.")
        elif seconds < 240:
            st.warning("Under 4 minutes. You have room for more demo.")
        else:
            st.success("Fits inside 6 minutes with breathing space.")

        st.divider()
        st.subheader("Things juries do not like hearing")
        flags = {
            "good morning respected jury": "Skip the greeting. Start inside the story.",
            "as you can see": "Say what it does, not what is on screen.",
            "revolutionary": "Show it instead of claiming it.",
            "disrupt": "Same. Concrete beats visionary.",
            "we would like to": "Just do the thing.",
        }
        lower = text.lower()
        found = [(p, note) for p, note in flags.items() if p in lower]
        if found:
            for phrase, note in found:
                st.write(f"**“{phrase}”** — {note}")
        else:
            st.write("Nothing flagged. Clean script.")

