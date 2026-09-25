---
name: troubleshoot-bitlocker-recovery
description: Guide safe triage for a managed Windows computer repeatedly asking for its BitLocker recovery key or looping back to recovery after a valid key. Use for BitLocker recovery screens, startup loops, or post-firmware-update recovery on company devices.
---

# Troubleshoot BitLocker recovery

1. Ask whether this is a company device, whether the key is accepted before the prompt returns, the displayed recovery key ID (not the 48-digit key), recent BIOS/firmware/TPM changes, and whether Windows ever starts. Treat an incorrect-key message differently from an accepted-key boot loop.
2. Do not ask the user to send a recovery key in chat. Direct them to the organization's approved recovery flow and verify device identity and authorization through that flow. Never invent a key or suggest bypassing encryption.
3. If the key is rejected, have authorized IT match the on-screen key ID to the escrowed key for this exact device and confirm keyboard layout/entry. If accepted then looping, gather the screen sequence and stop repeated blind key entry; investigate boot/TPM/firmware or Windows recovery causes through the managed device process.
4. Preserve data. Do not suggest clearing the TPM, wiping/reinstalling, deleting partitions, turning off Secure Boot, or suspending BitLocker without an authorized technician assessing impact and recovery-key escrow. If WinRE is used, note that recovery may request the key again and use only approved, documented repair procedures.
5. If signs suggest hardware failure, boot corruption, or a widespread firmware change, escalate with device identity, key ID, exact messages, recent changes, and whether the key was accepted. Separate observed facts from likely causes; do not claim that storage or encryption is healthy solely because the key was accepted.
