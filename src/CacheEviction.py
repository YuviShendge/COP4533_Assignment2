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

def lru(k, requests):
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
def optff(k, requests):
    cache = []
    misses = 0
    m = len(requests)

    for i in range(m):
        r = requests[i]

        if r in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.append(r)
        else:
            # find  next request occurs farthest in the future
            farthest_index = -1
            item_to_remove = None

            for item in cache:
                if item in requests[i+1:]:
                    next_use = requests[i+1:].index(item)
                else:
                    next_use = float('inf')

                if next_use > farthest_index:
                    farthest_index = next_use
                    item_to_remove = item

            cache.remove(item_to_remove)
            cache.append(r)

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
    lru_misses = lru(k, requests)
    optff_misses = optff(k, requests)

    print("FIFO  :", fifo_misses)
    print("LRU  :", lru_misses)
    print("OPTFF :", optff_misses)



if __name__ == "__main__":
    main()