# MCP Chat

MCP Chat is a command-line interface application that enables interactive chat capabilities with AI models through AWS Bedrock. The application supports document retrieval, command-based prompts, and extensible tool integrations via the MCP (Model Control Protocol) architecture.

## About This Project

This project was built following the free online course [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) by Anthropic. The course provides hands-on experience with MCP concepts including:

- Building MCP servers and clients
- Implementing tools, resources, and prompts
- Integrating with AI models through AWS Bedrock
- Creating interactive CLI applications

This implementation demonstrates practical MCP usage patterns and serves as a reference for developers learning the Model Context Protocol.

## AWS Setup Details

This project was developed using:
- **AWS Account**: Janus Dev environment
- **AI Model**: Claude 3.5 Haiku via Amazon Bedrock
- **Authentication**: IAM user with inline permission `bedrock:InvokeModel`

The application connects to AWS Bedrock to access Claude's language model capabilities for the chat interface.

## Prerequisites

- Python 3.9+
- AWS Account with Bedrock access
- AWS CLI configured or AWS credentials

## Setup

### Step 1: Configure AWS and environment variables

1. **Set up AWS credentials** (choose one option):
   - Configure AWS CLI: `aws configure`
   - Set environment variables: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
   - Use IAM roles (if running on EC2)

2. **Configure IAM permissions**:
   - Create an IAM user or use existing credentials
   - Attach the following inline policy to allow Bedrock model invocation:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "bedrock:InvokeModel",
         "Resource": "*"
       }
     ]
   }
   ```

3. **Request model access** in AWS Bedrock console:
   - Go to AWS Bedrock → Model access
   - Request access to Claude 3.5 Haiku model

4. **Configure environment variables**:
   - Copy `.env.example` to `.env`: `cp .env.example .env`
   - Update `.env` with your AWS credentials if not using AWS CLI
   - The default configuration uses:

```
CLAUDE_MODEL=anthropic.claude-3-5-haiku-20241022-v1:0
AWS_REGION=us-west-2
USE_UV=1
```

**Important:** Never commit your `.env` file to version control. It's already excluded in `.gitignore`.

### Step 2: Install dependencies

#### Option 1: Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
pip install uv
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -e .
```

4. Run the project

```bash
uv run main.py
```

#### Option 2: Setup without uv

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install boto3 python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
```

3. Run the project

```bash
python main.py
```

## Usage

### Basic Interaction

Simply type your message and press Enter to chat with the model.

### Document Retrieval

Use the @ symbol followed by a document ID to include document content in your query:

```
> Tell me about @deposition.md
```

### Commands

Use the / prefix to execute commands defined in the MCP server:

```
> /summarize deposition.md
```

Commands will auto-complete when you press Tab.

## Security Notes

- **Never commit your `.env` file** - it contains sensitive credentials
- Configure AWS credentials via AWS CLI or IAM roles when possible
- Keep your AWS access keys secure and rotate them regularly
- The `.env.example` file shows the required environment variables

## Development

### Adding New Documents

Edit the `mcp_server.py` file to add new documents to the `docs` dictionary.

### Implementing MCP Features

To fully implement the MCP features:

1. Complete the TODOs in `mcp_server.py`
2. Implement the missing functionality in `mcp_client.py`

### Linting and Typing Check

There are no lint or type checks implemented.

## Learning Resources

- [Introduction to Model Context Protocol Course](https://anthropic.skilljar.com/introduction-to-model-context-protocol) - Free course by Anthropic
- [MCP Documentation](https://modelcontextprotocol.io/) - Official MCP specification and guides
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/) - AWS Bedrock service documentation

## Contributing

This project serves as a learning example from the Anthropic MCP course. Feel free to:
- Extend functionality with additional MCP features
- Add new tools and resources
- Improve the CLI interface
- Add tests and documentation
