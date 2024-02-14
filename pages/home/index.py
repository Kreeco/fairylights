import streamlit as st
def home():
    st.title("🚀 100 GenAI projects 🤖")
    st.write("I can't wait to explore what's possible with generative AI with you by shipping 100 happy and helpful use-cases. Every project shipped here has solved a problem for at least one real person.")
    st.write("Try them out for yourself, and [subscribe for the newest possibilities](https://fairylightsai.substack.com/) 💌🥰")

    st.subheader("✨Magical Moments")
    st.warning("- 🏆 I co-won the [people's choice award at Fishburners Young Entrepreneur Pitch Night](https://www.linkedin.com/posts/martinkarafilis_entrepreneurs-genz-ai-activity-7120197635935768576-mG7E) for a robotic plush panda you can have a two-way convo with (collab project with a friend who did the IOT and I did the GenAI). \n - 🚀 One of my proprietry GenAI use-cases (specialist profile generator from scraped data) led to a 350% in organic traffic and 300% increase in patient bookings for a health startup in a single month. \n - 👷 I became a community advisor at [Builders club](https://www.linkedin.com/company/the-builders-club-ai/), and spearhead the [Humans of Builders club series](https://builder-club.beehiiv.com/).")
    with st.expander("🥰 See full timeline of magical milestones!"):
            st.markdown("**Feb 2023**")
            st.markdown("- 🎉 Got accepted onto Microsoft's Startup Founder Hub ($2.5k OpenAI credits + more).")

            st.markdown("**Dec 2023**")
            st.markdown("- 🎉 Launched this 100 GenAI project site with first use-case.")

            st.markdown("**Nov 2023**")
            st.markdown("- 🚀 One of my proprietry GenAI use-cases led to a 350% in organic traffic and 300% increase in patient bookings for a health startup in a single month.")

            st.markdown("**Oct 2023**")
            st.markdown("- 👷‍ Became a community advisor at [AI Builders Club](https://www.linkedin.com/company/the-builders-club-ai/) which does weekly hackathons and opens up a world of opportunities for fellow builders and founders (joined at 250 members on the Slack channel).")
            st.markdown("- 🚀‍ Launched [Humans of Builders club series](https://builder-club.beehiiv.com/), which interviews builders about their incredibly inspiring build journeys.")

            st.markdown("**Sep 2023**")
            st.markdown("- 📈 First 50 subscribers at [Fairylights newsletter](https://fairylightsai.substack.com/).")
            st.markdown("- 🏆 Won people's choice award at Fishburners Young Entrepreneur Pitch Night for a robotic plush panda you can have a two-way convo with (collab project with a friend who did the IOT and I did the GenAI).")
            st.write("")
            st.image("images/pitch_panda.webp")

            st.markdown("**Aug 2023**")
            st.markdown("- 🚀 Started Fairylights newsletter ([sign up here](https://fairylightsai.substack.com/)).")
            st.write("")

    st.subheader("Pitch Panda")
    st.write("A robotic plush panda you can have a two-way convo with! Winner of the People's Choice Award at a Young Entrepreneur Pitch night. Collab project!")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=pitch-panda)")
    st.image("images/featured/pitch_panda.png", use_column_width=True)

    st.subheader("Thought Checker")
    st.write("Enter a journal entry and this GenAI program will auto-detect unhelpful thinking patterns (cognitive distortions) that are present in your entry, so you can focus on reframing them.")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=thought-checker)")
    st.image("images/featured/thought_checker.png", use_column_width=True)

    st.subheader("Transcript Analyser")
    st.write("Upload transcripts of user interviews, YouTube videos, podcasts etc and get back direct quotes that are related to specific questions or topics.")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=transcript-analyser)")
    st.image("images/featured/transcript_analyser.png", use_column_width=True)

    st.subheader("Ask Your Database")
    st.write("Upload CSV files, ask questions about your data in plain english and this GenAI program with auto-generate and execute a SQL statement to retrieve the data you need to answer the question.")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=ask-your-database)")
    st.image("images/featured/ask_your_database.png", use_column_width=True)

    st.subheader("Lip Syncing Avatar")
    st.write("Turn any character image into a lip-syncing avatar that you can use in product demos, to bring your children's stories to life or create virtual gift cards!")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=lip-syncing-avatar)")
    st.image("images/featured/lip_syncing_avatar.png", use_column_width=True)

    st.subheader("Chatty Characters")
    st.write("Generate a 3D avatar character and then chat to them via text, they will respond back to you by talking! The voice matches character gender too (male, female, other).")
    st.markdown("[Try it out!](https://100-genai-projects.streamlit.app/?project=chatty-character)")
    st.image("images/featured/chatty_characters.png", use_column_width=True)