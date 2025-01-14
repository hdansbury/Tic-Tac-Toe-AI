# File Guide:
- pvp-cl.py = Player vs Player with a Command Line Interface
- pvp-gui.py = Player vs Player with Pygame GUI
- minimax-cl.py = Player vs AI with Command Line Interface
- minimax-gui = Player vs AI with GUI (minimax)
- aivai-nn.py = AI vs AI using Q-learning
- aivai-dqn = AI vs AI using DQN

---

# Tic-Tac-Toe-AI
Implementations of Neural Network-based AI (Q-Learning), Reinforcement Learning (DQN), and the Minimax Algorithm for playing Tic-Tac-Toe.

## 1. Minimax Algorithm
The **Minimax algorithm** is a decision-making strategy that assumes both players play optimally. It aims to minimize the worst-case scenario for the current player, maximizing the chances of winning or minimizing the chances of losing.
- It recursively evaluates all possible moves in the game until it reaches an end state.
- The move with the best score is selected.


## 2. Q-Learning
**Q-Learning** is a model-free reinforcement learning (RL) algorithm. It focuses on learning the value of actions in specific states, called **Q-values**. The Q-value represents the expected future reward the agent will receive after taking a particular action in a given state.
- The Q-network receives the current state of the game and outputs a set of Q-values corresponding to the available actions.


## 3. Deep Q-Learning (DQN)
**Deep Q-Learning** (DQN) is a specialized form of Q-Learning that utilizes deep neural networks to approximate the Q-function. This allows the agent to learn the optimal policy without explicitly needing to model every possible state-action pair.
1. Selects a move based on Q-values.
2. Updates its Q-values after each action.
3. Replays its past experiences to improve its decision-making.

