# Basic-AI-Agent
Basic AI Agent 
# Basic AI Agent

## Student Information

- Name: Anuradha Namdev Jahdav 
- Course: CSE(AIML)
- Subject: AI-Augmented Workflow

## Project Overview

This project demonstrates the development of a basic AI Agent using Python and an LLM (OpenAI API or Ollama).

## Documentation

- ADR 1: Technology Stack
- C4 Diagram
- Contribution Log
- Peer Review

# SLE-2: BFS vs DFS Profiling


## Objective

This project compares **Breadth First Search (BFS)** and **Depth First Search (DFS)** on the same graph.

## Profiling Tool

**py-spy** was used to profile both algorithms and generate flame graphs.

## Files

* `bfs.py` – BFS implementation
* `dfs.py` – DFS implementation
* `comparison.py` – BFS vs DFS comparison
* `profile_bfs.py` – BFS profiling program
* `profile_dfs.py` – DFS profiling program
* `AI_CONTRIBUTION_LOG.md` – AI contribution details

## Profiling Commands

```bash
py-spy record -o bfs_profile.svg -- python profile_bfs.py
```

```bash
py-spy record -o dfs_profile.svg -- python profile_dfs.py
```

## Result

BFS and DFS were tested using the same graph. Their node expansion and profiling results were compared to understand their practical performance.

## AI Contribution

AI was used to understand the SLE-2 requirements, get coding guidance, understand py-spy, and organize the documentation. The actual programs were executed and the profiling results were checked by the student.
