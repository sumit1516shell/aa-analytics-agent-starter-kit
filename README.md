# Adobe Analytics Agent — Starter Kit

**Generate stakeholder-ready slide decks from Adobe Analytics — automatically, in your own company template.**

CJA customers have a "Generate Slides" button. Adobe Analytics doesn't — but with this kit, it does.
No coding required. If you can edit a text file, you can do this.

---

## What you need before starting

| Requirement | How to check |
|---|---|
| VS Code installed | Free download: code.visualstudio.com |
| GitHub Copilot in VS Code | Your company's enterprise Copilot licence |
| Adobe Analytics access | Your normal Workspace login works |
| 30 minutes | One-time setup, then it runs forever |

---

## Setup — 5 steps

### Step 1 — Download this kit
Click the green **Code** button at the top of this page → **Download ZIP** → unzip it to a folder on your Desktop.

### Step 2 — Open the folder in VS Code
VS Code → File → Open Folder → select the unzipped folder.
You'll see all the files in the left panel.

### Step 3 — Fill in your details (2 files to edit)

**`.vscode/mcp.json`** — replace the placeholders:
- `<COMPANY>` → your Adobe Analytics company ID (ask your admin, or it's in your Workspace URL)
- Leave everything else as-is to start — VS Code will ask you to log in with your normal Adobe ID the first time (this is the OAuth option — easiest)

**`memory.md`** — this is the agent's brain. Replace the examples with YOUR implementation:
- Your report suite name
- Your key segment ID (copy it from any Workspace URL)
- Your eVar meanings ("eVar5 = market", "eVar7 = platform" etc.)
- Any known data quirks your team has learned the hard way

💡 **Shortcut:** if your Solution Design Reference lives in Confluence, just tell the
agent: *"Read this page and write memory.md for me: [paste URL]"* — it does it in one turn.

### Step 4 — Add your company template (optional but recommended)
Drop your organisation's PowerPoint template (`.potx`) into the folder and add a
`design_rules.md` describing your brand colours and fonts. The agent will generate
decks in YOUR branding.

### Step 5 — Run it
In VS Code: open Copilot chat → switch to **Agent** mode → select the best
available model (e.g. Claude Opus) → type:

> **Read instructions.md and execute for last month**

That's it. The agent pulls live data, writes the analysis, and saves a finished
deck to your Desktop. You review it, personalise it, send it.

---

## Making it fully automatic (optional)

Want the deck to appear every Monday morning without opening VS Code?

1. **Token automation:** ask your Adobe admin for an *OAuth Server-to-Server*
   credential, put the client ID and secret into `get_token.py` — it fetches a fresh
   token automatically before every run (tokens expire; this solves that forever).
2. **Scheduling:** Mac → one line in `crontab`. Windows → Task Scheduler pointing
   at `run_monthly` — instructions are inside that file.

---

## The golden rule

**The agent does the mechanics. YOU bring the implementation knowledge.**

When it gets something wrong (it will, once), correct it and add the rule to
`memory.md`. It never makes that mistake again. Accuracy compounds with every run.

⚠️ **Never put real tokens, API keys, or client secrets in any file you share or
commit.** The placeholders in this kit exist for a reason.
