import re
import pyperclip


def format(text):
    # 行末のハイフンと改行を削除
    lines = re.split("\n", text)
    output = ""
    for line in lines:
        line = line.rstrip()
        if line:
            if line[-1] == "-":
                # 末尾がハイフンなら、そのまま連結
                output += line[:-1]
            else:
                # そうでなければ、スペースで連結
                output += line + " "
    return output


def main():
    text = pyperclip.paste()
    formated = format(text)
    pyperclip.copy(formated)


if __name__ == "__main__":
    main()
