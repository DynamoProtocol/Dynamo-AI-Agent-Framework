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
   - Interact with the `AgentFactory` contract to initiate the creation of a new agent by calling the `requestAgentCreation` function with the desired metadata:
     ```solidity
     agentFactory.requestAgentCreation("Agent Metadata");
     ```
   - This action emits the `AgentCreationRequested` event, which the middleware listens for to proceed with agent creation.


2. **Middleware Actions**:
   - Upon detecting the `AgentCreationRequested` event, the middleware:
     - Sends the provided metadata to the GOAT API to generate the AI agent.
     - Receives the agent details from the GOAT API.
     - Calls the `finalizeAgentCreation` function on the `AgentFactory` contract to register the new agent on the blockchain.

3. **Monitor Logs**:
   - Observe the console output of the middleware for:
     - Detection of the `AgentCreationRequested` event.
     - Communication with the GOAT API.
     - Confirmation of the `finalizeAgentCreation` transaction on the blockchain.

### Notes
- Ensure the Ethereum wallet specified in the `.env` file has sufficient funds to cover gas fees for blockchain transactions.
- Maintain an active internet connection to allow the middleware to interact with both the blockchain and the GOAT API.
- Regularly update dependencies to their latest versions to maintain compatibility and security.

### Example Workflow
1. A user triggers `requestAgentCreation` on the `AgentFactory` contract with specific metadata.
2. The middleware:
   - Listens for the emitted `AgentCreationRequested` event.
   - Sends the metadata to the GOAT API for processing.
   - Calls `finalizeAgentCreation` on the blockchain with the generated agent details.

This workflow enables seamless integration between the blockchain and the GOAT API for AI agent management.
```
