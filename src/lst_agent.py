
from deepseek import DeepSeekAPI
from web3 import Web3

class DynamoAgent:
    def __init__(self, name, eth_rpc_url, private_key, deepseek_api_key):
        self.name = name
        self.web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
        self.private_key = private_key
        self.address = self.web3.eth.account.from_key(private_key).address
        self.deepseek_api = DeepSeekAPI(api_key=deepseek_api_key)

    def get_balances(self, user_address):
        eth_balance = self.web3.eth.get_balance(user_address)
        eth_balance_ether = self.web3.fromWei(eth_balance, 'ether')
        return {
            "ETH": eth_balance_ether,
            "DAI": 350.0  # Placeholder for token balance via contract interaction
        }

    def perform_stake(self, staking_details):
        token_address = staking_details.get("token_address")
        amount = staking_details.get("amount")
        if amount > 0:
            transaction = {
                'to': token_address,
                'value': self.web3.toWei(amount, 'ether'),
                'gas': 21000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': self.web3.eth.getTransactionCount(self.address),
            }
            signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        return False

    def analyze_portfolio(self, portfolio_data):
        response = self.deepseek_api.analyze(portfolio_data)
        return response.get("recommendations")

# Example Usage
if __name__ == "__main__":
    agent = DynamoAgent(
        name="DynamoAgent",
        eth_rpc_url="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        private_key="YOUR_PRIVATE_KEY",
        deepseek_api_key="YOUR_DEEPSEEK_API_KEY"
    )
    balances = agent.get_balances("0xMockAddress")
    print("Balances:", balances)
    stake_result = agent.perform_stake({"token_address": "0xTokenAddress", "amount": 1.0})
    print("Staking Result:", stake_result)
    recommendations = agent.analyze_portfolio({"tokens": ["ETH", "DAI"], "values": [1.2, 350]})
    print("Recommendations:", recommendations)
