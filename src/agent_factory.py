from web3 import Web3
import os

class AgentFactory:
    def __init__(self, web3, private_key, contract_address):
        """
        Initializes the AgentFactory class.

        Args:
            web3 (Web3): A Web3 instance connected to the Ethereum network.
            private_key (str): The private key of the wallet interacting with the contract.
            contract_address (str): The address of the deployed AgentFactory contract.
        """
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
        """
        Requests the creation of a new agent by calling the `requestAgentCreation` function on the contract.

        Args:
            metadata (str): Metadata for the agent creation request.

        Returns:
            str: The transaction hash of the request.
        """
        # Build the transaction
        transaction = self.contract.functions.requestAgentCreation(metadata).buildTransaction({
            "from": self.address,
            "gas": 2000000,
            "gasPrice": self.web3.toWei("50", "gwei"),
            "nonce": self.web3.eth.getTransactionCount(self.address),
        })

        # Sign and send the transaction
        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return self.web3.toHex(tx_hash)

    def finalize_agent_creation(self, agent_address, metadata):
        """
        Finalizes the creation of an agent by calling the `finalizeAgentCreation` function on the contract.

        Args:
            agent_address (str): The address of the newly created agent.
            metadata (str): Metadata associated with the agent.

        Returns:
            str: The transaction hash of the finalization.
        """
        # Build the transaction
        transaction = self.contract.functions.finalizeAgentCreation(agent_address, metadata).buildTransaction({
            "from": self.address,
            "gas": 2000000,
            "gasPrice": self.web3.toWei("50", "gwei"),
            "nonce": self.web3.eth.getTransactionCount(self.address),
        })

        # Sign and send the transaction
        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return self.web3.toHex(tx_hash)

    def get_agent_count(self):
        """
        Retrieves the total number of agents created.

        Returns:
            int: The number of agents.
        """
        return self.contract.functions.getAgentCount().call()

    def get_all_agents(self):
        """
        Retrieves details of all agents.

        Returns:
            list: A list of agent details (address, metadata, creator).
        """
        return self.contract.functions.getAllAgents().call()

    def set_agent_creation_cost(self, new_cost):
        """
        Updates the agent creation cost (only callable by the owner).

        Args:
            new_cost (int): The new cost to create an agent (in $DYNAMO tokens).

        Returns:
            str: The transaction hash of the update.
        """
        # Build the transaction
        transaction = self.contract.functions.setAgentCreationCost(new_cost).buildTransaction({
            "from": self.address,
            "gas": 2000000,
            "gasPrice": self.web3.toWei("50", "gwei"),
            "nonce": self.web3.eth.getTransactionCount(self.address),
        })

        # Sign and send the transaction
        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return self.web3.toHex(tx_hash)

    def withdraw_dynamo(self, amount):
        """
        Withdraws $DYNAMO tokens from the contract (only callable by the owner).

        Args:
            amount (int): The amount of $DYNAMO tokens to withdraw.

        Returns:
            str: The transaction hash of the withdrawal.
        """
        # Build the transaction
        transaction = self.contract.functions.withdrawDynamo(amount).buildTransaction({
            "from": self.address,
            "gas": 2000000,
            "gasPrice": self.web3.toWei("50", "gwei"),
            "nonce": self.web3.eth.getTransactionCount(self.address),
        })

        # Sign and send the transaction
        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return self.web3.toHex(tx_hash)
