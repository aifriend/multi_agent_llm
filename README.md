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

Install the dependencies with Poetry (Python 3.11 or 3.12 is required):

    make setup

The agents read their API keys from a `.env` file in the directory you run them from. The repository does not ship a `.env.example`, so create `.env` yourself with the two keys the code looks up (`src/service/Tools.py`):

    OPENAI_API_KEY=your-openai-key
    SERPER_API_KEY=your-serper-key

`SERPER_API_KEY` is only needed by the agents that use web search (`financial_agent.py`, `planning_agent.py` and `tool_agent.py`). Do not commit `.env`.

## Running the agents

The agent scripts import `service.Tools`, so run them from inside `src/`:

    cd src
    poetry run python simple_agent.py
    poetry run python multi_agent.py
    poetry run python tool_agent.py
    poetry run python planning_agent.py
    poetry run python financial_agent.py

`multi_agent.py`, `tool_agent.py`, `planning_agent.py` and `financial_agent.py` also import `crewai_tools`, which is not declared in `pyproject.toml` (see the comment there) and must be installed manually.

## FastAPI service

    poetry run uvicorn src.agent_api:app --reload

Then open `http://127.0.0.1:8000/` (example requests are in `tests/test_agent.http`).

## Tests and linting

    make test
    make lint

## Credits

The course material this project is based on is "Multi AI Agent Systems with crewAI" by DeepLearning.AI, taught by Joao Moura, creator of crewAI. The goals section above follows the course description.
