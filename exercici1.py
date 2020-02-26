#Function to transform the name and the number to a final and real id
def generate_userid (name, identifier):
    letters=""
    words=name.split(" ")
    for w in words:
        letters += w [0].lower()
    return str(identifier)+ "_" + letters
#Function maked to do a test for the correct us of the program
def test_generate_userid():
    assert generate_userid("Roger España",23) == ("23_re")
#
final = generate_userid("Roger España",23)
print(final)

