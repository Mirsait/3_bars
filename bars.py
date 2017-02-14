import json
import os


def load_data(filepath):
    """ load json-data from file"""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    def b(x): return x['SeatsCount']
    dist = sorted(data, key =b, reverse=True)
    return dist[0]['Name']


def get_smallest_bar(data):
    def b(x): return x['SeatsCount']
    dist = sorted(data, key =b, reverse=False)
    return dist[0]['Name']


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    parse_str = load_data('bars.json')
    print(get_biggest_bar(parse_str))
    print(get_smallest_bar(parse_str))
