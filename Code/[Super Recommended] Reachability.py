"""[Super Recommended] Reachability"""
import json

def main():
    """main"""
    out = []
    check = {}
    graph = str(input())
    graph = graph.replace("'", "\"")
    graph = json.loads(graph)
    link = str(input())
    out.extend(graph[link])
    check[link] = True
    out.append(link)
    count = 0
    while True:
        for i in out:
            if i not in check:
                check[i] = False
            if check[i] is True:
                pass
            else:
                out.extend(graph[i])
                check[i] = True
        count += 1
        if count >= len(out):
            break
    output = list(set(out))
    output.sort()
    print(output)
main()
