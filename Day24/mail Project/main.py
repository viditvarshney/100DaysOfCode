NAME = "[name]"

with open(r"Day24\mail Project\Input\Names\invited_names.txt") as file:
    data = file.readlines()


with open(r"Day24\mail Project\Input\Letters\starting_letter.txt") as letter:
    letter_contents = letter.read()

    for name in data:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(NAME, stripped_name)
        with open(rf"Day24\mail Project\Output\ReadyToSend\letter_for{stripped_name}.txt", mode='w') as output:
            output.write(new_letter)
