# -*- coding: utf8 -*-

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code

# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"
    return message


def is_help_command(user_input:str):
    if user_input.lower() in ('h', "help"):
      return True
    return False

def is_validated_english_sentence(user_input:str):
    new = ''
    for u in user_input:
      if (u.isdigit()) or (u in r"""_@#$%^&*()-+=[]{}"';:\|`~"""):
        return False
      if not u in " .,!?":
        new += u
    if not new: # new가 공백이라면
      return False
    return True

def is_validated_morse_code(user_input:str):
    for u in user_input:
      if not u in "-., " :
        return False
    for u1 in user_input.split():
      if u1 not in get_morse_code_dict().values():
        return False
    return True
    
def get_cleaned_english_sentence(raw_english_sentence:str):
    new = ''
    for r in raw_english_sentence:
      if r not in ".,!?":
        new += r
    return new.strip() # 예제에서는 왼쪽 공백을 잡아주지 못했다.

def decoding_character(morse_character):
    inv_map = {v: k for k, v in get_morse_code_dict().items()}
    return inv_map[morse_character]

def encoding_character(english_character):
    return get_morse_code_dict()[english_character.upper()]

def decoding_sentence(morse_sentence):
    res = []
    for m in morse_sentence.split(' '):
      if m:
        res.append(decoding_character(m))
      else:
        res.append(' ')
    return ''.join(res)

def encoding_sentence(english_sentence):
    res = []
    for word in english_sentence.split():
      tmp = ''
      for w in word:
        tmp += encoding_character(w)+' '
      res.append(tmp)
    return ' '.join(res).strip() 

def main():
    print("Morse Code Program!!")
    
    while 1:
      input_ = input("Input your message(H - Help, 0 - Exit): ")
      if input_ == '0':
        break
      elif is_help_command(input_):
        print(get_help_message())
      else:
        if is_validated_english_sentence(input_):
          print(encoding_sentence(get_cleaned_english_sentence(input_)))
        elif is_validated_morse_code(input_):
          print(decoding_sentence(input_))
        else:
          print("Wrong Input")

    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()