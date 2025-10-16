import streamlit as st

# App title
st.set_page_config(page_title="Our Love Story ❤️", layout="centered")

# Background song
audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Main heading
st.title("The Chapters Of Us ❤️")

st.write("This is our little journey together, filled with laughter, memories, and love. Each photo here reminds me of how special you are to me.")

# Chapters and captions
chapters = {
    "chapter1.jpg": "This is where it all began. I still remember how happy we were that day. Every time I look at this picture, I feel that same warmth and comfort.",
    "chapter2.jpg": "You made this moment unforgettable. We laughed so much that day, and it felt like the world stopped just for us.",
    "chapter3.jpg": "This picture always makes me smile. You looked so effortlessly perfect, and being beside you made everything better.",
    "chapter4.jpg": "One of my favorite memories. The way you looked at me here was everything — full of love and peace.",
    "chapter5.jpg": "I love this picture because it captures our real selves — no posing, no pretending, just us being happy together.",
    "chapter6.jpg": "Every time I see this, I remember how lucky I am. I never thought someone could make me feel this safe and loved.",
    "chapter7.jpg": "This moment still feels like yesterday. I wish I could relive it again, just to hold your hand one more time there.",
    "chapter8.jpg": "We may not always be perfect, but this picture reminds me that we’ve always chosen each other, no matter what.",
    "chapter9.jpg": "This day was full of laughter and love. You always know how to make every simple thing feel so special.",
    "chapter10.jpg": "The final chapter — but really, it’s just the beginning of our forever story. I love you more than words can ever say."
}

# Show each photo and caption
for photo, caption in chapters.items():
    st.image(photo, use_column_width=True)
    st.write(caption)
    st.markdown("---")
