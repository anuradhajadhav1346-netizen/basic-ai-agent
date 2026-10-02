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


# SLE-3: AI Contribution Log

## Project

**Basic AI Agent – Architectural Design using Full C4 Model**

## AI Tools Used

* ChatGPT
* PlantUML / PUM(L) for generating and rendering C4 architecture diagrams

## Contribution of AI

AI assistance was used during SLE-3 to understand the Full C4 Model and the requirements of the architectural design task. ChatGPT was used to obtain guidance for creating the Context, Container, Component, and Code-level diagrams. AI also helped in organizing the project architecture and explaining the purpose of the different system elements.

AI assistance was also used to troubleshoot PlantUML errors and simplify the diagram code so that the diagrams could be generated successfully.

## Student's Contribution

The student reviewed the suggested architecture, selected the relevant system elements, entered and tested the PlantUML code, generated the diagrams, and checked the output. The student prepared the SLE-3 documentation and arranged the diagrams according to the faculty guidelines.

The final architecture, diagrams, documentation, and submission were reviewed by the student before submission.

## Summary

AI was used as a supporting tool for understanding, diagram generation guidance, troubleshooting, and documentation. The student remained responsible for reviewing, modifying, testing, and finalizing the SLE-3 work.
