import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Teacher's Day Celebration",
    page_icon="🖤",
    layout="wide"
)

# =========================================================
# BLACKPINK STYLE CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at top left, #3d0b2d 0%, transparent 30%),
        radial-gradient(circle at bottom right, #26001b 0%, transparent 30%),
        #080808;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Main width */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

/* Titles */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #ff1493;
    text-shadow:
        0 0 10px rgba(255,20,147,.7),
        0 0 25px rgba(255,20,147,.5);
}

.subtitle {
    text-align: center;
    color: #ffb6d9;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Cards */
.card {
    background: linear-gradient(145deg, #1b1b1b, #101010);
    border: 1px solid #ff1493;
    border-radius: 20px;
    padding: 25px;
    margin: 12px 0;
    box-shadow: 0 0 18px rgba(255,20,147,.15);
}

.card h2 {
    color: #ff69b4;
}

.card h3 {
    color: #ff8fc7;
}

.card p {
    color: #eeeeee;
}

/* Navigation buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #ff1493, #ff4db8) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 10px !important;
}

.stButton > button:hover {
    box-shadow: 0 0 18px rgba(255,20,147,.7);
    transform: translateY(-2px);
}

/* Inputs */
.stTextInput label,
.stTextArea label {
    color: #ff8fc7 !important;
    font-weight: 600 !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #171717 !important;
    color: white !important;
    border: 1px solid #ff1493 !important;
    border-radius: 12px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #100810;
    border-right: 1px solid #ff1493;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

hr {
    border-color: #ff1493;
    opacity: .3;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA
# =========================================================

teachers = [
    {
        "name": "Miss Sumaira Tabassum",
        "subject": "Urdu",
        "message": "Thank you for inspiring us every day! 💗"
    },
    {
        "name": "Miss Shanza",
        "subject": "Mathematics",
        "message": "You make difficult things easy to understand! 🌸"
    },
    {
        "name": "Ms. Fareeha",
        "subject": "Science",
        "message": "Thank you for making learning exciting! ✨"
    },
    {
        "name": "Miss Fahmida",
        "subject": "Urdu",
        "message": "Your kindness makes our classroom special! 🖤"
    },
     {
        "name": "Miss Ayesha altaf",
        "subject": "English",
        "message": "Your kindness makes our classroom special! 🖤"
    },
      {
        "name": "Miss Tanveer",
        "subject": "Spoken English",
        "message": "Your kindness makes our classroom special! 🖤"
    },
      {
        "name": "Miss Malaika",
        "subject": "Computer",
        "message": "Your kindness makes our classroom special! 🖤"
    },
]
]

teams = {
    "A123": {
        "team": "Chair Champs",
        "leader": "Mukkarma",
        "task": "Arrange chairs"
    },
    "B456": {
        "team": "Sparkle Squad",
        "leader": "Lisa",
        "task": "Decorate the board"
    },
    "C789": {
        "team": "Snack Stars",
        "leader": "Rosé",
        "task": "Serve snacks"
    },
    "D111": {
        "team": "Bloom Crew",
        "leader": "Jisoo",
        "task": "Table decoration"
    }
}

schedule = [
    ("09:00 AM", "Welcome Ceremony"),
    ("09:45 AM", "Cake Cutting 🎂"),
    ("10:00 AM","Picture time"),
    ("10:15 AM", "Lunch Party"),
    ("12:00 PM", "Thank You Session")
]


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.markdown(
    "<h1 style='color:#ff1493;'>🖤💗 Teacher's day</h1>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='color:#ffb6d9;'>Teacher's Day Celebration</p>",
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "🌸 Choose a page",
    [
        "🏠 Home",
        "👩‍🏫 Teachers",
        "🎀 Teams & Tasks",
        "🗓️ Schedule",
        "🏆 Awards"
    ]
)


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🖤💗 HAPPY TEACHER\'S DAY 💗🖤</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Celebrating the amazing teachers who inspire us every day ✨'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h2>👩‍🏫 Teachers</h2>
            <p>Meet the wonderful teachers who make learning special.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>🎉 Celebration</h2>
            <p>Enjoy speeches, games, performances and awards.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h2>💌 Appreciation</h2>
            <p>Leave a special thank-you message for your teacher.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h2>🌸 Welcome to Our Celebration!</h2>
        <p>
        Teachers plant the seeds of knowledge that grow forever.
        Let's make this Teacher's Day memorable with love,
        appreciation and lots of smiles! 💗
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# TEACHERS
# =========================================================

elif page == "👩‍🏫 Teachers":

    st.markdown(
        '<div class="main-title">👩‍🏫 OUR AMAZING TEACHERS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">The people who inspire us every day 💗</div>',
        unsafe_allow_html=True
    )

    for teacher in teachers:

        st.markdown(
            f"""
            <div class="card">
                <h2>🌸 {teacher['name']}</h2>
                <h3>📚 Subject: {teacher['subject']}</h3>
                <p>💌 {teacher['message']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TEAMS & TASKS
# =========================================================

elif page == "🎀 Teams & Tasks":

    st.markdown(
        '<div class="main-title">🎀 TEAMS & TASKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Find your celebration duty using your team code.</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "🌸 Enter your name",
        placeholder="Your name..."
    )

    code = st.text_input(
        "🎟️ Enter your team code",
        placeholder="Example: A123"
    )

    if st.button("✨ SHOW MY TASK ✨"):

        if code in teams:

            info = teams[code]

            st.success(f"💗 Hello {name or 'BLINK'}!")

            st.write("🌸 **Team:**", info["team"])
            st.write("👑 **Leader:**", info["leader"])
            st.write("🎀 **Your Task:**", info["task"])

        else:

            st.error(
                "❌ Invalid code. Please check your team code."
            )


# =========================================================
# SCHEDULE
# =========================================================

elif page == "🗓️ Schedule":

    st.markdown(
        '<div class="main-title">🗓️ CELEBRATION SCHEDULE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">A day full of fun, appreciation and memories ✨</div>',
        unsafe_allow_html=True
    )

    for time, activity in schedule:

        st.markdown(
            f"""
            <div class="card">
                <h3>⏰ {time}</h3>
                <h2>{activity}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

elif page == "🏆 Awards":

    st.markdown(
        '<div class="main-title">🏆 TEACHER AWARDS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Celebrating teachers for their wonderful qualities 💗</div>',
        unsafe_allow_html=True
    )

    awards = [
        ("🌟", "Most Inspiring Teacher"),
        ("💗", "Most Caring Teacher"),
        ("😊", "Friendliest Teacher"),
        ("📚", "Best Mentor"),
        ("✨", "Students' Choice Award")
    ]

    for icon, award in awards:

        st.markdown(
            f"""
            <div class="card">
                <h2>{icon} {award}</h2>
                <p>
                    This award celebrates a teacher who makes
                    a positive difference in students' lives.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <p style="text-align:center;color:#ff8fc7;">
        🖤💗 Made with love for Teacher's Day 💗🖤
    </p>
    """,
    unsafe_allow_html=True
)
