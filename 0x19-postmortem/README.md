# Postmortem

On Monday, August 14, 2023, around 6:00 AM WAT, an incident of the "Too Many Open Files" error occurred on an isolated Ubuntu 14.04 container(Sandbox) running an Nginx web server. The incident impacted the web server's performance, leading to failed requests, non-2xx responses, and a degraded user experience. Roughly 30% of users were affected by the incident. The primary cause of the incident was a low default ULIMIT value, which led to "Too many open files" errors and exceeded file descriptor limits.

## Root Cause and Resolution:
**Root Cause:** The low default ULIMIT value led to file descriptor limits being exceeded, causing "Too many open files" errors during high traffic.
**Resolution:** The incident was mitigated by temporarily increasing the ULIMIT value using a shell command. A permanent solution was implemented using Puppet to enforce higher ULIMIT values across servers.

## Corrective and Preventative Measures:

**Corrective Measures:**
- Implement automated tests to validate Puppet manifests before applying changes.
- Regularly review resource limits based on anticipated traffic patterns.
- Enhance monitoring to proactively detect resource limit issues.

**Preventative Measures:**
- Maintain updated documentation on configurations and incident handling.
- Regularly assess system performance and resource limits to identify bottlenecks.

## Tasks to Address the Issue:

- Review and adjust **ULIMIT** values using Puppet manifests.
- Conduct thorough testing of Puppet-managed configurations.
- Implement proactive monitoring of file descriptor usage.
## Conclusion:
The incident, caused by low **ULIMIT** values, was resolved promptly. Temporary mitigation was achieved through a shell command, followed by a robust Puppet-based solution for long-term stability. Through corrective and preventative measures, we aim to enhance system resilience and proactively address resource-related issues.
