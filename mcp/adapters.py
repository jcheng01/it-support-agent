"""Explicit boundaries for future Microsoft and Freshservice adapters.

Real adapters should enforce user authorization server-side and must never trust
an employee identity merely supplied as a model-generated tool argument.
"""


def integration_status() -> dict[str, str]:
    return {
        "entra": "not_configured",
        "intune": "not_configured",
        "exchange": "not_configured",
        "freshservice": "not_configured",
    }


class IntegrationNotConfigured(RuntimeError):
    """A requested live tenant capability has no approved connector."""


class MicrosoftAdapter:
    def recent_sign_ins(self, authenticated_subject: str) -> None:
        raise IntegrationNotConfigured("Entra sign-in access is not configured")

    def device_compliance(self, authenticated_subject: str) -> None:
        raise IntegrationNotConfigured("Intune access is not configured")


class TicketAdapter:
    def create_ticket(self, authenticated_subject: str, description: str) -> None:
        raise IntegrationNotConfigured("Freshservice access is not configured")
