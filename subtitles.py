
def get_clear_text(lines):
    skip_list = ["-->","</c>"]
    last_line = ""
    ret = []
    for line in lines:
        skip = False
        for s in skip_list:
            if s in line:
                skip = True
                break
        if skip or line.strip(" \t\n") == "":
            continue
        if line == last_line:
            continue
        last_line = line
        ret.append(line.strip(" \t\n"))
    return ret

if __name__ == "__main__":
    f = open("q4DFuQ8hfqQ.ru.vtt", "r")
    lines = f.readlines()
    f.close()
    ret=get_clear_text(lines)
    for l in ret:
        print(l)
