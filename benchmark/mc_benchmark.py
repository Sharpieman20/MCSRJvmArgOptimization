import time

target_attempts = 1000

attempts = 0

def loop():
    '''
    hold down reset all key
    '''
    pass

def is_done():
    return attempts >= target_attempts

def main():
    start_time = time.time()
    while not is_done():
        loop()
    end_time = time.time()
    print(f'Duration: {end_time-start_time}')

if __name__ == '__main__':
    main()
