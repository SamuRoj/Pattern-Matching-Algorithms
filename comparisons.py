import matplotlib.pyplot as plt
import sys
from pattern_matching import execution_time_gathering


def choose_algortihms():
    sys.setrecursionlimit(5000)

    print("""Please enter the algorithms to test:
    1. Naive Approach
    2. Rabin-Karp
    3. Knuth-Morris-Pratt""")
    algorithms = list(map(int, input().split()))
    algorithmsNames = ["Naive Approach", "Rabin-Karp", "KMP"]

    print("Enter the minimum size of the strings to test:")
    minimum_size = int(input())
    
    print("Enter the maximum size of the strings to test:")
    maximum_size = int(input())

    print("Enter the step: ")
    step = int(input())

    print("Enter the amount of samples by size: ")
    samples_by_size = int(input())

    data = execution_time_gathering.take_execution_time_choose(minimum_size, maximum_size, step, 
                                                               samples_by_size, algorithms)
    
    j = 1
    sizes = [row[0] for row in data]

    for i in algorithms:
        times = [row[j] for row in data]
        plt.scatter(sizes, times, label=algorithmsNames[i-1])
        plt.plot(sizes, times)
        j += 1

    plt.xlabel("Tamaño de los datos")
    plt.ylabel("Tiempo de ejecución en ms")
    plt.title("Comparación algoritmos de decisión de pattern matching")

    plt.legend()

    plt.show()

choose_algortihms()