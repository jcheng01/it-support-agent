# IT Support Agent starter

An employee-facing ChatGPT agent for guided IT troubleshooting. The three skills cover Outlook sign-in, BitLocker recovery loops, and Entra/Intune device trust. They work conversationally without company access. The MCP folder is a separate, local-only scaffold for future authenticated integrations.

## What is ready

| Component | State |
| --- | --- |
| `skills/` | Three self-contained `SKILL.md` playbooks; no tenant credentials needed |
| `agent/INSTRUCTIONS.md` | Instructions to paste into a private Workspace Agent |
| `mcp/` | Runs locally, exposes only `integration_status`; deliberately has no Entra, Intune, Exchange, or Freshservice access |
| `.github/workflows/validate.yml` | Validates the skill metadata and compiles the Python scaffold on PRs and pushes |

## Try the agent in ChatGPT

1. In an eligible ChatGPT workspace, create a private Workspace Agent named **IT Support Pilot**.
2. Paste `agent/INSTRUCTIONS.md` into its instructions. Add the three folders under `skills/` with the agent builder's **Add skill** → upload flow. Keep the pilot private while testing.
3. Preview with the prompts in `tests/scenarios.md`. Verify that it asks for evidence and never claims it queried company systems or opened a ticket.
4. When you have access to a company workspace, have its admin review the skills, data handling, and audience before publishing the agent to employees. Company access is a separate step from making this repo available.

Skills are files in this repository, but GitHub changes do not automatically update the ChatGPT agent. After merging a reviewed change, upload the revised skill to the agent and retest. A PR runs validation; merging alone does not deploy the agent.

## Run the optional MCP scaffold locally

The agent needs no MCP server for the first three skills. To inspect the separate integration scaffold:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r mcp/requirements.txt
.venv/bin/python mcp/server.py
```

The default Streamable HTTP endpoint is `http://127.0.0.1:8765/mcp`. It exposes only `integration_status`, which reports that all company integrations are unconfigured. **Do not publish this unauthenticated scaffold on the internet.** Add an authentication and authorization design, per-user scope, approval for writes, logging controls, and real adapters before any company data is connected.

## Source and deployment

Edit skills in `skills/`, propose changes in a branch and PR, and review the instructions as operational policy. GitHub Actions checks syntax. Upload the approved skill versions to ChatGPT. Later, the MCP service can be deployed separately to an authenticated HTTPS host and connected to the agent. Azure Container Apps or App Service are possible hosts, not requirements of the skills.

No secrets, tenant IDs, recovery keys, ticket data, or production configuration belong in this repository.
