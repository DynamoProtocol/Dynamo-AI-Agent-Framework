### **Middleware for Agent Factory and GOAT API**

#### **Purpose**

The middleware acts as a bridge between the **AgentFactory smart contract** and the **GOAT API**. It listens for events emitted by the `AgentFactory` contract, triggers the GOAT API to generate AI agents, and finalizes the agent creation process on the blockchain.

#### **File Location**

The middleware script is located in the `middleware/middleware.js` file.

* * *

### **Prerequisites**

Before running the middleware, ensure the following:

1.  **Install Dependencies**:
    Run the following command to install the required Node.js packages:

    bash

    Copy

    npm install ethers axios dotenv

2.  **Configure the `.env` File**:
    Update the `.env` file in the repository with the required configuration:

    -   `ETH_RPC_URL`: Ethereum RPC endpoint (e.g., Infura or Alchemy).
    -   `PRIVATE_KEY`: Your wallet’s private key (with sufficient funds for gas fees).
    -   `AGENT_FACTORY_CONTRACT`: Address of the deployed `AgentFactory` contract.
    -   `GOAT_API_URL`: URL of the GOAT API.
3.  **Deploy the AgentFactory Contract**:
    -   Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum).
    -   Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.
* * *

### **Running the Middleware**

1.  Navigate to the `middleware` directory:

    bash

    Copy

    cd middleware

2.  Start the middleware script:

    bash

    Copy

    node middleware.js

    The middleware will start listening for `AgentCreationRequested` events emitted by the `AgentFactory` contract.

* * *

### **How It Works**

1.  **Event Listening**:
    -   The middleware listens for the `AgentCreationRequested` event emitted by the `AgentFactory` contract.
    -   When the event is detected, the middleware extracts the `creator` address and `metadata` associated with the agent creation request.
2.  **API Interaction**:
    -   The middleware sends the `metadata` to the GOAT API to generate an AI agent.
    -   The GOAT API returns the agent details, including the `agentAddress` and `agentMetadata`.
3.  **Blockchain Interaction**:
    -   The middleware calls the `finalizeAgentCreation` function on the `AgentFactory` contract to register the new agent on the blockchain.
    -   The agent details are stored in the contract, and the `AgentCreated` event is emitted.
* * *

### **Usage**

1.  **Trigger Agent Creation**:
    -   Interact with the `AgentFactory` contract to initiate the creation of a new agent by calling the `requestAgentCreation` function with the desired metadata.
2.  **Monitor Logs**:
    -   Observe the console output of the middleware for:
        -   Detection of the `AgentCreationRequested` event.
        -   Communication with the GOAT API.
        -   Confirmation of the `finalizeAgentCreation` transaction on the blockchain.
* * *

### **Notes**

-   **Wallet Funds**: Ensure the Ethereum wallet specified in the `.env` file has sufficient funds to cover gas fees for blockchain transactions.
-   **API Connectivity**: Maintain an active internet connection to allow the middleware to interact with both the blockchain and the GOAT API.
-   **Dependency Updates**: Regularly update dependencies to their latest versions to maintain compatibility and security.
* * *

### **Example Workflow**

1.  A user calls the `requestAgentCreation` function on the `AgentFactory` contract with specific metadata.
2.  The middleware:
    -   Listens for the emitted `AgentCreationRequested` event.
    -   Sends the metadata to the GOAT API for processing.
    -   Calls `finalizeAgentCreation` on the blockchain with the generated agent details.
3.  The new agent is registered on the blockchain, and its details are stored in the `AgentFactory` contract.
* * *

### **Troubleshooting**

-   **Connection Issues**:
    -   Verify the RPC URL in `.env` is correct.
    -   Ensure the Ethereum node is accessible and responsive.
-   **API Errors**:
    -   Check the GOAT API logs for errors.
    -   Ensure the API key and URL are correctly configured in `.env`.
-   **Transaction Failures**:
    -   Check your wallet balance for sufficient ETH/ARB to cover gas fees.
    -   Verify the correctness of the `AgentFactory` contract address.
