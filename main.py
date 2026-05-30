# main.py
import tkinter as tk
import team_manager

# Load existing data
players = team_manager.load_players()

def set_team_name():
    team = team_name_entry.get()
    if team != "":
        heading.config(text=f"{team} Performance Tracker")
        output_label.config(text=f"Team name updated to: {team}", fg="green")

def add_player():
    name = name_entry.get()
    spikes_text = spikes_entry.get()
    blocks_text = blocks_entry.get()
    aces_text = aces_entry.get()

    if name == "" or spikes_text == "" or blocks_text == "" or aces_text == "":
        output_label.config(text="Error: Please fill in all fields.", fg="red")
    elif "," in name:
        output_label.config(text="Error: Commas are not allowed in names.", fg="red")
    else:
        try:
            spikes = int(spikes_text)
            blocks = int(blocks_text)
            aces = int(aces_text)

            players.append([name, spikes, blocks, aces])
            team_manager.save_player(name, spikes, blocks, aces)

            # Clear entry boxes
            name_entry.delete(0, tk.END)
            spikes_entry.delete(0, tk.END)
            blocks_entry.delete(0, tk.END)
            aces_entry.delete(0, tk.END)

            output_label.config(text=f"Success: {name} added to the team!", fg="green")
        except:
            output_label.config(text="Error: Stats must be numbers.", fg="red")

def show_awards():
    awards_text = team_manager.calculate_awards(players)
    output_label.config(text=awards_text, fg="blue")

def generate_pdf():
    success = team_manager.create_pdf_report(players)
    if success == True:
        output_label.config(text="Success: 'Team_Report.pdf' saved!", fg="green")
    else:
        output_label.config(text="Error: No players to graph.", fg="red")

def view_roster():
    roster_text = team_manager.get_all_players(players)
    output_label.config(text=roster_text, fg="black")

def search_for_player():
    search_name = name_entry.get()
    result = team_manager.search_player(players, search_name)
    output_label.config(text=result, fg="blue")

def delete_player_button():
    search_name = name_entry.get()
    result = team_manager.delete_player(players, search_name)
    output_label.config(text=result, fg="red")
    name_entry.delete(0, tk.END)

# --- CREATE MAIN WINDOW ---
window = tk.Tk()
window.title("Volleyball Team Tracker")
window.geometry("550x650") 

# --- HEADER SECTION ---
heading = tk.Label(window, text="Volleyball Manager", font=("Arial", 18, "bold"))
heading.pack(pady=10)

team_frame = tk.Frame(window)
team_frame.pack(pady=5)
tk.Label(team_frame, text="Team Name:", font=("Arial", 10)).grid(row=0, column=0)
team_name_entry = tk.Entry(team_frame, font=("Arial", 10), width=20)
team_name_entry.grid(row=0, column=1, padx=5)
tk.Button(team_frame, text="Set", command=set_team_name, bg="lightgrey").grid(row=0, column=2)

# --- MAIN DASHBOARD (SPLIT LEFT & RIGHT) ---
dashboard_frame = tk.Frame(window)
dashboard_frame.pack(pady=15)

# LEFT ZONE: Input Boxes
input_frame = tk.Frame(dashboard_frame, bd=2, relief="groove", padx=15, pady=15)
input_frame.grid(row=0, column=0, padx=10)

tk.Label(input_frame, text="Player Details", font=("Arial", 12, "bold")).pack(pady=(0, 10))

tk.Label(input_frame, text="Player Name:").pack()
name_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
name_entry.pack(pady=2)

tk.Label(input_frame, text="Total Spikes:").pack()
spikes_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
spikes_entry.pack(pady=2)

tk.Label(input_frame, text="Total Blocks:").pack()
blocks_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
blocks_entry.pack(pady=2)

tk.Label(input_frame, text="Total Aces:").pack()
aces_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
aces_entry.pack(pady=2)

# RIGHT ZONE: Player Actions (Add/Search/Delete)
action_frame = tk.Frame(dashboard_frame, bd=2, relief="groove", padx=15, pady=15)
action_frame.grid(row=0, column=1, padx=10, sticky="n")

tk.Label(action_frame, text="Manage Player", font=("Arial", 12, "bold")).pack(pady=(0, 10))

tk.Button(action_frame, text="Add Player", command=add_player, width=15, bg="#b3ffb3").pack(pady=5)
tk.Button(action_frame, text="Search Player", command=search_for_player, width=15, bg="#b3d9ff").pack(pady=5)
tk.Button(action_frame, text="Delete Player", command=delete_player_button, width=15, bg="#ffb3b3").pack(pady=5)
tk.Label(action_frame, text="(Uses Name Box)", font=("Arial", 8, "italic"), fg="grey").pack()

# --- BOTTOM ZONE: Team Reports ---
report_frame = tk.Frame(window, bd=2, relief="groove", padx=10, pady=10)
report_frame.pack(pady=5, fill="x", padx=40)

tk.Label(report_frame, text="Team Reports", font=("Arial", 12, "bold")).pack(pady=(0, 5))

button_row = tk.Frame(report_frame)
button_row.pack()

tk.Button(button_row, text="View Roster", command=view_roster, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_row, text="Show Awards", command=show_awards, width=15).grid(row=0, column=1, padx=5)
tk.Button(button_row, text="Generate PDF", command=generate_pdf, width=15, bg="orange").grid(row=0, column=2, padx=5)

# --- OUTPUT SCREEN ---
output_label = tk.Label(window, text="Ready to track performance...", font=("Arial", 11), justify="center", fg="black")
output_label.pack(pady=15)

# Run app
window.mainloop()