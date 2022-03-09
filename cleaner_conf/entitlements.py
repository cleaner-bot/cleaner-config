"""
Entitlments are read-only.
"""

from .values import PlanValue, IntegerValue, DictType


entitlements: DictType = {
    "plan": PlanValue(default=0, description="Current plan."),
    "workers": PlanValue(default=1, description="Workers unlock."),
    "workers_cpu": IntegerValue(
        default=10, min=10, max=50, description="CPU time per message. (in ms)"
    ),
    "workers_ram": IntegerValue(
        default=1024 * 128,
        min=1024 * 128,
        max=1024 * 1024,
        description="RAM per worker. (in bytes)",
    ),
    "workers_size": IntegerValue(
        default=1024 * 16,
        min=1024 * 16,
        max=1024 * 1024,
        description="JS size of the worker. (in bytes)",
    ),
    "challenge_interactive_join_risk": PlanValue(
        default=1, description="Custom and disabled join risk unlock."
    ),
    "challenge_interactive_custom_embed": PlanValue(
        default=1, description="Custom embed unlock."
    ),
    "challenge_interactive_custom_webpage": PlanValue(
        default=1, description="Custom webpage unlock."
    ),
    "contact_standard": PlanValue(default=1, description="Standard support unlock."),
    "contact_email": PlanValue(default=2, description="EMail support unlock."),
    "bot_limit": IntegerValue(default=0, min=0, max=100, description="Limit of bots."),
    "bot_dedicated": PlanValue(default=2, description="Dedicated bot unlock."),
    "logging_downloads": PlanValue(default=1, description="Logging downloads unlock."),
    "logging_retention": IntegerValue(
        default=3, min=0, max=12, description="Logging data retention (in months)."
    ),
}


class Entitlements:
    plan: int
    workers: int
    workers_cpu: int
    workers_ram: int
    workers_size: int
    challenge_interactive_join_risk: int
    challenge_interactive_custom_embed: int
    challenge_interactive_custom_webpage: int
    contact_standard: int
    contact_email: int
    bot_limit: int
    bot_dedicated: int
    logging_downloads: int
    logging_retention: int
