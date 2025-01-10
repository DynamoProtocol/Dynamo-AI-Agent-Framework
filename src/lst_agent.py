from web3 import Web3
from .deepseek import DeepSeekAPI
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DynamoAgent:
    def __init__(self, name, eth_rpc_url, private_key, deepseek_api_key):
        self.name = name
        self.web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
        self.private_key = private_key
        self.address = self.web3.eth.account.from_key(private_key).address
        self.deepseek_api = DeepSeekAPI(api_key=deepseek_api_key)

    def get_balances(self, user_address):
        try:
            eth_balance = self.web3.eth.get_balance(user_address)
            eth_balance_ether = self.web3.fromWei(eth_balance, 'ether')
            return {
                "ETH": eth_balance_ether,
                "DAI": 350.0  # Placeholder for token balance via contract interaction
            }
        except Exception as e:
            logger.error(f"Error fetching balances: {e}")
            return None

    def perform_stake(self, staking_details):
        try:
            token_address = staking_details.get("token_address")
            amount = staking_details.get("amount")
            if amount > 0:
                transaction = {
                    'to': token_address,
                    'value': self.web3.toWei(amount, 'ether'),
                    'gas': int(os.getenv("GAS_LIMIT", 21000)),
                    'gasPrice': self.web3.toWei(os.getenv("GAS_PRICE", "50"), "gwei"),
                    'nonce': self.web3.eth.getTransactionCount(self.address),
                }
                signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
                tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                return self.web3.toHex(tx_hash)
            return False
        except Exception as e:
            logger.error(f"Error performing stake: {e}")
            return False

    def analyze_portfolio(self, portfolio_data):
        try:
            response = self.deepseek_api.analyze(portfolio_data)
            return response.get("recommendations")
        except Exception as e:
            logger.error(f"Error analyzing portfolio: {e}")
            return None
