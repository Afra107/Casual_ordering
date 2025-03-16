import threading
import time
import random
from collections import deque

class Message:
    def __init__(self, sender, timestamp, content):
        self.sender = sender
        self.timestamp = timestamp  # Vector timestamp
        self.content = content
    
    def __repr__(self):
        return f"Message(from P{self.sender}, TS={self.timestamp})"

class Process(threading.Thread):
    def __init__(self, pid, num_processes, network):
        super().__init__()
        self.pid = pid  # Process ID
        self.num_processes = num_processes
        self.vector_clock = [0] * num_processes  # Vector timestamp
        self.buffer = deque()  # Buffer for delayed messages
        self.network = network  # Shared network queue (simulated)

    def send_message(self, content):
        """Send a message to all other processes."""
        self.vector_clock[self.pid] += 1  # Step 1: Increment own clock
        timestamp = self.vector_clock.copy()
        message = Message(self.pid, timestamp, content)
        
        recipients = [p.pid for p in self.network if p.pid != self.pid]
        print(f"P{self.pid} sending message to P{recipients}, TS={timestamp}")
        
        # Simulate sending to all processes with randomized delays
        for process in self.network:
            if process.pid != self.pid:
                time.sleep(random.uniform(0.1, 1))  # Artificial delay to create out-of-order arrivals
                process.receive_message(message)

    def receive_message(self, message):
        """Receive a message and decide whether to buffer or deliver."""
        print(f"P{self.pid} received {message}")
        
        # Step 2: Check delivery conditions
        sender = message.sender
        ts = message.timestamp
        
        if (self.vector_clock[sender] == ts[sender] - 1 and
            all(self.vector_clock[k] >= ts[k] for k in range(self.num_processes) if k != sender)):
            self.deliver_message(message)
        else:
            print(f"P{self.pid} buffering {message} as causal constraints are not met.")
            self.buffer.append(message)
            self.buffer = deque(sorted(self.buffer, key=lambda m: (m.timestamp, m.sender)))
    
    def deliver_message(self, message):
        """Deliver a message and update vector clock."""
        sender = message.sender
        self.vector_clock[sender] += 1  # Rule 3(a): Update clock
        print(f"P{self.pid} DELIVERED {message}")
        
        # Rule 3(b): Check if any buffered messages can be delivered
        self.process_buffer()
    
    def process_buffer(self):
        """Try delivering buffered messages in order."""
        for message in list(self.buffer):
            sender = message.sender
            ts = message.timestamp
            
            if (self.vector_clock[sender] == ts[sender] - 1 and
                all(self.vector_clock[k] >= ts[k] for k in range(self.num_processes) if k != sender)):
                print(f"P{self.pid} now delivering previously buffered {message}")
                self.buffer.remove(message)
                self.deliver_message(message)

    def run(self):
        """Simulate process execution."""
        time.sleep(random.uniform(0.5, 2))
        self.send_message(f"Message from P{self.pid}")
        time.sleep(random.uniform(0.5, 1.5))  # Additional delay to ensure out-of-order arrivals

# Number of processes
num_processes = 3
network = []

# Create processes
for i in range(num_processes):
    network.append(Process(i, num_processes, network))

# Start processes
for process in network:
    process.start()

# Join threads
for process in network:
    process.join()
