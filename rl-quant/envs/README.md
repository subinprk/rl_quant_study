# Environments Directory

This directory contains custom gym environments for reinforcement learning quantitative trading.

## Purpose

Define trading environments that implement the OpenAI Gym interface:
- State space (market observations, portfolio state)
- Action space (buy, sell, hold actions)
- Reward functions
- Environment dynamics

## Notes

- Each environment should inherit from `gym.Env`
- Document the observation and action spaces clearly
