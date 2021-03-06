#我的方法
def checkio(text):

    # replace this for solution
    text = text.lower()
    a = []
    num = 0

    for i in text:
        if i.isalpha():
            a.append(i)
            a.sort()
    # print(a)
    for m in a:
        if a.count(m) > num:
            num = a.count(m)
            c = m
    print(c)
    return c

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")



#最好的方法
import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
