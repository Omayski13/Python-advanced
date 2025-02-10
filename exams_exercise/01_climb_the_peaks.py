from collections import deque

food = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
day = 0
peaks = deque(["Vihren",80, "Kutelo",90, "Banski Suhodol",100, "Polezhan",60, "Kamenitza",70])
conquered_peaks = []

while food and stamina:
    if day == 7:
        break
    if not peaks:
        break
    current_food = food.pop()
    current_stamina = stamina.popleft()
    current_sum = current_food + current_stamina
    current_peak = peaks[0]
    current_difficult = int(peaks[1])
    if current_sum >= current_difficult:
        conquered_peaks.append(current_peak+"\n")
        peaks.popleft()
        peaks.popleft()
    day += 1

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f"Conquered peaks:")
    print(f"{''.join(conquered_peaks)}\n")






