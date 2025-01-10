const hre = require("hardhat");

async function main() {
    const [deployer] = await hre.ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const dynamoTokenAddress = process.env.DYNAMO_TOKEN_ADDRESS;
    const agentCreationCost = process.env.AGENT_CREATION_COST;

    if (!dynamoTokenAddress || !agentCreationCost) {
        console.error("❌ Missing DYNAMO_TOKEN_ADDRESS or AGENT_CREATION_COST in .env file.");
        process.exit(1);
    }

    console.log("DYNAMO Token Address:", dynamoTokenAddress);
    console.log("Agent Creation Cost:", agentCreationCost);

    const AgentFactory = await hre.ethers.getContractFactory("AgentFactory");
    const agentFactory = await AgentFactory.deploy(dynamoTokenAddress, agentCreationCost);

    await agentFactory.deployed();

    console.log("AgentFactory deployed to:", agentFactory.address);
    console.log("✅ Deployment successful!");
    console.log("Update AGENT_FACTORY_CONTRACT in your .env file with the following address:");
    console.log(agentFactory.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("❌ Deployment failed:", error);
        process.exit(1);
    });
