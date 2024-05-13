#!/bin/bash

# Stop all running agents, demons, and angels along with their legions.

echo "Stopping all agents..."
for i in $(seq 1 $AGENT_COUNT); do
    echo "Stopping agent $i..."
    # Assuming there's a function to stop an agent by ID
    # This would typically send a signal to stop the agent's process
    stop_agent $i
done

echo "Stopping all demons..."
for i in $(seq 1 $DEMON_COUNT); do
    echo "Stopping demon $i..."
    # Assuming there's a function to stop a demon by ID
    # This would typically send a signal to stop the demon's process
    stop_demon $i
done

echo "Stopping all angels..."
for i in $(seq 1 $ANGEL_COUNT); do
    echo "Stopping angel $i..."
    # Assuming there's a function to stop an angel by ID
    # This would typically send a signal to stop the angel's process
    stop_angel $i
done

echo "Stopping all legions..."
# Assuming each agent has the same number of legions
for i in $(seq 1 $(($AGENT_COUNT * $LEGION_COUNT_PER_AGENT))); do
    echo "Stopping legion $i..."
    # Assuming there's a function to stop a legion by ID
    # This would typically send a signal to stop the legion's process
    stop_legion $i
done

echo "All agents, demons, angels, and legions have been stopped."