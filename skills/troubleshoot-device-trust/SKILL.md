---
name: troubleshoot-device-trust
description: Guide Entra ID and Intune device-registration and compliance triage when a managed Windows user cannot access Microsoft 365 or company apps due to device trust or Conditional Access. Use for device-not-compliant, device-not-registered, sign-in blocked, or access-works-in-browser-but-not-desktop issues.
---

# Troubleshoot device trust

1. Identify the affected app, error text/code, time, user, device, and whether browser, desktop, other devices, or other users work. Do not ask for passwords, MFA codes, or device recovery keys.
2. On Windows, ask an authorized technician to inspect `dsregcmd /status` in the affected user's context and record relevant AzureAdJoined, DomainJoined, WorkplaceJoined, device ID, and SSO state. Explain that these signals alone do not establish compliance or the exact Conditional Access reason.
3. With approved read-only tools, correlate the Entra sign-in event for that user/app/time with Conditional Access evaluation; compare its device ID to the Entra device object and Intune managed device, compliance status, and last check-in. A missing Intune record, stale check-in, noncompliant policy, and wrong device ID call for different follow-up. Never present a local diagnostic as a live tenant lookup.
4. Check whether the device is online, has correct time, and can open Company Portal where applicable. Have IT inspect the actual noncompliance policy and remediation detail before suggesting a specific fix.
5. Do not bypass Conditional Access, disable compliance requirements, remove/re-enroll the device, or grant a policy exception as routine troubleshooting. Escalate with sign-in correlation ID, device IDs, compliance reason, last check-in, and the checks already performed. State what is observed versus inferred.
