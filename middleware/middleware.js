const { ethers } = require("ethers");
const axios = require("axios");
require("dotenv").config();

// Load environment variables
const CONTRACT_ADDRESS = process.env.AGENT_FACTORY_CONTRACT;
const PROVIDER_URL = process.env.ETH_RPC_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const GOAT_API_URL = process.env.GOAT_API_URL;

// Initialize Ethereum provider and wallet
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Load AgentFactory contract ABI
const CONTRACT_ABI = require("./AgentFactoryABI.json");

// Connect to the contract
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, wallet);

// Listen for AgentCreationRequested events
contract.on("AgentCreationRequested", async (creator, metadata, event) => {
    console.log(`Agent creation requested by ${creator} with metadata: ${metadata}`);

    try {
        // Call GOAT API
        const response = await axios.post(`${GOAT_API_URL}/generateAgent`, { metadata });
        const agentData = response.data;

        console.log("GOAT API response:", agentData);

        // Extract agent details
        const { agentAddress, agentMetadata } = agentData;

        // Finalize agent creation on blockchain
        const tx = await contract.finalizeAgentCreation(agentAddress, agentMetadata);
        await tx.wait();

        console.log(`Agent creation finalized on blockchain: ${agentAddress}`);
    } catch (error) {
        console.error("Error processing agent creation:", error.message);
    }
});

console.log("Middleware is listening for AgentCreationRequested events...");
