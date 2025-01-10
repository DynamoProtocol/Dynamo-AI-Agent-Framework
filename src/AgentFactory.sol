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

    /**
     * @dev Sets the $DYNAMO token address and creation cost.
     * @param _dynamoToken Address of the $DYNAMO token contract.
     * @param _agentCreationCost Cost to create an agent (in $DYNAMO tokens).
     */
    constructor(address _dynamoToken, uint256 _agentCreationCost) {
        dynamoToken = IERC20(_dynamoToken);
        agentCreationCost = _agentCreationCost;
    }

    /**
     * @dev Function to request the creation of a new agent.
     * Requires the caller to pay the agent creation cost in $DYNAMO tokens.
     * @param metadata Metadata for the agent creation request.
     */
    function requestAgentCreation(string memory metadata) external {
        // Transfer $DYNAMO tokens from the caller to this contract
        require(
            dynamoToken.transferFrom(msg.sender, address(this), agentCreationCost),
            "Payment failed: Insufficient $DYNAMO tokens or allowance."
        );

        emit AgentCreationRequested(msg.sender, metadata);
    }

    /**
     * @dev Function to finalize the creation of an agent after API processing.
     * @param agentAddress The address of the newly created agent.
     * @param metadata Metadata associated with the agent.
     */
    function finalizeAgentCreation(address agentAddress, string memory metadata) external {
        require(!isAgent[agentAddress], "Agent already exists");

        // Store the agent details
        agents.push(Agent({
            agentAddress: agentAddress,
            metadata: metadata,
            creator: msg.sender
        }));

        isAgent[agentAddress] = true;

        emit AgentCreated(agentAddress, metadata, msg.sender);
    }

    /**
     * @dev Returns the total number of agents created.
     */
    function getAgentCount() external view returns (uint256) {
        return agents.length;
    }

    /**
     * @dev Returns all agents.
     */
    function getAllAgents() external view returns (Agent[] memory) {
        return agents;
    }

    /**
     * @dev Updates the agent creation cost (only callable by the owner).
     * @param _newCost New cost to create an agent (in $DYNAMO tokens).
     */
    function setAgentCreationCost(uint256 _newCost) external onlyOwner {
        agentCreationCost = _newCost;
    }

    /**
     * @dev Withdraws $DYNAMO tokens from the contract (only callable by the owner).
     * @param _amount Amount of $DYNAMO tokens to withdraw.
     */
    function withdrawDynamo(uint256 _amount) external onlyOwner {
        require(dynamoToken.transfer(msg.sender, _amount), "Withdrawal failed.");
    }
}
