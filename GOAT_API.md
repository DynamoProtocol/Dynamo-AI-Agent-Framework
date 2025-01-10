# GOAT API Integration

## Overview
The middleware interacts with the GOAT API to generate AI agents. This document explains how to set up and use the GOAT API.

## Obtaining an API Key
1. Sign up for an account on the GOAT platform.
2. Navigate to the API section in your account settings.
3. Generate an API key and add it to your `.env` file:
```plaintext
GOAT_API_KEY=<Your API Key>
```


# Endpoints

## Generate Agent

**URL:** POST /generateAgent

### Request Body:

```json
{
  "metadata": "string"
}
```

### Response:

```json
{
  "agentAddress": "string",
  "agentMetadata": "string"
}
```

### Example

#### Request

```bash
curl -X POST https://api.goat-ai.com/generateAgent \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"metadata": "Example Metadata"}'
```

#### Response

```json
{
  "agentAddress": "0xAgentAddress",
  "agentMetadata": "Example Metadata"
}
```

# Troubleshooting

- **API Errors**: Check the GOAT API logs for errors.
- **Invalid API Key**: Ensure the API key in `.env` is correct.
- **Network Issues**: Verify your internet connection and the GOAT API URL.
