import argparse
import pandas as pd

from collections import (Counter, defaultdict)

parser = argparse.ArgumentParser()
parser.add_argument('data', type=str)


def get_msg_counter(data):
    return sorted(Counter(data['User']).items(),
                  key=lambda x: x[1], reverse=True)


def get_word_counter(data):
    counter = defaultdict(lambda: 0)

    for idx, row in data.iterrows():
        counter[row['User']] += len(row['Message'].strip().split(' '))
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


def get_freq_counter(data):
    counter = defaultdict(lambda: defaultdict(lambda: 0))
    stats = dict()
    for idx, row in data.iterrows():
        words = row['Message'].strip().split(' ')
        for word in words:
            counter[row['User']][word] += 1

    for user in counter.keys():
        stats[user] = sorted(counter[user].items(),
                             key=lambda x: x[1], reverse=True)[:8]

    return stats


if __name__ == '__main__':
    args = parser.parse_args()
    kakaodata = pd.read_csv(args.data)
    print(kakaodata, end='\n\n')

    print(get_msg_counter(kakaodata))
    print(get_word_counter(kakaodata))

    stats = get_freq_counter(kakaodata)
    for user in stats.keys():
        print(user, stats[user])
