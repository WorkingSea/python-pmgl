## Purpose
Intended for use on https://paimon.moe/ as an alternative to their script, the reason for that is that I play Genshin Impact on Linux with wine.
You can use the URL outputted by this script during step 10 on Paimon.Moe's wish import page: https://paimon.moe/wish/import.
## Prerequisites

- Python 3.x installed
- Genshin Impact installed and cache data available
- The script assumes you have opened your Wish History in Genshin Impact at least once, as this generates the necessary cache data.


## Usage

1. Place the `extract_wish.py` file in the same directory as Genshin Impact's cache data. If you installed the game with Lutris that path should be:
   `~/Games/genshin-impact/drive_c/Program Files/HoYoPlay/games/Genshin Impact game/GenshinImpact_Data/webCaches/2.28.0.0/Cache/Cache_Data/`

2. Open a terminal in the same directory.

3. Run the following command:
   ```
   python extract_wish.py
   ```

4. If a valid Wish URL is found, it will be printed to the terminal. You can copy this URL and proceed to Step 10 on https://paimon.moe/wish/import to import your wish history.
   
## Note
- The script is designed to work on Linux, but should be compatible with other operating systems as well.
- If the script fails to find a valid Wish URL, double-check that you have the correct file on the correct folder and have opened the Wish History page in Genshin Impact.
