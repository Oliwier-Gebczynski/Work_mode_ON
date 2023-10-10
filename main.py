import subprocess


def read_from_file(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()

        ide_path = (lines[0].split('"'))[1]
        first_url = (lines[1].split('"'))[1]
        second_url = (lines[2].split('"'))[1]
        spotify_path = (lines[3].split('"'))[1]
        spotify_playlist = (lines[4].split('"'))[1]

        list = [ide_path, first_url, second_url, spotify_path, spotify_playlist]

        return list
    except FileNotFoundError:
        print("File error!")


result = read_from_file("configuration.txt")

subprocess.Popen([result[0]])

subprocess.Popen(['firefox', result[1]])
subprocess.Popen(['firefox', result[2]])

subprocess.Popen([result[3], f'--uri=spotify:playlist:{result[4]}'])
