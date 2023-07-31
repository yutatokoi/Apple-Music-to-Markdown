from bs4 import BeautifulSoup
import lxml
import glob

def parse_xml(file_path):
    # Load the file
    with open(file_path, "r") as file:
        content = file.read()

    # Create a BeautifulSoup object
    bs = BeautifulSoup(content, "xml")

    # Initialize empty lists for names and artists
    names = []
    artists = []

    # Find all 'key' tags
    keys = bs.find_all('key')
    
    for i in range(len(keys)):
        # If the key's text is 'Name' or 'Artist', add the next tag's text to the appropriate list
        if keys[i].text == 'Name':
            names.append(keys[i].find_next().text)
        elif keys[i].text == 'Artist':
            artists.append(keys[i].find_next().text)

    return names, artists


# Grab names of all .xml files
pattern = f"*.xml"
xml_files = glob.glob(pattern)

names_of_playlists = []
tracks_in_playlists = []
artists_in_playlists = []
for file in xml_files:
    # Use the function
    names, artists = parse_xml(file)

    playlist_name = names[-1]
    names.pop()
    
    names_of_playlists.append(playlist_name)
    tracks_in_playlists.append(names)
    artists_in_playlists.append(artists)

for i in range(len(names_of_playlists)):
    filename = f"{names_of_playlists[i]}.md"
    with open(filename, "w") as file:
        for j in range(len(tracks_in_playlists[i])):
            song = tracks_in_playlists[i][j]
            musician = artists_in_playlists[i][j]
            file.write(f"- {song}\n")
            file.write(f"    - [[{musician}]]\n")


central_md = "apple-music-playlists.md"
with open(central_md, "w") as playlist_file:
    for playlist in names_of_playlists:
        playlist_file.write(f"- [[{playlist}]]\n")