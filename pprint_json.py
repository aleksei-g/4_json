import json
import os.path


def load_data(filepath):
    with open(filepath, 'r', encoding='utf_8') as f:
        data = json.loads(f.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    while True:
        filepath = input('Enter file path: ')
        if os.path.exists(filepath):
            break
        else:
            print('File not found!')
    data = load_data(filepath)
    pretty_print_json(data)
