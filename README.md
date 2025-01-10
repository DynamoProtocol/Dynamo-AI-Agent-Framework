# Dynamo AI Agent Framework

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#dynamo-ai-agent-framework)

The Dynamo AI Agent Framework is a cutting-edge platform designed to deploy AI-driven agents for automating tasks in decentralized finance (DeFi) ecosystems. It supports Ethereum and Arbitrum networks, offering flexibility and scalability for users. Key features include staking APY monitoring, portfolio analysis, and liquidity provisioning.

## Features

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#features)

### Staking APY Monitoring:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#staking-apy-monitoring)

-   Automates token staking based on real-time APY data.
-   Supports Ethereum and Arbitrum networks.

### Portfolio Analysis:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#portfolio-analysis)

-   Utilizes AI (via DeepSeek) to provide investment strategy recommendations.
-   Integrates with DeFi protocols for real-time data.

### Liquidity Provisioning:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#liquidity-provisioning)

-   Automates liquidity provision in DeFi pools.
-   Optimizes returns by monitoring market conditions.

## Installation

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#installation)

Follow these steps to set up the Dynamo AI Agent Framework:

### 1\. Request $DYNAMO Tokens

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#1-request-dynamo-tokens)

-   Join the Dynamo Discord server.
-   Request $DYNAMO tokens for your desired network (Ethereum or Arbitrum).
-   Once you receive the tokens, configure the framework to use the appropriate network.

### 2\. Clone the Repository:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#2-clone-the-repository)

```shell
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```

### 3\. Install Dependencies:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#3-install-dependencies)

-   Install Python dependencies:

bash

Copy

pip install -r requirements.txt

-   Install Node.js dependencies (for middleware):

bash

Copy

cd middleware npm install cd ..

### 4\. Configure Environment Variables:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#4-configure-environment-variables)

-   Copy the example `.env` file:

bash

Copy

cp configs/.env.example configs/.env

-   Edit `configs/.env` and fill in the required values:
    -   RPC URLs for Ethereum and Arbitrum.
    -   Wallet private key.
    -   Contract addresses for `AgentFactory` and $DYNAMO tokens.
    -   API keys for GOAT and DeepSeek.

### 5\. Deploy the AgentFactory Contract:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#5-deploy-the-agentfactory-contract)

-   Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum).
-   Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

### 6\. Run the Middleware:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#6-run-the-middleware)

-   Navigate to the middleware directory:

bash

Copy

cd middleware

-   Start the middleware script:

bash

Copy

node middleware.js

### 7\. Launch an AI Agent:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#7-launch-an-ai-agent)

-   Use the `quick_start.py` script to launch an AI agent:

bash

Copy

python examples/quick\_start.py

## Usage

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#usage)

### Staking APY Monitoring:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#staking-apy-monitoring-1)

-   Automate token staking based on real-time APY data.

Example:

python

Copy

tx\_hash = agent.perform\_stake({"token\_address": "0xTokenAddress", "amount": 1.0})

### Portfolio Analysis:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#portfolio-analysis-1)

-   Analyze portfolios and get investment recommendations.

Example:

python

Copy

recommendations = agent.analyze\_portfolio({"tokens": \["ETH", "DAI"\], "values": \[1.2, 350\]})

### Liquidity Provisioning:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#liquidity-provisioning-1)

-   Automate liquidity provision in DeFi pools.

Example:

python

Copy

tx\_hash = agent.provide\_liquidity({"pool\_address": "0xPoolAddress", "amount": 1000})

## Troubleshooting

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#troubleshooting)

### Connection Issues:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#connection-issues)

-   Verify the RPC URL in `.env` is correct.
-   Ensure your Ethereum node is accessible.

### API Errors:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#api-errors)

-   Check the GOAT and DeepSeek API logs for errors.
-   Ensure the API keys in `.env` are valid.

### Transaction Failures:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#transaction-failures)

-   Check your wallet balance for sufficient ETH/ARB to cover gas fees.
-   Verify the correctness of the `AgentFactory` contract address.

## Roadmap

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#roadmap)

-   Add support for additional blockchain networks (e.g., Polygon, Binance Smart Chain).
-   Implement advanced portfolio analysis features.
-   Add a user interface for managing AI agents.
-   Integrate with more DeFi protocols for staking and liquidity provisioning.

## Contributing

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#contributing)

We welcome contributions to the Dynamo AI Agent Framework! Follow these steps to contribute:

### Fork the Repository:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#fork-the-repository)

-   Fork the repository on GitHub.

### Create a New Branch:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#create-a-new-branch)

-   Create a new branch for your feature or bugfix:

bash

Copy

git checkout -b feature/your-feature-name

### Submit a Pull Request:

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#submit-a-pull-request)

-   Push your changes to the branch and submit a pull request with a detailed description of your changes.

## License

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#license)

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

[](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework/blob/main/README.md#support)

For support or questions, please contact the development team or open an issue on the GitHub repository.
