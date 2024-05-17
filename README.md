# Multi AI Agent Systems

A multi-agent system (MAS or "self-organized system") is a computerized system composed of multiple interacting intelligent agents. Multi-agent systems can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve. Intelligence may include methodic, functional, procedural approaches, algorithmic search or reinforcement learning.
Despite considerable overlap, a multi-agent system is not always the same as an agent-based model (ABM). The goal of an ABM is to search for explanatory insight into the collective behavior of agents (which do not necessarily need to be "intelligent") obeying simple rules, typically in natural systems, rather than in solving specific practical or engineering problems. The terminology of ABM tends to be used more often in the science, and MAS in engineering and technology. Applications where multi-agent systems research may deliver an appropriate approach include online trading, disaster response, target surveillance and social structure modelling.

# Agents with LLMs

Exceed the performance of prompting a single LLM by designing and prompting a team of AI agents through natural language.
Use an open source library, crewAI, to automate repeatable, multi-step tasks like tailoring a resume to a job description; and automate business processes that are typically done by a group of people, like event planning.
By creating a team of AI agents, you can define a specific role, goal, and backstory for each agent, which breaks down complex multi-step tasks and assigns them to agents that are customized to perform those tasks.

# Goals

Learn key principles of designing effective AI agents, and organizing a team of AI agents to perform complex, multi-step tasks. Apply these concepts to automate 6 common business processes.

Explore key components of multi-agent systems:
* Role-playing: Assign specialized roles to agents 
Memory: Provide agents with short-term, long-term, and shared memory
* Tools: Assign pre-built and custom tools to each agent (e.g. for web search)
* Focus: Break down the tasks, goals, and tools and assign to multiple AI agents for better performance
* Guardrails: Effectively handle errors, hallucinations, and infinite loops
* Cooperation: Perform tasks in series, in parallel, and hierarchically

Throughout the course, you’ll work with crewAI, an open source library designed for building multi-agent systems. You’ll learn to build agent crews that execute common business processes, such as:
* Tailor resumes and interview prep for job applications
* Research, write and edit technical articles
* Automate customer support inquiries
* Conduct customer outreach campaigns
* Plan and execute events
* Perform financial analysis

## Environment

Setup:

    make requirements 

## Loading datasets

Loading and preparation of data:

    make data /PROJECT_DIR/data/raw /PROJECT_DIR/data/interim

## Feature extraction

    make features /PROJECT_DIR/data/interim /PROJECT_DIR/data/processed

## Analysis

## Prediction

    make train /PROJECT_DIR/data/processed
    make predict /PROJECT_DIR/data/processed

