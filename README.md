THis project shows how to create mcp server.
I implemented an architecture based on the Model Context Protocol (MCP) to securely integrate a Large Language Model with internal enterprise tools.

The MCP server exposes well-defined tools that encapsulate access to the employee database (e.g., leave balance, leave history, and related HR data). Direct database access is not exposed to the model; all interactions are routed through controlled tool interfaces.

The MCP client is powered by Llama 3.1 8B and connects to the MCP server over the MCP protocol. When a user submits a natural language query, the model interprets the intent, invokes the appropriate MCP tool, and returns a structured response.

This design ensures secure, auditable, and controlled access to employee data while enabling conversational querying capabilities and the client gives answers.