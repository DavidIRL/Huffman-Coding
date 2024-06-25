import heapq as hq

def freq_dict(message):
    freq = {}
    for char in message:
        # count frequency of each char in message
        if char not in freq:
            freq[char] = 1
        freq[char] += 1
    return freq

def make_heap(freq):
    heap = [[freq, [char, '']] for char, freq in freq.items()]
    hq.heapify(heap)
    return heap

def make_code(heap):
    while len(heap) > 1:
        # get 2 smallest freq value nodes
        node1 = hq.heappop(heap)
        node2 = hq.heappop(heap)
        # get [char, ''] of each
        for group in node1[1:]:
            # 0 for left value
            group[1] = '0' + group[1]
        for group in node2[1:]:
            # 1 for right value
            group[1] = '1' + group[1]
        # put back into queue as [added up freq, char/ '' char/ '']
        hq.heappush(heap, [node1[0] + node2[0]] + node1[1:] + node2[1:])
    
    # output sorted by freq heap minus freq value
    return sorted(hq.heappop(heap)[1:], key=lambda code: (len(code[-1]), code))

def make_key(code):
    # turn code list into key dict
    key = {}
    for li in code:
        key[li[0]] = li[1]
    return key

def encode(message, key):
    coded_message = ''
    for char in message:
        coded_message += key[char]
    return coded_message