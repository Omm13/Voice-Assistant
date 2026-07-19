from speech import take_command


while True:

    command = take_command()

    if command:
        print("Command received:", command)

    if "exit" in command:
        break