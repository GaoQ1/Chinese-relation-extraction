import codecs
import json
from uuid import uuid1

def txt2json_dict(readfile, writefile):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_dict = {}
    for line in f:
        key, value = line.strip().split()
        write_dict[key] = value

    f2.write(json.dumps(write_dict, ensure_ascii=False, indent=2))

    f.close()
    f2.close()


def txt2json_vec(readfile, writefile, fromline):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_data = []
    lines = f.readlines()
    for line in lines[fromline:]:
        temp_dict = {}
        splitdata = line.strip().split()

        word, vec = splitdata[0], splitdata[1:]

        temp_dict["word"] = word
        temp_dict["vec"] = vec

        write_data.append(temp_dict)

    f2.write(json.dumps(write_data, ensure_ascii=False, indent=2))


    f.close()
    f2.close()


def txt2json_data(readfile, writefile):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_data = []
    for line in f:
        temp_dict = {
            "head": {},
            "relation": "",
            "sentence": "",
            "tail": {}
        }
        splitdata = line.strip().split()

        headword, tailword, relation, sentence = splitdata[0], splitdata[1], splitdata[2], splitdata[3:]

        if len(write_data) > 0:
            for item in write_data:
                if item["head"] and item["head"]["word"] == headword:
                    temp_dict["head"] = item["head"]
                elif item["tail"] and item["tail"]["word"] == headword:
                    temp_dict["head"] = item["tail"]
                else:
                    temp_dict["head"] = {
                        "word": headword,
                        "id": str(uuid1())
                    }

                if item["head"] and item["head"]["word"] == tailword:
                    temp_dict["tail"] = item["head"]
                elif item["tail"] and item["tail"]["word"] == tailword:
                    temp_dict["tail"] = item["tail"]
                else:
                    temp_dict["tail"] = {
                        "word": tailword,
                        "id": str(uuid1())
                    }
        else:
            temp_dict["head"] = {
                "word": headword,
                "id": str(uuid1())
            }
            temp_dict["tail"] = {
                "word": tailword,
                "id": str(uuid1())
            }


        temp_dict["sentence"] = ''.join(sentence)
        temp_dict["relation"] = relation

        write_data.append(temp_dict)
        
    f2.write(json.dumps(write_data, ensure_ascii= False, indent=2))
    f.close()
    f2.close()


txt2json_dict('./origindata/relation2id.txt', './data/cndata/rel2id.json')
txt2json_vec('./origindata/vec.txt', './data/cndata/word_vec.json', 1)
txt2json_data('./origindata/train.txt', './data/cndata/train.json')
txt2json_data('./origindata/test.txt', './data/cndata/test.json')
