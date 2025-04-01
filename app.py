from pattern_matching import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 100000
    step = 10000
    samples_by_size = 20
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Naive Approach | Rabin Karp | KMP")
    for row in table:
        print(row)
