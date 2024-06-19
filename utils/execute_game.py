import subprocess


def execute_game(game_file):
    try:
        subprocess.Popen(["python", game_file])
    except FileNotFoundError:
        print(f"Error: El archivo {game_file} no fue encontrado.")
