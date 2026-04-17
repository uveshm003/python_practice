# 🤖 All-in-One Telegram Bot

A fully self-contained Telegram bot built with Python — **no paid APIs, no external data sources**. Just your Bot Token from [@BotFather](https://t.me/BotFather) and you're good to go.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧮 **Calculator** | Evaluates any maths expression — supports `sqrt`, `sin`, `cos`, `log`, `^`, `%` and more |
| 📐 **Unit Converter** | 26 conversions across length, weight, temperature, speed, area, and volume |
| 📝 **To-Do List** | Add, view, mark tasks as done, or clear your list — stored per user |
| 😂 **Jokes** | 18 random two-liner jokes |
| 🌟 **Quotes** | 15 inspirational quotes from famous figures |
| 🔬 **Random Facts** | 22 interesting facts about science, history, and nature |
| 🧠 **Trivia Quiz** | 15 multiple-choice questions with correct answer explanations |
| 🔤 **Hangman** | Classic word guessing game — 20 words with hints and 6 lives |

---

## 📐 Unit Converter — Supported Conversions

| Category | Conversions |
|---|---|
| 📏 Length | km ↔ miles, m ↔ ft, cm ↔ inches |
| ⚖️ Weight | kg ↔ lb, g ↔ oz |
| 🌡️ Temperature | °C ↔ °F, °C ↔ K |
| 💨 Speed | km/h ↔ mph, m/s ↔ km/h |
| 🟫 Area | m² ↔ ft², hectares ↔ acres |
| 🫙 Volume | litres ↔ gallons, ml ↔ fl oz |

---

## 🤖 Bot Commands

| Command | Description |
|---|---|
| `/start` or `/hello` | Welcome message + main menu |
| `/menu` | Open the main menu anytime |
| `/help` | List all features |

---

## 🚀 Getting Started

### 1. Create a Bot on Telegram

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Copy your **Bot Token**

### 2. Install the Dependency

```bash
pip install pyTelegramBotAPI
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Set Your Bot Token

**Linux / macOS:**
```bash
export BOT_TOKEN="your_token_here"
```

**Windows (Command Prompt):**
```cmd
set BOT_TOKEN=your_token_here
```

**Windows (PowerShell):**
```powershell
$env:BOT_TOKEN="your_token_here"
```

### 4. Run the Bot

```bash
python bot.py
```

You should see `✅ Bot is running…` in the terminal. Open Telegram, find your bot, and send `/start`.

---

## 🌐 Deploying (Making It Live 24/7)

### Option 1 — Railway.app (Easiest, Free Tier)

1. Push `bot.py` and `requirements.txt` to a GitHub repository
2. Go to [railway.app](https://railway.app) and sign in with GitHub
3. Click **New Project → Deploy from GitHub repo**
4. Select your repository
5. Go to **Variables** and add: `BOT_TOKEN` = `your_token_here`
6. Set the **Start Command** to: `python bot.py`
7. Click **Deploy** — your bot will now run 24/7 ✅

### Option 2 — Render.com (Free Tier)

1. Push files to GitHub
2. Go to [render.com](https://render.com) → New → **Web Service**
3. Connect your repo
4. Set **Build Command**: `pip install -r requirements.txt`
5. Set **Start Command**: `python bot.py`
6. Add environment variable `BOT_TOKEN`
7. Deploy ✅

> ⚠️ Render's free tier spins down after inactivity. Use Railway for always-on hosting.

### Option 3 — Linux VPS (Most Reliable)

If you have a VPS (DigitalOcean, Hetzner, Linode, etc.):

```bash
# Install dependency
pip install pyTelegramBotAPI

# Run in background (persists after terminal closes)
nohup python bot.py > bot.log 2>&1 &

# Check logs
tail -f bot.log

# Stop the bot
kill $(pgrep -f bot.py)
```

For a more robust setup, use `systemd`:

```ini
# /etc/systemd/system/telebot.service
[Unit]
Description=Telegram Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
Restart=always
Environment=BOT_TOKEN=your_token_here

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable telebot
sudo systemctl start telebot
```

---

## 📁 Project Structure

```
├── bot.py            # Main bot file (all logic self-contained)
├── requirements.txt  # Single dependency: pyTelegramBotAPI
└── README.md         # This file
```

---

## ⚙️ How It Works

- All data (jokes, facts, quotes, trivia, hangman words) is **hardcoded** — no external API calls
- User state (to-do lists, active game sessions, pending inputs) is stored **in memory** per user ID
- State resets when the bot restarts — for persistence across restarts, a database like SQLite can be added later
- The calculator uses Python's `math` module in a sandboxed `eval` — safe for standard expressions

---

## 🛠️ Requirements

- Python 3.8+
- `pyTelegramBotAPI >= 4.18.0`
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)

---

## 📄 License

MIT — free to use, modify, and distribute.