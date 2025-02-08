def echo(text: str, repetitions: int = 3) -> str:
    """Makes an echo."""
    text = text.strip().split()[-1]  
    result = "\n".join(text[-i:] for i in range(repetitions, 0, -1)) + "\n."
    return result  

if __name__ == "__main__":
    user_input = input("Yell something at a mountain: ")
    print(echo(user_input, len(user_input.split()[-1])))  
