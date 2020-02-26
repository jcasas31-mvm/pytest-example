def generate_userid(name,identifier):
    words = name.split(" ")
    letters = ""
    for i in words:
        print(i)
        print(i[0].lower())
        letters += i[0].lower()
    print(letters)
    return str(identifier)+"_"+letters

def test_generator_userid():
    assert generate_userid("Mauro Batista",3) == "3_mb"

def test_invalid_userid():
    assert generate_userid("Mauro Batista",3) != "4_mb"
