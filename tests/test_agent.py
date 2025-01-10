import unittest
from src.lst_agent import DynamoAgent

class TestDynamoAgent(unittest.TestCase):
    def test_get_balances(self):
        agent = DynamoAgent(
            "TestAgent",
            "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
            "0xYourPrivateKey",
            "YourDeepSeekAPIKey"
        )
        user_address = "0xUserAddress"
        balances = agent.get_balances(user_address)
        self.assertIsInstance(balances, dict)

    def test_perform_stake(self):
        agent = DynamoAgent(
            "TestAgent",
            "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
            "0xYourPrivateKey",
            "YourDeepSeekAPIKey"
        )
        staking_details = {
            "token_address": "0xTokenAddress",
            "amount": 1000
        }
        result = agent.perform_stake(staking_details)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
