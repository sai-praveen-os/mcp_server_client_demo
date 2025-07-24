# MCP (Model Context Protocol) in Kiro - Getting Started

## What is MCP?

MCP lets Kiro connect to external tools and services. Think of it as giving Kiro superpowers - it can now interact with Git, fetch web content, and more.

## Two Types of MCP Servers

### 🏠 Local Servers
- Run on your computer
- Your data stays private
- Work offline
- Free to use

### ☁️ Remote Servers  
- Run on external services (like GitHub's servers)
- May send your data to external companies
- Require internet connection
- May have usage costs

## What Works in Kiro Right Now

### ✅ Local Servers (Ready to Use)

**Git Server** - Work with your Git repositories
```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git"],
      "disabled": false,
      "autoApprove": ["git_status", "git_log"]
    }
  }
}
```

**Fetch Server** - Get content from websites
```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### ❌ What Doesn't Work Yet

**GitHub Copilot MCP Server** - This works in VS Code but not in Kiro (yet)

## Quick Setup

1. **Find your MCP config file**: `.kiro/settings/mcp.json`

2. **Add both working servers**:
```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git"],
      "disabled": false,
      "autoApprove": ["git_status", "git_log"]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

3. **Restart Kiro** or reconnect MCP servers

4. **Test it**:
   - Ask Kiro: "What's my git status?"
   - Ask Kiro: "Fetch content from https://example.com"

## What You Can Do Now

### With Git Server:
- Check repository status
- View commit history
- See file changes
- Create commits
- Switch branches

### With Fetch Server:
- Get content from any website
- Convert web pages to markdown
- Extract text from articles

## Troubleshooting

**"Package not found" error?**
- Make sure you have `uv` installed: `pip install uv`
- Check if `uvx` is available: `which uvx`

**Server not responding?**
- Restart Kiro
- Check the MCP Server view in Kiro's feature panel

## What's Next?

- More local servers may become available as PyPI packages
- GitHub MCP server support might come to Kiro in the future
- You can build custom servers if you're adventurous

## Key Takeaway

Right now, Kiro supports 2 local MCP servers that work great for Git operations and web content fetching. They're free, private, and easy to set up!