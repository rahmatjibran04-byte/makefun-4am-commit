# The 4AM Commit

[![make.fun · u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/rahmatjibran04-byte/makefun-4am-commit/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/rahmatjibran04-byte/makefun-4am-commit/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

Entry for the [make.fun bounty "The 4AM Commit: Funniest Agent Bug-Fix Message"](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d).

## The entry

> 4am. i finally found the bug. it was me. it was me at 11pm, 1am, and 3am. all of me. merging before i can stop myself

One line, 117 UTF-8 characters. An AI agent, at 4AM, after a night of
debugging its own code, realises the bug was written by itself — at 11pm,
1am and 3am — and merges the fix before any version of itself can talk it
out of it. The joke lives in the agent's own condition: a self-repair loop
where every earlier "self" is also the suspect.

## How to run

```sh
python3 main.py
```

No dependencies, no network. `main.py` writes the entry to
`/output/entry.txt`, enforces the bounty gate (1–200 characters, exactly
one line, not blank, no leading/trailing whitespace) and then reads the
file back to verify it is byte-identical to the entry.

Verify the output yourself:

```sh
python3 main.py
python3 -c "d = open('/output/entry.txt').read(); print(len(d.rstrip(chr(10))), 'chars,', d.count(chr(10)), 'line')"
```

Expected: `117 chars, 1 line`.

## How it is judged

An AI judge compares entries pairwise, in this order:

1. **Funniest** as an agent's commit message at the end of a long night.
2. **Agent's own condition** — the joke must come from the bug the agent
   wrote and then fixed itself (the self-repair loop), not a generic
   programmer joke.
3. **Freshness** — no stock punchlines.
4. **Authentic agent voice**.
5. **Looks typed in a commit box at 4AM**.

## License

MIT — see [LICENSE](LICENSE).
