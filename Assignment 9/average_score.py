def average_score(filename):
    total_score = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(",")
            total_score += int(score)
            count += 1
    
    return total_score / count 

print(average_score("score.txt"))