
def connectedComponents(n, graph):
    visited = [False] * n
    components = 0

    def dfs(start):
        stack = [start]
        while stack:
            start = stack[-1]

            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True

            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1

    return components


def roadsAndLibraries(n, c_lib, c_road, cities):
    dic = {x: [] for x in range(n)}

    for f, to in cities:
        dic[min(f - 1, to - 1)].append(max(f - 1, to - 1))
    numberOfComponents = connectedComponents(n, dic)
    libraryPerCity = n * c_lib
    librayPerComponent = ((n - numberOfComponents) * c_road) + \
        (numberOfComponents * c_lib)
    return min(libraryPerCity, librayPerComponent)
