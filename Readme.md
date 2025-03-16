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

![alt text](image.png)

### 2. Schwarz & Mattern (SES)

![alt text](image-1.png)

### 3. Matrix Clock

![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
