---
title: Boltzmann Wealth Model
authors:
  - himanksingh2024-svg
domain:
  - economics
  - inequality
complexity: beginner
mesa_version_min: "4.0"
status: incubator
keywords: [wealth, inequality, emergence, boltzmann]
---

## Abstract
A simple model where 50 agents randomly exchange wealth. Starting from perfect equality, wealth inequality emerges naturally through random interactions — demonstrating how unequal distributions can arise without any unfair rules.

## Model Description
- **Agents:** 50 MoneyAgents, each starting with 1 unit of wealth
- **Rules:** Each step, an agent gives 1 unit of wealth to a random other agent (if they have any)
- **Space:** No grid — agents interact globally
- **Parameters:** n_agents (default 50)

## How to Run
```bash
pip install mesa solara matplotlib
solara run app.py
```

## Results & Discussion
Total wealth is conserved at 50 across all steps. Despite equal starting conditions, wealth concentrates rapidly — a few agents accumulate large amounts while many drop to zero. This mirrors real-world wealth distributions (Boltzmann/Pareto distributions).

## References
- Dragulescu & Yakovenko (2000), Statistical mechanics of money