import re
import streamlit as st

st.set_page_config(
    page_title="Orbit Chat",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Orbit Chat: curated, offline demo assistant. No external AI API required.
GUIDES = [
    {
        "title": "Python programming",
        "category": "Programming",
        "keywords": ["python", "learn python", "python basics", "python programming", "loops", "functions", "list", "dictionary"],
        "answer": """## Python programming

Python is a readable, general-purpose language used for automation, websites, data analysis, scripting, and AI projects.

### Core building blocks
- **Variables:** `name = "Orbit"` stores a value.
- **Conditions:** `if score >= 50:` makes decisions.
- **Loops:** `for item in items:` repeats work.
- **Functions:** `def greet(name):` packages reusable logic.
- **Collections:** lists, dictionaries, tuples, and sets store data.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Orbit"))
```

### A good learning path
1. Practise variables, strings, numbers, and input/output.
2. Learn conditions, loops, functions, and collections.
3. Build a quiz, calculator, and expense tracker.
4. Learn files, exceptions, modules, and virtual environments.
5. Publish one polished project with a clear README."""
    },
    {
        "title": "Web development",
        "category": "Development",
        "keywords": ["html", "css", "javascript", "website", "web development", "frontend", "frontend development"],
        "answer": """## HTML, CSS and JavaScript

These three technologies work together to build most websites.

- **HTML** defines page structure and content.
- **CSS** styles layout, spacing, colours, typography, and responsive behaviour.
- **JavaScript** adds interactions such as click handling, form validation, and dynamic updates.

```html
<h1>Hello, world!</h1>
<button onclick="alert('Hello!')">Click me</button>
```

Save this snippet as `index.html` and open it in a browser. As projects grow, keep the technologies in separate files and use browser developer tools to debug."""
    },
    {
        "title": "Artificial intelligence",
        "category": "Technology",
        "keywords": ["ai", "artificial intelligence", "machine learning", "generative ai", "llm", "large language model", "chatbot"],
        "answer": """## Artificial intelligence, simply explained

Artificial intelligence is a broad field of systems that recognise patterns, understand language, plan, or make predictions.

- **Machine learning:** learns patterns from examples.
- **Deep learning:** uses multi-layer neural networks.
- **Generative AI:** creates text, images, audio, code, and more.
- **Large language models:** generate language using patterns learned during training.

AI can help with brainstorming, summarising, writing, and coding, but it can also make confident mistakes. Verify important claims and avoid sharing sensitive information with tools unless you understand their privacy terms."""
    },
    {
        "title": "Deploy a Streamlit app",
        "category": "Deployment",
        "keywords": ["deploy", "deployment", "streamlit cloud", "public link", "publish app", "host app", "online app"],
        "answer": """## Deploy a Streamlit app online

### Prepare your repository
Your GitHub repository should contain `app.py`, `requirements.txt`, and preferably a `README.md`.

### Publish it
1. Upload the files to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect GitHub and select your repository.
4. Choose the `main` branch and main file path `app.py`.
5. Click **Deploy** and wait for the build.
6. Share the generated `*.streamlit.app` link.

### If the build fails
Check that `requirements.txt` is in the repository root, add packages your code imports, and inspect the deployment logs. Never upload passwords or API keys to a public repository."""
    },
    {
        "title": "College project ideas",
        "category": "Projects",
        "keywords": ["project idea", "college project", "final year", "mini project", "portfolio project", "project ideas", "btech project"],
        "answer": """## College project ideas worth demonstrating

### Beginner
- Expense tracker with monthly summaries and CSV export.
- Quiz application with topic filters and answer explanations.
- Study planner with tasks, deadlines, and progress statistics.

### Intermediate
- Campus Lost & Found portal with search and a verification flow.
- Placement tracker for applications, DSA practice, and mock interviews.
- Inventory dashboard with low-stock notifications.

### More advanced
- Accessibility checker for colour contrast.
- Document search for revision notes.
- Energy dashboard to visualise time-series data.

**Make it stand out:** define a clear problem, deliver a reliable live demo, include sample data, document limitations, and explain what you personally built."""
    },
    {
        "title": "Interview preparation",
        "category": "Career",
        "keywords": ["interview", "placement", "hr round", "job interview", "resume", "tell me about yourself"],
        "answer": """## A focused interview preparation plan

- Research the company, role, product, and required skills.
- Prepare a 60–90 second introduction.
- Prepare project stories using **STAR**: Situation, Task, Action, Result.
- Practise “Tell me about yourself”, “Why this role?”, and “What did you build?”
- For technical rounds, state assumptions, explain your approach, test edge cases, and discuss trade-offs.
- Prepare two thoughtful questions for the interviewer."""
    },
    {
        "title": "Study techniques",
        "category": "Learning",
        "keywords": ["study", "exam", "concentration", "learn faster", "revision", "focus", "studying"],
        "answer": """## Study more effectively

- **Active recall:** close your notes and explain the concept from memory.
- **Spaced repetition:** revisit material over increasing intervals.
- **Practice questions:** use mistakes to discover weak areas.
- **Focused sessions:** try 25 minutes of work followed by a 5-minute break.
- **Protect sleep:** fatigue makes learning harder.

### A 60-minute session
5 min plan → 20 min learn → 20 min practise → 10 min review mistakes → 5 min plan next steps.

Measure progress by what you can recall and solve, not only by hours spent."""
    },
    {
        "title": "Cybersecurity basics",
        "category": "Technology",
        "keywords": ["cybersecurity", "security", "phishing", "password", "online safety", "hacking"],
        "answer": """## Cybersecurity basics

- Use unique passwords and a password manager.
- Enable multi-factor authentication.
- Keep your operating system, browser, and apps updated.
- Verify unexpected links and urgent payment requests through a separate channel.
- Back up important files and test recovery.
- Never share one-time passwords or authentication codes.

For organisations, security also includes access controls, monitoring, and incident response."""
    },
    {
        "title": "Git and GitHub",
        "category": "Development",
        "keywords": ["git", "github", "repository", "commit", "push code", "version control"],
        "answer": """## Git and GitHub

**Git** tracks changes to files on your computer. **GitHub** hosts repositories online so you can share code and collaborate.

```bash
git init
git add .
git commit -m "Initial commit"
```

Create a repository on GitHub, then follow its instructions to connect and push your local folder. Use `.gitignore`, write a useful README, and never commit passwords or API keys."""
    },
    {
        "title": "Debug a Python error",
        "category": "Development",
        "keywords": ["error", "bug", "debug", "traceback", "not working", "exception", "module not found"],
        "answer": """## Debug a Python error

1. Read the last line of the traceback first.
2. Find the file name and line number.
3. Check indentation, spelling, variable names, and data types.
4. Reduce the issue to the smallest example that still fails.
5. Fix one thing at a time and rerun.

Common errors:
- `SyntaxError` — invalid Python syntax.
- `NameError` — undefined or misspelled name.
- `TypeError` — an operation received an unsuitable type.
- `ModuleNotFoundError` — a package is missing from the active environment.
- `FileNotFoundError` — the path or working directory is wrong."""
    },
    {
        "title": "Beat procrastination",
        "category": "Productivity",
        "keywords": ["procrastination", "productivity", "time management", "motivation", "get started"],
        "answer": """## Make starting easier

1. Break a big task into a next step that takes under ten minutes.
2. Commit to five minutes of work instead of promising to finish everything.
3. Prepare files and tools before starting.
4. Pick one priority before opening messages.
5. Track completed actions, not just time spent.
6. If you're stuck, ask whether the task is unclear, too large, boring, or stressful.

**Try this now:** write one tiny action, set a 10-minute timer, and begin."""
    },
]

WELCOME = """Hey, welcome to **Orbit Chat** ✦

A little more clarity, a little less clutter. Ask a question, explore a topic, or pick a prompt below to get started.

*Demo mode: replies come from a built-in knowledge library. No API key is required.*"""

SUGGESTIONS = [
    ("01", "Learn something", "Explain Python from the basics", "Programming · Concepts"),
    ("02", "Build a project", "Give me college project ideas", "Ideas · Tech stack"),
    ("03", "Launch online", "How do I deploy a Streamlit app?", "GitHub · Deployment"),
    ("04", "Prepare for a job", "Help me prepare for interviews", "Career · Practice"),
]

def normalise(text):
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).strip()

def get_reply(prompt):
    q = normalise(prompt)
    if not q:
        return "Type a question below and I'll try to help."
    if q in {"hi", "hello", "hey", "hey there", "namaste"}:
        return "Hey! 👋 What are you working on today? Ask about Python, web development, AI, projects, interview prep, studying, cybersecurity, GitHub, or deployment."
    if "thank" in q:
        return "You're welcome! ✨ What would you like to explore next?"
    if any(term in q for term in ["who are you", "what are you", "your name"]):
        return "I'm Orbit Chat, a Streamlit chatbot demo using a built-in knowledge library. I can explain the listed topics, but this no-API edition isn't a live generative AI model."

    q_words = set(q.split())
    best_guide, best_score = None, 0.0
    for guide in GUIDES:
        score = 0.0
        for phrase in [guide["title"]] + guide["keywords"]:
            p = normalise(phrase)
            useful = set(p.split()) - {"how", "what", "the", "for", "and", "from", "with", "basics", "help", "me", "please"}
            if p and p in q:
                score += 8 + 2 * len(p.split())
            score += 1.15 * len(useful & q_words)
        if score > best_score:
            best_guide, best_score = guide, score

    if best_guide and best_score >= 2.3:
        return best_guide["answer"]
    return (
        "I don't have a prepared guide for that exact question yet.\n\n"
        "Try **Python**, **web development**, **AI**, **cybersecurity**, **college projects**, "
        "**interview prep**, **study techniques**, **GitHub**, **debugging**, or **Streamlit deployment**.\n\n"
        "This demo runs without an AI API, so its answers are limited to the built-in knowledge library."
    )

def export_chat(messages):
    output = []
    for message in messages:
        label = "YOU" if message["role"] == "user" else "ORBIT CHAT"
        output.append(f"{label}\n{message['content']}")
    return "\n\n---\n\n".join(output)

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
if "chats" not in st.session_state:
    st.session_state.chats = [{"title": "New conversation", "messages": [{"role": "assistant", "content": WELCOME}]}]
if "active_chat" not in st.session_state:
    st.session_state.active_chat = 0
st.session_state.active_chat = min(st.session_state.active_chat, len(st.session_state.chats) - 1)
active = st.session_state.chats[st.session_state.active_chat]
messages = active["messages"]

dark = st.session_state.theme == "Dark"
if dark:
    BG, PANEL, PANEL2, FG, MUTED, BORDER = "#100d18", "#191522", "#231d30", "#f7f1ff", "#aaa0b8", "#352c45"
    ACCENT, ACCENT2, ACCENT3, INPUT = "#d5ff62", "#ff6eaa", "#ad8cff", "#191522"
else:
    BG, PANEL, PANEL2, FG, MUTED, BORDER = "#fbf6f1", "#fffdfb", "#f1e8ed", "#29212d", "#827381", "#e7dbe4"
    ACCENT, ACCENT2, ACCENT3, INPUT = "#9ccf35", "#e75391", "#8760d8", "#fffdfb"

with st.sidebar:
    st.markdown(
        "<div class='brand'><div class='brand-icon'>✦</div><div><div class='brand-title'>orbit<span>chat</span></div><div class='brand-sub'>YOUR LITTLE CORNER OF CLARITY</div></div></div>",
        unsafe_allow_html=True,
    )
    st.radio("Theme", ["Dark", "Light"], horizontal=True, key="theme", label_visibility="collapsed")
    if st.button("＋  New chat", type="primary", use_container_width=True):
        st.session_state.chats.append({"title": "New conversation", "messages": [{"role": "assistant", "content": WELCOME}]})
        st.session_state.active_chat = len(st.session_state.chats) - 1
        st.rerun()

    st.markdown("<div class='side-title'>RECENT CHATS</div>", unsafe_allow_html=True)
    for i, chat in enumerate(st.session_state.chats):
        name = chat["title"][:25]
        if st.button(("✦  " if i == st.session_state.active_chat else "·  ") + name, key=f"history_{i}", use_container_width=True):
            st.session_state.active_chat = i
            st.rerun()

    st.markdown("<div class='side-title'>EXPLORE TOPICS</div>", unsafe_allow_html=True)
    categories = ["All topics"] + sorted({guide["category"] for guide in GUIDES})
    category = st.selectbox("Filter topic guides", categories, label_visibility="collapsed")
    query = st.text_input("Search guides", placeholder="⌕  Search topics…", label_visibility="collapsed")
    filtered = [
        guide for guide in GUIDES
        if (category == "All topics" or guide["category"] == category)
        and (not query or query.lower() in guide["title"].lower() or query.lower() in guide["category"].lower()
             or any(query.lower() in term.lower() for term in guide["keywords"]))
    ]
    for i, guide in enumerate(filtered):
        with st.expander(guide["title"]):
            st.caption(guide["category"])
            st.markdown(guide["answer"][:360] + ("…" if len(guide["answer"]) > 360 else ""))
            if st.button("Open in chat ↗", key=f"guide_{category}_{i}"):
                active["messages"].append({"role": "user", "content": f"Tell me about {guide['title']}"})
                active["messages"].append({"role": "assistant", "content": guide["answer"]})
                st.rerun()

    st.markdown("<div class='side-title'>CHAT TOOLS</div>", unsafe_allow_html=True)
    if st.button("Clear current chat", use_container_width=True):
        active["messages"] = [{"role": "assistant", "content": WELCOME}]
        active["title"] = "New conversation"
        st.rerun()
    st.download_button("↓  Export conversation", export_chat(messages), file_name="orbit-chat.txt", mime="text/plain", use_container_width=True)
    st.markdown("<div class='sidebar-footer'>MADE TO EXPLORE.<br>NO API KEY NEEDED.</div>", unsafe_allow_html=True)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {{ font-family:'Manrope',sans-serif; }}
.stApp {{
    color:{FG}; background:
      radial-gradient(ellipse at 18% 0%, {'#39204a55' if dark else '#f6c6db66'} 0%, transparent 36%),
      radial-gradient(ellipse at 90% 32%, {'#45305433' if dark else '#d6e9ae55'} 0%, transparent 32%),
      {BG};
    background-attachment: fixed;
}}
[data-testid="stSidebar"] {{ background:{PANEL}; border-right:1px solid {BORDER}; }}
[data-testid="stSidebar"] * {{ color:{FG}; }}
.block-container, [data-testid="stMainBlockContainer"] {{ max-width:980px!important; width:calc(100% - 48px)!important; margin-left:auto!important; margin-right:auto!important; padding-top:1.05rem!important; padding-bottom:2rem!important; }}
.brand {{ display:flex;align-items:center;gap:11px;padding:8px 2px 20px; }}
.brand-icon {{ width:42px;height:42px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,{ACCENT2},{ACCENT3});color:white;font-size:26px;font-weight:800;box-shadow:0 6px 22px {ACCENT2}3b; }}
.brand-title {{ font-size:26px;font-weight:800;letter-spacing:-1.4px;line-height:1.05;color:{FG}; }}
.brand-title span {{ color:{ACCENT2}; }}
.brand-sub {{ font-family:'DM Mono',monospace;font-size:7px;letter-spacing:1px;color:{MUTED};margin-top:5px; }}
.side-title {{ font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1.7px;color:{MUTED};margin:22px 0 10px; }}
.sidebar-footer {{border-top:1px solid {BORDER};margin-top:24px;padding-top:14px;color:{MUTED};font-family:'DM Mono',monospace;font-size:8px;letter-spacing:1px;line-height:1.8;}}
.topbar {{ display:flex;justify-content:space-between;align-items:center;gap:12px;border-bottom:1px solid {BORDER};padding:4px 0 13px;margin-bottom:18px; }}
.topbar-brand {{font-family:'DM Mono',monospace;color:{ACCENT2};font-size:9px;letter-spacing:1.5px;}}
.topbar-status {{font-family:'DM Mono',monospace;color:{MUTED};font-size:8px;letter-spacing:1px;}}
.welcome {{
  position:relative;overflow:hidden;border:1px solid {BORDER};border-radius:22px;
  padding:27px 29px 23px;margin-bottom:16px;
  background:linear-gradient(125deg,{PANEL} 0%,{PANEL2} 100%);
  animation:riseIn .6s ease both;
}}
.welcome:before {{
  content:'';position:absolute;width:190px;height:190px;right:-52px;top:-75px;border-radius:50%;
  background:radial-gradient(circle,{ACCENT2}40,transparent 68%);filter:blur(9px);animation:floatGlow 7s ease-in-out infinite;
}}
.welcome:after {{
  content:'✦';position:absolute;right:37px;top:22px;color:{ACCENT};opacity:.65;font-size:76px;
  animation:orbitSpin 24s linear infinite;
}}
.welcome-kicker {{font-family:'DM Mono',monospace;color:{ACCENT2};font-size:9px;letter-spacing:1.8px;text-transform:uppercase;position:relative;z-index:1;}}
.welcome h1 {{font-size:clamp(32px,3.6vw,47px);line-height:1.06;letter-spacing:-2px;font-weight:800;margin:12px 0;color:{FG};position:relative;z-index:1;}}
.welcome h1 em {{font-style:normal;background:linear-gradient(90deg,{ACCENT2},{ACCENT3});-webkit-background-clip:text;background-clip:text;color:transparent;}}
.welcome p {{max-width:630px;color:{MUTED};font-size:13px;line-height:1.75;margin:0;position:relative;z-index:1;}}
.welcome-tags {{display:flex;gap:7px;flex-wrap:wrap;margin-top:15px;position:relative;z-index:1;}}
.welcome-tag {{border:1px solid {BORDER};background:{PANEL};padding:5px 8px;border-radius:7px;color:{MUTED};font-family:'DM Mono',monospace;font-size:8px;letter-spacing:.5px;}}
.section-label {{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1.6px;color:{MUTED};margin:16px 0 9px;}}
.suggestion-card {{border:1px solid {BORDER};border-radius:13px;background:{PANEL};padding:13px 14px;min-height:79px;margin-bottom:6px;transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease;}}
.suggestion-card:hover {{transform:translateY(-3px);border-color:{ACCENT2};box-shadow:0 9px 23px {ACCENT2}17;}}
.sugg-number {{font-family:'DM Mono',monospace;font-size:8px;color:{ACCENT2};letter-spacing:1px;}}
.sugg-title {{font-size:13px;font-weight:800;color:{FG};margin:5px 0 2px;}}
.sugg-desc {{font-size:10px;color:{MUTED};}}
div[data-testid="stChatMessage"] {{
    border:1px solid {BORDER};border-radius:15px;background:{PANEL};
    padding:13px 16px;margin:0 0 10px;animation:riseIn .35s ease both;
    width:100%;box-sizing:border-box;
}}
div[data-testid="stChatMessage"] p,div[data-testid="stChatMessage"] li {{color:{FG};font-size:14px;line-height:1.75;}}
div[data-testid="stChatMessage"] h1,div[data-testid="stChatMessage"] h2,div[data-testid="stChatMessage"] h3 {{color:{FG};letter-spacing:-.5px;}}
div[data-testid="stChatMessage"] pre {{border:1px solid {BORDER};border-radius:11px;}}
/* Make the bottom composer comfortably medium sized, never edge-to-edge giant */
[data-testid="stBottom"] {{background:transparent!important;}}
/* Current Streamlit bottom block selector: constrain composer, not the whole screen */
[data-testid="stBottomBlockContainer"] {{
    max-width:820px!important;width:calc(100% - 48px)!important;
    margin-left:auto!important;margin-right:auto!important;
    padding-left:0!important;padding-right:0!important;padding-bottom:8px!important;
}}
[data-testid="stBottom"] [data-testid="stChatInput"],
[data-testid="stChatInput"] {{
    width:100%!important;max-width:820px!important;height:58px!important;min-height:58px!important;
    box-sizing:border-box!important;padding:6px 12px!important;
    background:{INPUT}!important;border:1px solid {BORDER}!important;
    border-radius:15px!important;box-shadow:0 8px 25px #00000012!important;
    margin-left:auto!important;margin-right:auto!important;
}}
[data-testid="stChatInput"] textarea {{
    color:{FG}!important;height:38px!important;min-height:38px!important;max-height:90px!important;
    font-size:14px!important;line-height:1.45!important;padding:7px 0!important;
}}
.stButton>button {{
    min-height:39px;border-radius:10px;border:1px solid {BORDER};
    background:{PANEL};color:{FG};font-weight:650;transition:all .18s ease;
}}
.stButton>button:hover {{border-color:{ACCENT2};color:{ACCENT2};transform:translateY(-1px);}}
button[kind="primary"] {{background:linear-gradient(100deg,{ACCENT2},{ACCENT3})!important;border:0!important;color:white!important;}}
button[kind="primary"]:hover {{filter:brightness(1.07);color:white!important;}}
[data-testid="stSelectbox"] div[data-baseweb="select"]>div,[data-testid="stTextInput"] input {{
    background:{INPUT};border-color:{BORDER};border-radius:9px;color:{FG};
}}
a {{color:{ACCENT2}!important;}}
hr {{border-color:{BORDER};}}
footer {{visibility:hidden;}}
@keyframes riseIn {{from {{opacity:0;transform:translateY(9px)}} to {{opacity:1;transform:translateY(0)}}}}
@keyframes floatGlow {{0%,100% {{transform:translate(0,0) scale(1)}} 50% {{transform:translate(-14px,12px) scale(1.12)}}}}
@keyframes orbitSpin {{from {{transform:rotate(0deg)}} to {{transform:rotate(360deg)}}}}
@media(max-width:760px) {{
    .block-container, [data-testid="stMainBlockContainer"] {{width:calc(100% - 20px)!important;padding-top:.7rem!important;}}
    [data-testid="stBottomBlockContainer"] {{width:calc(100% - 18px)!important;}}
    [data-testid="stChatInput"] {{height:54px!important;min-height:54px!important;padding:5px 9px!important;}}
    [data-testid="stChatInput"] textarea {{height:36px!important;min-height:36px!important;}}
    .block-container {{padding-top:.7rem;}}
    .welcome {{padding:22px 18px 20px;}}
    .welcome h1 {{font-size:34px;letter-spacing:-1.4px;}}
    .welcome:after {{right:18px;top:17px;font-size:52px;}}
    [data-testid="stBottom"]>div {{width:calc(100% - 18px)!important;}}
    div[data-testid="stChatMessage"] {{padding:12px 13px;}}
}}
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{animation-duration:.01ms!important;transition-duration:.01ms!important;}}
}}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='topbar'><div class='topbar-brand'>✦ &nbsp; ORBIT CHAT / STUDIO</div><div class='topbar-status'>CONVERSATION MODE&nbsp; · &nbsp;PRIVATE SESSION</div></div>",
    unsafe_allow_html=True,
)

if len(messages) == 1:
    st.markdown(
        """<div class='welcome'>
        <div class='welcome-kicker'>A BETTER PLACE TO BE CURIOUS</div>
        <h1>What's on your<br><em>mind today?</em></h1>
        <p>Ask a question, explore a new skill, or find a starting point. Pick one of the prompts or type your message below.</p>
        <div class='welcome-tags'><span class='welcome-tag'>LIGHT + DARK</span><span class='welcome-tag'>ANIMATED UI</span><span class='welcome-tag'>NO API KEY</span></div>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='section-label'>A FEW GOOD PLACES TO START</div>", unsafe_allow_html=True)
    cards = st.columns(2)
    for i, (num, title, prompt, desc) in enumerate(SUGGESTIONS):
        with cards[i % 2]:
            st.markdown(
                f"<div class='suggestion-card'><div class='sugg-number'>PROMPT / {num}</div><div class='sugg-title'>{title}</div><div class='sugg-desc'>{desc}</div></div>",
                unsafe_allow_html=True,
            )
            if st.button("Try this ↗", key=f"suggest_{i}", use_container_width=True):
                active["messages"].append({"role": "user", "content": prompt})
                active["messages"].append({"role": "assistant", "content": get_reply(prompt)})
                if active["title"] == "New conversation":
                    active["title"] = title
                st.rerun()

for msg in active["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Message Orbit Chat…")
if prompt:
    active["messages"].append({"role": "user", "content": prompt})
    if active["title"] == "New conversation":
        active["title"] = prompt.strip()[:27] or "New conversation"
    active["messages"].append({"role": "assistant", "content": get_reply(prompt)})
    st.rerun()

st.markdown(
    f"<div style='max-width:850px;margin:25px auto 0;border-top:1px solid {BORDER};padding-top:11px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;font-family:DM Mono,monospace;font-size:8px;letter-spacing:.7px;color:{MUTED}'><span>ORBIT CHAT / STREAMLIT PROJECT</span><span>CURATED KNOWLEDGE MODE</span></div>",
    unsafe_allow_html=True,
)
