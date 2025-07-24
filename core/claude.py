import boto3
import json
from typing import Dict, List, Any


class Claude:
    def __init__(self, model: str, region: str = "us-east-1"):
        self.client = boto3.client("bedrock-runtime", region_name=region)
        self.model = model

    def add_user_message(self, messages: list, message):
        user_message = {
            "role": "user",
            "content": message.get("content") if isinstance(message, dict) else str(message),
        }
        messages.append(user_message)

    def add_assistant_message(self, messages: list, message):
        content = message.get("content") if isinstance(message, dict) else str(message)
        assistant_message = {
            "role": "assistant", 
            "content": content,
        }
        messages.append(assistant_message)

    def text_from_message(self, message):
        if isinstance(message, dict):
            if "content" in message:
                content = message["content"]
                if isinstance(content, list):
                    return "\n".join([block.get("text", "") for block in content if block.get("type") == "text"])
                return str(content)
        return str(message)

    def chat(
        self,
        messages,
        system=None,
        temperature=1.0,
        stop_sequences=[],
        tools=None,
        thinking=False,
        thinking_budget=1024,
    ):
        # Convert messages to Bedrock format
        bedrock_messages = []
        for msg in messages:
            bedrock_messages.append({
                "role": msg["role"],
                "content": [{"type": "text", "text": str(msg["content"])}]
            })

        # Build the request body for Bedrock
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 8000,
            "messages": bedrock_messages,
            "temperature": temperature,
        }

        if system:
            body["system"] = [{"text": system}]

        if stop_sequences:
            body["stop_sequences"] = stop_sequences

        if tools:
            body["tools"] = tools

        # Make the request to Bedrock
        response = self.client.invoke_model(
            modelId=self.model,
            body=json.dumps(body)
        )

        # Parse the response
        response_body = json.loads(response["body"].read())
        
        # Return in a format compatible with the existing code
        return {
            "content": response_body.get("content", []),
            "stop_reason": response_body.get("stop_reason", "end_turn"),
            "usage": response_body.get("usage", {})
        }
