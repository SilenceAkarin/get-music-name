import os, sys, tinytag

def get_folder(folder):
    filenames = []
    for filename in os.listdir(folder):
        if filename.endswith(".flac"):
            filenames.append(filename.replace(".flac", ""))
    return filenames  # 返回包含文件名的列表

def remove_left_numbers_and_dash(names):
    new_names = []
    for name in names:
        # 分割字符串，最大分割次数为1
        parts = name.split(" - ", 1)
        if len(parts) > 1:
            # 如果字符串被分割，那么我们取第二部分
            new_names.append(parts[1])
        else:
            # 如果字符串没有被分割，那么我们保留原来的字符串
            new_names.append(name)
    return new_names

# def get_music_

if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        folder = ' '.join(sys.argv[1:])
        print("\n".join(remove_left_numbers_and_dash(get_folder(folder))))
    else:
        print("请提供一个文件路径")


# 读取文件
# filenameInput = input("请输入文件名")
# filename = filenameInput.replace("\\" , "\\\\")