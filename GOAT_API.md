# GOAT API Integration

## Overview
The middleware interacts with the GOAT API to generate AI agents. This document explains how to set up and use the GOAT API.

## Endpoints
- **Generate Agent**: `POST /generateAgent`
  - Request Body:
    ```json
    {
      "metadata": "string"
    }
    ```
  - Response:
    ```json
    {
      "agentAddress": "string",
      "agentMetadata": "string"
    }
    ```

## API Key
To use the GOAT API, obtain an API key from the GOAT platform and add it to your `.env` file:

```plaintext
GOAT_API_KEY=<Your API Key>
