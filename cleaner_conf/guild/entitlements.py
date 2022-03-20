"""
Entitlments are read-only.
"""

from pydantic import BaseModel, Field


class GuildEntitlements(BaseModel):
    suspended: bool = Field(False)
    plan: int = Field(0, ge=0, le=2)
    workers: int = Field(1, ge=0, le=2)
    workers_cpu: int = Field(10, ge=10, le=50)
    workers_ram: int = Field(1024 * 128, ge=1024 * 128, le=1024 * 1024)
    workers_size: int = Field(1024 * 16, ge=1024 * 16, le=1024 * 1024)
    challenge_interactive_join_risk: int = Field(1, ge=0, le=2)
    challenge_interactive_custom_embed: int = Field(1, ge=0, le=2)
    challenge_interactive_custom_webpage: int = Field(1, ge=0, le=2)
    contact_standard: int = Field(1, ge=0, le=2)
    contact_email: int = Field(2, ge=0, le=2)
    bot_limit: int = Field(0, ge=0, le=100)
    bot_dedicated: int = Field(2, ge=0, le=2)
    logging_downloads: int = Field(1, ge=0, le=2)
    logging_retention: int = Field(3, ge=3, le=12)
