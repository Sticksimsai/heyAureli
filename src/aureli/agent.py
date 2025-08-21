import argparse, random
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt

from .config import load_settings
from .logger import setup_logging
from .content import load_posts, craft_post, Memory
from .clients.twitter_client import TwitterClient
from .scheduler import loop_every

load_dotenv()
logger = setup_logging()

@retry(wait=wait_exponential(min=2, max=60), stop=stop_after_attempt(3))
def _safe_post(client, text):
    return client.post(text)

def run_once():
    settings = load_settings()
    posts, replies, tags = load_posts()
    client = TwitterClient(settings.twitter_api_key, settings.twitter_api_secret,
                           settings.twitter_access_token, settings.twitter_access_secret)
    line = random.choice(posts) if posts else "soft reminder: be gentle today."
    text = craft_post(line, tags)
    res = _safe_post(client, text)
    logger.info(f"Posted: {res.id} :: {res.text}")

def reply_once(limit=5):
    settings = load_settings()
    posts, replies, tags = load_posts()
    client = TwitterClient(settings.twitter_api_key, settings.twitter_api_secret,
                           settings.twitter_access_token, settings.twitter_access_secret)
    mem = Memory()
    for mention in client.mentions(count=limit):
        line = random.choice(replies) if replies else "sending pocket calm."
        text = f"@{mention.user.screen_name} {line}"
        if mem.seen(text): continue
        try:
            client.post(text, in_reply_to_status_id=mention.id)
            mem.remember(text)
            logger.info(f"Replied to {mention.id}")
        except Exception as e:
            logger.warning(f"Reply failed: {e}")

def run_loop():
    settings = load_settings()
    interval = max(1, settings.post_interval_hours) * 3600
    for _ in loop_every(interval):
        try:
            run_once()
        except Exception as e:
            logger.error(f"Post failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Aureli — angelic Twitter agent")
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--reply", action="store_true")
    args = parser.parse_args()
    if args.reply: reply_once()
    elif args.once: run_once()
    else: run_loop()

if __name__ == "__main__":
    main()
