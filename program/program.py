import sqlite3
import networkx as nx
from tabulate import tabulate

# DATABASE SETUP (SQL)
def setup_database():
    cont = sqlite3.connect('vit_bhopal.db')
    cursor = cont.cursor()
    
    # Create table for campus routes
    cursor.execute('DROP TABLE IF EXISTS routes')
    cursor.execute('''
        CREATE TABLE routes (
            start_node TEXT, 
            end_node TEXT, 
            distance_meters INTEGER,
            crowd_level INTEGER
        )
    ''')

    # Real-world data: Locations and Distances (Weights)
    campus_data = [
        ('Hostel_Block', 'Mess', 200, 5),
        ('Hostel_Block', 'Academic_Block', 600, 2),
        ('Mess', 'Lab_Complex', 300, 8),
        ('Academic_Block', 'Library', 150, 1),
        ('Academic_Block', 'Lab_Complex', 400, 3),
        ('Lab_Complex', 'Sports_Complex', 500, 4),
        ('Library', 'Canteen', 100, 9)
    ]
    
    cursor.executemany('INSERT INTO routes VALUES (?, ?, ?, ?)', campus_data)
    cont.commit()
    return cont

# SEARCH LOGIC AI STRATEGY 
def find_shortest_route(start, destination):
    cont = sqlite3.connect('vit_bhopal.db')
    cursor = cont.cursor()
    
    #Fetch data from SQL to build the graph
    cursor.execute('SELECT start_node, end_node, distance_meters FROM routes')
    rows = cursor.fetchall()
    
    # Using NetworkX to create a Graph
    G = nx.Graph()
    for row in rows:
        G.add_edge(row[0], row[1], weight=row[2])
    
    try:
        # IMPLEMENTING DIJKSTRA'S ALGORITHM (Informed Search)
        path = nx.shortest_path(G, source=start, target=destination, weight='weight')
        total_dist = nx.shortest_path_length(G, source=start, target=destination, weight='weight')
        
        # PRESENTATION 
        table_data = []
        for i, node in enumerate(path):
            table_data.append([f"Step {i+1}", node])
            
        print(f"\n Optimal Route Found from {start} to {destination}")
        print(tabulate(table_data, headers=["Sequence", "Location"], tablefmt="grid"))
        print(f" Total Walking Distance: {total_dist} meters")
        
    except nx.NetworkXNoPath:
        print(" Error: No path found between these two locations.")
    finally:
        cont.close()

#  MAIN EXECUTION 
if __name__ == "__main__":
    setup_database()
    print("VIT Bhopal Campus Navigator")
    print("enter the destination in the same format as in the example ")
    start_loc = input("Enter your current location (e.g., Hostel_Block): ")
    end_loc = input("Enter destination (e.g., Library): ")
    find_shortest_route(start_loc, end_loc)
