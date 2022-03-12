"""
Config variables are read/write.
"""

from ..values import (
    BaseValue,
    BooleanValue,
    BotTokenValue,
    IntegerValue,
    ListValue,
    SnowflakeValue,
    URLValue,
    DictType,
)


phishing = {}
for rule in (
    "phishing_content",
    "phishing_domain_blacklisted",
    "phishing_domain_heuristic",
    "phishing_embed",
    "selfbot_embed",
    "ping_hidden",
    "ping_roles",
    "ping_users_many",
    "ping_users_few",
    "ping_broad",
    "advertisement_discord_server",
    "emoji_mass",
):
    default = 2
    if (
        rule.startswith("advertisement_")
        or rule == "ping_broad"
        or rule == "ping_users_few"
    ):
        default = 1
    elif rule == "emoji_mass":
        default = 0

    phishing[f"rules_{rule}"] = IntegerValue(
        default=default, min=0, max=2, description=f"Firewall rule {rule}."
    )

antispam = {}
for rule in ("similar", "exact", "token", "sticker", "attachment"):
    antispam[f"antispam_{rule}"] = BooleanValue(
        default=True, description=f"Antispam {rule}."
    )

config: DictType = {
    **phishing,
    **antispam,
    "overview_modroles": ListValue(
        description="Moderator roles.", item=SnowflakeValue(default=0, description=None)
    ),
    "overview_dehoisting_enabled": BooleanValue(
        default=True, description="Dehoist members."
    ),
    "overview_discordimpersonation_enabled": BooleanValue(
        default=True, description="Kick discord impersonators."
    ),
    "slowmode_enabled": BooleanValue(default=True, description="Slowmode enabled."),
    "slowmode_exceptions": ListValue(
        description="Slowmode exceptions.",
        item=SnowflakeValue(default=0, description=None),
    ),
    "challenge_timeout_enabled": BooleanValue(
        default=True, description="Timeout challenges enabled."
    ),
    "challenge_interactive_enabled": BooleanValue(
        default=False, description="Interactive challenges enabled."
    ),
    "challenge_interactive_take_role": BooleanValue(
        default=False, description="Take role when challenge is completed."
    ),
    "challenge_interactive_role": SnowflakeValue(
        default=0, description="Role to give or take."
    ),
    "challenge_interactive_joinrisk_custom": IntegerValue(
        default=70, min=0, max=100, description="Custom join risk."
    ),
    "challenge_interactive_level": IntegerValue(
        default=3,
        min=0,
        max=5,
        description="Security level. custom/off/low/medium/high/iuam",
    ),
    "challenge_interactive_webpage_splash": URLValue(
        description="Background splash of webpage."
    ),
    "logging_enabled": BooleanValue(default=False, description="Logging enabled."),
    "logging_channel": SnowflakeValue(default=0, description="Channel to log into."),
    "logging_option_join": BooleanValue(
        default=False, description="Enable log on join."
    ),
    "logging_downloads_enabled": BooleanValue(
        default=False, description="Download logs"
    ),
    "workers_enabled": BooleanValue(default=False, description="Workers enabled."),
    "workers_script": BaseValue(default="", description="Worker scripts.", hidden=True),
    "bot_custom": BotTokenValue(description="Custom bot."),
}


class Config:
    rules_phishing_content: int
    rules_phishing_domain_blacklisted: int
    rules_phishing_domain_heuristic: int
    rules_phishing_embed: int
    rules_selfbot_embed: int
    rules_ping_hidden: int
    rules_ping_roles: int
    rules_ping_users_many: int
    rules_ping_users_few: int
    rules_ping_broad: int
    rules_advertisement_discord_server: int
    rules_emoji_mass: int
    antispam_similar: bool
    antispam_exact: bool
    antispam_token: bool
    antispam_sticker: bool
    antispam_attachment: bool
    overview_modroles: list[int]
    overview_dehoisting_enabled: bool
    overview_discordimpersonation_enabled: bool
    slowmode_enabled: bool
    slowmode_exceptions: list[int]
    challenge_timeout_enabled: bool
    challenge_interactive_enabled: bool
    challenge_interactive_take_role: bool
    challenge_interactive_role: int
    challenge_interactive_joinrisk_custom: int
    challenge_interactive_level: int
    challenge_interactive_webpage_splash: str
    logging_enabled: bool
    logging_channel: int
    logging_option_join: bool
    logging_downloads_enabled: bool
    workers_enabled: bool
    workers_script: str
    bot_custom: str
