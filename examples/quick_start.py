import os
from web3 import Web3
from src.agent_factory import AgentFactory

def main():
    print("🚀 Dynamo AI Agent Framework Quick Start!")

    # Load environment variables
    network = os.getenv("DEFAULT_NETWORK", "ethereum").lower()
    if network not in ["ethereum", "arbitrum"]:
        print("❌ Invalid DEFAULT_NETWORK specified. Use 'ethereum' or 'arbitrum'.")
        return

    rpc_url = os.getenv(f"{network.upper()}_RPC_URL")
    token_address = os.getenv(f"{network.upper()}_TOKEN_ADDRESS")
    if not rpc_url or not token_address:
        print(f"❌ Missing RPC URL or token address for {network}.")
        return

    # Initialize Web3
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    if not web3.isConnected():
        print(f"❌ Unable to connect to {network} network.")
        return

    try:
        print(f"💡 Launching AI Agent on {network.capitalize()}...")
        agent_factory = AgentFactory(
            web3,
            os.environ["PRIVATE_KEY"],
            os.environ["AGENT_FACTORY_CONTRACT"]
        )
        tx_hash = agent_factory.request_agent_creation("Test Metadata")
        print(f"⏳ Transaction sent! Tx Hash: {tx_hash}")
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt["status"] == 1:
            print(f"✅ AI Agent '{os.environ['AGENT_TOKEN_NAME']}' launched on {network.capitalize()}!")
        else:
            print("❌ Transaction failed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
