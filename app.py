from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def story():
    content = """
    <html>
    <head>
        <title>The Chapter of Us</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background-color: #fff9f9;
                color: #333;
                margin: 40px;
                line-height: 1.8;
            }
            h1 {
                text-align: center;
                color: #e75480;
                font-size: 2.5em;
            }
            h2 {
                color: #e75480;
                margin-top: 40px;
            }
            img {
                display: block;
                margin: 20px auto;
                border-radius: 20px;
                width: 80%;
                max-width: 600px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            }
            p {
                text-align: justify;
                font-size: 1.05em;
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <h1>📖 The Chapter of Us</h1>

        <h2>💌 Chapter 1: When Strangers Cross Paths</h2>
        <img src="/static/chapter1.jpg" alt="Chapter 1">
        <p>We met as complete strangers during university life. I didn’t expect anything special at that time. You were just another person I happened to meet, but somehow you caught my attention. I had a small crush on you, but it wasn’t love. It was just a simple feeling that made me smile whenever I saw you around.</p>

        <h2>🌸 Chapter 2: From Smiles to Friendship</h2>
        <img src="/static/chapter2.jpg" alt="Chapter 2">
        <p>As time went by, we started talking more often and slowly became friends. Everything felt comfortable and easy between us. We shared jokes, random talks, and moments that slowly built a connection. I never thought that this simple friendship would one day turn into something much more meaningful.</p>

        <h2>🌙 Chapter 3: Getting Closer Without Realizing</h2>
        <img src="/static/chapter3.jpg" alt="Chapter 3">
        <p>Day by day, we became closer without even noticing it. We started sharing personal stories, helping each other, and being there through small ups and downs. It felt natural to open up to you. That’s when I realized how much you had already become a part of my everyday life.</p>

        <h2>💞 Chapter 4: The Beginning of Us</h2>
        <img src="/static/chapter4.jpg" alt="Chapter 4">
        <p>One day, I decided to take the first step and confess my feelings to you. I was nervous but ready to be honest about how I felt. When you said yes, I couldn’t stop smiling. That was the beginning of our relationship. It wasn’t dramatic or planned, it was just real, and it felt right.</p>

        <h2>🍲 Chapter 5: Learning to Cook for You</h2>
        <img src="/static/chapter5.jpg" alt="Chapter 5">
        <p>After we got together, I started learning how to cook from scratch. I wanted to do something special for you even though I didn’t know much about cooking. You were always appreciative of my effort and enjoyed whatever I made. Those moments made me happy because I knew you valued every little thing I did.</p>

        <h2>⚽ Chapter 6: Your Football Moments</h2>
        <img src="/static/chapter6.jpg" alt="Chapter 6">
        <p>Football has always been something you love deeply. I’ve always enjoyed watching you play and seeing how passionate you are about it. Every time you won or celebrated a victory, I felt proud of you. Those moments showed how much effort and dedication you put into what you love.</p>

        <h2>💔 Chapter 7: Standing Strong Through Hard Times</h2>
        <img src="/static/chapter7.jpg" alt="Chapter 7">
        <p>There came a point in my life when things got really hard for me. During that time, you didn’t leave my side. You stood by me and gave me all the support I needed. You carried my pain with me and helped me stay strong even when I felt like giving up. That was when I truly started to love you more deeply.</p>

        <h2>❤️ Chapter 8: Loving Each Other More</h2>
        <img src="/static/chapter8.jpg" alt="Chapter 8">
        <p>At first, I thought I was the one who loved harder. But over time, you proved me wrong. You showed love through small actions and patience. You were always there, being kind and understanding even when things were not perfect. That’s when I realized how much your love meant to me.</p>

        <h2>✈️ Chapter 9: Our Long-Distance Chapter</h2>
        <img src="/static/chapter9.jpg" alt="Chapter 9">
        <p>When uni like ended for you, we entered a new phase of our relationship. We had to continue our love story from a distance. It wasn’t easy, but we both made the effort to keep things strong. We call, talk, and stay connected no matter how far apart we are. Even though we’re not in the same place, it still feels like we’re close.</p>

        <h2>💫 Final Chapter: Our Story Continues</h2>
        <img src="/static/chapter10.jpg" alt="Chapter 10">
        <p>This isn’t the end of our story. It’s just another beginning for both of us. From being strangers to becoming each other’s person, we’ve come a long way together. There’s still so much more waiting for us ahead, and I’m excited to keep writing our chapters, one memory at a time.</p>

    </body>
    </html>
    """
    return render_template_string(content)

if __name__ == '__main__':
    app.run(debug=True)
