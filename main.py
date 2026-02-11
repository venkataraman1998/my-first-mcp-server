from mcp.server.fastmcp import FastMCP
from typing import List

# In-memory mock database
employee_leaves = {
    "101": {"balance": 18, "history": ["2024-12-25", "2025-01-01"]},
    "102": {"balance": 20, "history": []}
}

mcp = FastMCP("LeaveManager")


@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """
    Get remaining leave balance.

    Args:
        employee_id: Employee ID as string (e.g., "101")
    """
    data = employee_leaves.get(employee_id)
    if data:
        return f"{employee_id} has {data['balance']} leave days remaining."
    return "Employee ID not found."


@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]) -> str:
    """
    Apply leave for specific dates.

    Args:
        employee_id: Employee ID as string (e.g., "101")
        leave_dates: List of dates in YYYY-MM-DD format
    """
    if employee_id not in employee_leaves:
        return "Employee ID not found."

    requested_days = len(leave_dates)
    available_balance = employee_leaves[employee_id]["balance"]

    if available_balance < requested_days:
        return (
            f"Insufficient leave balance. "
            f"You requested {requested_days} day(s) but have only {available_balance}."
        )

    employee_leaves[employee_id]["balance"] -= requested_days
    employee_leaves[employee_id]["history"].extend(leave_dates)

    return (
        f"Leave applied for {requested_days} day(s). "
        f"Remaining balance: {employee_leaves[employee_id]['balance']}."
    )


@mcp.tool()
def get_leave_history(employee_id: str) -> str:
    """
    Get leave history.

    Args:
        employee_id: Employee ID as string (e.g., "101")
    """
    data = employee_leaves.get(employee_id)
    if data:
        history = ", ".join(data["history"]) if data["history"] else "No leaves taken."
        return f"Leave history for {employee_id}: {history}"
    return "Employee ID not found."


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting."""
    return f"Hello, {name}! How can I assist you with leave management today?"


if __name__ == "__main__":
    mcp.run(transport="stdio")
