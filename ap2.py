def generate_userid(name,identifier):
    word=name.split(" ")
    letters=""
    for i in word:
        print(i)
        print (i[0].lower())
        letters+=i[0].lower()
    print(letters)
    return str(identifier)+"_"+letters

def test_my_function():
    assert generate_userid("Lovedeep Singh",498)== "498_ls"

def test_invalid_my_function():
    assert generate_userid("Lovedeep Singh",498) != "4_ls"

id=generate_userid("Lovedeep Singh",498)
print(id)