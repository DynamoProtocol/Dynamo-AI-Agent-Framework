# Middleware for Agent Factory and GOAT API

## Purpose
The middleware acts as a bridge between the AgentFactory smart contract and the GOAT API. It listens for events emitted by the AgentFactory contract, triggers the GOAT API to generate AI agents, and finalizes the agent creation process on the blockchain.
## Middleware Workflow


```plaintext
+-------------------+       +-------------------+       +-------------------+
| AgentFactory      |       | Middleware        |       | GOAT API          |
| Smart Contract    |       | (middleware.js)   |       |                   |
+-------------------+       +-------------------+       +-------------------+
        |                           |                           |
        | AgentCreationRequested    |                           |
        |-------------------------->|                           |
        |                           | Generate Agent            |
        |                           |-------------------------->|
        |                           |                           |
        |                           | Agent Data                |
        |                           |<--------------------------|
        | FinalizeAgentCreation     |                           |
        |<--------------------------|                           |
```


## Prerequisites
1. Install dependencies:
```bash
npm install ethers axios dotenv
```

# Middleware Setup and Workflow

## Configure the .env File

- Set the required values in the `.env` file:
  - **ETH_RPC_URL**: Ethereum RPC URL (e.g., Infura or Alchemy).
  - **PRIVATE_KEY**: Your wallet private key.
  - **AGENT_FACTORY_CONTRACT**: Address of the deployed AgentFactory contract.

## Running the Middleware

### Navigate to the middleware directory:

```bash
cd middleware
```

### Start the middleware script:

```bash
node middleware.js
```

## Workflow

1. The middleware listens for `AgentCreationRequested` events.
2. It sends the metadata to the GOAT API to generate an AI agent.
3. It finalizes the agent creation on the blockchain by calling `finalizeAgentCreation`.

## Example Logs

```plaintext
💡 Middleware is listening for AgentCreationRequested events...
🔔 Agent creation requested by 0xCreatorAddress with metadata: Example Metadata
✅ Agent creation finalized on blockchain: 0xAgentAddress
```

## Troubleshooting

- **Connection Issues**: Verify the RPC URL in `.env` is correct.
- **API Errors**: Check the GOAT API logs for errors.
- **Transaction Failures**: Ensure your wallet has sufficient ETH/ARB for gas fees.

