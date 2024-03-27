import os
import random
import unicodedata

from mastodon import Mastodon


def setrange(*args):
    return set(range(*args))


GOOD_RANGES = {
    # range, word index
    'taixuanjing': ({*setrange(119556,119639)}-{119571}, -1),

    'greekgods': (range(11223, 11240), -1),
    'kangxi': (range(12032, 12246), -1),
    'ideograph': (range(12832, 12873), -1),
    'phaistos': (range(66000, 66046), 3),
    'emoji': (
        setrange(127789, 128765)
        - setrange(127995, 128000)
        - setrange(128337, 128348)
        - setrange(128408, 128420)
        - setrange(128728, 128733)
        - setrange(128749, 128752)
        | setrange(129292, 129536),
        -1),
    'alchemy': (setrange(128768, 128884), 3),
}


def get_poem(wordrange=(9, 15), wordsep="  \n", dictionary="taixuanjing"):
    RANGE, INDEX = GOOD_RANGES[dictionary]
    coolwords = [unicodedata.name(chr(i)).split()[INDEX] for i in RANGE]
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
