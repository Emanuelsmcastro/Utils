import json

information1 = {'name': 'Eu', 'idade': 20}
information2 = {'name': 'Eu2', 'idade': 300}
information3 = {'name': 'Eu3', 'idade': 300}


def open_json(filename, method):
    return open(filename + '.json', f'{method}')


def format_to_json(information):
    return json.dumps(information, indent=4)


def format_to_dict(information):
    return json.loads(information)


def structure_json(key):
    json_list = []
    return {f'{key}': json_list}


def writer(filename, key, information_dict, append=True):
    struct_json = structure_json(key)
    if append:
        struct_json[key].append(information_dict)
    else:
        struct_json[key] = information_dict
    formatted_information = format_to_json(struct_json)
    with open_json(filename, 'w') as file_writer:
        file_writer.write(formatted_information)


def write_json(filename, key, information_dict):
    if len(load_json(filename)) == 0:
        writer(filename, key, information_dict)
    else:
        content = load_json(filename)
        key_content = content[key]
        key_content.append(information_dict)
        writer(filename, key, key_content, append=False)


def load_json(filename):
    try:
        with open_json(filename, 'r') as file_reader:
            file_contents_string = file_reader.read()
        file_contents_dict = format_to_dict(file_contents_string)
        return file_contents_dict
    except json.decoder.JSONDecodeError:
        return {}


write_json('test', 'people', information3)

test = load_json('test')

for key, info in test.items():
    print(key)
    for i in info:
        print(i)
