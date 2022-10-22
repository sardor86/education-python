def read_last(file, lines: int) -> str: return "\n".join(file.read().split("\n")[::-1][:lines+1])

