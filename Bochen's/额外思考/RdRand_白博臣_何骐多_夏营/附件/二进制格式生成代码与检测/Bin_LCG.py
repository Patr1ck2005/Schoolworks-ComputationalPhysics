import os

class LCG:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

def int_to_binary_string(num, bit_length):
    """Convert an integer to a binary string of specified length."""
    return format(num, f'0{bit_length}b')

def main():
    num_samples = 1000
    bits_per_sample = 1000000
    directory = 'target/data3'

    # Ensure the target data directory exists
    os.makedirs(directory, exist_ok=True)

    lcg = LCG(seed=123, a=1664525, c=1013904223, m=2**32)

    for sample_index in range(num_samples):
        sample_data = ''.join(int_to_binary_string(lcg.random(), 32) for _ in range(bits_per_sample // 32))
        file_path = os.path.join(directory, f'sample_{sample_index}.bin')
        with open(file_path, 'wb') as file:
            file.write(int(sample_data, 2).to_bytes((len(sample_data) + 7) // 8, byteorder='big'))

if __name__ == "__main__":
    main()
