first = input()
second = input()
third = input()
fourth = input()

sign_input = [first, second, third, fourth]
sign_text = []


def check(text) -> bool:
    if len(text) > 16:
        return False
    return True


def center(text) -> str:
    ...


for i in sign_input:
    if not check(i):
        print(f"Максимальная длина 16 символов ({i})")
        break
    else:
        text = center(i)


# text to sign
