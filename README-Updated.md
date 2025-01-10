# Dynamo AI Agent Framework

The **Dynamo AI Agent Framework** is a cutting-edge platform designed to deploy AI-driven agents for automating tasks in decentralized finance (DeFi) ecosystems. It supports **Ethereum** and **Arbitrum** networks, offering flexibility and scalability for users. Key features include **staking APY monitoring**, **portfolio analysis**, and **liquidity provisioning**.

---

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

---

## Installation

Follow these steps to set up the Dynamo AI Agent Framework:

### Prerequisites
- Python 3.8 or higher.
- Node.js (for middleware functionality).
- Docker (optional, for containerized deployment).

### Steps

#### 1. Clone the Repository:
```bash
git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
cd Dynamo-AI-Agent-Framework
```

#### 2\. Install Dependencies:

-   Install Python dependencies:

    bash

    Copy

    pip install \-r requirements.txt

-   Install Node.js dependencies (for middleware):

    bash

    Copy

    cd middleware
    npm install
    cd ..

#### 3\. Configure Environment Variables:

-   Copy the example `.env` file:

    bash

    Copy

    cp configs/.env.example configs/.env

-   Edit `configs/.env` and fill in the required values:
    -   **RPC URLs** for Ethereum and Arbitrum.
    -   **Wallet private key**.
    -   **Contract addresses** for `AgentFactory` and $DYNAMO tokens.
    -   **API keys** for GOAT and DeepSeek.

#### 4\. Deploy the AgentFactory Contract:

-   Compile and deploy the `AgentFactory.sol` contract to your desired network (Ethereum or Arbitrum):

    bash

    Copy

    npx hardhat run scripts/deploy.js \--network mainnet  \# For Ethereum
    npx hardhat run scripts/deploy.js \--network arbitrum  \# For Arbitrum

-   Update the `AGENT_FACTORY_CONTRACT` variable in `.env` with the deployed contract address.

#### 5\. Run the Middleware:

-   Navigate to the middleware directory:

    bash

    Copy

    cd middleware

-   Start the middleware script:

    bash

    Copy

    node middleware.js

#### 6\. Launch an AI Agent:

-   Use the `quick_start.py` script to launch an AI agent:

    bash

    Copy

    python examples/quick\_start.py

* * *

## Usage

### Staking APY Monitoring:

-   Automate token staking based on real-time APY data.

Example:

python

Copy

tx\_hash \= agent.perform\_stake({"token\_address": "0xTokenAddress", "amount": 1.0})

### Portfolio Analysis:

-   Analyze portfolios and get investment recommendations.

Example:

python

Copy

recommendations \= agent.analyze\_portfolio({"tokens": \["ETH", "DAI"\], "values": \[1.2, 350\]})

### Liquidity Provisioning:

-   Automate liquidity provision in DeFi pools.

Example:

python

Copy

tx\_hash \= agent.provide\_liquidity({"pool\_address": "0xPoolAddress", "amount": 1000})

* * *

## Cross-Chain Support

The $DYNAMO token is deployed on **Ethereum mainnet** and bridged to **Arbitrum**. The framework supports both networks:

-   **Ethereum**: Use the Ethereum RPC URL and token address.
-   **Arbitrum**: Use the Arbitrum RPC URL and bridged token address.
* * *

## Running Tests

To run the unit tests:

bash

Copy

python \-m unittest tests/test\_agent.py

* * *

## Contributing

We welcome contributions to the Dynamo AI Agent Framework! Follow these steps to contribute:

### 1\. Fork the Repository:

-   Fork the repository on GitHub.

### 2\. Create a New Branch:

-   Create a new branch for your feature or bugfix:

    bash

    Copy

    git checkout \-b feature/your-feature-name

### 3\. Submit a Pull Request:

-   Push your changes to the branch and submit a pull request with a detailed description of your changes.

For more details, see [CONTRIBUTING.md](https://chat.deepseek.com/a/chat/s/CONTRIBUTING.md).

* * *

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE) file for details.

* * *

## Support

For support or questions, please contact the development team or open an issue on the GitHub repository.
