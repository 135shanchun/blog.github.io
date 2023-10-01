import os

# 获取当前目录下的所有 markdown 文件
files = [file for file in os.listdir('.') if file.endswith('.md')]

# 指定要添加的文字
text_to_add = "<!---->\n<!--more-->\n"

# 遍历每个文件并在第二次出现 "---" 字符串的后面一行添加指定的文字
for file in files:
    with open(file, 'r+', encoding='utf-8') as f:
        content = f.readlines()
        # print(content)
        if "<!--more-->\n" in content:
            print(f'{file}跳过')
            continue
        
        # 查找第二次出现 "---" 字符串的索引
        delimiter_count = 0
        index = -1
        for i, line in enumerate(content):
            if line.strip() == '---':
                delimiter_count += 1
                if delimiter_count == 2:
                    index = i
                    break
        
        if index != -1:
            content.insert(index + 1, text_to_add)
            f.seek(0, 0)
            f.writelines(content)
            print(f"在文件 {file} 的第二个分隔符后添加了指定的文字")
        else:
            print(f"文件 {file} 中未找到第二个分隔符")