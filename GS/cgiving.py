import heapq


class Solutions:
    def giving(self, funds):
        heap = [[0, 'A'], [0, 'B'], [0, 'C']]
        result = []
        for fund in funds:
            c = heapq.heappop(heap)
            result.append(c[1])
            c[0] += fund
            heapq.heappush(heap, c)
        return result


if __name__ == '__main__':
    print(Solutions().giving([25, 8, 2, 35, 15, 120, 55, 42]))
