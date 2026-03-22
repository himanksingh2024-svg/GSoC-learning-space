---
title: SIR Epidemic Model
authors:
  - himanksingh2024-svg
domain:
  - epidemiology
  - public-health
complexity: beginner
mesa_version_min: "4.0"
status: incubator
keywords: [SIR, epidemic, disease, spread, recovery]
---

## Abstract
A classic SIR (Susceptible-Infected-Recovered) epidemic model where agents spread disease through random contact. Starting with 5 infected agents out of 100, the model shows how an epidemic rises, peaks, and fades.

## Model Description
- **Agents:** 100 PersonAgents with states: Susceptible, Infected, or Recovered
- **Rules:** Each step, infected agents randomly contact up to 3 susceptible agents and may infect them. Infected agents recover with a fixed probability.
- **Space:** No grid — agents interact globally
- **Parameters:** n_agents (100), infection_rate (0.3), recovery_rate (0.1)

## How to Run
```bash
pip install mesa solara matplotlib
solara run app.py
```

## Results & Discussion
The model produces a classic epidemic curve — susceptible population crashes, infected peaks then falls, recovered climbs. Total population is conserved. Adjusting infection_rate and recovery_rate produces dramatically different outcomes.

## References
- Kermack & McKendrick (1927), A Contribution to the Mathematical Theory of Epidemics