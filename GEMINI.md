## Writing rules (Anti-Slop Kit)

Follow these whenever you write or edit prose: READMEs, docs, comments, commit messages,
pull request text, changelogs and release notes.

1. Start with the answer or the fact. No warm-up line, no `Certainly!`, no `Great question`.
2. Use plain words. `use`, not `leverage` or `utilize`. `start`, not `embark`. `many`, not `a plethora of`.
3. No hype. Do not write `blazing fast`, `game-changer`, `seamless`, `revolutionary` or `world-class`.
   If something is fast, give the measured time. If you did not measure it, do not claim it.
4. No `It's not X, it's Y` and no `Not just X, but Y`. Say what the thing is, once.
5. Do not use em dashes. Use a period, comma, colon or parentheses.
6. No emoji at the start of headings or list items.
7. Keep sentences under 25 words when you can. Split anything over 40.
8. One exclamation mark per document at most. Usually zero.
9. No filler: `it is important to note that`, `in order to`, `at the end of the day`, `in conclusion`.
10. No placeholders left behind: `[Insert ...]`, `TODO: add`, `lorem ipsum`.
11. Be specific. Name the file, the command, the number, the version.
12. Keep the author's voice. Fix the problems above. Do not rewrite everything into one flat style.

If a slop_check.py script is available, run it on what you wrote and fix every HIGH finding
before you say you are done.
