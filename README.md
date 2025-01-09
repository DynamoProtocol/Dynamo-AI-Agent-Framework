
# Dynamo Advanced Crypto Agent Framework

This framework enables the deployment of AI-driven agents targeting Liquid Staking Tokens (LST), Real World Assets (RWA), and DeFi use cases. Built on the GOAT toolkit, it supports Ethereum mainnet, Arbitrum, and customizable logic for staking, bridging, and liquidity provisioning.

## Features
- **Staking APY Monitoring**: Automatically stake tokens based on real-time APY.
- **Portfolio Analysis**: Leverage OpenAI to suggest optimal strategies.
- **Liquidity Provisioning**: Automate liquidity provision in DeFi pools.

## Installation

### Prerequisites
- Python 3.8+
- Node.js (if using the GOAT interface)
- Docker (optional for containerized deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd advanced_crypto_agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Copy `configs/.env.example` to `configs/.env` and update with your details.

## Usage

Run the agent:
```bash
python src/lst_agent.py
```

## Documentation

See [docs](./docs/index.md) for detailed guides.

## Contributing
Pull requests are welcome. For major changes, please open an issue to discuss what you'd like to change.
