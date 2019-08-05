import multiprocessing
import time

def prime(start, stop, prime_numbers):
    print("Range: {}-{}".format(start, stop))
    for num in range(start, stop+1):
        is_prime=True
        for div in range(2, num):
            if num%div == 0:
                is_prime=False
                break
        if is_prime:
            prime_numbers.append(num)

if __name__ == '__main__':
    start_time = time.time()

    # Normal Method
    prime_numbers = []
    start = 1
    stop = 200000
    prime(start, stop, prime_numbers)
        
    print(sorted(prime_numbers))
    print("Total Time: {}".format(time.time()-start_time))