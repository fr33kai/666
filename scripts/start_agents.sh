#!/bin/bash

# Start the agent manager which will in turn start all agents, angels, and demons
echo "Starting Agent Manager..."
python agents/manager.py &

# Wait for the manager to initialize
sleep 5

# Start angels
echo "Starting Angels..."
for i in $(seq 1 $ANGEL_COUNT); do
    python agents/angel_agent.py &
done

# Start demons
echo "Starting Demons..."
for i in $(seq 1 $DEMON_COUNT); do
    python agents/demon_agent.py &
done

# Start legions for each agent
echo "Starting Legions for each Agent..."
for i in $(seq 1 $AGENT_COUNT); do
    python agents/legion.py &
done

echo "All agents, angels, demons, and their legions have been started."
echo "Check logs for details on the initialization status."