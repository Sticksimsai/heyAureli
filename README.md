# Aureli — an angelic Twitter agent

A minimal, replicable Twitter bot that posts gentle, Ghibli-flavored micro‑notes about calm, kindness, and wonder. Built to pair with **heavendex.xyz**.

> ✨ You will need access to X (Twitter) API keys to post automatically.

## Features
- Rotates through short angelic prompts and seasonal lines
- Reply mode: gently answers mentions with encouraging, minimal messages
- Pluggable content sources (YAML lists, local files)
- GitHub Actions workflow for scheduled posting
- Optional OpenAI generation (commented out by default)

## Quick start

1. **Clone** this repo and create a virtualenv.
2. **Copy** `.env.example` to `.env` and fill in your credentials.
3. **Edit** `data/seed_posts.yaml` with your voice.
4. Run locally:
   ```bash
   pip install -r requirements.txt
   python src/bot.py --once
   ```
5. Or enable the GitHub Actions workflow to post on a schedule.

### Environment variables
See `.env.example` for all variables.

### Heavendex integration
`HEAVENDEX_URL` can point to a page or API on heavendex.xyz; the bot will include it in its bio and occasional tweets.

### Notes
- X/Twitter API access is required (paid tiers may apply). If you prefer a different network, the posting client is abstracted in `src/post_client.py`.
- Keep messages short, soft, and kind.
