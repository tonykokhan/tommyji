import re


def find_main_characters(character_name):
    with open('sanguo.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(character_name, data)
        print('主角 %s 出现 %s 次' % (character_name, len(name_num)))
    return character_name, len(name_num)
    # return len(name_num)    # 报错


# 读取人物信息
name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            char_name, char_number = find_main_characters(n)
            name_dict[char_name] = char_number
            # print(char_name)
            # print(char_number)


# 读取武器信息
weapon_dict = {}
with open('weapon.txt', encoding='UTF-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            # weapon_name, weapon_number = find_main_characters(line.strip('\n'))
            weapon_name, weapon_number = find_main_characters(line.strip())
            weapon_dict[weapon_name] = weapon_number
        i += 1


name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
print(weapon_sorted[0:10])

