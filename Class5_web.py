import streamlit as st
import sqlite3
import random
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Teacher's Day Celebration",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect("teachers_day.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    teacher TEXT,
    message TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    award TEXT,
    teacher TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    memory TEXT,
    created_at TEXT
)
""")

conn.commit()

# =========================================================
# TEACHER DATA
# =========================================================

teachers = [
    {
        "name": "Miss Sumaira Tabassum",
        "subject": "Urdu",
        "code": "T101",
        "emoji": "🌸",
        "message": "You make our language shine with beauty. 💗",
        "task": "Prepare a beautiful Urdu appreciation card for your teacher."
    },
    {
        "name": "Miss Shanza",
        "subject": "Mathematics",
        "code": "T102",
        "emoji": "🧮",
        "message": "You make numbers feel like magic. ✨",
        "task": "Create a fun mathematics appreciation challenge."
    },
    {
        "name": "Ms. Fareeha",
        "subject": "Science",
        "code": "T103",
        "emoji": "🔬",
        "message": "You show us the wonders behind everything. 🔬✨",
        "task": "Prepare a mini science-themed surprise."
    },
    {
        "name": "Miss Fahmida",
        "subject": "Islamiat",
        "code": "T104",
        "emoji": "🌙",
        "message": "You guide us with wisdom and faith. 🖤",
        "task": "Prepare a respectful appreciation message."
    },
    {
        "name": "Miss Ayesha Altaf",
        "subject": "English",
        "code": "T105",
        "emoji": "📖",
        "message": "You turn words into worlds. 🖤",
        "task": "Write a creative English thank-you note."
    },
    {
        "name": "Miss Tanveer",
        "subject": "Spoken English",
        "code": "T106",
        "emoji": "🎤",
        "message": "You give us confidence to speak the world's language. 🖤",
        "task": "Prepare a short spoken-English appreciation speech."
    },
    {
        "name": "Miss Malaika",
        "subject": "Computer",
        "code": "T107",
        "emoji": "💻",
        "message": "You open doors to the digital future. 🖤",
        "task": "Create a small digital surprise for Teacher's Day."
    }
]

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

if "selected_teacher" not in st.session_state:
    st.session_state.selected_teacher = None

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #4b0737 0%, transparent 28%),
        radial-gradient(circle at 90% 90%, #360025 0%, transparent 30%),
        #070707;
    color: white;
    font-family: 'Poppins', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* MAIN TITLE */

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #ff1493;
    text-shadow:
        0 0 10px rgba(255,20,147,.8),
        0 0 25px rgba(255,20,147,.5);
}

.subtitle {
    text-align: center;
    color: #ffb6d9;
    font-size: 18px;
    margin-bottom: 30px;
}

/* CARDS */

.card {
    background: linear-gradient(145deg, #1b1b1b, #0e0e0e);
    border: 1px solid #ff1493;
    border-radius: 22px;
    padding: 24px;
    margin: 12px 0;
    box-shadow: 0 0 20px rgba(255,20,147,.15);
    transition: .3s;
}

.card:hover {
    box-shadow: 0 0 28px rgba(255,20,147,.35);
    transform: translateY(-2px);
}

.card h2 {
    color: #ff69b4;
}

.card h3 {
    color: #ff9bd0;
}

.card p {
    color: #eeeeee;
}

/* HERO */

.hero {
    padding: 45px;
    border-radius: 30px;
    text-align: center;
    background:
        linear-gradient(
            135deg,
            rgba(255,20,147,.18),
            rgba(0,0,0,.75)
        );
    border: 1px solid #ff1493;
    box-shadow: 0 0 35px rgba(255,20,147,.2);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 55px;
    color: #ff1493;
    margin-bottom: 10px;
}

.hero p {
    color: #ffc4e2;
    font-size: 20px;
}

/* SPECIAL GOODBYE */

.goodbye-hero {
    padding: 55px 35px;
    border-radius: 35px;
    text-align: center;
    background:
        linear-gradient(
            135deg,
            rgba(255,20,147,.25),
            rgba(80,0,55,.45),
            rgba(0,0,0,.85)
        );
    border: 2px solid #ff69b4;
    box-shadow:
        0 0 25px rgba(255,20,147,.3),
        inset 0 0 30px rgba(255,20,147,.08);
    margin-bottom: 30px;
}

.goodbye-hero h1 {
    font-size: 58px;
    color: #ff69b4;
    text-shadow:
        0 0 10px #ff1493,
        0 0 25px rgba(255,20,147,.7);
}

.goodbye-hero h2 {
    color: #ffb6d9;
    font-size: 28px;
}

.goodbye-hero p {
    color: #eeeeee;
    font-size: 19px;
    line-height: 1.8;
}

.memory-card {
    background: linear-gradient(145deg, #20101c, #0d0d0d);
    border: 1px solid #ff69b4;
    border-radius: 25px;
    padding: 28px;
    text-align: center;
    min-height: 210px;
    box-shadow: 0 0 20px rgba(255,20,147,.12);
}

.memory-card h2 {
    font-size: 42px;
}

.memory-card h3 {
    color: #ff69b4;
}

.memory-card p {
    color: #eeeeee;
    line-height: 1.7;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #ff1493,
        #ff4db8
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 13px !important;
    font-weight: 700 !important;
    padding: 11px !important;
    transition: .2s;
}

.stButton > button:hover {
    box-shadow: 0 0 20px rgba(255,20,147,.8);
    transform: translateY(-2px);
}

/* INPUTS */

.stTextInput label,
.stTextArea label,
.stSelectbox label {
    color: #ff9bd0 !important;
    font-weight: 600 !important;
}

.stTextInput input,
.stTextArea textarea {
    background: #171717 !important;
    color: white !important;
    border: 1px solid #ff1493 !important;
    border-radius: 12px !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #100810;
    border-right: 1px solid #ff1493;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #151015;
    border: 1px solid #ff1493;
    padding: 15px;
    border-radius: 18px;
}

[data-testid="stMetricValue"] {
    color: #ff69b4 !important;
}

/* DIVIDER */

hr {
    border-color: #ff1493;
    opacity: .3;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#ff1493;">🖤💗</h1>
        <h2 style="color:#ff69b4;">Teacher's Day</h2>
        <p style="color:#ffb6d9;">Celebration Portal</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# ONLY THESE 5 PAGES
pages = [
    "🏠 Home",
    "👩‍🏫 Teachers",
    "✨ My Teacher Task",
    "💌 Appreciation Wall",
    "🌷 Special Goodbye"
]

page = st.sidebar.radio(
    "🌸 Explore",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="text-align:center;color:#ff8fc7;">
        Made with 💗 by students
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">

        <h1>
        🖤💗 HAPPY TEACHER'S DAY 💗🖤
        </h1>

        <p>
        Celebrating the people who inspire us
        to dream bigger ✨
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown(
        "## 🌸 Welcome to the Celebration Portal"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👩‍🏫 Teachers",
            len(teachers)
        )

    with col2:

        message_count = cursor.execute(
            "SELECT COUNT(*) FROM messages"
        ).fetchone()[0]

        st.metric(
            "💌 Messages",
            message_count
        )

    with col3:

        memory_count = cursor.execute(
            "SELECT COUNT(*) FROM memories"
        ).fetchone()[0]

        st.metric(
            "📸 Memories",
            memory_count
        )

    st.markdown("---")

    st.markdown("""
    <div class="card">

        <h2>
        🌷 A Special Message
        </h2>

        <p>
        A teacher doesn't simply teach lessons.
        A teacher inspires dreams, builds confidence,
        encourages creativity and helps students discover
        what they are capable of.
        </p>

        <h3>
        Thank you, teachers! 💗
        </h3>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ✨ Quick Access")

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button("👩‍🏫 Meet Teachers"):

            st.session_state.page = "👩‍🏫 Teachers"
            st.rerun()

    with c2:

        if st.button("✨ Find My Task"):

            st.session_state.page = "✨ My Teacher Task"
            st.rerun()

    with c3:

        if st.button("💌 Write Appreciation"):

            st.session_state.page = "💌 Appreciation Wall"
            st.rerun()

# =========================================================
# TEACHERS
# =========================================================

elif page == "👩‍🏫 Teachers":

    st.markdown(
        '<div class="main-title">👩‍🏫 OUR AMAZING TEACHERS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">The stars of our celebration 💗</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for i, teacher in enumerate(teachers):

        with cols[i % 2]:

            st.markdown(
                f"""
                <div class="card">

                    <h2>
                    {teacher['emoji']} {teacher['name']}
                    </h2>

                    <h3>
                    📚 {teacher['subject']}
                    </h3>

                    <p>
                    💌 {teacher['message']}
                    </p>

                    <p>
                    <b style="color:#ff69b4;">
                    Teacher Code: {teacher['code']}
                    </b>
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# MY TEACHER TASK
# =========================================================

elif page == "✨ My Teacher Task":

    st.markdown(
        '<div class="main-title">✨ FIND YOUR TEACHER TASK</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Enter your teacher code and unlock the surprise 🎁</div>',
        unsafe_allow_html=True
    )

    code = st.text_input(
        "🔐 Enter Teacher Code",
        placeholder="Example: T101"
    )

    if st.button("✨ SHOW MY TASK ✨"):

        found = None

        for teacher in teachers:

            if teacher["code"].upper() == code.strip().upper():

                found = teacher
                break

        if found:

            st.session_state.selected_teacher = found

            st.success("Teacher found! 🎉")

            st.markdown(
                f"""
                <div class="hero">

                    <h1>
                    {found['emoji']} {found['name']}
                    </h1>

                    <p>
                    📚 {found['subject']}
                    </p>

                    <hr>

                    <h2 style="color:#ff69b4;">
                    🎯 YOUR SPECIAL TASK
                    </h2>

                    <p>
                    {found['task']}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.snow()

        else:

            st.error(
                "❌ Teacher code not found. Please check the code."
            )

    st.markdown("---")

    st.info(
        "💡 Teacher codes are displayed on the Teachers page."
    )

# =========================================================
# APPRECIATION WALL
# =========================================================

elif page == "💌 Appreciation Wall":

    st.markdown(
        '<div class="main-title">💌 APPRECIATION WALL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Leave a message that your teacher will remember 🌸</div>',
        unsafe_allow_html=True
    )

    student = st.text_input(
        "👤 Your Name",
        placeholder="Enter your name"
    )

    teacher_names = [
        teacher["name"]
        for teacher in teachers
    ]

    selected_teacher = st.selectbox(
        "👩‍🏫 Choose Teacher",
        teacher_names
    )

    message = st.text_area(
        "💌 Your Appreciation Message",
        placeholder="Write something special..."
    )

    if st.button("💗 POST MESSAGE"):

        if student.strip() and message.strip():

            cursor.execute(
                """
                INSERT INTO messages
                (student, teacher, message, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    student,
                    selected_teacher,
                    message,
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    )
                )
            )

            conn.commit()

            st.success(
                "💗 Your message has been added!"
            )

            st.rerun()

        else:

            st.warning(
                "Please enter your name and message."
            )

    st.markdown("---")

    st.markdown(
        "## 🌸 Messages from Students"
    )

    messages = cursor.execute(
        """
        SELECT student, teacher, message, created_at
        FROM messages
        ORDER BY id DESC
        """
    ).fetchall()

    if not messages:

        st.info(
            "No messages yet. Be the first one! 💌"
        )

    for student_name, teacher_name, msg, created in messages:

        st.markdown(
            f"""
            <div class="card">

                <h3>
                💗 {student_name} → {teacher_name}
                </h3>

                <p>
                “{msg}”
                </p>

                <small style="color:#888;">
                {created}
                </small>

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# SPECIAL GOODBYE - MISS SHANZA
# =========================================================

elif page == "🌷 Special Goodbye":

    st.markdown(
        '<div class="main-title">🌷 A SPECIAL GOODBYE 🌷</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">For our beloved Maths Teacher, Miss Shanza 💗</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # GOODBYE HERO
    # -----------------------------------------------------

    st.markdown("""
    <div class="goodbye-hero">

        <h1>
        🧮💗 MISS SHANZA 💗🧮
        </h1>

        <h2>
        Our Maths Teacher • Our Memories • Our Inspiration
        </h2>

        <p>
        "Some teachers leave the school,
        but they never leave our hearts." 🌸
        </p>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # LETTER
    # -----------------------------------------------------

    st.markdown("""
    <div class="card">

        <h2>
        💌 Dear Miss Shanza,
        </h2>

        <p style="font-size:18px;line-height:1.9;">

        You may have left our school, but the lessons,
        memories and moments you gave us will always
        remain a beautiful part of our Class 5 journey. 💗

        </p>

        <p style="font-size:18px;line-height:1.9;">

        You taught us more than just numbers and equations.
        You taught us to keep trying when a question seemed
        difficult and to never give up. 🧮✨

        </p>

        <p style="font-size:18px;line-height:1.9;">

        We will miss your classes, your explanations,
        your corrections and all those little moments
        that made our Maths lessons special. 🥺🌷

        </p>

        <p style="font-size:18px;line-height:1.9;">

        Wherever you are, we hope you know that your students
        remember you with love, respect and gratitude. 💗

        </p>

        <h2 style="text-align:center;">
        💗 Thank You For Everything, Miss Shanza! 💗
        </h2>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # MEMORY CARDS
    # -----------------------------------------------------

    st.markdown(
        "## 🌸 What We Will Remember"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="memory-card">

            <h2>🧮</h2>

            <h3>
            Maths Lessons
            </h3>

            <p>
            The equations, questions,
            practice and all those moments
            when Maths finally made sense! ✨
            </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="memory-card">

            <h2>😂</h2>

            <h3>
            Classroom Memories
            </h3>

            <p>
            The smiles, little jokes,
            questions and unforgettable
            classroom moments. 💗
            </p>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="memory-card">

            <h2>🌟</h2>

            <h3>
            Your Lessons
            </h3>

            <p>
            The confidence to keep trying
            even when the answer wasn't
            easy to find. 💪✨
            </p>

        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # MEMORY FORM
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown(
        "## 💌 Leave a Memory for Miss Shanza"
    )

    st.markdown(
        """
        <p style="color:#ffb6d9;font-size:17px;">
        Write one memory, message or thank-you note
        that you would like Miss Shanza to remember. 🌷
        </p>
        """,
        unsafe_allow_html=True
    )

    goodbye_student = st.text_input(
        "👤 Your Name",
        placeholder="Enter your name...",
        key="goodbye_student"
    )

    goodbye_memory = st.text_area(
        "💗 Your Message",
        placeholder="Write your favourite memory or a goodbye message...",
        key="goodbye_memory"
    )

    if st.button(
        "🌷 SAVE MY MEMORY",
        key="save_goodbye"
    ):

        if (
            goodbye_student.strip()
            and goodbye_memory.strip()
        ):

            cursor.execute(
                """
                INSERT INTO memories
                (student, memory, created_at)
                VALUES (?, ?, ?)
                """,
                (
                    goodbye_student,
                    goodbye_memory,
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    )
                )
            )

            conn.commit()

            st.success(
                "💗 Your memory has been saved for Miss Shanza!"
            )

            st.snow()

        else:

            st.warning(
                "Please enter your name and message first."
            )

    # -----------------------------------------------------
    # MEMORY WALL
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown(
        "## 🌸 Memories From Class 5"
    )

    memories = cursor.execute(
        """
        SELECT student, memory, created_at
        FROM memories
        ORDER BY id DESC
        """
    ).fetchall()

    if not memories:

        st.info(
            "🌷 No memories have been added yet. "
            "Be the first student to leave one!"
        )

    else:

        for student_name, memory, created in memories:

            st.markdown(
                f"""
                <div class="card">

                    <h3>
                    💗 {student_name}
                    </h3>

                    <p style="
                        font-size:18px;
                        line-height:1.7;
                    ">
                    "{memory}"
                    </p>

                    <small style="color:#888;">
                    🌷 Class 5 Memory • {created}
                    </small>

                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # FINAL GOODBYE
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("""
    <div class="goodbye-hero">

        <h1>
        🌷 WE WILL MISS YOU 🌷
        </h1>

        <p>
        Thank you for being a part of our journey. 💗
        </p>

        <p style="
            font-size:24px;
            color:#ff69b4;
            font-weight:bold;
        ">
        Once our teacher, always our teacher. 🧮💗
        </p>

        <p style="font-size:30px;">
        🌸 💗 🧮 ✨ 🌷
        </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <p style="
        text-align:center;
        color:#ff8fc7;
        font-size:15px;
    ">

        🖤💗 Made with 💗 for Teacher's Day 💗🖤by ABIHA KASHIF
        <br>

        <b>
        by ABIHA KASHIF
        </b>

        <br>

        ✨ Learn • Create • Appreciate • Celebrate ✨

    </p>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CLOSE DATABASE
# =========================================================

conn.close()

