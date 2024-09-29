import re
import os


def process_wish_url(wish_url):
    print(wish_url)
    print("Link found. You can use this URL in paimon.moe")
    return True


# Assume we're already in the correct folder, path should be something like /HoYoPlay/games/Genshin Impact game/GenshinImpact_Data/webCaches/2.28.0.0/Cache/Cache_Data/
data_file = "data_2"

if os.path.exists(data_file):
    with open(data_file, "rb") as file:
        content = file.read()

    decoded_content = content.decode("latin-1")
    splitted = decoded_content.split("1/0/")[-1]
    match = re.search(r"https.+?game_biz=hk4e_(global|cn)", splitted)

    if match:
        wish_url = match.group(0)
        if process_wish_url(wish_url):
            exit()

    print(
        "No valid link found! Make sure Genshin Impact is installed and open Wish History page at least once."
    )
else:
    print(
        "Genshin Impact cache file not found! Make sure Genshin Impact this script is on the correct folder and open Wish History page at least once."
    )
