# Anti-Slop Rules

Free plain-writing rules for AI coding agents, so Claude Code, Cursor and Codex write READMEs, docs, commits and PR text in plain words.

They help the agent avoid chatbot openers like `Certainly!`, hype like `blazing fast`, the `It's not X, it's Y` move, em dashes, and emoji at the start of list items.

Also on Gumroad (same free pack): https://tidybyte.gumroad.com/l/anti-slop-rules-free

This version is instructions only. Nothing checks the result. The agent can still slip.

## Install

**By hand (about 2 minutes):**

1. Clone the repo:

```bash
git clone https://github.com/tidybytetools/anti-slop-rules.git
cd anti-slop-rules
python3 tests/test_free.py
```

2. Pick the file for your tool and copy it in:
   - Claude Code: paste `slop-rules.md` into `CLAUDE.md`.
   - Cursor: copy `templates/anti-slop.mdc` into `.cursor/rules/`.
   - Codex and other tools: paste `templates/AGENTS-anti-slop-block.md` into `AGENTS.md`.
   - Optional skill: copy `skills/de-slop-lite/` into `~/.claude/skills/` or `~/.cursor/skills/`.

3. Start a new session and ask: "de-slop my README" or "write the PR description in plain words".

**With the skills CLI (Claude Code, Cursor, Codex and more):**

```bash
npx skills add tidybytetools/anti-slop-rules
```

**Claude Code plugin marketplace:**

```text
/plugin marketplace add tidybytetools/anti-slop-rules
/plugin install anti-slop-rules@tidybytetools-anti-slop
```

**Gemini CLI:**

```bash
gemini extensions install https://github.com/tidybytetools/anti-slop-rules
```

## A real example

A typical AI-written intro:

```text
Welcome to QuickCSV! In today's fast-paced world, working with data shouldn't be hard. QuickCSV is a game-changer that will revolutionize the way you handle CSV files.
```

The same facts, rewritten with these rules:

```text
QuickCSV cleans messy CSV files from the command line: it fixes broken quotes, trims spaces and removes duplicate rows.
```

(This example is from the paid Anti-Slop Kit, which uses the same 12 rules.)

## What is inside

| File | What it is |
|---|---|
| `slop-rules.md` | 12 writing rules. Paste them into CLAUDE.md, AGENTS.md or any agent instructions. |
| `templates/anti-slop.mdc` | The same rules as a Cursor rule. Copy it to `.cursor/rules/`. |
| `templates/AGENTS-anti-slop-block.md` | A short block for AGENTS.md (Codex and other tools). |
| `GEMINI.md`, `gemini-extension.json` | The same rules as a Gemini CLI extension. |
| `skills/de-slop-lite/SKILL.md` | A skill that rewrites text in plain words and keeps your facts, commands and code the same. |
| `tests/test_free.py` | The tests. Run `python3 tests/test_free.py`. |

## Next step

If you want a checker that gives line numbers, a Claude Code hook, a git hook and a GitHub Action, see the [Anti-Slop Kit](https://tidybyte.gumroad.com/l/anti-slop-kit) ($9). It also has 4 skills, safe automatic word swaps, and 35 tests.

Website: https://tidybytetools.github.io/tools/anti-slop-rules-free/

MIT license. Made by Tidy Byte Tools.
