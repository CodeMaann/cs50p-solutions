# solved the week0 problem 3 - Making Faces
def changing_the_text_with_emoji (text):
    the_return_text = text.replace(":(", "🙁")
    the_return_text = the_return_text.replace(":)", "🙂")
    return the_return_text

def main():
    text = input()
    print(changing_the_text_with_emoji(text))
    
main()