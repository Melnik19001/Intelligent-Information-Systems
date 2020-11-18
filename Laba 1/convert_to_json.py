import json

class Parser:
    def __init__(self):
        pass

    def parse(self, source_file, destination_file):
        result = []
        with open(source_file, 'r') as file:
            for line in file:
                if line == '\n':
                    continue
                data = line.split('=>')
                assert len(data) == 2
                if_statement = self.parse_if(data[0])
                then_statement = self.parse_then(data[1])
                result.append({'if': if_statement, 'then': then_statement})

        with open(destination_file, 'w') as file:
            json.dump(result, file, indent=2, ensure_ascii=False)

    def parse_if(self, statement):
        statements = statement.split('&')
        res = []
        for statement in statements:
            key, value = map(self.erase_spaces, tuple(statement.split('=')))
            res.append({"condition": key, "consequence": value})
        return res

    def parse_then(self, statement):
        key, value = map(self.erase_spaces, tuple(statement.split('=')))
        return {"target": key, "value": value}

    def erase_spaces(self, text):
        while len(text) and text[-1] in [' ', '\n']:
            text = text[:-1]
        while len(text) and text[0] in [' ', '\n']:
            text = text[1:]
        return text


if __name__ == '__main__':
    Parser().parse('data/melnichenka_rules_new.txt', 'data/rules.json')
