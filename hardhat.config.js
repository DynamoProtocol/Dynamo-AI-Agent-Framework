// Import Hardhat and dotenv for environment variables
require("@nomiclabs/hardhat-waffle");
require("dotenv").config();

module.exports = {
  // Solidity compiler version
  solidity: "0.8.0",

  // Network configurations
  networks: {
    // Ethereum Mainnet
    mainnet: {
      url: process.env.ETH_RPC_URL, // Ethereum RPC endpoint
      accounts: [process.env.PRIVATE_KEY], // Private key of the deployer wallet
    },
    // Arbitrum Testnet
    arbitrum_testnet: {
      url: process.env.ARBITRUM_RPC_URL, // Arbitrum RPC endpoint
      accounts: [process.env.PRIVATE_KEY], // Private key of the deployer wallet
    },
    // Local Hardhat Network (for testing)
    localhost: {
      url: "http://127.0.0.1:8545", // Local Hardhat node
    },
  },

  // Optional: Configure paths for artifacts and cache
  paths: {
    sources: "./src", // Solidity source files
    tests: "./tests", // Test files
    cache: "./cache", // Compilation cache
    artifacts: "./artifacts", // Compiled contract artifacts
  },

  // Optional: Add plugins for additional functionality
  plugins: [
    "@nomiclabs/hardhat-ethers", // Ethers.js plugin
    "@nomiclabs/hardhat-waffle", // Waffle testing plugin
  ],
};
