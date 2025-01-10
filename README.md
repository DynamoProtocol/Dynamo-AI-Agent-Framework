
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

Follow these steps to set up the Dynamo AI Agent Framework:

### Prerequisites

- Python 3.8 or higher.
- Node.js (for middleware functionality).
- Docker (optional, for containerized deployment).

### Steps

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

#### Run the Middleware:

- Navigate to the middleware directory:

```bash
cd middleware
```

- Start the middleware script:

```bash
node middleware.js
```

#### Launch an AI Agent:

- Use the `quick_start.py` script to launch an AI agent:

```bash
python examples/quick_start.py
```

## Usage

### Staking APY Monitoring:

- Automate token staking based on real-time APY data.

Example:

```python
tx_hash = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
```

### Portfolio Analysis:

- Analyze portfolios and get investment recommendations.

Example:

```python
recommendations = agent.analyze_portfolio({"tokens": ["ETH", "DAI"], "values": [1.2, 350]})
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

We welcome contributions to the Dynamo AI Agent Framework! Follow these steps to contribute:

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
