# CampusWatch SNMP

SNMP-based monitoring concept for school network infrastructure, designed for educational labs and hackathon scenarios.

## Overview

CampusWatch SNMP is a lightweight monitoring project for observing traffic and health indicators from switches and routers in a school or campus network. It is designed as a teaching artifact: students can connect a dashboard to an API, poll device metrics, and reason about operational visibility.

## Problem

Educational networks depend on stable connectivity, but many failures are discovered only after they affect classes. A monitoring baseline helps teams detect traffic bottlenecks, device overload, and degraded links earlier.

## Solution Concept

- Use SNMP agents on switches and routers as metric sources.
- Implement a manager service that polls interface and health data.
- Expose data to a dashboard for traffic and status visualization.
- Use the project as a practical exercise in network observability.

## Architecture

- SNMP agents: network devices that expose MIB data.
- SNMP manager: backend service responsible for polling.
- Dashboard: frontend surface for charts, interface status, and alerts.

## Suggested Stack

- Python for polling and backend services.
- React for dashboard experiments.
- SNMP libraries for GET/WALK operations.
- Charting library for traffic visualization.

## Development Direction

- Implement polling loops with safe timeouts.
- Add device inventory configuration.
- Add API endpoints for current status and historical samples.
- Add dashboard charts for traffic per port.
- Add tests for parsing and polling logic.

## Professional Context

This repository connects network monitoring, SNMP, education technology, and practical infrastructure troubleshooting.

## License

MIT. See [LICENSE](LICENSE).
