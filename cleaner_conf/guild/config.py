"""
Config variables are read/write.
"""
from pydantic import BaseModel, Field, conint, conlist, constr

snowflake_re = r"^(0|\d{17,21})$"


class GuildConfig(BaseModel):
    rules_phishing_content: conint(ge=0, le=2) = 2
    rules_phishing_content_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_phishing_domain_blacklisted: conint(ge=0, le=2) = 2
    rules_phishing_domain_blacklisted_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_phishing_domain_heuristic: conint(ge=0, le=2) = 2
    rules_phishing_domain_heuristic_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_phishing_embed: conint(ge=0, le=2) = 2
    rules_phishing_embed_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_selfbot_embed: conint(ge=0, le=2) = 2
    rules_selfbot_embed_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_ping_hidden: conint(ge=0, le=2) = 2
    rules_ping_hidden_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_ping_roles: conint(ge=0, le=2) = 2
    rules_ping_roles_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_ping_users_many: conint(ge=0, le=2) = 2
    rules_ping_users_many_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_ping_users_few: conint(ge=0, le=2) = 1
    rules_ping_users_few_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_ping_broad: conint(ge=0, le=2) = 1
    rules_ping_broad_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_advertisement_discord_invite: conint(ge=0, le=2) = 1
    rules_advertisement_discord_invite_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    rules_emoji_mass: conint(ge=0, le=2) = 0
    rules_emoji_mass_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antispam_similar: bool = True
    antispam_similar_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antispam_exact: bool = True
    antispam_exact_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antispam_token: bool = True
    antispam_token_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antispam_sticker: bool = True
    antispam_sticker_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antispam_attachment: bool = True
    antispam_attachment_channels: conlist(
        constr(regex=snowflake_re), max_items=25, unique_items=True
    ) = Field(default_factory=list)
    antiraid_enabled: bool = False
    antiraid_limit: constr(regex=r"^\d{1,5}/\d{1,3}$") = "10/10"
    antiraid_mode: conint(ge=0, le=3) = 0  # all/1day/3days/week
    general_modroles: conlist(
        constr(regex=snowflake_re), max_items=256, unique_items=True
    ) = Field(default_factory=list)
    general_dehoisting_enabled: bool = True
    slowmode_enabled: bool = True
    slowmode_exceptions: conlist(
        constr(regex=snowflake_re), max_items=256, unique_items=True
    ) = Field(default_factory=list)
    challenge_timeout_enabled: bool = True
    challenge_interactive_enabled: bool = False
    challenge_interactive_take_role: bool = False
    challenge_interactive_role: constr(regex=snowflake_re) = "0"
    challenge_interactive_joinrisk_custom: conint(ge=0, le=100) = 70
    challenge_interactive_level: conint(
        ge=0, le=5
    ) = 2  # custom/off/low/medium/high/iuam
    verification_enabled: bool = False
    verification_role: constr(regex=snowflake_re) = "0"
    logging_enabled: bool = False
    logging_channel: constr(regex=snowflake_re) = "0"
    logging_option_join: bool = False
    logging_option_leave: bool = False
    logging_option_verify: bool = False
    logging_downloads_enabled: bool = False
    impersonation_discord_enabled: bool = True
    impersonation_advanced_enabled: bool = False
    impersonation_advanced_subwords: conlist(
        constr(max_length=32), max_items=300
    ) = Field(default_factory=list)
    impersonation_advanced_words: conlist(constr(max_length=32), max_items=300) = Field(
        default_factory=list
    )
    report_enabled: bool = False
    report_channel: constr(regex=snowflake_re) = "0"
    workers_enabled: bool = False
    bot_custom: constr(
        regex=r"^([a-zA-Z0-9+/]+\.[a-zA-Z0-9+/]+\.[a-zA-Z0-9+/]+)?$", max_length=256
    ) = ""
    branding_splash_enabled: bool = False
    branding_embed_enabled: bool = False
    branding_embed_title: constr(max_length=200) = ""
    branding_embed_description: constr(max_length=2048) = ""
