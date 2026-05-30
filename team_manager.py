# team_manager.py
import matplotlib.pyplot as plt

def load_players():
    # Data Structure: Returns a list of lists containing player data
    players = []
    try:
        # Opens the file in read mode as taught in class
        file = open("players.txt", "r")
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            spikes = int(data[1])
            blocks = int(data[2])
            aces = int(data[3])
            
            # Appends the player as a list inside the main list
            players.append([name, spikes, blocks, aces])
        file.close()
    except:
        # If the file does not exist yet, we just pass and return an empty list
        pass
        
    return players

def save_player(name, spikes, blocks, aces):
    # Opens the file in 'a' (append) mode to add a new line without deleting old data
    file = open("players.txt", "a")
    file.write(f"{name},{spikes},{blocks},{aces}\n")
    file.close()

def calculate_awards(players):
    # Algorithm to determine award winners based on stats
    if len(players) == 0:
        return "No players have been added yet."

    best_attacker = ""
    highest_spikes = -1

    best_defender = ""
    highest_blocks = -1

    mvp = ""
    highest_total = -1

    # Loop through the list to compare player stats
    for player in players:
        name = player[0]
        spikes = player[1]
        blocks = player[2]
        aces = player[3]

        # Algorithm 1: Find highest spikes
        if spikes > highest_spikes:
            highest_spikes = spikes
            best_attacker = name
        
        # Algorithm 2: Find highest blocks
        if blocks > highest_blocks:
            highest_blocks = blocks
            best_defender = name

        # Algorithm 3: Find MVP (total of all stats)
        total = spikes + blocks + aces
        if total > highest_total:
            highest_total = total
            mvp = name

    # Use f-strings to format the output text
    report = f"Best Attacker: {best_attacker} ({highest_spikes} Spikes)\n"
    report += f"Best Defender: {best_defender} ({highest_blocks} Blocks)\n"
    report += f"Team MVP: {mvp} ({highest_total} Total Points)"
    
    return report

def create_pdf_report(players):
    # Creates a simple bar chart and saves it as a PDF
    if len(players) == 0:
        return False

    names = []
    totals = []

    # Loop to gather data for the graph
    for player in players:
        names.append(player[0])
        total_score = player[1] + player[2] + player[3]
        totals.append(total_score)

    # Generate Matplotlib chart
    plt.bar(names, totals, color='blue')
    plt.title("Overall MVP Points per Player")
    plt.xlabel("Player Name")
    plt.ylabel("Total Stats (Spikes + Blocks + Aces)")
    
    # Save the chart to a PDF file
    plt.savefig("Team_Report.pdf")
    plt.clf() # Clears the chart so it doesn't overlap if run twice
    
    return True

def get_all_players(players):
    # Algorithm to format all players into a readable list (Practice Code 2)
    if len(players) == 0:
        return "No players in the system."
    
    report = "--- TEAM ROSTER ---\n"
    for player in players:
        name = player[0]
        spikes = player[1]
        blocks = player[2]
        aces = player[3]
        report += f"Player: {name} | Spikes: {spikes} | Blocks: {blocks} | Aces: {aces}\n"
    
    return report

def search_player(players, search_name):
    # Algorithm to search for a specific player (Practice Code 1)
    if search_name == "":
        return "Please enter a name to search."

    for player in players:
        # .lower() makes it so "Sam" and "sam" both work
        if player[0].lower() == search_name.lower():
            name = player[0]
            spikes = player[1]
            blocks = player[2]
            aces = player[3]
            return f"FOUND {name}:\nSpikes: {spikes}\nBlocks: {blocks}\nAces: {aces}"
    
    return "Player not found."

def delete_player(players, delete_name):
    # Algorithm to find and remove a player, then update the text file
    if delete_name == "":
        return "Please enter a name to delete."

    for i in range(len(players)):
        if players[i][0].lower() == delete_name.lower():
            # Remove from the Python list
            removed_player = players.pop(i)
            
            # Open file in "w" (write) mode to overwrite the old file completely
            file = open("players.txt", "w")
            for p in players:
                file.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")
            file.close()
            
            return f"SUCCESS: {removed_player[0]} has been removed from the team."
    
    return "Error: Player not found. Cannot delete."