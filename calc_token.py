import tiktoken
import json
import sys
from tqdm import tqdm

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def main(json_file_path):
    # 打开并读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # 加载JSON文件内容到data变量

    # 收集所有唯一出现过的键
    all_keys = set()
    for element in data:
        if isinstance(element, dict):
            all_keys.update(element.keys())

    # 初始化key的token统计字典
    tokens_per_key = {key: 0 for key in all_keys}

    # 使用tqdm创建进度条
    for element in tqdm(data, desc="Processing JSON elements"):
        if isinstance(element, dict):
            # 仅为当前字典中存在的键更新计数
            for key in all_keys.intersection(element.keys()):
                num = num_tokens_from_string(element[key], "cl100k_base")
                tokens_per_key[key] += num

    # 计算并添加总的token数量
    total_tokens = sum(tokens_per_key.values())
    tokens_per_key['total'] = total_tokens

    print(tokens_per_key)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_file_path>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    main(json_file_path)
