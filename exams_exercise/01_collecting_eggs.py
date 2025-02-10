from collections import deque

eggs = deque([int(x)for x in input().split(", ")])
papers = deque([int(x) for x in input().split(", ")])
boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        first_paper = papers.popleft()
        last_peper = papers.pop()
        papers.insert(len(papers), first_paper)
        papers.insert(0, last_peper)
        continue
    current_papper = papers.pop()
    current_sum = current_egg + current_papper
    if current_sum <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")


