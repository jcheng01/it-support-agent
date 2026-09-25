"""Local-only MCP integration scaffold; no live company connectors are enabled."""

from mcp.server.fastmcp import FastMCP

from adapters import integration_status

server = FastMCP(
    "it-support-scaffold", host="127.0.0.1", port=8765, stateless_http=True
)


@server.tool()
def get_integration_status() -> dict[str, str]:
    """Report which IT integrations are configured; this never queries company data."""
    return integration_status()


if __name__ == "__main__":
    server.run(transport="streamable-http")
