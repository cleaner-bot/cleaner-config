"""
Entitlments are read-only.
"""

from pydantic import BaseModel, conint


class GuildEntitlements(BaseModel):
    plan: conint(ge=0, le=2) = 0
    suspended: bool = False
    partnered: bool = False

    antiraid: conint(ge=0, le=2) = 0  # unused
    antispam: conint(ge=0, le=2) = 0  # unused
    backup: conint(ge=0, le=2) = 1
    bot_limit: conint(ge=0, le=100) = 0  # unused
    bot_dedicated: conint(ge=0, le=2) = 2  # unused
    branding_splash: conint(ge=0, le=2) = 1
    branding_embed: conint(ge=0, le=2) = 1  # unused
    branding_vanity: conint(ge=0, le=2) = 1  # unused
    challenge_interactive_join_risk: conint(ge=0, le=2) = 1
    contact_standard: conint(ge=0, le=2) = 1
    contact_email: conint(ge=0, le=2) = 1
    firewall: conint(ge=0, le=2) = 0  # unused
    impersonation: conint(ge=0, le=2) = 0  # unused
    impersonation_advanced: conint(ge=0, le=2) = 1
    logging: conint(ge=0, le=2) = 0  # unused
    logging_downloads: conint(ge=0, le=2) = 1
    logging_retention: conint(ge=3, le=12) = 3
    slowmode: conint(ge=0, le=2) = 0  # unused
    statistics: conint(ge=0, le=2) = 0
    report: conint(ge=0, le=2) = 1
    verification: conint(ge=0, le=2) = 0  # unused
    workers: conint(ge=0, le=2) = 1  # unused
    workers_cpu: conint(ge=10, le=50) = 10  # unused
    workers_ram: conint(ge=1024 * 128, le=1024 * 1024) = 1024 * 128  # unused
    workers_size: conint(ge=1024 * 16, le=1024 * 256) = 1024 * 256  # unused
