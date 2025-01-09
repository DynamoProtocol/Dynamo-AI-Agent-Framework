import os
from web3 import Web3
from src.agent_factory import launch_new_agent

def main():
    print("🚀 Dynamo AI Agent Framework Quick Start!")
    required_env_vars = [
        "ETH_RPC_URL", "PRIVATE_KEY", "DYNAMO_TOKEN_ADDRESS", 
        "AGENT_FACTORY_CONTRACT", "AGENT_TOKEN_NAME", "AGENT_TOKEN_SYMBOL"
    ]
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        return

    web3 = Web3(Web3.HTTPProvider(os.environ["ETH_RPC_URL"]))
    if not web3.isConnected():
        print("❌ Unable to connect to Ethereum.")
        return

    try:
        print("💡 Launching AI Agent...")
        tx_hash = launch_new_agent(
            web3,
            os.environ["PRIVATE_KEY"],
            os.environ["AGENT_FACTORY_CONTRACT"],
            os.environ["AGENT_TOKEN_NAME"],
            os.environ["AGENT_TOKEN_SYMBOL"]
        )
        print(f"⏳ Transaction sent! Tx Hash: {tx_hash}")
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt["status"] == 1:
            print(f"✅ AI Agent '{os.environ['AGENT_TOKEN_NAME']}' launched!")
        else:
            print("❌ Transaction failed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
