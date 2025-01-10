# Dynamo AI Agent Framework

The Dynamo AI Agent Framework is a cutting-edge platform designed to deploy AI-driven agents for automating tasks in decentralized finance (DeFi) ecosystems. It supports Ethereum and Arbitrum networks, offering flexibility and scalability for users. Key features include staking APY monitoring, portfolio analysis, and liquidity provisioning.

## Features

### Staking APY Monitoring:
- Automates token staking based on real-time APY data.
- Supports Ethereum and Arbitrum networks.

### Portfolio Analysis:
- Utilizes AI (via DeepSeek) to provide investment strategy recommendations.
- Integrates with DeFi protocols for real-time data.

### Liquidity Provisioning:
- Automates liquidity provision in DeFi pools.
- Optimizes returns by monitoring market conditions.

## Installation

### 1. Request $DYNAMO Tokens
- Join the Dynamo Discord server.
- Request $DYNAMO tokens for your desired network (Ethereum or Arbitrum).
- Once you receive the tokens, configure the framework to use the appropriate network.

### 2. Clone the Repository:
```bash
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```


# Setup and Usage Guide

## 3. Install Dependencies

### Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Install Node.js dependencies (for middleware):

```bash
cd middleware
npm install
cd ..
```

## 4. Configure Environment Variables

- Copy the example `.env` file:

```bash
cp configs/.env.example configs/.env
```

- Edit `configs/.env` and fill in the required values:
  - RPC URLs for Ethereum and Arbitrum.
  - Wallet private key.
  - Contract addresses for `AgentFactory` and `$DYNAMO` tokens.
  - API keys for GOAT and DeepSeek.

## 5. Deploy the AgentFactory Contract

- Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum).
- Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

## 6. Run the Middleware

- Navigate to the middleware directory:

```bash
cd middleware
```

- Start the middleware script:

```bash
node middleware.js
```

## 7. Launch an AI Agent

- Use the `quick_start.py` script to launch an AI agent:

```bash
python examples/quick_start.py
```

# Usage

## Staking APY Monitoring

- Automate token staking based on real-time APY data.

Example:

```python
tx_hash = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
```

## Portfolio Analysis

- Analyze portfolios and get investment recommendations.

Example:

```python
recommendations = agent.analyze_portfolio({"tokens": ["ETH", "DAI"], "values": [1.2, 350]})
```

## Liquidity Provisioning

- Automate liquidity provision in DeFi pools.

Example:

```python
tx_hash = agent.provide_liquidity({"pool_address": "0xPoolAddress", "amount": 1000})
```

# Advanced Features

## Withdraw $DYNAMO Tokens

- The owner can withdraw `$DYNAMO` tokens from the AgentFactory contract.

Example:

```python
tx_hash = agent_factory.withdraw_dynamo(amount)
```

## Set Agent Creation Cost

- The owner can update the cost of creating an agent.

Example:

```python
tx_hash = agent_factory.set_agent_creation_cost(new_cost)
```

# Troubleshooting

- **Connection Issues**: Verify the RPC URL in `.env` is correct.
- **API Errors**: Check the GOAT and DeepSeek API logs for errors.
- **Transaction Failures**: Ensure your wallet has sufficient ETH/ARB for gas fees.

# Contributing

- Fork the repository and create a new branch for your feature or bugfix.
- Submit a pull request with a detailed description of your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Support

For support or questions, contact the development team or open an issue on GitHub.

