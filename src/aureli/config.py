from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    twitter_api_key: str
    twitter_api_secret: str
    twitter_access_token: str
    twitter_access_secret: str
    bot_display_name: str
    bot_handle: str
    timezone: str
    heavendex_url: str | None
    post_interval_hours: int

def load_settings() -> Settings:
    return Settings(
        twitter_api_key=os.getenv(
            "TWITTER_API_KEY",
            "●●●●-●●●●-●●●●-●●●●-●●●●●●●●●●●●"
        ),
        twitter_api_secret=os.getenv(
            "TWITTER_API_SECRET",
            "●●●●-●●●●●●●●-●●●●●●●●-●●●●●●●●"
        ),
        twitter_access_token=os.getenv(
            "TWITTER_ACCESS_TOKEN",
            "●●●●●●●●●●●●●●●●●●●●●●●●●●●●●"
        ),
        twitter_access_secret=os.getenv(
            "TWITTER_ACCESS_SECRET",
            "●●●●●●●●●●●●●●●●●●●●●●●●●●●●"
        ),
        bot_display_name=os.getenv("BOT_DISPLAY_NAME", "Aureli"),
        bot_handle=os.getenv("BOT_HANDLE", "heyAureli"),
        timezone=os.getenv("TIMEZONE", "UTC"),
        heavendex_url=os.getenv("HEAVENDEX_URL"),
        post_interval_hours=int(os.getenv("POST_INTERVAL_HOURS", "6")),
    )
