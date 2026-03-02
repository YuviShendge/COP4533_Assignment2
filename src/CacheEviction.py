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

def lru_policy(k, requests):
    cache = []
    last_used = {}
    misses = 0

    for time in range(len(requests)):
        r = requests[time]
        if r in cache:
            last_used[r] = time
        else:
            misses += 1

            if len(cache) < k:
                cache.append(r)
                last_used[r] = time
            else:
                # to remove the most recent access time is the oldest
                lru_item = min(cache, key=lambda x: last_used[x])
                cache.remove(lru_item)

                cache.append(r)
                last_used[r] = time

    return misses

def main():
    if len(sys.argv) != 2:
        print("Usage: python cache_sim.py <input_file>")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        first_line = f.readline().strip().split()
        k = int(first_line[0]) # capacity
        m = int(first_line[1]) # seq of requests

        requests = list(map(int, f.readline().strip().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru_policy(k, requests)

    print("FIFO  :", fifo_misses)
    print("LRU  :", lru_misses)



if __name__ == "__main__":
    main()