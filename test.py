import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="us.anthropic.claude-sonnet-4-6",
    messages=[{"role": "user", "content": [{"text": "Hello"}]}],
)

print(response["output"]["message"]["content"][0]["text"])
#!/usr/bin/env python
# -*- coding:utf-8 -*-
