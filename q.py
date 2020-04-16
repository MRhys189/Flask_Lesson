question = "This is a common interview question"
question2 = question.lower()
character = [*question2]
print(character)

char2 = [character.count(char) for char in character]
char3 = [char2*1 for char in character]
print(char2)
print(char3)

# characters2 = [characters.count(char) for char in characters]
# characters3 = [char*1 for char in characters]
# print(max(characters3.count(characters)), max(characters2))
