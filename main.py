import random

if __name__ == '__main__':
    print("Please give AI some data to learn...")
    print("The current data length is 0, 100 symbols left")

    string = ""

    while len(string) < 100:
        print("Print a random string containing 0 or 1:\n")

        for i in input():
            if i in ["0", "1"]:
                string += i

        if len(string) < 100:
            print(f"The current data length is {len(string)}, "
                  f"{100 - len(string)} symbols left")

    print("\nFinal data string:")
    print(string)

    balance = 1000

    print("\nYou have $1000. Every time the system successfully "
          "predicts your next press, you lose $1.")
    print("""Otherwise, you earn $1. Print "enough" to leave 
    the game. Let's go!\n""")

    dict_of_triads = {"000": [0, 0], "001": [0, 0], "010": [0, 0],
                      "011": [0, 0], "100": [0, 0], "101": [0, 0],
                      "110": [0, 0], "111": [0, 0]}

    while True:
        print("Print a random string containing 0 or 1:")

        random_string = ""
        string_input = input()

        if string_input == "enough":
            print("Game over!")
            break
        elif string_input[0] not in ["0", "1"]:
            print()
            continue

        for i in string_input:
            if i in ["0", "1"]:
                random_string += i

        for i in range(len(random_string) - 3):
            key = str(random_string[i] + random_string[i + 1]
                      + random_string[i + 2])

            if key in ["000", "001", "010", "011",
                       "100", "101", "110", "111"]:
                if int(random_string[i + 3]) == 0:
                    dict_of_triads[key][0] += 1
                else:
                    dict_of_triads[key][1] += 1

        print("prediction:")

        projected_n = random.choices(["0", "1"], k=3)
        predicted_string = ''.join(projected_n)

        i = 0
        while len(predicted_string) != len(random_string):
            key = random_string[i:i + 3]

            if dict_of_triads[key][0] > dict_of_triads[key][1]:
                predicted_string += "0"
            elif dict_of_triads[key][0] < dict_of_triads[key][1]:
                predicted_string += "1"
            else:
                predicted_string += random.choice(["0", "1"])

            i += 1

        print(predicted_string)

        coincidences = [i for i in range(3, len(random_string))
                        if random_string[i] == predicted_string[i]]

        interest = round((len(coincidences) / (len(random_string) - 3)) * 100, 2)
        print(f"\nComputer guessed right {len(coincidences)} "
              f"out of {len(random_string) - 3} symbols ({interest} %)")

        balance = balance - 2 * len(coincidences) + len(random_string) - 3.
        print(f"Your balance is now ${int(balance)}")
        print()
