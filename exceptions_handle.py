try:
    text = input("Enter something -->")
except EOFError:
    print("Why did you do an EOF On me")
except KeyboardInterrupt:
    print("You cancelled the operation")
else:
    print("You Entered {}".format(text))
