import queue as Q
dict_gn = {
    'Arad': {'Zerind': 32, 'Sibiu': 2, 'Timisoara': 10},
    'Zerind': {'Arad': 75, 'Sibiu': 2},
    'Sibiu': {'Timisoara': 10},
    'Timisoara': {'Arad': 34}
    }
dict_hn = {
    "Arad": 34,
    "Sibiu": 78,
    "Zerind": 33,
    "Timisoara": 110
}
start = 'Arad'
goal = 'Timisoara'
result=''

def get_fn(city_path):
    cities = city_path.split(",")
    hn=gn = 0
    for i in range(0,len(cities) - 1):
        gn += dict_gn[cities[i]][cities[i + 1]]
    hn = dict_hn[cities[-1]]
    return gn + hn

def a_star_search(start, goal):
    cityq = Q.PriorityQueue()
    cityq.put((get_fn(start), start, start))  
    visited = set()

    while not cityq.empty():
        fn, path, current_city = cityq.get()
        if current_city in visited:
            continue
        visited.add(current_city)

        if current_city == goal:
            return f"{path} :: {fn}"

        for neighbor in dict_gn[current_city]:
            if neighbor not in visited:
                new_path = path + "," + neighbor
                cityq.put((get_fn(new_path), new_path, neighbor))
    
    return " path found."

def main():
    
    result = a_star_search(start, goal)
    print("The A* path with the total is:")
    print(result)

main()
