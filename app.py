import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Chapter of Us", page_icon="📖", layout="wide")

# --- CSS FOR ANIMATION & STYLE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

h1 {
    color: #e75480;
    text-align: center;
    font-size: 3rem;
    margin-top: 1rem;
}

.chapter {
    scroll-snap-align: start;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    animation: fadeIn 1.5s ease;
    text-align: center;
    padding: 2rem;
}

.chapter h2 {
    color: #e75480;
    font-size: 1.8rem;
    margin-bottom: 1rem;
}

.chapter p {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #444;
    max-width: 700px;
}

img {
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    width: 80%;
    max-width: 600px;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

.main {
    scroll-snap-type: y mandatory;
    overflow-y: scroll;
    height: 100vh;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1>📖 The Chapter of Us</h1>", unsafe_allow_html=True)

# --- CHAPTER DATA ---
chapters = [
    ("💌 Chapter 1: When Strangers Cross Paths", "chapter1.jpg",
     "We met as complete strangers during university life. I didn’t expect anything special at that time. You were just another person I happened to meet, but somehow you caught my attention. I had a small crush on you, but it wasn’t love. It was just a simple feeling that made me smile whenever I saw you around."),

    ("🌸 Chapter 2: From Smiles to Friendship", "chapter2.jpg",
     "As time went by, we started talking more often and slowly became friends. Everything felt comfortable and easy between us. We shared jokes, random talks, and moments that slowly built a connection. I never thought that this simple friendship would one day turn into something much more meaningful."),

    ("🌙 Chapter 3: Getting Closer Without Realizing", "chapter3.jpg",
     "Day by day, we became closer without even noticing it. We started sharing personal stories, helping each other, and being there through small ups and downs. It felt natural to open up to you. That’s when I realized how much you had already become a part of my everyday life."),

    ("💞 Chapter 4: The Beginning of Us", "chapter4.jpg",
     "One day, I decided to take the first step and confess my feelings to you. I was nervous but ready to be honest about how I felt. When you said yes, I couldn’t stop smiling. That was the beginning of our relationship. It wasn’t dramatic or planned, it was just real, and it felt right."),

    ("🍲 Chapter 5: Learning to Cook for You", "chapter5.jpg",
     "After we got together, I started learning how to cook from scratch. I wanted to do something special for you even though I didn’t know much about cooking. You were always appreciative of my effort and enjoyed whatever I made. Those moments made me happy because I knew you valued every little thing I did."),

    ("⚽ Chapter 6: Your Football Moments", "chapter6.jpg",
     "Football has always been something you love deeply. I’ve always enjoyed watching you play and seeing how passionate you are about it. Every time you won or celebrated a victory, I felt proud of you. Those moments showed how much effort and dedication you put into what you love."),

    ("💔 Chapter 7: Standing Strong Through Hard Times", "chapter7.jpg",
     "There came a point in my life when things got really hard for me. During that time, you didn’t leave my side. You stood by me and gave me all the support I needed. You carried my pain with me and helped me stay strong even when I felt like giving up. That was when I truly started to love you more deeply."),

    ("❤️ Chapter 8: Loving Each Other More", "chapter8.jpg",
     "At first, I thought I was the one who loved harder. But over time, you proved me wrong. You showed love through small actions and patience. You were always there, being kind and understanding even when things were not perfect. That’s when I realized how much your love meant to me."),

    ("✈️ Chapter 9: Our Long-Distance Chapter", "chapter9.jpg",
     "When university ended, we entered a new phase of our relationship. We had to continue our love story from a distance. It wasn’t easy, but we both made the effort to keep things strong. We call, talk, and stay connected no matter how far apart we are. Even though we’re not in the same place, it still feels like we’re close."),

    ("💫 Final Chapter: Our Story Continues", "chapter10.jpg",
     "This isn’t the end of our story. It’s just another beginning for both of us. From being strangers to becoming each other’s person, we’ve come a long way together. There’s still so much more waiting for us ahead, and I’m excited to keep writing our chapters, one memory at a time.")
]

# --- DISPLAY CONTENT ---
st.markdown('<div class="main">', unsafe_allow_html=True)
for title, image, text in chapters:
    st.markdown(f"""
        <div class="chapter">
            <h2>{title}</h2>
            <img src="{image}" alt="{title}">
            <p>{text}</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
