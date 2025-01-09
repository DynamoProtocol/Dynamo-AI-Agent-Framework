// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgentFactory {
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

    /**
     * @dev Function to request the creation of a new agent.
     * Emits the `AgentCreationRequested` event.
     * @param metadata Metadata for the agent creation request.
     */
    function requestAgentCreation(string memory metadata) external {
        emit AgentCreationRequested(msg.sender, metadata);
    }

    /**
     * @dev Function to finalize the creation of an agent after API processing.
     * Emits the `AgentCreated` event.
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
}
