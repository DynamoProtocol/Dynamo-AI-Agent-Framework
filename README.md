# Dynamo AI Agent Framework

The Dynamo AI Agent Framework enables the deployment of AI-driven agents in decentralized finance (DeFi) ecosystems. It supports Ethereum and Arbitrum networks for enhanced flexibility and scalability.

## Features
- **Staking APY Monitoring**: Automates token staking based on real-time APY data.
- **Portfolio Analysis**: Utilizes OpenAI for investment strategy recommendations.
- **Liquidity Provisioning**: Automates liquidity provision in DeFi pools.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js (if using the GOAT interface)
- Docker (optional for containerized deployment)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework.git
   cd Dynamo-AI-Agent-Framework
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variables

   The framework requires a `.env` file to store configuration details for interacting with blockchain networks and deployed contracts. Follow these steps:

   - **Create the `.env` File**:
     ```bash
     cp configs/.env.example configs/.env
     ```

   - **Edit the `.env` File**:
     Open the `.env` file in a text editor and replace the placeholder values with your actual configuration details:

     - **Ethereum RPC URL**:
       - Obtain an RPC URL from a provider like [Infura](https://infura.io) or [Alchemy](https://www.alchemy.com).
       - Replace `YOUR_PROJECT_ID` with your actual project ID:
         ```plaintext
         ETH_RPC_URL=https://mainnet.infura.io/v3/YOUR_PROJECT_ID
         ```

     - **Arbitrum RPC URL**:
       - Similar to Ethereum, get an RPC URL for Arbitrum from your provider.
       - Replace `YOUR_PROJECT_ID` accordingly:
         ```plaintext
         ARBITRUM_RPC_URL=https://arbitrum.infura.io/v3/YOUR_PROJECT_ID
         ```

     - **Wallet Private Key**:
       - Use the private key of your wallet that holds sufficient funds for transaction fees.
       - **Important**: Keep this key secure and do not share it publicly:
         ```plaintext
         PRIVATE_KEY=your_private_key_here
         ```

     - **Dynamo Token Contract Addresses**:
       - These are the deployed contract addresses for the Dynamo token:
         ```plaintext
         DYNAMO_TOKEN_ADDRESS=0xBfFAF03F35D75417091f0f42de3EC6809ffA51eB
         ARBITRUM_TOKEN_ADDRESS=0x4d91c0cdf64e995e4391254f0bc19a8a128765b9
         ```

     - **Agent Factory Contract Address**:
       - Replace with the actual deployed Agent Factory contract address:
         ```plaintext
         AGENT_FACTORY_CONTRACT=0xYourAgentFactoryContractAddress
         ```

     - **AI Agent Token Configuration**:
       - Define the name and symbol for your AI agent token:
         ```plaintext
         AGENT_TOKEN_NAME=YourAgentTokenName
         AGENT_TOKEN_SYMBOL=YourAgentTokenSymbol
         ```

     - **Default Network**:
       - Set the default blockchain network (`ethereum` or `arbitrum`):
         ```plaintext
         DEFAULT_NETWORK=ethereum
         ```

   - **Save the `.env` File**:
     After entering all the necessary information, save the `.env` file.

   - **Proceed with Deployment**:
     With the environment variables configured, continue with the deployment steps as outlined in the **Usage** section of this guide.

   **Note**: Ensure that your `.env` file is not exposed publicly to protect sensitive information like your private key.


---

## Environment Configuration

The `.env` file supports both Ethereum and Arbitrum networks. Example:

```plaintext
# Ethereum Mainnet Configuration
ETH_RPC_URL=https://mainnet.infura.io/v3/YOUR_PROJECT_ID
DYNAMO_TOKEN_ADDRESS=0xBfFAF03F35D75417091f0f42de3EC6809ffA51eB

# Arbitrum Network Configuration
ARBITRUM_RPC_URL=https://arbitrum.infura.io/v3/YOUR_PROJECT_ID
ARBITRUM_TOKEN_ADDRESS=0x4d91c0cdf64e995e4391254f0bc19a8a128765b9

# Common Settings
PRIVATE_KEY=<Your Wallet Private Key>
AGENT_FACTORY_CONTRACT=0xYourAgentFactoryContractAddress
AGENT_TOKEN_NAME=TestAgentToken
AGENT_TOKEN_SYMBOL=TAT
DEFAULT_NETWORK=ethereum # Options: ethereum, arbitrum
```

---

## Quick Start

To launch an AI agent, use the Quick Start script:

```bash
python examples/quick_start.py
```

### Script Behavior
- Reads the `DEFAULT_NETWORK` value from the `.env` file to determine which network to use.
- Connects to the specified network and launches an agent using the provided details.

---

## Usage Example

Run the Liquid Staking Token (LST) agent:

```bash
python src/lst_agent.py
```

---

## Notes
1. Ensure you have sufficient DYNAMO tokens on the chosen network.
2. Both Ethereum and Arbitrum tokens are supported, with their respective configurations in `.env`.
3. For bridging tokens between Ethereum and Arbitrum, use supported bridge solutions (not included in this repository).

---

## Troubleshooting

1. **Connection Issues**:
   - Verify the RPC URL in `.env` is correct.
   - Ensure you have internet access and a valid Infura/Alchemy project.

2. **Missing Environment Variables**:
   - Check the `.env` file for completeness.
   - Ensure all required fields are filled out.

3. **Transaction Failure**:
   - Check your wallet balance for sufficient ETH/ARB to cover gas fees.
   - Verify the correctness of the agent factory contract address.

---

## Contributing

Contributions are welcome! Submit issues or pull requests on the [GitHub repository](https://github.com/DynamoProtocol/Dynamo-AI-Agent-Framework).

---

## License

This project is licensed under the MIT License.

