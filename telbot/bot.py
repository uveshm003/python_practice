import os
import math
import random
from telebot import TeleBot, types
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)

# ─────────────────────────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────────────────────────

JOKES = [
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("I told my wife she was drawing her eyebrows too high.", "She looked surprised."),
    ("Why don't eggs tell jokes?", "They'd crack each other up!"),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("Why did the bicycle fall over?", "Because it was two-tired!"),
    ("What do you call cheese that isn't yours?", "Nacho cheese!"),
    ("Why can't you give Elsa a balloon?", "Because she'll let it go!"),
    ("I'm reading a book about anti-gravity.", "It's impossible to put down!"),
    ("Did you hear about the mathematician who's afraid of negative numbers?", "He'll stop at nothing to avoid them!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("What's a computer's favourite snack?", "Microchips!"),
    ("Why did the developer go broke?", "Because he used up all his cache!"),
    ("How do you comfort a JavaScript bug?", "You console it!"),
    ("Why was the math book sad?", "It had too many problems."),
    ("What do you call a fish without eyes?", "A fsh!"),
    ("I used to hate facial hair...", "But then it grew on me."),
    ("Why did the coffee file a police report?", "It got mugged!"),
]

FACTS = [
    "Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts, blue blood, and nine brains (one central + one per arm).",
    "The shortest war in history lasted 38–45 minutes — between Britain and Zanzibar in 1896.",
    "Bananas are berries, but strawberries are not — botanically speaking.",
    "A day on Venus is longer than a year on Venus.",
    "The Eiffel Tower grows about 15 cm taller in summer due to thermal expansion.",
    "There are more possible chess games than atoms in the observable universe.",
    "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid.",
    "Sharks are older than trees — sharks have existed for ~450M years; trees for ~350M.",
    "A bolt of lightning is 5× hotter than the surface of the Sun.",
    "Wombat poop is cube-shaped — the only known animal to produce cubic droppings.",
    "The human body contains enough iron to make a 3 cm nail.",
    "Oxford University is older than the Aztec Empire.",
    "Sea otters hold hands while sleeping so they don't drift apart.",
    "The average person walks ~100,000 miles in their lifetime — roughly 4× around the Earth.",
    "A snail can sleep for up to 3 years.",
    "Crows can recognise and remember human faces.",
    "The dot over the letter 'i' is called a 'tittle'.",
    "Pineapples take about 2 years to grow.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Hot water freezes faster than cold water — this is called the Mpemba effect.",
]

QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Strive not to be a success, but rather to be of value.", "Albert Einstein"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("Whether you think you can or think you can't, you're right.", "Henry Ford"),
    ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("An unexamined life is not worth living.", "Socrates"),
    ("Spread love everywhere you go.", "Mother Teresa"),
    ("Always remember that you are absolutely unique — just like everyone else.", "Margaret Mead"),
    ("Do one thing every day that scares you.", "Eleanor Roosevelt"),
    ("Well behaved women seldom make history.", "Laurel Thatcher Ulrich"),
]

TRIVIA = [
    {"q": "What is the chemical symbol for Gold?",
     "options": ["Go", "Au", "Gd", "Ag"], "answer": 1,
     "explanation": "Gold's symbol 'Au' comes from the Latin word 'Aurum'."},
    {"q": "Which planet is known as the Red Planet?",
     "options": ["Venus", "Jupiter", "Mars", "Saturn"], "answer": 2,
     "explanation": "Mars appears red due to iron oxide (rust) on its surface."},
    {"q": "How many sides does a hexagon have?",
     "options": ["5", "6", "7", "8"], "answer": 1,
     "explanation": "'Hexa' is Greek for six."},
    {"q": "Who wrote 'Romeo and Juliet'?",
     "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Homer"], "answer": 2,
     "explanation": "Shakespeare wrote it around 1594–1596."},
    {"q": "What is the largest ocean on Earth?",
     "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 3,
     "explanation": "The Pacific Ocean covers about 165 million km²."},
    {"q": "Which element has the atomic number 1?",
     "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"], "answer": 1,
     "explanation": "Hydrogen is the lightest and most abundant element in the universe."},
    {"q": "In which year did World War II end?",
     "options": ["1943", "1944", "1945", "1946"], "answer": 2,
     "explanation": "WWII ended in 1945 — V-E Day (May 8) and V-J Day (Sep 2)."},
    {"q": "What is the capital of Japan?",
     "options": ["Kyoto", "Osaka", "Hiroshima", "Tokyo"], "answer": 3,
     "explanation": "Tokyo has been Japan's capital since 1869."},
    {"q": "How many bones are in the adult human body?",
     "options": ["196", "206", "216", "226"], "answer": 1,
     "explanation": "Adults have 206 bones; babies are born with around 270."},
    {"q": "Which language has the most native speakers?",
     "options": ["English", "Spanish", "Hindi", "Mandarin Chinese"], "answer": 3,
     "explanation": "Mandarin Chinese has over 900 million native speakers."},
    {"q": "What is the speed of light (approx.) in km/s?",
     "options": ["200,000", "300,000", "400,000", "500,000"], "answer": 1,
     "explanation": "Light travels at ~299,792 km/s in a vacuum."},
    {"q": "Which country invented pizza?",
     "options": ["France", "Greece", "USA", "Italy"], "answer": 3,
     "explanation": "Pizza originated in Naples, Italy in the 18th century."},
    {"q": "What gas do plants absorb from the atmosphere?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 2,
     "explanation": "Plants absorb CO₂ and release O₂ during photosynthesis."},
    {"q": "How many continents are there on Earth?",
     "options": ["5", "6", "7", "8"], "answer": 2,
     "explanation": "The 7 continents: Africa, Antarctica, Asia, Australia, Europe, North America, South America."},
    {"q": "What is the smallest prime number?",
     "options": ["0", "1", "2", "3"], "answer": 2,
     "explanation": "2 is the smallest and only even prime number."},
]

HANGMAN_WORDS = [
    ("PYTHON",      "A popular programming language 🐍"),
    ("TELEGRAM",    "A messaging platform known for bots 📱"),
    ("GALAXY",      "A system of millions of stars ✨"),
    ("JUNGLE",      "A dense tropical forest 🌿"),
    ("BRIDGE",      "A structure built to cross a gap 🌉"),
    ("CLOCK",       "A device that tells time ⏰"),
    ("OXYGEN",      "The gas we breathe 💨"),
    ("DIAMOND",     "The hardest natural material 💎"),
    ("CASTLE",      "A large medieval fortified building 🏰"),
    ("THUNDER",     "The loud sound following lightning ⚡"),
    ("COMPASS",     "A tool used for navigation 🧭"),
    ("MIRAGE",      "An optical illusion seen in deserts 🏜️"),
    ("PLANET",      "A large body orbiting a star 🪐"),
    ("FOSSIL",      "Preserved remains of ancient life 🦕"),
    ("WALRUS",      "A large Arctic mammal with tusks 🦭"),
    ("SPHINX",      "An ancient Egyptian monument 🗿"),
    ("QUARTZ",      "A common crystalline mineral 💠"),
    ("BLIZZARD",    "A severe snowstorm ❄️"),
    ("VOLCANO",     "A mountain that can erupt 🌋"),
    ("LANTERN",     "A portable light source 🏮"),
]

CONVERSIONS = {
    # length
    "km_to_mi":    ("km",        "miles",       lambda x: x * 0.621371),
    "mi_to_km":    ("miles",     "km",          lambda x: x * 1.60934),
    "m_to_ft":     ("m",         "ft",          lambda x: x * 3.28084),
    "ft_to_m":     ("ft",        "m",           lambda x: x * 0.3048),
    "cm_to_in":    ("cm",        "inches",      lambda x: x * 0.393701),
    "in_to_cm":    ("inches",    "cm",          lambda x: x * 2.54),
    # weight
    "kg_to_lb":    ("kg",        "lb",          lambda x: x * 2.20462),
    "lb_to_kg":    ("lb",        "kg",          lambda x: x * 0.453592),
    "g_to_oz":     ("g",         "oz",          lambda x: x * 0.035274),
    "oz_to_g":     ("oz",        "g",           lambda x: x * 28.3495),
    # temperature
    "c_to_f":      ("°C",        "°F",          lambda x: x * 9/5 + 32),
    "f_to_c":      ("°F",        "°C",          lambda x: (x - 32) * 5/9),
    "c_to_k":      ("°C",        "K",           lambda x: x + 273.15),
    "k_to_c":      ("K",         "°C",          lambda x: x - 273.15),
    # speed
    "kmh_to_mph":  ("km/h",      "mph",         lambda x: x * 0.621371),
    "mph_to_kmh":  ("mph",       "km/h",        lambda x: x * 1.60934),
    "ms_to_kmh":   ("m/s",       "km/h",        lambda x: x * 3.6),
    "kmh_to_ms":   ("km/h",      "m/s",         lambda x: x / 3.6),
    # area
    "sqm_to_sqft": ("m²",        "ft²",         lambda x: x * 10.7639),
    "sqft_to_sqm": ("ft²",       "m²",          lambda x: x * 0.0929),
    "ha_to_ac":    ("hectares",  "acres",       lambda x: x * 2.47105),
    "ac_to_ha":    ("acres",     "hectares",    lambda x: x * 0.404686),
    # volume
    "l_to_gal":    ("litres",    "gallons(US)", lambda x: x * 0.264172),
    "gal_to_l":    ("gallons(US)","litres",     lambda x: x * 3.78541),
    "ml_to_floz":  ("ml",        "fl oz",       lambda x: x * 0.033814),
    "floz_to_ml":  ("fl oz",     "ml",          lambda x: x * 29.5735),
}

# ─────────────────────────────────────────────────────────────────
#  STATE  (in-memory, resets on restart)
# ─────────────────────────────────────────────────────────────────
todo_lists:    dict[int, list[str]] = {}
trivia_state:  dict[int, dict]      = {}
hangman_state: dict[int, dict]      = {}
pending:       dict[int, str]       = {}   # what input we're waiting for

# ─────────────────────────────────────────────────────────────────
#  KEYBOARDS
# ─────────────────────────────────────────────────────────────────
def main_menu() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("🧮 Calculator",     callback_data="menu_calc"),
        types.InlineKeyboardButton("📐 Unit Converter",  callback_data="menu_conv"),
        types.InlineKeyboardButton("📝 To-Do List",      callback_data="menu_todo"),
        types.InlineKeyboardButton("😂 Joke",            callback_data="menu_joke"),
        types.InlineKeyboardButton("🌟 Quote",           callback_data="menu_quote"),
        types.InlineKeyboardButton("🔬 Random Fact",     callback_data="menu_fact"),
        types.InlineKeyboardButton("🧠 Trivia Quiz",     callback_data="menu_trivia"),
        types.InlineKeyboardButton("🔤 Hangman",         callback_data="menu_hangman"),
    )
    return kb

def back_btn(label="🔙 Main Menu", data="menu_back") -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(label, callback_data=data))
    return kb

def conv_cat_menu() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    cats = [
        ("📏 Length",       "cat_length"),
        ("⚖️ Weight",       "cat_weight"),
        ("🌡️ Temperature",  "cat_temp"),
        ("💨 Speed",        "cat_speed"),
        ("🟫 Area",         "cat_area"),
        ("🫙 Volume",       "cat_volume"),
    ]
    for label, data in cats:
        kb.add(types.InlineKeyboardButton(label, callback_data=data))
    kb.add(types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back"))
    return kb

def conv_sub_menu(keys: list) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=1)
    for k in keys:
        frm, to, _ = CONVERSIONS[k]
        kb.add(types.InlineKeyboardButton(f"{frm}  →  {to}", callback_data=f"conv_{k}"))
    kb.add(types.InlineKeyboardButton("🔙 Categories", callback_data="menu_conv"))
    return kb

def todo_action_menu() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("➕ Add task",       callback_data="todo_add"),
        types.InlineKeyboardButton("✅ Mark done",       callback_data="todo_done"),
        types.InlineKeyboardButton("📋 View list",       callback_data="todo_view"),
        types.InlineKeyboardButton("🗑️ Clear all",       callback_data="todo_clear"),
        types.InlineKeyboardButton("🔙 Main Menu",       callback_data="menu_back"),
    )
    return kb

# ─────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────
HANGMAN_ART = ["😄", "🙂", "😐", "😟", "😨", "😵"]

def hangman_text(state: dict) -> str:
    word    = state["word"]
    guessed = state["guessed"]
    wrong   = state["wrong"]
    shown   = " ".join(c if c in guessed else "\\_" for c in word)
    face    = HANGMAN_ART[min(len(wrong), 5)]
    wrong_s = "  ".join(wrong) if wrong else "none yet"
    lives   = 6 - len(wrong)
    return (
        f"🔤 *Hangman*  {face}  ❤️ {lives}/6\n\n"
        f"`{shown}`\n\n"
        f"💡 Hint: _{state['hint']}_\n"
        f"❌ Wrong: {wrong_s}\n\n"
        "_Send a single letter to guess!_"
    )

def safe_calc(expr: str) -> str:
    expr = expr.strip().replace("^", "**").replace("×", "*").replace("÷", "/")
    allowed_chars = set("0123456789+-*/(). %")
    # also allow math function names
    clean = expr
    for fn in dir(math):
        if not fn.startswith("_"):
            clean = clean.replace(fn, "")
    if not all(c in allowed_chars or c.isspace() for c in clean):
        return "⚠️ Invalid characters in expression."
    try:
        ns = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        ns["__builtins__"] = {}
        ns["abs"] = abs
        ns["round"] = round
        result = eval(expr, ns)  # noqa: S307
        if isinstance(result, float):
            result = round(result, 8)
            if result == int(result):
                result = int(result)
        return str(result)
    except ZeroDivisionError:
        return "⚠️ Division by zero!"
    except Exception:
        return "⚠️ Could not evaluate. Try: `25 * 4`, `sqrt(144)`, `2^10`"

# ─────────────────────────────────────────────────────────────────
#  COMMANDS
# ─────────────────────────────────────────────────────────────────
@bot.message_handler(commands=["start", "hello"])
def cmd_start(msg):
    name = msg.from_user.first_name or "there"
    bot.send_message(
        msg.chat.id,
        f"👋 Hey *{name}*! I'm your all-in-one assistant bot.\n\nPick a feature from the menu below:",
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )

@bot.message_handler(commands=["menu"])
def cmd_menu(msg):
    bot.send_message(msg.chat.id, "📋 Main Menu:", reply_markup=main_menu())

@bot.message_handler(commands=["help"])
def cmd_help(msg):
    bot.send_message(msg.chat.id,
        "*Features:*\n\n"
        "🧮 *Calculator* — any maths expression\n"
        "📐 *Unit Converter* — length, weight, temp, speed, area, volume\n"
        "📝 *To-Do List* — add, view, remove tasks\n"
        "😂 *Joke* — random two-liner\n"
        "🌟 *Quote* — inspirational quote\n"
        "🔬 *Fact* — random interesting fact\n"
        "🧠 *Trivia* — multiple-choice quiz\n"
        "🔤 *Hangman* — word guessing game\n\n"
        "Type /menu anytime to open the menu.",
        parse_mode="Markdown")

# ─────────────────────────────────────────────────────────────────
#  CALLBACK HANDLER
# ─────────────────────────────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: True)
def on_callback(call):
    uid = call.from_user.id
    cid = call.message.chat.id
    mid = call.message.message_id
    d   = call.data
    bot.answer_callback_query(call.id)

    # ── Main menu ──────────────────────────────────────────────
    if d == "menu_back":
        bot.edit_message_text("📋 Main Menu:", cid, mid, reply_markup=main_menu())

    # ── Joke ───────────────────────────────────────────────────
    elif d == "menu_joke":
        setup, punchline = random.choice(JOKES)
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("😂 Another", callback_data="menu_joke"),
               types.InlineKeyboardButton("🔙 Menu",    callback_data="menu_back"))
        bot.edit_message_text(f"😂 *{setup}*\n\n_{punchline}_",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)

    # ── Quote ──────────────────────────────────────────────────
    elif d == "menu_quote":
        quote, author = random.choice(QUOTES)
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("🌟 Another", callback_data="menu_quote"),
               types.InlineKeyboardButton("🔙 Menu",    callback_data="menu_back"))
        bot.edit_message_text(f"🌟 _{quote}_\n\n— *{author}*",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)

    # ── Fact ───────────────────────────────────────────────────
    elif d == "menu_fact":
        fact = random.choice(FACTS)
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("🔬 Another", callback_data="menu_fact"),
               types.InlineKeyboardButton("🔙 Menu",    callback_data="menu_back"))
        bot.edit_message_text(f"🔬 *Did you know?*\n\n{fact}",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)

    # ── Calculator ─────────────────────────────────────────────
    elif d == "menu_calc":
        pending[uid] = "calc"
        bot.edit_message_text(
            "🧮 *Calculator*\n\n"
            "Send me any maths expression:\n"
            "• `25 * 4 + 10`\n"
            "• `sqrt(144)`\n"
            "• `2^10`\n"
            "• `sin(pi / 2)`\n"
            "• `log(1000, 10)`",
            cid, mid, parse_mode="Markdown",
            reply_markup=back_btn())

    # ── Unit Converter categories ───────────────────────────────
    elif d == "menu_conv":
        bot.edit_message_text("📐 *Unit Converter* — choose a category:",
                              cid, mid, parse_mode="Markdown", reply_markup=conv_cat_menu())

    elif d == "cat_length":
        bot.edit_message_text("📏 *Length:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["km_to_mi","mi_to_km","m_to_ft","ft_to_m","cm_to_in","in_to_cm"]))
    elif d == "cat_weight":
        bot.edit_message_text("⚖️ *Weight:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["kg_to_lb","lb_to_kg","g_to_oz","oz_to_g"]))
    elif d == "cat_temp":
        bot.edit_message_text("🌡️ *Temperature:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["c_to_f","f_to_c","c_to_k","k_to_c"]))
    elif d == "cat_speed":
        bot.edit_message_text("💨 *Speed:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["kmh_to_mph","mph_to_kmh","ms_to_kmh","kmh_to_ms"]))
    elif d == "cat_area":
        bot.edit_message_text("🟫 *Area:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["sqm_to_sqft","sqft_to_sqm","ha_to_ac","ac_to_ha"]))
    elif d == "cat_volume":
        bot.edit_message_text("🫙 *Volume:*", cid, mid, parse_mode="Markdown",
                              reply_markup=conv_sub_menu(["l_to_gal","gal_to_l","ml_to_floz","floz_to_ml"]))

    elif d.startswith("conv_"):
        key = d[5:]
        frm, to, _ = CONVERSIONS[key]
        pending[uid] = key
        bot.edit_message_text(
            f"📐 Send the value in *{frm}* to convert to *{to}*\nExample: `100`",
            cid, mid, parse_mode="Markdown",
            reply_markup=back_btn("🔙 Categories", "menu_conv"))

    # ── To-Do ──────────────────────────────────────────────────
    elif d == "menu_todo":
        tasks = todo_lists.get(uid, [])
        body  = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) or "_No tasks yet._"
        bot.edit_message_text(f"📝 *Your To-Do List*\n\n{body}",
                              cid, mid, parse_mode="Markdown", reply_markup=todo_action_menu())

    elif d == "todo_view":
        tasks = todo_lists.get(uid, [])
        body  = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) or "_No tasks yet._"
        bot.edit_message_text(f"📋 *Tasks:*\n\n{body}",
                              cid, mid, parse_mode="Markdown", reply_markup=todo_action_menu())

    elif d == "todo_add":
        pending[uid] = "todo_add"
        bot.edit_message_text("➕ Type the task you want to add:",
                              cid, mid, reply_markup=back_btn("🔙 To-Do", "menu_todo"))

    elif d == "todo_done":
        tasks = todo_lists.get(uid, [])
        if not tasks:
            bot.edit_message_text("📭 No tasks to remove!", cid, mid, reply_markup=todo_action_menu())
        else:
            pending[uid] = "todo_done"
            body = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
            bot.edit_message_text(f"✅ *Send the number of the completed task:*\n\n{body}",
                                  cid, mid, parse_mode="Markdown",
                                  reply_markup=back_btn("🔙 To-Do", "menu_todo"))

    elif d == "todo_clear":
        todo_lists[uid] = []
        bot.edit_message_text("🗑️ All tasks cleared!", cid, mid, reply_markup=todo_action_menu())

    # ── Trivia ─────────────────────────────────────────────────
    elif d == "menu_trivia":
        q = random.choice(TRIVIA)
        trivia_state[uid] = q
        kb = types.InlineKeyboardMarkup(row_width=1)
        for i, opt in enumerate(q["options"]):
            kb.add(types.InlineKeyboardButton(opt, callback_data=f"trivia_{i}"))
        bot.edit_message_text(f"🧠 *Quiz time!*\n\n{q['q']}",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)

    elif d.startswith("trivia_"):
        chosen = int(d.split("_")[1])
        q = trivia_state.get(uid)
        if not q:
            return
        correct = chosen == q["answer"]
        result  = "✅ *Correct!*" if correct else f"❌ *Wrong!* The answer was *{q['options'][q['answer']]}*"
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("🧠 Next question", callback_data="menu_trivia"),
               types.InlineKeyboardButton("🔙 Menu",          callback_data="menu_back"))
        bot.edit_message_text(f"{result}\n\n💡 _{q['explanation']}_",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)

    # ── Hangman ────────────────────────────────────────────────
    elif d == "menu_hangman":
        word, hint = random.choice(HANGMAN_WORDS)
        hangman_state[uid] = {"word": word, "hint": hint, "guessed": set(), "wrong": []}
        bot.edit_message_text(hangman_text(hangman_state[uid]),
                              cid, mid, parse_mode="Markdown",
                              reply_markup=back_btn("🛑 Give up", "hangman_quit"))

    elif d == "hangman_quit":
        state = hangman_state.pop(uid, None)
        word  = state["word"] if state else "?"
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("🔤 Play again", callback_data="menu_hangman"),
               types.InlineKeyboardButton("🔙 Menu",       callback_data="menu_back"))
        bot.edit_message_text(f"😅 The word was *{word}*. Better luck next time!",
                              cid, mid, parse_mode="Markdown", reply_markup=kb)


# ─────────────────────────────────────────────────────────────────
#  TEXT MESSAGE HANDLER
# ─────────────────────────────────────────────────────────────────
@bot.message_handler(func=lambda m: True, content_types=["text"])
def on_text(msg):
    uid  = msg.from_user.id
    cid  = msg.chat.id
    text = msg.text.strip()

    # ── Calculator ─────────────────────────────────────────────
    if pending.get(uid) == "calc":
        pending.pop(uid)
        result = safe_calc(text)
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("🧮 Calculate again", callback_data="menu_calc"),
               types.InlineKeyboardButton("🔙 Menu",            callback_data="menu_back"))
        bot.send_message(cid, f"🧮 `{text}` = *{result}*",
                         parse_mode="Markdown", reply_markup=kb)
        return

    # ── Unit conversion ────────────────────────────────────────
    if pending.get(uid) in CONVERSIONS:
        key = pending.pop(uid)
        frm, to, fn = CONVERSIONS[key]
        try:
            val    = float(text.replace(",", "."))
            result = fn(val)
            result = round(result, 6)
            if result == int(result):
                result = int(result)
            reply = f"📐 *{val} {frm}* = *{result} {to}*"
        except ValueError:
            reply = "⚠️ Please send a valid number (e.g. `100`)."
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("📐 Convert more", callback_data="menu_conv"),
               types.InlineKeyboardButton("🔙 Menu",         callback_data="menu_back"))
        bot.send_message(cid, reply, parse_mode="Markdown", reply_markup=kb)
        return

    # ── To-Do: add ─────────────────────────────────────────────
    if pending.get(uid) == "todo_add":
        pending.pop(uid)
        todo_lists.setdefault(uid, []).append(text)
        tasks = todo_lists[uid]
        body  = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("➕ Add more", callback_data="todo_add"),
               types.InlineKeyboardButton("📝 To-Do",   callback_data="menu_todo"))
        bot.send_message(cid, f"✅ Task added!\n\n*Your list:*\n{body}",
                         parse_mode="Markdown", reply_markup=kb)
        return

    # ── To-Do: mark done ───────────────────────────────────────
    if pending.get(uid) == "todo_done":
        pending.pop(uid)
        tasks = todo_lists.get(uid, [])
        try:
            idx = int(text) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                body    = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) or "_No tasks left._"
                reply   = f"✅ Done: ~~{removed}~~\n\n*Remaining:*\n{body}"
            else:
                reply = f"⚠️ Please send a number between 1 and {len(tasks)}."
        except ValueError:
            reply = "⚠️ Please send a valid task number."
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("📝 To-Do menu", callback_data="menu_todo"))
        bot.send_message(cid, reply, parse_mode="Markdown", reply_markup=kb)
        return

    # ── Hangman guess ───────────────────────────────────────────
    if uid in hangman_state:
        state = hangman_state[uid]
        if len(text) == 1 and text.isalpha():
            letter = text.upper()
            guessed = state["guessed"]
            wrong   = state["wrong"]

            if letter in guessed or letter in wrong:
                bot.reply_to(msg, f"You already guessed *{letter}*! Try another letter.",
                             parse_mode="Markdown")
                return

            if letter in state["word"]:
                guessed.add(letter)
                if all(c in guessed for c in state["word"]):
                    hangman_state.pop(uid)
                    kb = types.InlineKeyboardMarkup(row_width=2)
                    kb.add(types.InlineKeyboardButton("🔤 Play again", callback_data="menu_hangman"),
                           types.InlineKeyboardButton("🔙 Menu",       callback_data="menu_back"))
                    bot.send_message(cid, f"🎉 *You got it!* The word was *{state['word']}*!",
                                     parse_mode="Markdown", reply_markup=kb)
                    return
                bot.send_message(cid, hangman_text(state), parse_mode="Markdown",
                                 reply_markup=back_btn("🛑 Give up", "hangman_quit"))
            else:
                wrong.append(letter)
                if len(wrong) >= 6:
                    hangman_state.pop(uid)
                    kb = types.InlineKeyboardMarkup(row_width=2)
                    kb.add(types.InlineKeyboardButton("🔤 Play again", callback_data="menu_hangman"),
                           types.InlineKeyboardButton("🔙 Menu",       callback_data="menu_back"))
                    bot.send_message(cid, f"😵 *Game over!* The word was *{state['word']}*.",
                                     parse_mode="Markdown", reply_markup=kb)
                    return
                bot.send_message(cid, hangman_text(state), parse_mode="Markdown",
                                 reply_markup=back_btn("🛑 Give up", "hangman_quit"))
        else:
            bot.reply_to(msg, "🔤 Send a *single letter* to guess!", parse_mode="Markdown")
        return

    # ── Fallback ───────────────────────────────────────────────
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📋 Open Menu", callback_data="menu_back"))
    bot.reply_to(msg, "Use /menu to open the feature menu 😊", reply_markup=kb)


# ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("✅ Bot is running…")
    bot.infinity_polling()