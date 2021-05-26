Sym_system = []
Bing_system = []

Bing = open('D:\github\Dissertation\data\Results\Bing API.txt')
Gramm = open('D:\github\Dissertation\data\Results\Grammerly.txt')
Sym = open('D:\github\Dissertation\data\Results\symspell.txt')
Bing_system.append(open('D:\github\Dissertation\data\Results\Bing API\System pass 1.txt'))
Bing_system.append(open('D:\github\Dissertation\data\Results\Bing API\System pass 2.txt'))
Bing_system.append(open('D:\github\Dissertation\data\Results\Bing API\System pass 3.txt'))
Sym_system.append(open('D:\github\Dissertation\data\Results\Symspell\System pass 1.txt'))
Sym_system.append(open('D:\github\Dissertation\data\Results\Symspell\System pass 2.txt'))
Sym_system.append(open('D:\github\Dissertation\data\Results\Symspell\System pass 3.txt'))

Bing_system_lines = []
Sym_system_lines = []
bing_lines = Bing.readlines()
Gramm_lines = Gramm.readlines()
Sym_lines = Sym.readlines()
for file in Bing_system:
    Bing_system_lines.append(file.readlines())
for file in Sym_system:
    Sym_system_lines.append(file.readlines())


count = 1

#
def the_same(lines_in):
    index = 0
    for line in lines_in:
        if line != lines_in[0]:
            print(index)
            return False
        index += 1
    return True

# bing, symspell, grammarly, bing hyb, symspell hyb
for line in bing_lines:
    total_line = []
    total_line.append(line.strip("\n"))
    total_line.append(Sym_lines[count-1].strip("\n"))
    total_line.append(Gramm_lines[count-1].strip("\n"))
    for lines in Bing_system_lines:
        total_line.append(lines[count-1].strip("\n"))
    for lines in Sym_system_lines:
        total_line.append(lines[count-1].strip("\n"))
    # if total_line[1] != total_line[3]:
    #     print(count)
    #     print(total_line)
    if count == 555:
        print(count)
        print(total_line)
    count += 1









def acc(file):
    lines = file.readlines()
    correct = 0
    count = 0

    for line in lines:
        line.lower()
        line = line.strip('\n')
        test = line.split(" ")
        if test[0] == test[1]:
            correct += 1
        count += 1
    return correct/count

# print("bing accuracy: " + str(acc(Bing)))
# print("grammarly accuracy: " + str(acc(Gramm)))
# print("Symspell accuracy: " + str(acc(Sym)))
# count = 1
# for file in Bing_system:
#     print("Bing hybrid accuracy" + " pass " + str(count) + ": " + str(acc(file)))
#     count += 1
# count = 1
# for file in Sym_system:
#     print("Symspell hybrid accuracy" + " pass " + str(count) + ": " + str(acc(file)))
#     count += 1
