# MCP Leave Manager --- Complete Setup & Run Guide

This document explains **from scratch** how to create, configure, and
run your MCP Leave Manager project using `uv`.

------------------------------------------------------------------------

# PART 1 --- Initial Setup (From Scratch)

## 1. Install uv (One Time Only)

``` powershell
pip install uv
```

Verify installation:

``` powershell
uv --version
```

------------------------------------------------------------------------

## 2. Create a New MCP Project

Navigate to your workspace:

``` powershell
cd C:\code\course-gen-ai
```

Create the project:

``` powershell
uv init my-first-mcp-server
```

Enter the project folder:

``` powershell
cd my-first-mcp-server
```

You should see:

-   main.py
-   pyproject.toml

------------------------------------------------------------------------

## 3. Add MCP Dependency

This is REQUIRED:

``` powershell
uv add "mcp[cli]"
```

If you see typer-related issues:

``` powershell
uv add typer
```

------------------------------------------------------------------------

## 4. Verify MCP Installation

``` powershell
uv run python -c "import mcp; print('MCP OK')"
```

Expected output:

    MCP OK

------------------------------------------------------------------------

# PART 2 --- Create MCP Server (main.py)

Replace the contents of `main.py` with your LeaveManager MCP server
code.

IMPORTANT: Your file must end with:

``` python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

This makes your server run over STDIO transport.

DO NOT manually run main.py in production use.

------------------------------------------------------------------------

# PART 3 --- Create MCP Client (client.py)

Create a new file:

``` powershell
notepad client.py
```

Paste your working MCP + Cerebras client code into this file.

The client will: - Launch the server - Connect via STDIO - Call Cerebras
LLM - Execute tools - Return responses

------------------------------------------------------------------------

# PART 4 --- Running The Project

Always navigate to the project directory first:

``` powershell
cd C:\code\course-gen-ai\my-first-mcp-server
```

Then run:

``` powershell
uv run client.py
```

That's it.

DO NOT run main.py directly.

------------------------------------------------------------------------

# What Happens Internally

When you run:

    uv run client.py

The following happens:

1.  Client starts
2.  Client launches main.py as MCP server
3.  MCP session initializes
4.  Client fetches tool schemas
5.  User asks question
6.  LLM decides tool
7.  Tool executes in server
8.  Result is printed

------------------------------------------------------------------------

# Testing Commands

After startup you should see:

    🚀 Leave Management AI Ready (Cerebras + MCP)
    Type 'exit' to quit

Try:

    Check leave balance for E001

    Apply leave for E002 on 2025-05-10 and 2025-05-11

    Show leave history for E001

------------------------------------------------------------------------

# How To Stop

Type:

    exit

Or press:

    Ctrl + C

------------------------------------------------------------------------

# If Something Breaks

Reset environment:

``` powershell
uv sync
```

Then run again:

``` powershell
uv run client.py
```

------------------------------------------------------------------------

# Important Rules

DO NOT run:

``` powershell
uv run main.py
```

The server must always be launched by the client.

------------------------------------------------------------------------

# Minimal Command Summary

## First-Time Setup

    uv init my-first-mcp-server
    cd my-first-mcp-server
    uv add "mcp[cli]"

## Every Time You Want To Run

    cd my-first-mcp-server
    uv run client.py

------------------------------------------------------------------------

You now have a clean, reproducible MCP project template.
