import json
import os.path
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf_8') as f:
        return json.load(f)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def createParser():
    parser = argparse.ArgumentParser(description='Чтение файлов  json \
                                     в удобном формате')
    parser.add_argument('-f', '--file', required=True, metavar='ФАЙЛ',
                        help='Путь до файла в формате json.')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    data = load_data(namespace.file)
    if data:
        pretty_print_json(data)
    else:
        print('Файл не найден!')
