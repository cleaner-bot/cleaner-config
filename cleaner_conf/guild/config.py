"""
Config variables are read/write.
"""
from pydantic import BaseModel, Field, conint, conlist, constr


class GuildConfig(BaseModel):
    rules_phishing_content: conint(ge=0, le=2) = 2
    rules_phishing_domain_blacklisted: conint(ge=0, le=2) = 2
    rules_phishing_domain_heuristic: conint(ge=0, le=2) = 2
    rules_phishing_embed: conint(ge=0, le=2) = 2
    rules_selfbot_embed: conint(ge=0, le=2) = 2
    rules_ping_hidden: conint(ge=0, le=2) = 2
    rules_ping_roles: conint(ge=0, le=2) = 2
    rules_ping_users_many: conint(ge=0, le=2) = 2
    rules_ping_users_few: conint(ge=0, le=2) = 1
    rules_ping_broad: conint(ge=0, le=2) = 1
    rules_advertisement_discord_server: conint(ge=0, le=2) = 1
    rules_emoji_mass: conint(ge=0, le=2) = 0
    antispam_similar: bool = True
    antispam_exact: bool = True
    antispam_token: bool = True
    antispam_sticker: bool = True
    antispam_attachment: bool = True
    overview_modroles: conlist(constr(regex=r"\d{1,21}"), max_items=256, unique_items=True) = Field(default_factory=list)
    overview_dehoisting_enabled: bool = True
    overview_discordimpersonation_enabled: bool = True
    slowmode_enabled: bool = True
    slowmode_exceptions: conlist(constr(regex=r"\d{1,21}"), max_items=256, unique_items=True) = Field(default_factory=list)
    challenge_timeout_enabled: bool = True
    challenge_interactive_enabled: bool = False
    challenge_interactive_take_role: bool = False
    challenge_interactive_role: constr(regex=r"\d{1,21}") = "0"
    challenge_interactive_joinrisk_custom: conint(ge=0, le=100) = 70
    challenge_interactive_level: conint(ge=0, le=5) = 2
    challenge_interactive_webpage_splash: constr(regex="https?://.+", max_length=256) = ""
    logging_enabled: bool = False
    logging_channel: constr(regex=r"\d{1,21}") = "0"
    logging_option_join: bool = False
    logging_downloads_enabled: bool = False
    workers_enabled: bool = False
    workers_script: constr(max_length=1024 * 256) = ""
    bot_custom: constr(regex=r"[a-zA-Z0-9+/]+\.[a-zA-Z0-9+/]+\.[a-zA-Z0-9+/]+", max_length=256) = ""
