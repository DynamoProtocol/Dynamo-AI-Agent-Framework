# Dynamo Advanced Crypto Agent Framework Documentation

## Overview

The Dynamo AI Agent Framework is a powerful tool designed to deploy AI-driven agents for automating tasks in decentralized finance (DeFi) ecosystems. It supports Ethereum and Arbitrum networks, providing flexibility and scalability for users. Key functionalities include:

- **Staking APY Monitoring**: Automates token staking based on real-time APY data.
- **Portfolio Analysis**: Utilizes AI (via DeepSeek) to provide investment strategy recommendations.
- **Liquidity Provisioning**: Automates liquidity provision in DeFi pools.

## Getting Started

Follow these steps to set up and use the Dynamo AI Agent Framework:

### 1. Request $DYNAMO Tokens

- Join the Dynamo Discord server.
- Request $DYNAMO tokens for your desired network (Ethereum or Arbitrum).
- Once you receive the tokens, configure the framework to use the appropriate network.

### 2. Installation

#### Clone the Repository:

```bash
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```


# Install Dependencies

## Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Install Node.js dependencies (for middleware):

```bash
cd middleware
npm install
cd ..
```

## Configure Environment Variables:

- Copy the example `.env` file:

```bash
cp configs/.env.example configs/.env
```

- Edit `configs/.env` and fill in the required values:
  - RPC URLs for Ethereum and Arbitrum.
  - Wallet private key.
  - Contract addresses for `AgentFactory` and `$DYNAMO` tokens.
  - API keys for GOAT and DeepSeek.

## Deploy the AgentFactory Contract:

- Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum).
- Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

# Running the Framework

## Start the Middleware:

- Navigate to the middleware directory:

```bash
cd middleware
```

- Run the middleware script:

```bash
node middleware.js
```

## Launch an AI Agent:

- Use the `quick_start.py` script to launch an AI agent:

```bash
python examples/quick_start.py
```

# Key Features

## Staking APY Monitoring:

- Automates staking of tokens based on real-time APY data.
- Supports Ethereum and Arbitrum networks.

## Portfolio Analysis:

- Uses DeepSeek AI to analyze portfolios and provide investment recommendations.
- Integrates with DeFi protocols for real-time data.

## Liquidity Provisioning:

- Automates liquidity provision in DeFi pools.
- Optimizes returns by monitoring market conditions.

# API References

The framework provides APIs for the following functionalities:

## Token Balances:

- Fetch token balances for a given address.

Example:

```python
balances = agent.get_balances("0xUserAddress")
```

## Staking APY:

- Automate token staking based on real-time APY data.

Example:

```python
tx_hash = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
```

## Liquidity Provisioning:

- Automate liquidity provision in DeFi pools.

Example:

```python
tx_hash = agent.provide_liquidity({"pool_address": "0xPoolAddress", "amount": 1000})
```

# Troubleshooting

## Connection Issues:

- Verify the RPC URL in `.env` is correct.
- Ensure your Ethereum node is accessible.

## API Errors:

- Check the GOAT and DeepSeek API logs for errors.
- Ensure the API keys in `.env` are valid.

## Transaction Failures:

- Check your wallet balance for sufficient ETH/ARB to cover gas fees.
- Verify the correctness of the `AgentFactory` contract address.

# Contributing

Contributions to the Dynamo AI Agent Framework are welcome! Follow these steps to contribute:

## Fork the Repository:

- Fork the repository on GitHub.

## Create a New Branch:

- Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

## Submit a Pull Request:

- Push your changes to the branch and submit a pull request with a detailed description of your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Support

For support or questions, please contact the development team or open an issue on the GitHub repository.
