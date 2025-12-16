def answer(strings_list):
    return min(strings_list, key=len)

if __name__ == "__main__":
    input_data = ["code", "backend", "ai", "circle"]
    print(answer(input_data))
