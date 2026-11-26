---
name: de-slop-lite
description: Use when asked to clean up, humanize or de-slop a README, docs page, PR description, commit message or release notes. Rewrites in plain words, keeps facts and voice. Prompt-only version (no checker script).
---

# De-slop (lite)

Rewrite the text so it keeps the same facts and voice, without the patterns that make writing sound machine-made.

## Look for these

- Chatbot openers and closers: `Certainly!`, `Great question`, `I hope this helps`.
- Hype: `blazing fast`, `game-changer`, `seamless`, `revolutionary`, `cutting-edge`.
- Fancy words: `delve`, `leverage`, `utilize`, `embark`, `tapestry`, `plethora`.
- The `It's not X, it's Y` move and `Not just X, but Y`.
- Em dashes, emoji at the start of headings or list items, lots of exclamation marks.
- Filler: `it is important to note that`, `in order to`, `at the end of the day`.
- Placeholders: `[Insert ...]`, `TODO: add`, `lorem ipsum`.

## Rewrite rules

1. Start with the answer or the fact.
2. Replace hype with numbers you have. If there is no number, use a plain word or cut it.
3. Keep every fact, command, link, name and code block exactly as it was.
4. Do not add claims. Do not make the text longer.
5. Split sentences over 40 words.

## Reply

Show the new text, then 3 to 6 bullets on what you changed and anything you left alone on purpose.
