import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Chapter of Us", page_icon="📖", layout="wide")

# --- CSS STYLE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    scroll-behavior: smooth;
    background-color: #fff5f8;
}

h1 {
    color: #e75480;
    text-align: center;
    font-size: 3rem;
    margin-top: 1rem;
}

.chapter {
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    animation: fadeIn 1.2s ease;
    text-align: center;
    padding: 3rem 1rem;
}

.chapter h2 {
    color: #e75480;
    font-size: 1.8rem;
    margin-bottom: 1.2rem;
}

.chapter img {
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    width: 70%;
    height: auto;
    margin-bottom: 0.5rem;
}

.caption {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 1.5rem;
    font-style: italic;
}

.chapter p {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #333;
    max-width: 700px;
    text-align: justify;
    margin-top: 1rem;
}

hr {
    border: none;
    border-top: 2px solid #f3a6c0;
    width: 60%;
    margin: 3rem auto;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1>📖 The Chapter of Us</h1>", unsafe_allow_html=True)

# --- CHAPTER DATA ---
chapters = [
    ("💌 Chapter 1: When Strangers Cross Paths", "chapter1.jpg", 
     "The day we met, just two strangers crossing paths for the first time.",
     "We met as complete strangers during university life. I didn’t expect anything special at that time. You were just another person I happened to meet, but somehow you caught my attention. I had a small crush on you, but it wasn’t love. It was just a simple feeling that made me smile whenever I saw you around."),

    ("🌸 Chapter 2: From Smiles to Friendship", "chapter2.jpg", 
     "The start of countless smiles and shared laughter.",
     "As time went by, we started talking more often and slowly became friends. Everything felt comfortable and easy between us. We shared jokes, random talks, and moments that slowly built a connection. I never thought that this simple friendship would one day turn into something much more meaningful."),

    ("🌙 Chapter 3: Getting Closer Without Realizing", "chapter3.jpg",
     "We didn’t know it, but our hearts were already getting closer.",
     "Day by day, we became closer without even noticing it. We started sharing personal stories, helping each other, and being there through small ups and downs. It felt natural to open up to you. That’s when I realized how much you had already become a part of my everyday life."),

    ("💞 Chapter 4: The Beginning of Us", "chapter4.jpg",
     "The moment where friendship turned into love.",
     "One day, I decided to take the first step and confess my feelings to you. I was nervous but ready to be honest about how I felt. When you said yes, I couldn’t stop smiling. That was the beginning of our relationship. It wasn’t dramatic or planned, it was just real, and it felt right."),

    ("🍲 Chapter 5: Learning to Cook for You", "chapter5.jpg",
     "Every meal was made with love and a little nervousness.",
     "After we got together, I started learning how to cook from scratch. I wanted to do something special for you even though I didn’t know much about cooking. You were always appreciative of my effort and enjoyed whatever I made. Those moments made me happy because I knew you valued every little thing I did."),

    ("⚽ Chapter 6: Your Football Moments", "chapter6.jpg",
     "Watching you chase your dreams made me admire you more.",
     "Football has always been something you love deeply. I’ve always enjoyed watching you play and seeing how passionate you are about it. Every time you won or celebrated a victory, I felt proud of you. Those moments showed how much effort and dedication you put into what you love."),

    ("💔 Chapter 7: Standing Strong Through Hard Times", "chapter7.jpg",
     "When everything felt heavy, we carried it together.",
     "There came a point in my life when things got really hard for me. During that time, you didn’t leave my side. You stood by me and gave me all the support I needed. You carried my pain with me and helped me stay strong even when I felt like giving up. That was when I truly started to love you more deeply."),

    ("❤️ Chapter 8: Loving Each Other More", "chapter8.jpg",
     "Your love taught me patience, understanding, and peace.",
     "At first, I thought I was the one who loved harder. But over time, you proved me wrong. You showed love through small actions and patience. You were always there, being kind and understanding even when things were not perfect. That’s when I realized how much your love meant to me."),

    ("✈️ Chapter 9: Our Long-Distance Chapter", "chapter9.jpg",
     "Even miles apart, our hearts never stopped talking.",
     "When university ended, we entered a new phase of our relationship. We had to continue our love story from a distance. It wasn’t easy, but we both made the effort to keep things strong. We call, talk, and stay connected no matter how far apart we are. Even though we’re not in the same place, it still feels like we’re close."),

    ("💫 Final Chapter: Our Story Continues", "chapter10.jpg",
     "Every ending is just another beautiful beginning.",
     "This isn’t the end of our story. It’s just another beginning for both of us. From being strangers to becoming each other’s person, we’ve come a long way together. There’s still so much more waiting for us ahead, and I’m excited to keep writing our chapters, one memory at a time.")
]

# --- DISPLAY CONTENT ---
for title, image, caption, text in chapters:
    st.markdown(f"<div class='chapter'><h2>{title}</h2>", unsafe_allow_html=True)
    st.image(image, use_container_width=False, width=700)
    st.markdown(f"<div class='caption'>{caption}</div>", unsafe_allow_html=True)
    st.markdown(f"<p>{text}</p></div><hr>", unsafe_allow_html=True)
