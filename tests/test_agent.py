import unittest
from src.lst_agent import LstAgent  # Adjusted to reflect the actual implementation

class TestLstAgent(unittest.TestCase):
    def test_get_balances(self):  # Renamed to match lst_agent.py's expected functionality
        agent = LstAgent("TestAgent")
        # Mock user_address and expected balances
        user_address = "0xMockAddress"
        balances = agent.get_balances(user_address)  # Adjusted method name
        self.assertIsInstance(balances, dict)  # Updated to check for expected return type

    def test_perform_stake(self):
        agent = LstAgent("TestAgent")
        # Mock staking parameters
        staking_details = {
            "token_address": "0xTokenAddress",
            "amount": 1000
        }
        result = agent.perform_stake(staking_details)
        self.assertTrue(result)  # Check if staking was successful

if __name__ == "__main__":
    unittest.main()
