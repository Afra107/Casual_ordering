# Logical Clocks: BSS, SES, and Matrix Clock Implementations

## Overview
This zip file for assignment contains implementations of three logical clock algorithms used for distributed systems:

1. **Birman-Schiper-Stephenson (BSS) Algorithm** - Ensures causal message delivery.
2. **Schwarz & Mattern (SES) Algorithm** - Efficiently tracks global states in distributed systems.
3. **Matrix Clock Algorithm** - Extends vector clocks to maintain a full history of causal dependencies.

These implementations help understand causality and event ordering in distributed computing.

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies 


### Running the Implementations
Each algorithm has its own script. You can execute them individually as follows:

#### Birman-Schiper-Stephenson (BSS)
```sh
python BSS.py
```
#### Schwarz & Mattern (SES)
```sh
python SES.py
```
#### Matrix Clock
```sh
python Matrix Clock.py
```

## Sample Inputs and Expected Outputs

### 1. Birman-Schiper-Stephenson (BSS)
#### **Input:**
A sequence of message exchanges between three processes.
```sh
Process 1 sends message to Process 2
Process 2 sends message to Process 3
Process 3 sends message to Process 1
```
#### **Expected Output:**
```sh
Process 1 sends: [1, 0, 0]
Process 2 receives: [1, 1, 0]
Process 2 sends: [1, 2, 0]
Process 3 receives: [1, 2, 1]
Process 3 sends: [1, 2, 2]
Process 1 receives: [2, 2, 2]
```

### 2. Schwarz & Mattern (SES)
#### **Input:**
State recording at different intervals.
```sh
Process 1 records state: {E1, E2}
Process 2 records state: {E3, E4}
```
#### **Expected Output:**
```sh
Global snapshot collected: {E1, E2, E3, E4}
```

### 3. Matrix Clock
#### **Input:**
Message exchanges between three processes.
```sh
P1 sends to P2
P2 sends to P3
P3 sends to P1
```
#### **Expected Output:**
```sh
P1: [[1,0,0],[0,0,0],[0,0,0]]
P2: [[1,0,0],[1,1,0],[0,0,0]]
P3: [[1,0,0],[1,1,0],[1,1,1]]
```

