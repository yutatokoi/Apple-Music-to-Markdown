# Apple-Music-to-Markdown
Archive Apple Music playlists to Markdown format

### Instructions
1. On the desktop app version of Apple Music click on a playlist. Then go to `File >> Library >> Export Playlist...`   Save the playlist as a `.xml` file.
2. Move the `.xml` files to the `Apple-Music-to-Markdown` folder.
3. Run `main.py`, making sure BeautifulSoup, and lxml are installed.
  (BeautifulSoup: https://pypi.org/project/beautifulsoup4/)
  (lxml: https://pypi.org/project/lxml/)

The playlists should be exported to a `.md` format, with the playlist name as the filename, and in each `.md`, the name of the song, as well as the name of the artist, in double bracket links.

<img width="751" alt="example-playlist" src="https://github.com/yutatokoi/Apple-Music-to-Markdown/assets/69610953/900ac781-7422-4ed0-a0d3-0fc3350207a1">
