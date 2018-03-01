from tqdm import tqdm


def removeNumbers(words):
    norm_words = []
    nums = '1234567890'

    for w in tqdm(words):
        word = w
        for nm in nums:
            if nm in word:
                word = "NUM"

        if not word == "NUM":
            norm_words.append(word)

    norm_words = set(norm_words)
    return norm_words


def removePunctuation(words):
    norm_words = []
    chars = ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'', '?', '%', '^', '&', '<', ';', ':', '"', ',', '/', '@', '=']

    for w in tqdm(words):
        word = w
        for ch in chars:
            if ch in word:
                word = word.replace(ch, '')

        norm_words.append(word)

    norm_words = set(norm_words)
    return norm_words

def main():
    file_path = "..\\data\\vocab"
    file = open(file_path, 'r')

    lines = file.read()
    lines = lines.split()

    lines = removePunctuation(lines)
    lines = removeNumbers(lines)

    data = '\n'.join(lines)

    file_path = "..\\data\\vocab_normal"
    file = open(file_path, 'w')
    file.write(data)

main()
