import sys, time

try:
    while True:
        # draw lines with increasing length
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(0.1)
        
        # draw lines with decreasing length
        for i in range(7, 1, -1):
            print('-' * (i * i))


except KeyboardInterrupt:
    sys.exit()
