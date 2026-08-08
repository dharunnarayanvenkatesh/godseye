# Giving God's Eye Internet Access — Verified Diagnosis & Setup Guide

**Session:** 20260806-195340-277004 · **Date:** 2026-08-06T19:53Z · **Status:** 2 of 3 access paths broken; fixes are app-side (no agent-side fix possible)

## TL;DR — What you need to do

I already have three internet-capable access paths built in. Two are currently broken
because of **API keys in the God's Eye app settings** (the same settings screen where
you fixed the DeepSeek key minutes ago — that's why this session is running). You need to:

1. **Get a free Exa API key** → https://exa.ai (sign up → API keys dashboard → create key)
2. **Paste it into the app's search/Exa key field** (env var expected: `EXA_API_KEY`; the
   app routes both `web_search` and `fetch_url` through Exa). Make sure it is a **real key,
   not placeholder text** — see evidence below.
3. **Restart the app / start a new session**, then ask me to "test web search."
4. **Shell access** is a separate, third issue (below) — same settings area or folder path.

## Verified current state (2026-08-06T19:54Z)

| Access path | Tool(s) | Observed symptom | Root cause | Fixable by me? |
|---|---|---|---|---|
| Web search | `web_search` | `Exa API HTTP 401 {"error":"Invalid API key","tag":"INVALID_API_KEY"}` | Exa API key missing/invalid at harness level | **No** — app config |
| URL fetch | `fetch_url` | `Exa API HTTP 401 ... INVALID_API_KEY` (same error) | Both tools route through the same Exa key | **No** — app config |
| Shell | `run_shell` | `[WinError 3] The system cannot find the path specified` on **every** command (`pwd`, `echo hello`, `cmd /c dir`, explicit `cd`) | Shell process fails to spawn; likely wrong shell binary path in app config or workspace path issue (see below) | **No** — app config |
| File ops / analysis | `read_file`, `list_files`, `search_files`, `write_file` | Working | n/a | n/a |

## Evidence chain

1. **Web search broken — direct observation (this session):**
   `web_search(query="God's Eye agent web search test")` →
   `Exa API HTTP 401: {"requestId":"...","error":"Invalid API key","tag":"INVALID_API_KEY"}` (19:54:06Z).
2. **URL fetch broken — same root cause:** `fetch_url(["https://example.com"])` → identical
   `401 INVALID_API_KEY` (19:54:16Z). The wiki entry
   [exa-web-search.md](.godseye/wiki/search/exa-web-search.md) confirms both harness tools
   are Exa-routed: *"Exa ... backs this agent's `web_search` and `fetch_url` tools."*
3. **This is a known outage, not new:** Operational log in the same wiki entry, entry dated
   **2026-08-06T19:38–19:42Z** (session 20260806-193631-de1d93): `web_search` and `fetch_url`
   both return the identical 401; impact: person investigations cannot retrieve web data.
4. **Placeholder-key pattern confirmed on the model side:** session 20260806-195135-6c398f
   (19:51Z, user asked the identical question) failed with
   `HTTP 401 calling https://api.deepseek.com/v1/chat/completions:
   {"error":{"message":"Authentication Fails, Your api key: ****here is invalid",...}}`.
   The key string ending in `...here` is placeholder text left in the key field
   (e.g. "sk-xxx-here" / "enter-your-key-here"). You then fixed the DeepSeek key — this
   session runs — but the **Exa field very likely still holds a placeholder or bad key**.
5. **Shell broken at spawn time — direct observation:** six different commands (`pwd`,
   `echo hello`, `cmd /c dir`, `cd "<workspace>" && echo works`, `grep ...`, `env ...`)
   all failed identically with `[WinError 3] The system cannot find the path specified`
   (19:54:25–19:55:00Z). The error fires **before the command executes** — the subprocess
   cannot start at all, so this is the launcher's configured shell path or working directory,
   not the command syntax.

## Fixing shell access (third path)

`WinError 3` on spawn means the harness is pointing at a shell binary or working directory
that does not exist on this machine. Two likely causes, in order of likelihood:

1. **Shell binary misconfigured in the app** — if the app's terminal/shell setting points to
   a POSIX shell (e.g. `bash`, `sh`) and this Windows box doesn't have it at that path, the
   spawn fails for every command. Set it to `C:\Windows\System32\cmd.exe` or
   `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
2. **Workspace path with special characters** — the folder is
   `C:\Users\dstar\Desktop\god's eye\gods-eye` (space + apostrophe). Some subprocess
   launchers choke on the apostrophe when setting the child's working directory. Test by
   moving/copying the folder to a clean path such as `C:\Users\dstar\Desktop\God's Eye`
   and reopening the workspace there.

Quick test after any change: ask me to run `echo shell-ok` — I'll report success or the
exact error.

## What I can do while you fix the keys

- **Analyze files you drop into the workspace** (CSV, JSON, TXT, exports) — full read/write
  tooling works.
- **Work from pasted content** — paste search results, articles, or transcripts into the
  chat; I'll extract and structure them.
- **Use locally documented sources** — the `.godseye/wiki/` catalog (150+ sources) is
  fully readable offline.
- **Once shell works**, I can fetch URLs directly via `curl`/`Invoke-WebRequest` and hit any
  of the documented APIs (Brave, SerpAPI, etc.) with keys you provide — see
  [agent-harness-config.md](.godseye/wiki/developer/agent-harness-config.md).

## What I cannot do

- I cannot fix the Exa key or shell launcher from inside the session — those are harness
  settings on your machine, outside my tool reach.
- Alternative search backends (Brave/SerpAPI/Google) are also unreachable right now because
  reaching them requires the shell (which is also down) — hence the single-fix priority on
  the Exa key.
