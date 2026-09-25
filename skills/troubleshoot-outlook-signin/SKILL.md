---
name: troubleshoot-outlook-signin
description: Guide employee or technician troubleshooting when Outlook desktop repeatedly prompts for a password, fails to sign in, or shows a Microsoft 365 authentication error. Use for Outlook sign-in problems, including cases where Teams or Outlook on the web works.
---

# Troubleshoot Outlook sign-in

1. Ask whether Outlook desktop, Outlook on the web, and Teams work; record the exact error, time, affected device, and whether other users are affected. Do not ask for passwords, MFA codes, tokens, or screenshots containing them.
2. Ask whether the problem followed a password change, device change, update, or network change. Check the clock and network only if symptoms suggest them.
3. If approved read-only tools exist, check the current user's account enabled state and relevant license; review matching recent Entra sign-in events for the affected app, timestamp, error code, Conditional Access result, and correlation ID. Only inspect mailbox state when sign-in succeeds but Outlook still cannot open the mailbox. If no tool exists, ask a technician to perform those checks; never imply they were done.
4. If web Outlook works and desktop Outlook fails, narrow to desktop-specific authentication, profile, update, or device state. If both fail, prioritize account, license, service health, and sign-in evidence. If Teams works, avoid treating that as proof that Outlook authentication or Exchange is healthy.
5. Recommend one reversible check at a time. Do not suggest disabling Conditional Access, MFA, endpoint protection, or deleting a profile/data file as a first step. Route policy changes and account operations to authorized IT staff.
6. State what is confirmed, what remains a hypothesis, and the next check. If unresolved, prepare a concise escalation summary with user-approved identifiers, symptoms, impact, timestamps, test results, relevant error/correlation IDs, and actions tried. Do not claim to have created a ticket without a connected ticket tool.
