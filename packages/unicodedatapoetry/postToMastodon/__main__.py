import os
import random
import unicodedata

from mastodon import Mastodon


GOOD_RANGES = {
    # start, length, word index
    'taixuanjing': (119556, 83, -1),

    'emoji0': (9900, 100, 0),
    'greekgods': (11223, 17, -1),
    'kangxi': (12032, 213, -1),
    'ideograph': (12832, 40, -1),
    'phaistos': (66000, 45, -1),
    'weather': (127744, 43, -1),
    'emoji1': (127789, 975, -1),  # with some gaps
    'alchemy': (128768, 115, 3),
    'emoji2': (129292, 249, -1),
}


def get_poem(wordrange=(9, 15), wordsep="  \n", dictionary="taixuanjing"):
    START, LENGTH, INDEX = GOOD_RANGES[dictionary]
    coolwords = [unicodedata.name(chr(START + i)).split()[INDEX] for i in range(LENGTH)]
    wordcount = random.randrange(*wordrange)

    words = random.sample(coolwords, wordcount)
    spacers = random.choices(wordsep, k=wordcount)

    return "".join(w + s for w, s in zip(words, spacers)).strip()


def post_to_mastodon(poem):
    client = Mastodon(
        client_id=os.environ["MASTODON_CLIENT_ID"],
        client_secret=os.environ["MASTODON_CLIENT_SECRET"],
        access_token=os.environ["MASTODON_ACCESS_TOKEN"],
        api_base_url=os.environ["MASTODON_BASE_URL"]
    )

    client.status_post(poem)


def main(args):
    poem = get_poem()
    post_to_mastodon(poem)
    return {"body": poem}
