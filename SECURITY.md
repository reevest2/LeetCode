# Security Policy

## Scope

This repository contains algorithmic solutions for educational purposes. It does not process user data, handle authentication, or run as a service. The security considerations here are narrower than most software projects but still important.

## Reporting a Vulnerability

If you discover a security concern -- for example, a solution that contains code injection vectors, malicious content, or links to harmful resources -- please report it by opening a private issue or contacting the maintainers directly.

Do NOT open a public issue for security concerns.

## What We Consider Security Issues

- Solutions containing malicious code disguised as algorithm implementations
- Links in study guides or documentation pointing to malicious sites
- Scripts in the `scripts/` directory that perform unintended actions
- Dependencies (if any are added in the future) with known vulnerabilities

## Code Safety Standards

All solutions in this repository must:

- Not access the filesystem, network, or any external resources
- Not use `eval`, `exec`, or equivalent dynamic code execution
- Not contain obfuscated code
- Not import modules beyond what is needed for the algorithm
- Be safe to compile and run in a sandboxed environment
