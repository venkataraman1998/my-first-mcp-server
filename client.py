import asyncio
import json
import httpx

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession


CEREBRAS_API_KEY = ""
MODEL = "llama3.1-8b"
ENDPOINT = "https://api.cerebras.ai/v1/chat/completions"


async def ask_llm(messages, tools):
    headers = {
        "Authorization": f"Bearer {CEREBRAS_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "temperature": 0,
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]


async def main():
    print("🚀 Leave Management AI Ready (Cerebras + MCP)")
    print("Type 'exit' to quit\n")

    server = StdioServerParameters(
        command="uv",
        args=["run", "main.py"],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            tool_schemas = []
            for tool in tools.tools:
                tool_schemas.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description,
                            "parameters": tool.inputSchema,
                        },
                    }
                )

            while True:
                user_input = input("You: ")

                if user_input.lower() == "exit":
                    break

                messages = [
                    {"role": "system", "content": "You are an HR leave management assistant."},
                    {"role": "user", "content": user_input},
                ]

                response_message = await ask_llm(messages, tool_schemas)

                if "tool_calls" in response_message:
                    tool_call = response_message["tool_calls"][0]
                    function_name = tool_call["function"]["name"]
                    arguments = json.loads(tool_call["function"]["arguments"])

                    result = await session.call_tool(function_name, arguments)

                    print("\n🔧 Tool Result:")
                    print(result.content[0].text)
                    print()

                else:
                    print("\n🤖 AI:")
                    print(response_message["content"])
                    print()


if __name__ == "__main__":
    asyncio.run(main())
