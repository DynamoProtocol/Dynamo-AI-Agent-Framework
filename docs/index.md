
# Dynamo Advanced Crypto Agent Framework Documentation

## Overview

The Dynamo AI Agent Framework is a powerful tool designed to deploy AI-driven agents for automating tasks in decentralized finance (DeFi) ecosystems. It supports Ethereum and Arbitrum networks, providing flexibility and scalability for users. Key functionalities include:

- **Staking APY Monitoring**: Automates token staking based on real-time APY data.
- **Portfolio Analysis**: Utilizes AI (via DeepSeek) to provide investment strategy recommendations.
- **Liquidity Provisioning**: Automates liquidity provision in DeFi pools.

## Getting Started

Follow these steps to set up and use the Dynamo AI Agent Framework:

### 1. Installation

#### Clone the Repository:

```bash
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```

#### Install Dependencies:

- Install Python dependencies:

```bash
pip install -r requirements.txt
```

- Install Node.js dependencies (for middleware):

```bash
cd middleware
npm install
cd ..
```

#### Configure Environment Variables:

- Copy the example `.env` file:

```bash
cp configs/.env.example configs/.env
```

- Edit `configs/.env` and fill in the required values:
  - RPC URLs for Ethereum and Arbitrum.
  - Wallet private key.
  - Contract addresses for `AgentFactory` and `$DYNAMO` tokens.
  - API keys for GOAT and DeepSeek.

#### Deploy the AgentFactory Contract:

- Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum).
- Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

To deploy the `AgentFactory` contract, follow these steps:

1.  **Install Hardhat**:
    Open your terminal and run the following command to install Hardhat:

    bash

    Copy

    npm install --save-dev hardhat

2.  **Compile the Contract**:
    Compile the `AgentFactory.sol` contract using Hardhat:

    bash

    Copy

    npx hardhat compile

3.  **Create a Deployment Script**:
    Create a new file named `deploy.js` in the `scripts` folder and add the following code:

    javascript

    Copy

    const hre \= require("hardhat");

    async function main() {
        const \[deployer\] \= await hre.ethers.getSigners();
        console.log("Deploying contracts with the account:", deployer.address);

        const AgentFactory \= await hre.ethers.getContractFactory("AgentFactory");
        const agentFactory \= await AgentFactory.deploy("0xDynamoTokenAddress", 1000000000000000000);

        await agentFactory.deployed();
        console.log("AgentFactory deployed to:", agentFactory.address);
    }

    main().catch((error) \=> {
        console.error(error);
        process.exit(1);
    });

4.  **Run the Deployment Script**:
    Deploy the contract to your desired network (e.g., Ethereum or Arbitrum) using Hardhat:

    bash

    Copy

    npx hardhat run scripts/deploy.js \--network <network\_name\>

5.  **Update `.env` File**:
    After deployment, update the `AGENT_FACTORY_CONTRACT` variable in your `.env` file with the deployed contract address:

    plaintext

    Copy

    AGENT\_FACTORY\_CONTRACT=0xYourDeployedContractAddress

* * *

### **Example Deployment to Ethereum Mainnet**

1.  Ensure your `.env` file contains the correct Ethereum RPC URL and private key.
2.  Run the deployment script:

    bash

    Copy

    npx hardhat run scripts/deploy.js \--network mainnet

### **Example Deployment to Arbitrum Testnet**

1.  Ensure your `.env` file contains the correct Arbitrum RPC URL and private key.
2.  Run the deployment script:

    bash

    Copy

    npx hardhat run scripts/deploy.js \--network arbitrum\_testnet

* * *

### **Notes**

-   Replace `0xDynamoTokenAddress` with the actual address of the $DYNAMO token contract.
-   Ensure your wallet has sufficient funds (ETH or ARB) to cover gas fees for deployment.
-   Use the appropriate network configuration in your `hardhat.config.js` file.


### 2. Running the Framework

#### Start the Middleware:

- Navigate to the middleware directory:

```bash
cd middleware
```

- Run the middleware script:

```bash
node middleware.js
```

The middleware will listen for `AgentCreationRequested` events and interact with the GOAT API.

#### Launch an AI Agent:

- Use the `quick_start.py` script to launch an AI agent:

```bash
python examples/quick_start.py
```

## Key Features

### Staking APY Monitoring:

- Automates staking of tokens based on real-time APY data.
- Supports Ethereum and Arbitrum networks.

### Portfolio Analysis:

- Uses DeepSeek AI to analyze portfolios and provide investment recommendations.
- Integrates with DeFi protocols for real-time data.

### Liquidity Provisioning:

- Automates liquidity provision in DeFi pools.
- Optimizes returns by monitoring market conditions.

## API References

The framework provides APIs for the following functionalities:

### Token Balances:

- Fetch token balances for a given address.

Example:

```python
balances = agent.get_balances("0xUserAddress")
```

### Staking APY:

- Automate token staking based on real-time APY data.

Example:

```python
tx_hash = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
```

### Liquidity Provisioning:

- Automate liquidity provision in DeFi pools.

Example:

```python
tx_hash = agent.provide_liquidity({"pool_address": "0xPoolAddress", "amount": 1000})
```

## Troubleshooting

### Connection Issues:

- Verify the RPC URL in `.env` is correct.
- Ensure your Ethereum node is accessible.

### API Errors:

- Check the GOAT and DeepSeek API logs for errors.
- Ensure the API keys in `.env` are valid.

### Transaction Failures:

- Check your wallet balance for sufficient ETH/ARB to cover gas fees.
- Verify the correctness of the `AgentFactory` contract address.

## Contributing

Contributions to the Dynamo AI Agent Framework are welcome! Follow these steps to contribute:

### Fork the Repository:

- Fork the repository on GitHub.

### Create a New Branch:

- Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

### Submit a Pull Request:

- Push your changes to the branch and submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For support or questions, please contact the development team or open an issue on the GitHub repository.

