import streamlit as st
import time
from app import run_wingman_pipeline

st.set_page_config(page_title="Sparkeefy Wingman", page_icon="🧠", layout="centered")

st.title("Sparkeefy Wingman 🧠💬")
st.markdown("Your smart friend for modern relationships, texting, and emotional navigation.")

st.markdown("---")

st.subheader("Enter Situation")
situation = st.text_area("What's happening? (e.g., 'She replied nice after I sent three photos')", height=150)

if st.button("Get Wingman Advice", type="primary"):
    if not situation.strip():
        st.warning("Please enter a situation first!")
    else:
        with st.spinner("Analyzing energy and generating strategies..."):
            try:
                # Add a tiny artificial delay to make it feel like it's "thinking" despite Groq being too fast
                time.sleep(0.5) 
                
                result = run_wingman_pipeline(situation)
                
                st.markdown("---")
                
                # Check for safety flag
                if result.get("safety_flag"):
                    st.error("⚠️ Safety Flag Triggered: The advice generated was flagged for potentially violating safety guidelines (manipulation, coercion, etc). Please review your situation.")
                else:
                    # Energy Read
                    st.subheader("⚡ Energy Read")
                    st.info(f"**{result.get('energy_read', 'Unknown')}**")
                    
                    # Wingman Response
                    st.subheader("🤖 Wingman Response")
                    st.success(result.get("wingman_response", "No response generated."))
                    
                    # Suggested Messages
                    st.subheader("💬 Suggested Messages")
                    messages = result.get("suggested_messages", [])
                    if messages:
                        for i, msg in enumerate(messages, 1):
                            st.code(msg, language=None)
                    else:
                        st.write("No specific messages suggested.")
                        
                    # Follow-up Question
                    follow_up = result.get("follow_up_question")
                    if follow_up:
                        st.subheader("❓ Clarification Needed")
                        st.warning(follow_up)
                        
                    # Confidence
                    st.markdown("---")
                    st.caption(f"📊 Confidence Score: {result.get('confidence', 0.0)}")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
