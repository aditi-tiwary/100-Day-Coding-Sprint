def count_consistent_cars(components, n, models):
    allowed = set(components)
    count = 0

    for model in models:
        is_consistent = True
        for ch in model:
            if ch not in allowed:
                is_consistent = False
                break
        if is_consistent:
            count += 1

    return count


if __name__ == '__main__':
    components = input().strip()
    n = int(input().strip())
    models = input().split()
    
    result = count_consistent_cars(components, n, models)
    print(result)
