import threading
import time
import numpy as np

class Process(threading.Thread):
    def __init__(self, process_id, num_processes, message_queue):
        super().__init__()
        self.process_id = process_id
        self.num_processes = num_processes
        self.matrix_clock = np.zeros((num_processes, num_processes), dtype=int)
        self.matrix_clock[self.process_id][self.process_id] = 0  # Initialize own clock to 1
        self.message_queue = message_queue
    
    def increment_clock(self):
        self.matrix_clock[self.process_id][self.process_id] += 1
        print(f"Process {self.process_id + 1}: Executed an event. Updated clock:\n{self.matrix_clock}\n")
    
    def send_message(self, recipient_id):
        self.increment_clock()
        message = (self.process_id, self.matrix_clock.copy())  # Send complete matrix
        self.message_queue[recipient_id].append(message)
        print(f"Process {self.process_id + 1} sent message to Process {recipient_id + 1}. Sent matrix:\n{message[1]}\n")
    
    def receive_message(self):
        while self.message_queue[self.process_id]:  # Process all messages in queue
            sender_id, received_matrix = self.message_queue[self.process_id].pop(0)
            self.matrix_clock = np.maximum(self.matrix_clock, received_matrix)  # Element-wise maximum update
            print(f"Process {self.process_id + 1} received message from Process {sender_id + 1}. Updated clock:\n{self.matrix_clock}\n")
    
    def run(self):
        time.sleep(1)  # Ensure proper order of execution
        if self.process_id == 0:
            self.send_message(1)  # P1 sends to P2
            time.sleep(1)
            self.send_message(2)  # P1 also sends to P3
        elif self.process_id == 1:
            time.sleep(1.5)
            self.receive_message()
            self.increment_clock()
            self.send_message(2)  # P2 sends to P3
        elif self.process_id == 2:
            time.sleep(2)
            self.receive_message()
            time.sleep(1)
            self.send_message(0)  # P3 sends to P1
            time.sleep(1)
            self.receive_message()
        time.sleep(1)  # Ensure proper order of execution
        if self.process_id == 0:
            self.send_message(1)  # P1 sends to P2
        elif self.process_id == 1:
            time.sleep(1.5)
            self.receive_message()
            self.send_message(2)  # P2 sends to P3
        elif self.process_id == 2:
            time.sleep(3)
            self.receive_message()

if __name__ == "__main__":
    num_processes = 3
    message_queue = {i: [] for i in range(num_processes)}
    processes = [Process(i, num_processes, message_queue) for i in range(num_processes)]
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
    
    print("Final Matrix Clocks:")
    for i, process in enumerate(processes):
        print(f"Process {i + 1}:\n{process.matrix_clock}\n")
