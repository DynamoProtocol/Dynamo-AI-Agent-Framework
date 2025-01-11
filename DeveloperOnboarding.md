
# Step-by-Step Instructions for New Developers

## 1. Prerequisites

Before starting, ensure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Git**
- **MetaMask** (or another Ethereum wallet)
- **Hardhat** (for local testing and deployment)

## 2. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```

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

## 4. Set Up Environment Variables

- Copy the example `.env` file:

```bash
cp configs/.env.example configs/.env
```

- Open `configs/.env` in a text editor and fill in the required values:
  - **ETH_RPC_URL**: Ethereum RPC endpoint (e.g., Infura or Alchemy).
  - **ARBITRUM_RPC_URL**: Arbitrum RPC endpoint (e.g., Infura or Alchemy).
  - **PRIVATE_KEY**: Your wallet’s private key (for deploying contracts and signing transactions).
  - **AGENT_FACTORY_CONTRACT**: Address of the deployed AgentFactory contract (leave blank for now).
  - **GOAT_API_KEY**: API key for the GOAT API (sign up at the GOAT platform to obtain one).
  - **DYNAMO_TOKEN_ADDRESS**: Address of the `$DYNAMO` token on your chosen network (Ethereum or Arbitrum).

## 5. Request $DYNAMO Tokens

1. Join the Dynamo Discord server.
2. Request `$DYNAMO` tokens for your desired network (Ethereum or Arbitrum).
3. Once you receive the tokens, ensure your wallet has a small amount of ETH/ARB for gas fees.

## 6. Deploy the AgentFactory Contract

- Compile the `AgentFactory.sol` contract:

```bash
npx hardhat compile
```

- Deploy the contract to your desired network (e.g., Ethereum or Arbitrum):

```bash
npx hardhat run scripts/deploy.js --network mainnet
```

Replace `mainnet` with `arbitrum_testnet` or `localhost` if deploying to Arbitrum or a local Hardhat network.

- Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

## 7. Run the Middleware

- Navigate to the middleware directory:

```bash
cd middleware
```

- Start the middleware script:

```bash
node middleware.js
```

The middleware will listen for `AgentCreationRequested` events and interact with the GOAT API.

## 8. Launch an AI Agent

- Use the `quick_start.py` script to launch an AI agent:

```bash
python examples/quick_start.py
```

### The script will:

1. Request agent creation on the blockchain.
2. Trigger the middleware to interact with the GOAT API.
3. Finalize the agent creation process.

## 9. Interact with the AI Agent

Once the agent is created, you can use it to:

### Monitor Staking APY:

```python
tx_hash = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
```

### Analyze Portfolio:

```python
recommendations = agent.analyze_portfolio({"tokens": ["ETH", "DAI"], "values": [1.2, 350]})
```

### Provide Liquidity:

```python
tx_hash = agent.provide_liquidity({"pool_address": "0xPoolAddress", "amount": 1000})
```

## 10. Test the Framework

- Run the provided tests:

```bash
python -m unittest discover tests
```

- Add more tests as needed to cover additional functionalities.

## 11. Troubleshooting

- **Connection Issues**: Verify the RPC URL in `.env` is correct.
- **API Errors**: Check the GOAT and DeepSeek API logs for errors.
- **Transaction Failures**: Ensure your wallet has sufficient ETH/ARB for gas fees.

## 12. Contribute to the Project

- Fork the repository and create a new branch:

```bash
git checkout -b feature/your-feature-name
```

- Make your changes and submit a pull request with a detailed description.

## Additional Resources

- **Discord Server**: Join the Dynamo Discord for support and token requests.
- **API Documentation**:
  - [GOAT API Documentation](#)
  - [DeepSeek API Documentation](#) (Add this if available)
- **Hardhat Documentation**: [Hardhat Docs](https://hardhat.org/docs)
