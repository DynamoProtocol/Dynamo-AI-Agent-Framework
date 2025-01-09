It seems there was an issue generating a downloadable link for the file. However, you can create the file manually by following these steps:

1. Copy the Markdown content below.
2. Save it as `Middleware_README.md` in your desired location.

---

### Markdown Content

```markdown
## Middleware for Agent Factory and GOAT API

### Purpose
The middleware bridges the `AgentFactory` smart contract and the GOAT API, enabling off-chain AI agent creation and management. It listens for events emitted by the `AgentFactory` contract and triggers the GOAT API to generate agents. The generated agent details are then finalized on the blockchain.

### File Location
- The middleware script is located in the `middleware/middleware.js` file.

### Prerequisites
1. **Install Dependencies**:
   Ensure the following dependencies are installed:
   ```bash
   npm install ethers axios dotenv
   ```

2. **Configure the `.env` File**:
   Update the `.env` file in the repository with the required configuration:
   ```plaintext
   # Blockchain Configuration
   ETH_RPC_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
   PRIVATE_KEY=your_wallet_private_key
   AGENT_FACTORY_CONTRACT=0xYourAgentFactoryContractAddress

   # GOAT API Configuration
   GOAT_API_URL=https://api.goat-ai.com
   ```

3. **Deploy the AgentFactory Contract**:
   Deploy the `AgentFactory` contract and update the `.env` file with its address.

### Running the Middleware
1. Navigate to the `middleware` directory:
   ```bash
   cd middleware
   ```

2. Run the middleware script:
   ```bash
   node middleware.js
   ```

### Usage
1. **Call the `requestAgentCreation` Function**:
   Call the `requestAgentCreation` function on the `AgentFactory` contract:
   ```solidity
   agentFactory.requestAgentCreation("Agent Metadata");
   ```
   - This emits the `AgentCreationRequested` event, which the middleware listens to.

2. **Middleware Actions**:
   - The middleware triggers the GOAT API using the event metadata.
   - Upon receiving the response, it calls the `finalizeAgentCreation` function on the `AgentFactory` contract to register the agent on the blockchain.

3. **Monitor Logs**:
   - Check the console output for event detections, API responses, and blockchain transactions.

### Notes
- Ensure the wallet specified in the `.env` file has sufficient funds to cover gas fees for finalizing agent creation.
- The middleware requires an active connection to the blockchain and the GOAT API.

### Example Workflow
1. A user triggers `requestAgentCreation` on the `AgentFactory` contract with specific metadata.
2. The middleware:
   - Listens for the emitted `AgentCreationRequested` event.
   - Sends the metadata to the GOAT API for processing.
   - Calls `finalizeAgentCreation` on the blockchain with the generated agent details.

This workflow enables seamless integration between the blockchain and the GOAT API for AI agent management.
```
