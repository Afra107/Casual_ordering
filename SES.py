import threading
import time
import random
from collections import defaultdict

class Process:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.vector_clock = [0] * num_processes
        self.message_buffer = []
        self.lock = threading.Lock()

    def send_message(self, receiver, network):
        with self.lock:
            self.vector_clock[self.process_id] += 1
            timestamp = self.vector_clock[:]
        
        message = (self.process_id, timestamp)
        print(f"Process {self.process_id} sent message {message} to Process {receiver}")
        network[receiver].receive_message(message)

    def receive_message(self, message):
        sender, timestamp = message
        self.message_buffer.append((sender, timestamp))
        self.deliver_messages()
    
    def deliver_messages(self):
        with self.lock:
            undelivered = []
            for sender, timestamp in self.message_buffer:
                if self.can_deliver(timestamp):
                    print(f"Process {self.process_id} delivered message from Process {sender}: {timestamp}")
                    self.update_vector_clock(timestamp)
                else:
                    undelivered.append((sender, timestamp))
            self.message_buffer = undelivered

    def can_deliver(self, timestamp):
        for i in range(self.num_processes):
            if timestamp[i] > self.vector_clock[i] + (1 if i == self.process_id else 0):
                return False
        return True

    def update_vector_clock(self, timestamp):
        for i in range(self.num_processes):
            self.vector_clock[i] = max(self.vector_clock[i], timestamp[i])
        self.vector_clock[self.process_id] += 1


def simulate():
    num_processes = 3
    network = {i: Process(i, num_processes) for i in range(num_processes)}

    threads = []
    for _ in range(5):
        sender = random.randint(0, num_processes - 1)
        receiver = random.randint(0, num_processes - 1)
        if sender != receiver:
            thread = threading.Thread(target=network[sender].send_message, args=(receiver, network))
            threads.append(thread)
            thread.start()
        time.sleep(0.5)

    for thread in threads:
        thread.join()
    
    print("Final vector clocks:")
    for i in range(num_processes):
        print(f"Process {i}: {network[i].vector_clock}")

if __name__ == "__main__":
    simulate()