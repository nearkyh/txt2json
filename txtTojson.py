# txt --> json

def convert(txtFile_name, jsonFile_path, file_format):
    txt_file = open("./{}".format(txtFile_name), 'r')
    lines = txt_file.readlines()
    data = []
    for line in lines:
        line = line[:-1]    # \n 제거
        line = line.strip() # 양쪽 끝 공백 제거
        data.append(line)   # 한줄씩 리스트로 담기

    json_file = open("./alignment.json", 'w')
    count = 0
    json_file.write("{\n")
    for contents in data:
        count += 1
        data = '  "{}/{}{}": "{}",\n'.format(jsonFile_path, count, file_format, contents)
        json_file.write(data)

    json_file.write("}")
    json_file.close()
    txt_file.close()

    print("Conversion complete !!!")


txtFile_name = "./연설문.txt"
jsonFile_path = "./datasets/polly/audio"
file_format = ".wav"
convert(txtFile_name, jsonFile_path, file_format)
