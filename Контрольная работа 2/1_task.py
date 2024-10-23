import re
def compress_string(S):
    # Шаблон
    pattern = r"(.)\1{4,}"
    def replace(match):
        char = match.group(1)
        count = len(match.group(0))
        return f"{char}{{{count}}}"
    return re.sub(pattern, replace, S)

S = input()
compressed_S = compress_string(S)
print(compressed_S)

