import sys

def fifo(k, requests):
    cache = []
    misses = 0

    for r in requests:
        if r in cache:
            continue  # this is a hit

        misses += 1

        if len(cache) < k:
            cache.append(r)
        else:
            # remove the first
            cache.pop(0)
            cache.append(r)

    return misses

def main():
    if len(sys.argv) != 2:
        print("Usage: python cache_sim.py <input_file>")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        first_line = f.readline().strip().split()
        k = int(first_line[0])

        requests = list(map(int, f.readline().strip().split()))

    fifo_misses = fifo(k, requests)

    print("FIFO  :", fifo_misses)


if __name__ == "__main__":
    main()