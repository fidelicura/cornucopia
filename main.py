from lib.server import GSIServer
import tkinter as tk
import os


TOKEN = "hello1234"


# gsi server initializator
def server_starter():
    # initializing gsi server with starting
    server = GSIServer(("127.0.0.1", 3000), TOKEN)
    server.start_server()
    print("[LOG]: Listening server at `127.0.0.1:3000`.")

    return server


# game info parser from server_started (gsi server)
def data_parser(server):
    # game info to use
    try:
        gpm = server.game_state.player.gold_per_minute
        xpm = server.game_state.player.experience_per_minute
        ks = server.game_state.player.kill_streak
        bb_cost = server.game_state.hero.buyback_cost
        match_id = server.game_state.map.match_id

        result = [gpm, xpm, ks, bb_cost, match_id]
        print(f"""[LOG]: Game info
GPM: {result[0]}
XPM: {result[1]}
Streak: {result[2]}
Buyback: {result[3]}
Match: {result[4]}""")

        return result
    except Exception as _ex:
        print("[ERROR]: No game found. Restart app.")
        os._exit(0)


# server instance
gsi_server = server_starter()
print("[LOG]: Server instance created.")


# ui with info
def main():
    # taking game info from data_parser with server_starter as gsi server
    game_info = data_parser(gsi_server)
    print("[LOG]: Server instance initialized.")

    # initiliazing window
    root = tk.Tk()
    root.geometry("140x150+5+130")
    root.resizable(False, False)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "#3c4f5b")
    root.config(bg="#3c4f5b")
    root.overrideredirect(True)


    # initializing labels of game info
    gpm_label = tk.Label(root, text=f"GPM: {game_info[0]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
    xpm_label = tk.Label(root, text=f"XPM: {game_info[1]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
    ks_label = tk.Label(root, text=f"Streak: {game_info[2]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
    bb_cost_label = tk.Label(root, text=f"Buyback cost: {game_info[3]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
    match_id = tk.Label(root, text=f"Match: {game_info[4]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
    print("[LOG]: Initialized labels.")
    

    # packing labels
    gpm_label.pack(side="top", anchor="w")
    xpm_label.pack(side="top", anchor="w")
    ks_label.pack(side="top", anchor="w")
    bb_cost_label.pack(side="top", anchor="w")
    match_id.pack(side="top", anchor="w")
    print("[LOG]: Packed labels.")


    # updating values every second
    def update_labels():
        game_info = data_parser(gsi_server)
        if game_info[0] == None:
            print("[ERROR] No game found. Restart app.")
            os._exit(0)
        
        gpm_label.config(text=f"GPM: {game_info[0]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
        xpm_label.config(text=f"XPM: {game_info[1]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
        ks_label.config(text=f"Streak: {game_info[2]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
        bb_cost_label.config(text=f"Buyback: {game_info[3]}", font=("Calibri", 12, "bold"), bg="#3c4f5b", fg="#e1e6f5")
        print("[LOG]: Updated labels.")

        root.after(300, update_labels)


    # update values every second and loop for app not to close by itself
    root.after(300, update_labels)
    print("[LOG]: First time updated labels.")

    root.mainloop()


if __name__ == "__main__":
    print("[LOG]: Program started.")
    main()