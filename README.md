# What’s this project about?
I built this Python-based Campus Navigation System specifically to solve a common problem at VIT Bhopal University: getting lost. Whether you're a first-year student trying to find a specific lab or a parent visiting for the first time, navigating a massive, growing campus can be a headache. This tool acts as a "mini-GPS" in your terminal, mapping out the best routes between academic blocks, hostels, and the lab complex so you don't have to wander around aimlessly
# Key Features
Custom Campus Map: I’ve pre-mapped all the essential buildings and landmarks across the university so the system knows exactly where everything is located.

Smart Pathfinding: It doesn't just give you any route; it uses AI search logic to find the absolute quickest way to get where you're going.

Simple Pick-and-Go: You don't need to type in coordinates—just choose your starting point and destination from the list of campus nodes.

Built-in Reality Check: The system double-checks your inputs to make sure the locations exist and that there’s an actual traversable path between them.

Follow-the-Breadcrumbs: Instead of a confusing map, it gives you a clean, text-based list of landmarks and turns to follow.

Know the Walk: It calculates the total distance of your trip so you can figure out if you need to hurry or if you have time for a coffee break.
# Tech Stack & Tools
Language: Python 3

Interface: Command Line (keeping it lightweight and fast)

The "Brain": AI Search Algorithms (specifically Dijkstra’s and A*)

# How to Get it Running
Prep: Make sure you have Python installed on your machine.

Grab the Code: Download or clone the project files from my repository.

Terminal Setup: Open your command prompt or terminal and head into the project folder: cd CampusNavigator.

Fire it Up: Run the script by typing: python navigator.py.
# Testing it Out
Start the program to see a full list of available campus spots (like the Lab Complex or Boys Hostel).

Type in where you’re standing right now (Current Location).

Tell the system where you want to go (Destination).

# The system will then:

Make sure both spots are actually on the campus map.

Run the AI logic to find the smartest shortcut.

Print out your step-by-step path and tell you exactly how far the walk is.
