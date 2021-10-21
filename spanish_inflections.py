
rules_adjetive = []
with open("MM.adj.txt",'r') as f:
    for line in f.readlines():
        rule = line.split()
        rules_adjetive.append({"word":rule[0], "lemma":rule[1], "code":rule[2]})

rules_noun = []
with open("MM.nom.txt",'r') as f:
    for line in f.readlines():
        rule = line.split()
        rules_noun.append({"word":rule[0], "lemma":rule[1], "code":rule[2]})

def search_rule(rules, word):
    for rule in rules:
        if word == rule["word"]:
            return rule
    return None

def search_word(rules, lemma, code):
    for rule_i in rules:
        if lemma == rule_i["lemma"] and code == rule_i["code"]:
            return rule_i["word"]
    return ""

def search_noun(noun):
    rule = search_rule(rules_noun, noun)
    if rule is None:
        return {"original": noun}
    else:
        lemma = rule["lemma"]
        code = rule["code"]
        result_i = {"original": noun}
        for sub_code in ["S","P"]:
            code = code[:3] + sub_code + code[4:]
            result_i[code[2:4]] = search_word(rules_noun, lemma, code)
        return result_i

def search_adjetive(adjetive):
    rule = search_rule(rules_adjetive, adjetive)

    if rule is None:
        return {"original": adjetive, "FS": "", "FP": "", "MS": "", "MP": ""}
    else:
        lemma = rule["lemma"]
        code = rule["code"]
        result_i = {"original": adjetive}
        for sub_code in ["FS","FP","MS", "MP", "CS", "CP"]:
            code = code[:3] + sub_code + code[5:]
            result_i[sub_code] = search_word(rules_adjetive, lemma, code)

        if result_i["CS"] != "":
            for sub_code in ["FS","MS"]:
                result_i[sub_code] = result_i["CS"]
            for sub_code in ["FP","MP"]:
                result_i[sub_code] = result_i["CP"]

        if result_i["FS"] == "":
            for sub_code in ["FS","MS"]:
                result_i[sub_code] = result_i["MS"]
            for sub_code in ["FP","MP"]:
                result_i[sub_code] = result_i["MP"]

        if result_i["MS"] == "":
            for sub_code in ["FS","MS"]:
                result_i[sub_code] = result_i["FS"]
            for sub_code in ["FP","MP"]:
                result_i[sub_code] = result_i["FP"]

        del result_i["CS"]
        del result_i["CP"]
        return result_i
