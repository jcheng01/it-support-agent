import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp"))

from adapters import IntegrationNotConfigured, MicrosoftAdapter, TicketAdapter, integration_status


class ScaffoldTests(unittest.TestCase):
    def test_unconfigured_integrations_never_return_fake_tenant_data(self):
        self.assertTrue(all(v == "not_configured" for v in integration_status().values()))
        with self.assertRaises(IntegrationNotConfigured):
            MicrosoftAdapter().recent_sign_ins("example")
        with self.assertRaises(IntegrationNotConfigured):
            TicketAdapter().create_ticket("example", "description")


if __name__ == "__main__":
    unittest.main()
