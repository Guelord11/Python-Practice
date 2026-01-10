# Countdown Timer

import time

start = int(input("Entrez le nombre pour commencer le compte à rebours : "))

print("\n ---- Le compte à rebours commence ----")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1

print("\n ---- Bonne année 2026 ! ----")