# Logical Clocks: BSS, SES, and Matrix Clock Implementations

## Overview
Causal ordering is crucial in distributed systems to ensure that events are processed in an order that respects causality.
This repository implements three different approaches to maintain causal ordering among distributed processes.

1. **Birman-Schiper-Stephenson (BSS) Algorithm** - Ensures causal message delivery.
2. **Schwarz & Mattern (SES) Algorithm** - Efficiently tracks global states in distributed systems.
3. **Matrix Clock Algorithm** - Extends vector clocks to maintain a full history of causal dependencies.

These implementations help understand causality and event ordering in distributed computing.


## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies 

## Installation

Clone the repository:

``` sh
git clone https://github.com/Afra107/Casual_ordering.git
cd Casual_ordering 
```


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

## Sample Outputs

### 1. Birman-Schiper-Stephenson (BSS)

![image](https://github.com/user-attachments/assets/7aa1ff0d-38c8-45d4-ac2c-d0ccb5029732)


### 2. Schwarz & Mattern (SES)

![image](https://github.com/user-attachments/assets/dd2a9d33-b5f2-4ade-805a-67146aa83487)


### 3. Matrix Clock

![image](https://github.com/user-attachments/assets/df7201bc-b8d4-44db-84f5-128e5ac673f3)

![image](https://github.com/user-attachments/assets/5825cb88-7030-48a5-aea9-7857356381a9)

![image](https://github.com/user-attachments/assets/8ae891bd-6259-46d3-a4fb-6d3dc26c54a3)

![image](https://github.com/user-attachments/assets/3746866d-0cad-4281-a63c-25abc1f30dec)

