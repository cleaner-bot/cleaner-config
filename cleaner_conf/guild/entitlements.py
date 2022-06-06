"""
Entitlments are read-only.
"""

from pydantic import BaseModel, conint


class GuildEntitlements(BaseModel):
    plan: conint(ge=0, le=2) = 0
    suspended: bool = False
    partnered: bool = False

    access: conint(ge=0, le=2) = 1
    antiraid: conint(ge=0, le=2) = 0  # unused
    antispam: conint(ge=0, le=2) = 0  # unused
    backup: conint(ge=0, le=2) = 1
    backup_snapshot_limit: int = 25
    bot_limit: conint(ge=0, le=100) = 0  # unused
    bot_dedicated: conint(ge=0, le=2) = 2  # unused
    branding_splash: conint(ge=0, le=2) = 1
    branding_embed: conint(ge=0, le=2) = 1
    branding_vanity: conint(ge=0, le=2) = 1
    branding_vanity_url: str = ""
    challenge_interactive_join_risk: conint(ge=0, le=2) = 1
    contact_standard: conint(ge=0, le=2) = 1
    contact_email: conint(ge=0, le=2) = 1
    firewall: conint(ge=0, le=2) = 0  # unused
    impersonation: conint(ge=0, le=2) = 0  # unused
    impersonation_advanced: conint(ge=0, le=2) = 1
    joinguard: conint(ge=0, le=2) = 1
    logging: conint(ge=0, le=2) = 0  # unused
    logging_downloads: conint(ge=0, le=2) = 1
    logging_retention: conint(ge=3, le=12) = 3
    slowmode: conint(ge=0, le=2) = 0  # unused
    statistics: conint(ge=0, le=2) = 0
    report: conint(ge=0, le=2) = 1
    verification: conint(ge=0, le=2) = 0  # unused
    workers: conint(ge=0, le=2) = 1
    workers_cpu: int = 1e6
    workers_ram: int = 1024 * 128
    workers_size: int = 1024 * 256
