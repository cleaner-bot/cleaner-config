"""
Entitlments are read-only.
"""

from pydantic import BaseModel, conint

conplan = conint(ge=0, le=2)


class GuildEntitlements(BaseModel):
    plan: conplan = 0
    suspended: bool = False
    partnered: bool = False
    workers: conplan = 1
    workers_cpu: conint(ge=10, le=50) = 10
    workers_ram: conint(ge=1024 * 128, le=1024 * 1024) = 1024 * 128
    workers_size: conint(ge=1024 * 16, le=1024 * 256) = 1024 * 256
    challenge_interactive_join_risk: conplan = 1
    challenge_interactive_custom_embed: conplan = 1
    challenge_interactive_custom_webpage: conplan = 1
    contact_standard: conplan = 1
    contact_email: conplan = 1
    bot_limit: conint(ge=0, le=100) = 0
    bot_dedicated: conplan = 2
    logging_downloads: conplan = 1
    logging_retention: conint(ge=3, le=12) = 3
    impersonation_advanced: conplan = 1
    verification_custom_webpage: conplan = 1
