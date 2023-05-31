def start_of_packet(signal, length):
    for i in range(length - 1, len(signal)):
        seq = signal[i - length + 1:i + 1]
        if len(set(seq)) == length:
            return i + 1

with open('input.txt') as f:
    signal = f.read()
    
print(start_of_packet(signal, 14))

