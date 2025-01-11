// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AgentFactory is Ownable, ReentrancyGuard {
    event AgentCreationRequested(address indexed creator, string metadata);
    event AgentCreated(address indexed agentAddress, string metadata, address indexed creator);

    struct Agent {
        address agentAddress;
        string metadata;
        address creator;
    }

    Agent[] public agents;
    mapping(address => bool) public isAgent;

    IERC20 public dynamoToken;
    uint256 public agentCreationCost;

    constructor(address _dynamoToken, uint256 _agentCreationCost) {
        dynamoToken = IERC20(_dynamoToken);
        agentCreationCost = _agentCreationCost;
    }

    function requestAgentCreation(string memory metadata) external nonReentrant {
        require(
            dynamoToken.transferFrom(msg.sender, address(this), agentCreationCost),
            "Payment failed: Insufficient $DYNAMO tokens or allowance."
        );
        emit AgentCreationRequested(msg.sender, metadata);
    }

    function finalizeAgentCreation(address agentAddress, string memory metadata) external onlyOwner {
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

    function getAllAgents(uint256 startIndex, uint256 endIndex) external view returns (Agent[] memory) {
        require(startIndex < endIndex && endIndex <= agents.length, "Invalid index range");
        Agent[] memory result = new Agent[](endIndex - startIndex);
        for (uint256 i = startIndex; i < endIndex; i++) {
            result[i - startIndex] = agents[i];
        }
        return result;
    }

    function setAgentCreationCost(uint256 _newCost) external onlyOwner {
        agentCreationCost = _newCost;
    }

    function withdrawDynamo(uint256 _amount) external onlyOwner nonReentrant {
        require(dynamoToken.transfer(msg.sender, _amount), "Withdrawal failed.");
    }
}
