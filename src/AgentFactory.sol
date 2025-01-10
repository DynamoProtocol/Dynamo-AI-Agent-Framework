// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AgentFactory is Ownable {
    // Event emitted when a new agent creation is requested
    event AgentCreationRequested(address indexed creator, string metadata);

    // Event emitted when an agent creation is finalized
    event AgentCreated(address indexed agentAddress, string metadata, address indexed creator);

    // Struct to store agent details
    struct Agent {
        address agentAddress;
        string metadata;
        address creator;
    }

    // Array to store all agents
    Agent[] public agents;

    // Mapping to quickly verify if an address is an agent
    mapping(address => bool) public isAgent;

    // $DYNAMO token contract
    IERC20 public dynamoToken;

    // Cost to create an agent (in $DYNAMO tokens)
    uint256 public agentCreationCost;

    constructor(address _dynamoToken, uint256 _agentCreationCost) {
        dynamoToken = IERC20(_dynamoToken);
        agentCreationCost = _agentCreationCost;
    }

    function requestAgentCreation(string memory metadata) external {
        require(
            dynamoToken.transferFrom(msg.sender, address(this), agentCreationCost),
            "Payment failed: Insufficient $DYNAMO tokens or allowance."
        );

        emit AgentCreationRequested(msg.sender, metadata);
    }

    function finalizeAgentCreation(address agentAddress, string memory metadata) external {
        require(!isAgent[agentAddress], "Agent already exists");

        agents.push(Agent({
            agentAddress: agentAddress,
            metadata: metadata,
            creator: msg.sender
        }));

        isAgent[agentAddress] = true;

        emit AgentCreated(agentAddress, metadata, msg.sender);
    }

    function getAgentCount() external view returns (uint256) {
        return agents.length;
    }

    function getAllAgents() external view returns (Agent[] memory) {
        return agents;
    }

    function setAgentCreationCost(uint256 _newCost) external onlyOwner {
        agentCreationCost = _newCost;
    }

    function withdrawDynamo(uint256 _amount) external onlyOwner {
        require(dynamoToken.transfer(msg.sender, _amount), "Withdrawal failed.");
    }
}
