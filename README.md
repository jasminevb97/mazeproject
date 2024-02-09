# Maze Project

## Project Description
This project explores the implementation of a maze-solving algorithm using a graph model. Each vertex in the graph represents a state, a combination for wo entities, Lucky and Rocket. The goal is to nagivate these entities through the maze to reach a specific goal node under certain conditions.

## Key Features
- **Graph Model**: Utilizes the vertices to represent the states of Lucky and Rocket's positions, with directed edges incidcating possible transitions.
- **Transition conditions**: Movement is allowed through corridors matching the current room's color.
- **Breadth-First Search (BFS)**: Find the shortest path to the maze
- **State Graph**: Create a state graph based on input nodes and edges, defining all possible movements and transitions.

## Running the Project
```bash
python maze_solver.py <file name>
```
