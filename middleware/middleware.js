const { ethers } = require("ethers");
const axios = require("axios");
const winston = require("winston");
require("dotenv").config();

// Configure logging
const logger = winston.createLogger({
    level: "info",
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: "middleware.log" }),
    ],
});

// Load environment variables
const CONTRACT_ADDRESS = process.env.AGENT_FACTORY_CONTRACT;
const PROVIDER_URL = process.env.ETH_RPC_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const GOAT_API_URL = process.env.GOAT_API_URL;
const GOAT_API_KEY = process.env.GOAT_API_KEY;

// Initialize Ethereum provider and wallet
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Load AgentFactory contract ABI
const CONTRACT_ABI = require("./AgentFactoryABI.json");

// Connect to the contract
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, wallet);

// Listen for AgentCreationRequested events
contract.on("AgentCreationRequested", async (creator, metadata, event) => {
    logger.info(`Agent creation requested by ${creator} with metadata: ${metadata}`);

    try {
        // Call GOAT API
        const response = await axios.post(
            `${GOAT_API_URL}/generateAgent`,
            { metadata },
            { headers: { Authorization: `Bearer ${GOAT_API_KEY}` } }
        );
        const agentData = response.data;

        logger.info("GOAT API response:", agentData);

        // Extract agent details
        const { agentAddress, agentMetadata } = agentData;

        // Finalize agent creation on blockchain
        const tx = await contract.finalizeAgentCreation(agentAddress, agentMetadata);
        const receipt = await tx.wait();

        if (receipt.status === 1) {
            logger.info(`Agent creation finalized on blockchain: ${agentAddress}`);
        } else {
            logger.error("Transaction failed.");
        }
    } catch (error) {
        logger.error("Error processing agent creation:", error.message);
    }
});

logger.info("Middleware is listening for AgentCreationRequested events...");
