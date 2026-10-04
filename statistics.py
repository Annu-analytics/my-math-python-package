
# Statistical functions
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers = sorted(numbers)
    mid = len(numbers) // 2

    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]
        
def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)
