import os
from web3 import Web3

class AgentFactory:
    def __init__(self, web3, private_key, contract_address):
        self.web3 = web3
        self.private_key = private_key
        self.contract_address = contract_address
        self.account = self.web3.eth.account.from_key(private_key)
        self.address = self.account.address

        # Load the contract ABI
        with open(os.path.join(os.path.dirname(__file__), "../middleware/AgentFactoryABI.json"), "r") as f:
            self.contract_abi = f.read()

        # Initialize the contract
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def request_agent_creation(self, metadata):
        try:
            transaction = self.contract.functions.requestAgentCreation(metadata).buildTransaction({
                "from": self.address,
                "gas": int(os.getenv("GAS_LIMIT", 2000000)),
                "gasPrice": self.web3.toWei(os.getenv("GAS_PRICE", "50"), "gwei"),
                "nonce": self.web3.eth.getTransactionCount(self.address),
            })
            signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            print(f"Error requesting agent creation: {e}")
            return None

    def finalize_agent_creation(self, agent_address, metadata):
        try:
            transaction = self.contract.functions.finalizeAgentCreation(agent_address, metadata).buildTransaction({
                "from": self.address,
                "gas": int(os.getenv("GAS_LIMIT", 2000000)),
                "gasPrice": self.web3.toWei(os.getenv("GAS_PRICE", "50"), "gwei"),
                "nonce": self.web3.eth.getTransactionCount(self.address),
            })
            signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            print(f"Error finalizing agent creation: {e}")
            return None

    def get_agent_count(self):
        try:
            return self.contract.functions.getAgentCount().call()
        except Exception as e:
            print(f"Error getting agent count: {e}")
            return None

    def get_all_agents(self):
        try:
            return self.contract.functions.getAllAgents().call()
        except Exception as e:
            print(f"Error getting all agents: {e}")
            return None

    def set_agent_creation_cost(self, new_cost):
        try:
            transaction = self.contract.functions.setAgentCreationCost(new_cost).buildTransaction({
                "from": self.address,
                "gas": int(os.getenv("GAS_LIMIT", 2000000)),
                "gasPrice": self.web3.toWei(os.getenv("GAS_PRICE", "50"), "gwei"),
                "nonce": self.web3.eth.getTransactionCount(self.address),
            })
            signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            print(f"Error setting agent creation cost: {e}")
            return None

    def withdraw_dynamo(self, amount):
        try:
            transaction = self.contract.functions.withdrawDynamo(amount).buildTransaction({
                "from": self.address,
                "gas": int(os.getenv("GAS_LIMIT", 2000000)),
                "gasPrice": self.web3.toWei(os.getenv("GAS_PRICE", "50"), "gwei"),
                "nonce": self.web3.eth.getTransactionCount(self.address),
            })
            signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            print(f"Error withdrawing $DYNAMO: {e}")
            return None
