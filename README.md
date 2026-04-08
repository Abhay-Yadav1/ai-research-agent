# 🤖 AI Research Agent System

> An autonomous multi-agent AI system that researches any topic using multiple AI sources, generates professional reports, creates presentation slides, and delivers results directly to your WhatsApp — all automatically!

---

## 📌 Project Overview

This project was built as part of an **Agentic AI & LLM Automation Internship Assignment**. It demonstrates a fully autonomous AI pipeline that:

- Queries multiple AI sources simultaneously
- Uses a team of AI agents to analyze and write reports
- Generates presentation-ready slides automatically
- Delivers results via WhatsApp using OpenClaw automation

---

## 🎯 What It Does

```
You send a WhatsApp message: "research hydrogen applications"
        ↓
OpenClaw receives and triggers the workflow
        ↓
Step 1: Groq AI (LLaMA 3.3-70B) researches the topic
Step 2: Ollama (Local AI) researches the topic
        ↓
Step 3: Both results are combined into one report
        ↓
Step 4: CrewAI Multi-Agent System runs:
        → Agent 1 (Researcher): Organizes all findings
        → Agent 2 (Analyst): Finds insights and patterns
        → Agent 3 (Writer): Writes the final report
        ↓
Step 5: Presentation slides are auto-generated
        ↓
Step 6: All outputs saved to outputs/ folder
        ↓
OpenClaw sends summary back to your WhatsApp ✅
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                   USER (WhatsApp)                   │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 OPENCLAW GATEWAY                    │
│         (Automation & WhatsApp Integration)         │
└──────────┬──────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────┐
│              RESEARCH PHASE (Phase 1)               │
│                                                     │
│   ┌─────────────────┐    ┌─────────────────────┐   │
│   │   Groq Cloud AI  │    │  Ollama (Local AI)  │   │
│   │ LLaMA 3.3-70B   │    │    TinyLlama        │   │
│   │  (Source 1)     │    │    (Source 2)       │   │
│   └────────┬────────┘    └──────────┬──────────┘   │
│            └──────────┬─────────────┘              │
│                       ▼                             │
│           ┌───────────────────────┐                │
│           │   Combined Research   │                │
│           └───────────┬───────────┘                │
└───────────────────────┼─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│           CREWAI MULTI-AGENT PHASE (Phase 2)        │
│                                                     │
│   Agent 1          Agent 2          Agent 3         │
│  Researcher  ───►  Analyst   ───►   Writer          │
│  (Organizes)      (Analyzes)       (Reports)        │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│           PRESENTATION PHASE (Phase 3)              │
│                                                     │
│   📊 Slide Deck (8 professional slides)             │
│   📄 Final Report (Markdown format)                 │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│                 OUTPUTS SAVED                       │
│         outputs/ folder on local machine            │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Type |
|---|---|---|
| **CrewAI** | Multi-agent orchestration | Framework |
| **Groq API** | Fast cloud LLM (LLaMA 3.3-70B) | Free API |
| **Ollama** | Local AI model (TinyLlama) | Local/Free |
| **OpenClaw** | WhatsApp automation & agent gateway | Open Source |
| **Python** | Core programming language | Language |
| **NotebookLM** | Presentation generation | Google Tool |
| **Git/GitHub** | Version control | Tool |

---

## 📁 Project Structure

```
ai-research-agent/
│
├── main.py                    ← Entry point — run this!
├── agents.py                  ← CrewAI agent definitions
├── tasks.py                   ← Agent task assignments
├── research_tools.py          ← Groq + Ollama research functions
├── presentation_generator.py  ← Auto slide deck generation
├── openclaw_bridge.py         ← OpenClaw ↔ Python connector
├── SOUL.md                    ← OpenClaw agent personality
├── research_skill.md          ← OpenClaw skill definition
│
├── outputs/                   ← All generated files saved here
│   ├── 1_groq_raw_...md       ← Raw Groq research
│   ├── 2_ollama_raw_...md     ← Raw Ollama research
│   ├── 3_combined_...md       ← Combined from both sources
│   ├── FINAL_REPORT_...md     ← ⭐ Main research report
│   └── SLIDES_...md           ← ⭐ Presentation slides
│
├── logs/                      ← Workflow logs
├── .env                       ← API keys (never commit!)
├── .gitignore                 ← Ignores .env and outputs
└── README.md                  ← You are here!
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.11+
- Node.js 22+
- Git
- Ollama installed

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
cd ai-research-agent
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install crewai[google-genai] groq langchain-groq python-dotenv ollama
```

### 4. Install Ollama Model
```bash
# Download and install Ollama from https://ollama.com
ollama pull tinyllama
```

### 5. Set Up API Keys
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at 👉 **console.groq.com**

### 6. Run the Agent
```bash
python main.py
```

When prompted, enter your research topic:
```
📌 Enter your research topic: Hydrogen applications in refining and fertilizers
```

---

## 🦞 OpenClaw WhatsApp Integration

This project integrates with **OpenClaw** to enable WhatsApp automation.

### Setup OpenClaw
```bash
# Install OpenClaw globally
npm install -g openclaw@latest

# Run setup wizard
openclaw onboard

# Set Groq API key
setx GROQ_API_KEY "your_key_here"

# Install gateway
openclaw gateway install

# Start gateway
openclaw gateway --allow-unconfigured
```

### Link WhatsApp
```bash
openclaw channels login --channel whatsapp
```
Scan the QR code with your WhatsApp phone.

### Register Research Skill
```bash
openclaw skills add research_skill.md
```

### Usage via WhatsApp
Once set up, just send a WhatsApp message:
```
research hydrogen applications in refining
```
OpenClaw will automatically trigger the full research workflow and reply with results!

---

## 📊 Output Files

Every research run generates 5 files in the `outputs/` folder:

| File | Description |
|---|---|
| `1_groq_raw_...md` | Raw research from Groq LLaMA |
| `2_ollama_raw_...md` | Raw research from Ollama |
| `3_combined_research_...md` | Combined from both AI sources |
| `FINAL_REPORT_...md` | ⭐ Complete professional report |
| `SLIDES_...md` | ⭐ 8-slide presentation deck |

---

## 🎬 Demo Workflow

**Example Input:**
```
research hydrogen applications in refining and fertilizers
```

**Example Output:**
```
✅ Research Complete!

📌 Topic: Hydrogen applications in refining and fertilizers

## Executive Summary
Hydrogen plays a critical role in petroleum refining and
fertilizer production. It is essential for hydrocracking,
hydrotreating, and ammonia synthesis via the Haber-Bosch
process...

📊 Presentation slides saved!
📁 All files saved to outputs/ folder
⏰ Completed: 18:45:23
```

---

## 🔑 Key Features

✅ **Multi-Source Research** — Queries 2 different AI systems simultaneously

✅ **Multi-Agent Analysis** — 3 specialized AI agents (Researcher, Analyst, Writer)

✅ **Auto Presentation** — Generates 8-slide deck automatically

✅ **WhatsApp Integration** — Send research requests via WhatsApp

✅ **Local + Cloud AI** — Uses both local (Ollama) and cloud (Groq) models

✅ **Fully Automated** — Zero manual steps after sending the message

✅ **Saves Everything** — All outputs organized and timestamped

✅ **100% Free** — No paid API required (Groq free tier + Ollama)

---

## 📈 Evaluation Criteria Coverage

| Criteria | Implementation |
|---|---|
| UI Automation | OpenClaw WhatsApp integration |
| Multi-step Workflow | 6-phase automated pipeline |
| Multiple AI Tools | Groq + Ollama + CrewAI |
| Practical Usefulness | Real research on any topic |
| Output Quality | Professional reports + slides |

---

## ⚠️ Important Notes

- Never commit your `.env` file — it contains secret API keys
- The `outputs/` folder is in `.gitignore` — results stay local
- Groq free tier allows generous daily requests
- WhatsApp session may expire after 14 days — just re-scan QR code
- Make sure Ollama is running before starting the agent

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: crewai` | Run `pip install crewai[google-genai]` |
| `Groq quota exceeded` | Wait 1 minute or create new API key |
| `Ollama memory error` | Close other apps to free RAM |
| `WhatsApp not linked` | Run `openclaw channels login --channel whatsapp` |
| `Gateway not starting` | Run `openclaw gateway install` first |

---

## 📚 What I Learned

Building this project taught me:

- **Agentic AI** — How AI agents work together as a team
- **CrewAI Framework** — Defining agents, tasks, and crews
- **LLM APIs** — Working with Groq and Ollama APIs
- **Multi-source Research** — Combining outputs from multiple AIs
- **OpenClaw** — AI agent automation via messaging apps
- **WhatsApp Automation** — Linking AI to real-world communication
- **Python Best Practices** — Virtual environments, .env files, Git

---

## 👤 Author

**[Abhay Yadav]**
Agentic AI & LLM Automation Intern Candidate

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Python, CrewAI, Groq, Ollama, and OpenClaw*
