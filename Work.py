# %%%
def remove_every_other(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(my_list[i])
        else:
            pass
    return new_list


# %%%
def find_arr(arrA, arrB, rng, wanted):
    temp_a = arrA
    temp_b = arrB
    in_both = []
    for i in range(len(temp_a)):
        if temp_a[i] in temp_b:
            in_both.append(temp_a[i])
            temp_a = temp_a.remove(temp_a[i])
        else:
            pass
    return in_both


# %%%
def animals(heads, legs):
    if (
        heads < 0
        or legs < 0
        or (heads == 0 and legs != 0)
        or (legs == 0 and heads != 0)
    ):
        return "No solutions"
    else:
        y = 2 * heads - 0.5 * legs
        x = heads - y
    if (x < 0 or y < 0) or (x + y != heads) or (x % 1 != 0 or y % 1 != 0):
        return "No solutions"
    else:
        return (int(y), int(x))


# %%%
def distances_from_average(test_list):
    average = sum(test_list) / len(test_list)
    list_dist = []
    for i in range(len(test_list)):
        list_dist.append(round(average - test_list[i], 1))
    return list_dist


# %%%
def get_chance(n, x, a):
    list_prob = []
    for i in range(a):
        list_prob.append(round(x / (n - i), 3))
    return sum(list_prob) / len(list_prob)


# %%%
def create_pass(length):
    import random

    char = list("".join(chr(x) for x in range(33, 127)))
    t_t = [[], [], [], []]
    new_pass = ""
    for i in range(length):
        new_pass += char[random.randint(0, len(char) - 1)]
    for i in range(length):
        if new_pass[i] in list("".join(chr(x) for x in range(65, 91))):
            t_t[0].append(new_pass[i])
        elif new_pass[i] in list("".join(chr(x) for x in range(97, 123))):
            t_t[1].append(new_pass[i])
        elif new_pass[i] in list("".join(chr(x) for x in range(48, 58))):
            t_t[2].append(new_pass[i])
        else:
            t_t[3].append(new_pass[i])
    if len(t_t[0]) == 0 or len(t_t[1]) == 0 or len(t_t[2]) == 0 or len(t_t[3]) == 0:
        new_pass = None
        create_pass(length)
    else:
        print(new_pass)


create_pass(15)


# %%%
def create_pass_optimized(length):
    import random

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = (
        "".join(chr(x) for x in range(33, 48))
        + "".join(chr(x) for x in range(58, 65))
        + "".join(chr(x) for x in range(91, 97))
        + "".join(chr(x) for x in range(123, 127))
    )
    all_chars = uppercase + lowercase + digits + special_chars
    new_pass = (
        random.choice(uppercase)
        + random.choice(lowercase)
        + random.choice(digits)
        + random.choice(special_chars)
    )
    for _ in range(length - 4):
        new_pass += random.choice(all_chars)
    new_pass_list = list(new_pass)
    random.shuffle(new_pass_list)
    new_pass = "".join(new_pass_list)
    print(new_pass)


create_pass(15)


# %%%
def root(two, one, zero):
    import math

    if two == 0 and one == 0:
        print(f"{two}, {one}, {zero} is not a valid input")
    elif two == 0:
        print(f"{two}, {one}, {zero} have roots at -{zero/one}")
    elif abs(one**2 - 4 * two * zero) != (one**2 - 4 * two * zero):
        print(f"{two}, {one}, {zero}  have imaginary roots")
    else:
        x = (
            ((-1) * one + math.sqrt(one**2 - 4 * two * zero)) / (2 * two),
            (((-1) * one - math.sqrt(one**2 - 4 * two * zero)) / (2 * two)),
        )
        print(f"{two}, {one}, {zero} have roots at {x}")


# %%%
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# %%%
def spin_words(sentence):
    def bleh(sentence):
        list_of_words = sentence.split(" ")
        list_of_let = []
        for i in range(len(list_of_words)):
            word = []
            for j in range(len(list_of_words[i])):
                word.append(list_of_words[i][j])
            list_of_let.append(word)
        for i in range(len(list_of_words)):
            if len(list_of_let[i]) >= 5:
                list_of_let[i].reverse()
        for i in range(len(list_of_let)):
            for j in range(len(list_of_let[i])):
                print(f"{list_of_let[i][j]}", end="")
                if j != 0:
                    if j % (len(list_of_let[i]) - 1) == 0:
                        print("", end=" ")

    return bleh(sentence)


# %%%
def flip_words(sentence):
    sent_split = sentence.split(" ")
    word_split = []

    # turn into list
    for i in range(len(sent_split)):
        word_split.append(list(sent_split[i]))

    # reversing
    for i in range(len(word_split)):
        if len(word_split[i]) >= 5:
            word_split.append(word_split[i].reverse())
            word_split.pop(-1)

    # printing segment
    for i in range(len(word_split)):
        print("", end=" ")
        for j in range(len(word_split[i])):
            print(word_split[i][j], end="")


# %%%
def DNA_strand(dna):
    type_list = []

    for char in dna[0]:
        if char == "T":
            type_list.append("A")
        elif char == "A":
            type_list.append("T")
        elif char == "C":
            type_list.append("G")
        elif char == "G":
            type_list.append("C")

    comp_strand = "".join(type_list)

    comp_strand = str(comp_strand)

    return comp_strand


# %%%
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# %%%
def summation_of_primes(primes):
    list_of_primes = []
    for i in range(primes + 1):
        if is_prime(i) == True:
            list_of_primes.append(i)
        else:
            pass
    a = sum(list_of_primes)
    return a


# %%%
def calc_pi(n):
    odd_list = [i for i in range(n * 2 + 1) if i % 2 != 0]
    tot = [(1 / odd_list[i]) * ((-1) ** i) for i in range(len(odd_list))]
    pi = 4 * sum(tot)
    return pi


# %%% BlackJack 1

import random


class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        # Assume a deck with more face cards (2x more face cards than number cards)
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = cards * 4 + cards * 8  # Twice as many face cards
        return [(card, suit) for card in deck for suit in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }
        total_value = sum(values[card[0]] for card in hand)
        # Adjust for Aces
        for card in hand:
            if card[0] == "A" and total_value > 21:
                total_value -= 10
        return total_value

    def display_hand(self, hand, hide_first_card=False):
        if hide_first_card:
            print(f"Hidden Card, {hand[1]}")
        else:
            print(", ".join(map(lambda x: f"{x[0]} of {x[1]}", hand)))

    def play(self):
        self.shuffle_deck()

        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        # Player's turn
        while True:
            print("\nPlayer's Hand:")
            self.display_hand(self.player_hand)
            player_value = self.calculate_hand_value(self.player_hand)

            if player_value == 21:
                print("Blackjack! You win!")
                break

            if player_value > 21:
                print("Bust! You lose.")
                break

            action = input("Do you want to hit or stand? ").lower()
            if action == "hit":
                self.deal_card(self.player_hand)
            elif action == "stand":
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        # Dealer's turn
        print("\nDealer's Hand:")
        self.display_hand(self.dealer_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        while dealer_value < 17:
            self.deal_card(self.dealer_hand)
            dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("\nFinal Results:")
        print("\nPlayer's Hand:")
        self.display_hand(self.player_hand)
        print(f"Player's Hand Value: {self.calculate_hand_value(self.player_hand)}")

        print("\nDealer's Hand:")
        self.display_hand(self.dealer_hand)
        print(f"Dealer's Hand Value: {dealer_value}")

        # Determine the winner
        if dealer_value > 21:
            print("Dealer bust! You win!")
        elif player_value > 21:
            print("You bust! Dealer wins!")
        elif player_value > dealer_value and player_value <= 21:
            print("You win!")
        elif player_value < dealer_value and dealer_value <= 21:
            print("You lose.")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.play()


# %%% Pokemon

import random
from sympy import isprime, nextprime


class Pokemon:
    def __init__(self, hp, skill, atk1, atk2):
        self.hp = hp
        self.skill = skill
        self.atk1 = atk1
        self.atk2 = atk2
        self.lvl = 1
        self.pts = 0

    def atk_f(self, other):
        random_int1 = random.randint(1, 4)
        rand_list = []
        for i in range(4):
            rand_list.append(random.randint(1, 4))
        if random_int1 in rand_list:
            if self.skill == "fire" and other.skill == "ground":
                other.hp -= self.atk1 * 1.25
            elif self.skill == "water" and other.skill == "fire":
                other.hp -= self.atk1 * 1.25
            elif self.skill == "ground" and other.skill == "lightning":
                other.hp -= self.atk1 * 1.25
            elif self.skill == "lightning" and other.skill == "water":
                other.hp -= self.atk1 * 1.25
            elif self.skill == "ground" and other.skill == "fire":
                other.hp -= self.atk1 * 0.75
            elif self.skill == "fire" and other.skill == "water":
                other.hp -= self.atk1 * 0.75
            elif self.skill == "lightning" and other.skill == "ground":
                other.hp -= self.atk1 * 0.75
            elif self.skill == "water" and other.skill == "lightning":
                other.hp -= self.atk1 * 0.75
            else:
                other.hp -= self.atk1
            print("The attack was successful!")
        else:
            print("The attack was unsuccessful!")

        if other.hp <= 0:
            print("The opponents pokemon has died!")
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            return other.hp

    def atk_s(self, other):
        random_int1 = random.randint(1, 4)
        rand_list = []
        for i in range(4):
            rand_list.append(random.randint(1, 4))
        if random_int1 in rand_list:
            if self.skill == "fire" and other.skill == "ground":
                other.hp -= self.atk2 * 1.25
            elif self.skill == "water" and other.skill == "fire":
                other.hp -= self.atk2 * 1.25
            elif self.skill == "ground" and other.skill == "lightning":
                other.hp -= self.atk2 * 1.25
            elif self.skill == "lightning" and other.skill == "water":
                other.hp -= self.atk2 * 1.25
            elif self.skill == "ground" and other.skill == "fire":
                other.hp -= self.atk2 * 0.75
            elif self.skill == "fire" and other.skill == "water":
                other.hp -= self.atk2 * 0.75
            elif self.skill == "lightning" and other.skill == "ground":
                other.hp -= self.atk2 * 0.75
            elif self.skill == "water" and other.skill == "lightning":
                other.hp -= self.atk2 * 0.75
            else:
                other.hp -= self.atk2
            print("The attack was successful!")
        else:
            print("The attack was unsuccessful!")

        if other.hp <= 0:
            print("The opponents pokemon has died!")
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            return other.hp

    def NUKE(self, other):
        hint_list = []
        while len(hint_list) < 4:
            num = random.randint(1, 20)
            if not isprime(num) and num not in hint_list:
                hint_list.append(num)

        password = [nextprime(num) for num in hint_list]
        print(f"Hint: {hint_list}")
        user_attempt = [int(input("Guess: ")) for num in hint_list]

        if user_attempt == password:
            other.hp = 0
        else:
            print("Sorry, your guess is incorrect. The correct password is:", password)

        if other.hp <= 0:
            print("The opponents pokemon has died!")
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            other.hp = other.hp

    def hide(self):
        random_int1 = random.randint(1, 4)
        random_int2 = random.randint(1, 4)
        if random_int1 == random_int2:
            self.hp *= 1.1
            self.lvl += 1
            return "Hide was effective!"
        else:
            return "Hide was ineffective!"

    def level_up(self):
        if self.pts >= 100:
            self.pts -= 100
            self.hp *= 2
            self.atk_f *= 1.75
            self.atk_s *= 1.5
            self.lvl += 1
            print("You have leveled up!")
        else:
            print("You do not have enough points to level up!")

    def __repr__(self):
        return f"Your pokeman is a {self.skill} type, with {self.hp} hp left! You are curently level {self.lvl}, and {100-self.pts} points away from leveling up!"


# %%% Uno

import random

# give_card = 2
# deck = []
# num = [1,2,3,4,5,6,7,8,9,10]
# col = ['red', 'blue', 'green', 'yellow']

# for i in range(give_card):
#     card = [num[random.randint(0,len(num)-1)], col[random.randint(0,len(col)-1)]]
#     deck.append(card)

play = [0]


class Uno:
    # def __init__(self):

    def deal(self):
        give_card = 7
        deck = []
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        col = ["red", "blue", "green", "yellow"]

        for i in range(give_card):
            card = [
                num[random.randint(0, len(num) - 1)],
                col[random.randint(0, len(col) - 1)],
            ]
            deck.append(card)

        self.hand = deck

    def take(self):
        give_card = 1
        deck = []
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        col = ["red", "blue", "green", "yellow"]

        for i in range(give_card):
            card = [
                num[random.randint(0, len(num) - 1)],
                col[random.randint(0, len(col) - 1)],
            ]
            deck.append(card)
        self.hand.append(deck)

    def place(self, num):
        play.insert(0, self.hand[num - 1])
        self.hand.remove(self.hand[num - 1])

    def __repr__(self):
        return f"{self.hand}"


# %%% Class Student
class Student:
    def __init__(self, name, identification, grade):
        self._name = name
        self._id = identification
        self._grade = grade

    def getName(self):
        return self._name

    def getID(self):
        return self._id

    def getGrade(self):
        return self._grade

    def updateGrade(self, newgrade):
        self._grade = newgrade
        return f"{self._name}'s updated grade is {newgrade}"

    def __repr__(self):
        return f"{self._name}'s ID is {self._id} and their grade is {self._grade}"


# %%%
def expanded_form(num):
    strnum = str(num)
    strnumlist = []
    list_to_print = []
    my_str = ""
    for i in range(len(strnum)):
        strnumlist.append(int(strnum[i]))
    for i in range(len(strnumlist)):
        strnumlist[i] *= 10 ** (len(strnumlist) - i - 1)
    for i in range(len(strnumlist) - 1):
        if strnumlist[i] != 0:
            list_to_print.append(f"{strnumlist[i]} + ")
    if strnumlist[len(strnumlist) - 1] != 0:
        list_to_print.append(str(strnumlist[len(strnumlist) - 1]))
        for i in range(len(list_to_print)):
            my_str += list_to_print[i]
    else:
        for i in range(len(list_to_print)):
            my_str += list_to_print[i]
        my_str = my_str[:-3]
    return my_str


# %%%
def domain_name(url):
    list_char = []
    for char in url:
        list_char.append(char)

    if "/" in list_char:

        def append_between_chars(char_list, start_char, end_char):
            result = []
            appending = False
            for char in char_list:
                if char == start_char:
                    appending = True
                elif char == end_char:
                    appending = False
                elif appending:
                    result.append(char)
            return "".join(result)

        result = append_between_chars(list_char, "/", ".")
    elif "." in list_char:

        def append_between_chars(char_list, start_end_char):
            result = []
            appending = False
            count = 0
            for char in char_list:
                if char == start_end_char:
                    count += 1
                    if count == 2:
                        appending = not appending
                elif appending:
                    result.append(char)
            return "".join(result)

        result = append_between_chars(list_char, ".")

    return result
    pass


# %%%
def count_bits(n):
    return sum([int(num) for num in bin(n)[2:]])


# %%%
def order(sentence):
    final = ""
    b = []
    a = sentence.split(" ")
    for word in range(len(a)):
        a[word] = [char for char in a[word]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            try:
                a[i][j] = int(a[i][j])
            except:
                ValueError
    for i in range(len(a)):
        b.append([])
    for i in range(len(a)):
        for j in range(len(a[i])):
            if type(a[i][j]) == int:
                b[a[i][j] - 1].append(a[i])
    for i in range(len(b)):
        for j in range(len(b[i])):
            final += " "
            for k in range(len(b[i][j])):
                final += str(b[i][j][k])
    return final.lstrip()


# %%%
def sum_dig_pow(a, b):
    result_list = []
    result_list2 = []
    list_to_print = []
    for num in range(a, b + 1):
        result_list.append([int(digit) for digit in str(num)])
    for num in range(a, b + 1):
        result_list2.append(num)
    for i in range(len(result_list)):
        for j in range(len(result_list[i])):
            result_list[i][j] = result_list[i][j] ** (j + 1)
    for i in range(len(result_list)):
        result_list[i] = sum(result_list[i])
    for i in range(len(result_list2)):
        if result_list[i] == result_list2[i]:
            list_to_print.append(result_list2[i])
    return list_to_print


# %%%
def scramble2(s1, s2):
    str1 = [char for char in s1]
    str2 = [char for char in s2]
    return str2.issubset(str1)


# %%%
def scramble(larger_list, sublist):
    larger_list = [char for char in larger_list]
    sublist = [char for char in sublist]
    len_sublist = len(sublist)
    for i in range(len(larger_list) - len_sublist + 1):
        if larger_list[i : i + len_sublist] == sublist:
            return True
    return False


# %%%
def are_characters_scrambled(list_a, list_b):
    from collections import Counter

    counter_a = Counter(list_a)
    counter_b = Counter(list_b)
    return counter_a >= counter_b


# %%%
def camel_case(s):
    string_to_print = ""
    s_split = s.split()
    for i in range(len(s_split)):
        s_split[i] = [char for char in s_split[i]]
    for i in range(len(s_split)):
        s_split[i][0] = s_split[i][0].upper()
    for word in s_split:
        for char in word:
            string_to_print += char
    return string_to_print


# %%%
def increment_string(strng):
    str_to_print = ""
    str_num = ""
    list_num = []
    str_list_new = []
    str_list = [char for char in strng]

    for i in range(len(str_list)):
        try:
            str_list[i] = int(str_list[i])
        except:
            ValueError
    if strng == "":
        return "1"
    elif type(str_list[-1]) != int:
        str_list.append("1")
        for i in range(len(str_list)):
            str_to_print += str_list[i]
        return str_to_print
    else:
        while type(str_list[len(str_list) - i - 1]) == int:
            for i in range(len(str_list)):
                if type(str_list[len(str_list) - i - 1]) == int:
                    list_num.insert(0, str_list[len(str_list) - i - 1])
        for i in range(len(list_num)):
            list_num[i] = str(list_num[i])
        for i in range(len(list_num)):
            str_num += list_num[i]
        num = str(int(str_num) + 1)
        num1 = [char for char in num]
        for i in range(len(str_list)):
            if type(str_list[i]) == str:
                str_list_new.append(str_list[i])
        while len(str_list) - len(str_list_new) > len(num):
            str_list_new.append("0")
        for i in range(len(num1)):
            str_list_new.append(num1[i])
        for i in range(len(str_list_new)):
            str_to_print += str_list_new[i]
        return str_to_print


# %%%
def increment_string2(s):
    import re

    match = re.search(r"(\d+)$", s)
    if match:
        number = str(int(match.group(1)) + 1)
        incremented_number = number.zfill(len(match.group(1)))
        result = s[: match.start()] + incremented_number
    else:
        result = s + "1"
    return result


# %%%
def fs(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]


# %%%
def productFib(prod):
    f = [0, 1]
    if prod < 0:
        return []
    while True:
        n = f[-1] + f[-2]
        if n > prod:
            break
        f.append(n)
    for i in range(len(f) - 1):
        if f[i] * f[i + 1] == prod:
            return [f[i], f[i + 1], True]
    for i in range(len(f) - 1):
        if f[i] * f[i + 1] > prod:
            return [f[i], f[i + 1], False]


# %%%
def snail(snail_map):
    n = len(snail_map)
    ltp = [num for num in snail_map[0]]
    for i in range(n - 1):
        ltp.append(snail_map[i + 1][n - 1])
    for i in range(n - 1):
        ltp.append(snail_map[n - 1][n - 2 - i])
    for i in range(n - 1):
        ltp.append(snail_map[1][i - 3])
    return ltp


# %%%
def snail2(array):
    result = []
    while array:
        result += array.pop(0)
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        if array:
            result += array.pop()[::-1]
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result


# %%%
def permutations2(s):
    perm = list(s)
    ltr = []
    for i in range(len(perm)):
        a = perm[len(perm) - 1]
        perm = perm[:-1]
        perm.insert(0, a)
        ltr.append(perm)
    lts = ["".join(row) for row in ltr]
    return lts


# %%%
def permutations(s):
    from itertools import permutations

    return list(set(["".join(p) for p in permutations(s)]))


# %%%
def fibonacci(n):
    fib_list = [0, 1]
    for i in range(100000):
        fib_list.append(fib_list[i] + fib_list[i + 1])

    try:
        return fib_list[n]
    except:
        IndexError


# %%%
def sum_pairs2(ints, s):
    from itertools import combinations

    list_op = list(combinations(ints, 2))

    for i in range(len(list_op)):
        list_op[i] = list(list_op[i])

    ltc = []
    for i in list_op:
        if sum(i) == s:
            ltc.append(i)

    loi = []
    for i in range(len(ltc)):
        loi.append(ints.index(ltc[i][1]))

    return loi


# %%%
def sum_pairs(int_list, s):
    seen = set()
    for number in int_list:
        complement = s - number
        if complement in seen:
            return [complement, number]
        seen.add(number)
    return None


# %%%
def order_weight1(strng):
    my_dict = {}
    list1 = list(strng.split(" "))
    list2 = []
    for i in range(len(list1)):
        list2.append([int(char) for char in list1[i]])

    for i in range(len(list2)):
        list2[i] = sum(list2[i])

    for i in range(len(list2)):
        my_dict[list2[i]] = list1[i]

    keys = list(my_dict.keys())
    keys = sorted(keys)

    ltp = ""
    for i in keys:
        ltp += f"{my_dict[i]} "
    ltp = ltp[:-1]

    return ltp


# %%%
def order_weight(strng):
    def weight(n):
        return sum(int(digit) for digit in n), n

    return " ".join(sorted(strng.split(), key=weight))


# %%%
def count_sheeps(sheep):
    a = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            a += 1
    return a


# %%%
def xo(s):
    if s.count("x") + s.count("X") == s.count("o") + s.count("O"):
        return True
    elif s.count("x") + s.count("X") == 0 and s.count("o") + s.count("O") == 0:
        return True
    else:
        return False


# %%%
def summation(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum


# %%%
def validate_pin(pin):
    a = [char for char in pin]
    if len(a) == 4 or len(a) == 6:
        try:
            for i in range(len(a)):
                int(a[i])
            return True
        except:
            ValueError
    return False


# %%%
def find_next_square(sq):
    a = sq**0.5
    if int(a) == a:
        c = (a + 1) ** 2
    else:
        c = -1
    return int(c)


# %%%
def number_to_string(num):
    return str(num)


# %%%
def proper_fractions(d):
    if d == 1:
        return 0
    result = d
    p = 2
    while p * p <= d:
        if d % p == 0:
            while d % p == 0:
                d //= p
            result -= result // p
        p += 1
    if d > 1:
        result -= result // d
    return result


# %%%
def expand(expr):
    a = list(char for char in expr)
    a.remove("(")
    a.remove(")")
    b = ""
    for i in range(len(a)):
        b += a[i]
    c = b.split("^")
    if "+" in c[0]:
        c[0] = c[0].split("x+")
    else:
        c[0] = c[0].split("x")

    ltw = []
    for i in range(int(c[1]) + 1):
        ltw.append([])

    ltw[0].append(int(c[0][0]) ** int(c[1]))
    ltw[-1].append(int(c[0][-1]) ** int(c[1]))
    ltw[1].append(int(c[1]) * int(c[0][0]) * int(c[0][1]))

    return ltw


# %%%
class Cube:
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side):
        self._side = abs(side)

    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)


# %%%
def squirrel1(h, H, S):
    return round((H / h) * ((h**2 + S**2) ** 0.5), 4)


# %%%
def squirrel2(h, H, S):
    import math

    return round((H / h) * (math.hypot(h, S)), 4)


# %%%
def squirrel3(h, H, S):
    return (h * h + S * S) ** 0.5 / h * H


# %%%
def squirrel(h, H, S):
    return f"{(h*h+S*S)**.5/h*H:.4}"


# %%%
def solve_runes(runes):
    def difference(list1, list2):
        list2_copy = list2.copy()
        return [
            item for item in list1 if item not in list2_copy or list2_copy.remove(item)
        ]

    if "+" in runes:
        op = "+"
        char1 = runes.split(op)
        char2 = char1[1].split("=")
        char1.pop()
        char = char1 + char2

        try:
            f = int(char[0])
        except:
            ValueError
            f = char[0]
        try:
            s = int(char[1])
        except:
            ValueError
            s = char[1]
        try:
            ans = int(char[2])
        except:
            ValueError
            ans = char[2]

        if type(f) == int:
            f1 = 0
        else:
            f1 = 1
        if type(s) == int:
            s1 = 0
        else:
            s1 = 1
        if type(ans) == int:
            ans1 = 0
        else:
            ans1 = 1

        # ? before operator
        if f1 == 1:
            nf = str(ans - s)
            f2 = list(char for char in f)
            nf1 = list(char for char in nf)
            r = difference(nf1, f2)
            return int(r[0])
        # ? after operator
        if s1 == 1:
            ns = str(ans - f)
            s2 = list(char for char in s)
            ns1 = list(char for char in ns)
            r = difference(ns1, s2)
            return int(r[0])
        # ? in answer
        if ans1 == 1:
            nans = str(f + s)
            ans2 = list(char for char in ans)
            nans1 = list(char for char in nans)
            r = difference(nans1, ans2)
            return int(r[0])

    if "-" in runes:
        op = "-"
        char1 = runes.split(op)
        char2 = char1[1].split("=")
        char1.pop()
        char = char1 + char2

        try:
            f = int(char[0])
        except:
            ValueError
            f = char[0]
        try:
            s = int(char[1])
        except:
            ValueError
            s = char[1]
        try:
            ans = int(char[2])
        except:
            ValueError
            ans = char[2]

        if type(f) == int:
            f1 = 0
        else:
            f1 = 1
        if type(s) == int:
            s1 = 0
        else:
            s1 = 1
        if type(ans) == int:
            ans1 = 0
        else:
            ans1 = 1

        # ? befor operator
        if f1 == 1:
            nf = str(ans + s)
            f2 = list(char for char in f)
            nf1 = list(char for char in nf)
            r = difference(nf1, f2)
            return int(r[0])
        # ? after operator
        if s1 == 1:
            ns = str(f - ans)
            s2 = list(char for char in s)
            ns1 = list(char for char in ns)
            r = difference(ns1, s2)
            return int(r[0])
        # ? in answer
        if ans1 == 1:
            nans = str(f - s)
            ans2 = list(char for char in ans)
            nans1 = list(char for char in nans)
            r = difference(nans1, ans2)
            return int(r[0])

    if "*" in runes:
        op = "*"
        char1 = runes.split(op)
        char2 = char1[1].split("=")
        char1.pop()
        char = char1 + char2

        try:
            f = int(char[0])
        except:
            ValueError
            f = char[0]
        try:
            s = int(char[1])
        except:
            ValueError
            s = char[1]
        try:
            ans = int(char[2])
        except:
            ValueError
            ans = char[2]

        if type(f) == int:
            f1 = 0
        else:
            f1 = 1
        if type(s) == int:
            s1 = 0
        else:
            s1 = 1
        if type(ans) == int:
            ans1 = 0
        else:
            ans1 = 1

        # ? before operator
        if f1 == 1:
            nf = str(ans / s)
            f2 = list(char for char in f)
            nf1 = list(char for char in nf)
            r = difference(nf1, f2)
            return int(r[0])
        # ? after operator
        if s1 == 1:
            ns = str(f / ans)
            s2 = list(char for char in s)
            ns1 = list(char for char in ns)
            r = difference(ns1, s2)
            return int(r[0])
        # ? in answer
        if ans1 == 1:
            nans = str(f * s)
            ans2 = list(char for char in ans)
            nans1 = list(char for char in nans)
            r = difference(nans1, ans2)
            return int(r[0])


# %%%
def calc(expression):
    import operator
    import re

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
    }

    def root_operation(match):
        base, exponent = map(float, match.groups())
        return str(exponent ** (1 / base))

    expression = re.sub(r"(\d+)rt(\d+)", root_operation, expression)
    expression = expression.replace("^", "**")
    try:
        return eval(expression, {"__builtins__": None}, ops)
    except Exception as e:
        return "Error: " + str(e)


# %%%
def solution(number):
    lts = []
    ltw = [i for i in range(number)]
    for i in ltw:
        if i % 5 == 0 and i % 3 == 0:
            lts.append(i)
        elif i % 5 == 0:
            lts.append(i)
        elif i % 3 == 0:
            lts.append(i)
    return sum(lts)


# %%%
def find_it1(seq):
    counts = {}
    keys = list(counts.keys())
    values = list(counts.values())
    for char in seq:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for i in range(len(values)):
        if values[i] % 2 != 0:
            return keys[i]


# %%%
def find_it(seq):
    from collections import Counter

    return next(k for k, v in Counter(seq).items() if v % 2)


# %%%
def digital_root(n):
    while len(str(n)) > 1:
        n = str(n)
        ltw = [int(char) for char in str(n)]
        n = sum(ltw)
    return n


# %%%
def duplicate_count(text):
    counts = {}

    for char in text.upper():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    keys = list(counts.keys())
    values = list(counts.values())

    rtn = 0
    for i in values:
        if i > 1:
            rtn += 1

    return rtn


# %%%
def find_outlier(integers):
    ltw = [integers[0] % 2, integers[1] % 2, integers[2] % 2]
    ltw = sorted(ltw)
    ltw.pop()
    for i in range(len(ltw)):
        ltw[i] = str(ltw[i])
    if "1" in ltw:
        for i in integers:
            if i % 2 == 0:
                return i
    else:
        for i in integers:
            if i % 2 != 0:
                return i


# %%%
def is_valid_walk(walk):
    counts = {}

    for char in walk:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    keys = list(counts.keys())
    values = list(counts.values())

    if "n" not in keys:
        counts["n"] = 0
    elif "s" not in keys:
        counts["s"] = 0
    elif "e" not in keys:
        counts["e"] = 0
    elif "w" not in keys:
        counts["w"] = 0

    try:
        lat = counts["e"] - counts["w"]
    except:
        KeyError
        lat = 0
    try:
        long = counts["n"] - counts["s"]
    except:
        KeyError
        long = 0

    if len(walk) != 10:
        return False
    elif lat == 0 and long == 0:
        return True
    else:
        return False


# %%%
def alphabet_position(text):
    my_dict = {}
    ltw = text.replace(" ", "")
    let = "abcdefghijklmnopqrstuvwxyz"
    stp = ""

    for i in range(len(let)):
        my_dict[let[i]] = i + 1

    ltw2 = [char for char in ltw]

    nl = ""

    for i in ltw2:
        try:
            i = int(i)
            nl += str(i)
        except:
            ValueError

    if len(nl) > 1:
        return nl

    if "." in ltw2:
        ltw2.remove(".")

    for i in range(len(ltw2)):
        try:
            ltw2[i] = ltw2[i].lower()
        except:
            KeyError

    for i in ltw2:
        if i not in let:
            ltw2.remove(i)

    for i in ltw2:
        try:
            stp += f"{my_dict[i]} "
        except:
            KeyError
    return stp[:-1]


# %%%
def persistence(n):
    if len(str(n)) == 1:
        return 1

    send = 0

    while len(str(n)) > 1:
        ltw = [int(num) for num in str(n)]
        s = 1
        for num in ltw:
            s *= num
        n = s
        send += 1
    return send


# %%%
def to_camel_case(text):
    s = text
    string_to_print = ""
    tgro = ["-", "_"]
    s_split = s.split("-")
    for i in range(len(tgro)):
        try:
            s_split.remove(tgro[i])
        except:
            ValueError
    for i in range(len(s_split)):
        s_split[i] = [char for char in s_split[i]]
    for i in range(len(s_split)):
        s_split[i][0] = s_split[i][0].upper()
    for word in s_split:
        for char in word:
            string_to_print += char
    return string_to_print


# %%%
def move_zeros(lst):
    count = 0
    count += sum(1 for i in lst if i == 0)
    for i in range(count):
        lst.remove(0)
    for i in range(count):
        lst.append(0)
    return lst


# %%%
def pig_it(text):
    let = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lst = text.split(" ")
    for i in range(len(lst)):
        lst[i] = [char for char in lst[i]]
    for i in range(len(lst)):
        lst[i].append(lst[i][0])
        lst[i].remove(lst[i][0])

    ltp = ""
    for i in lst:
        ltp += " "
        for j in i:
            ltp += j
        ltp += "ay"

    if ltp[-3] not in let:
        ltp = ltp[:-2]

    ltp = ltp.lstrip().rstrip()

    return ltp


# %%%
def make_readable(seconds):

    import math

    ints = int(seconds)
    if ints >= 3600:
        h = math.floor(ints / 3600)
        ints = ints % 3600
        if len(str(h)) == 1:
            h = f"0{h}"
    else:
        h = "00"
    if 3600 > ints >= 60:
        m = math.floor(ints / 60)
        ints = ints % 60
        if len(str(m)) == 1:
            m = f"0{m}"
    else:
        m = "00"
    if ints < 60:
        s = ints
        if len(str(s)) == 1:
            s = f"0{s}"

    return f"{h}:{m}:{s}"
#%%%
def rgb(r, g, b):
    def clamp_and_convert(value):
        return max(0, min(value, 255))

    def to_hex(value):
        return f"{clamp_and_convert(value):02X}"

    return to_hex(r) + to_hex(g) + to_hex(b)



# %%%

def rot13(message):
    from string import ascii_lowercase, ascii_uppercase
    trans = str.maketrans(
        ascii_lowercase + ascii_uppercase,
        ascii_lowercase[13:] + ascii_lowercase[:13] +
        ascii_uppercase[13:] + ascii_uppercase[:13]
    )
    return message.translate(trans)

rot13('hello world')
# %%%
def generate_hashtag(s):
    words = [word.capitalize() for word in s.split() if word]
    final = "#" + "".join(words)
    return final if 1 < len(final) <= 140 else False



# %%%
def cakes(recipe, available):
    return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)



# %%%
def cakes2(recipe, available):
    return (
        min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)
        or 0
    )


# %%%
def fac(num):
    ml = [i + 1 for i in range(num)]
    s = 1
    for i in ml:
        s *= ml[i - 1]

    s = str(s)
    a = s.rstrip("0")

    return len(s) - len(a)


#
# %%%
def zeros1(n):
    import math

    a = math.floor(n / 5)
    bad_list = [5, 11, 17, 23, 29]
    good_list = [0, 1, 2, 3, 4, 6]
    for i in range(1, 6):
        b = i + 5 * i - 1
        # print(b)
    counter = 0
    if a == 0:
        return 0
    elif (a % 31) in bad_list:
        a += 1
    for i in range(a):
        if i % 5 == 0:
            counter += 1
    return a + counter - 1


# %%%
def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


# %%%
def format_duration(seconds):
    if not seconds:
        return "now"
    units = [("year", 31536000), ("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    parts = []
    for unit, sec in units:
        qty = seconds // sec
        if qty:
            seconds %= sec
            parts.append(f"{qty} {unit}{'s' * (qty != 1)}")
    return ', '.join(parts[:-1]) + (' and ' if len(parts) > 1 else '') + parts[-1]



# %%%
def format_duration2(s):
    if s == 0:
        return "now"
    m, h, d, y = 60, 3600, 86400, 31536000
    y, d, h, m, s = s // y, s % y // d, s % d // h, s % h // m, s % m
    parts = [
        f"{x} {unit}{'s' * (x != 1)}"
        for x, unit in zip([y, d, h, m, s], ["year", "day", "hour", "minute", "second"])
        if x
    ]
    return (
        ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1]
        if parts
        else "now"
    )


# %%%
def format_duration3(s):
    if not s:
        return "now"
    parts = [
        f"{t} {u}{'s' * (t != 1)}"
        for t, u in zip(
            [
                s // 31536000,
                s % 31536000 // 86400,
                s % 86400 // 3600,
                s % 3600 // 60,
                s % 60,
            ],
            ["year", "day", "hour", "minute", "second"],
        )
        if t
    ]
    return (
        ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1]
        if parts
        else "now"
    )


# %%%
from collections import Counter

def mix(s1, s2):
    counter1 = Counter(filter(str.islower, s1))
    counter2 = Counter(filter(str.islower, s2))
    result = []
    for letter in set(counter1.keys()) | set(counter2.keys()):
        n1, n2 = counter1.get(letter, 0), counter2.get(letter, 0)
        if max(n1, n2) > 1:
            which = "1" if n1 > n2 else ("2" if n2 > n1 else "=")
            result.append(f"{which}:{letter * max(n1, n2)}")
    return "/".join(sorted(result, key=lambda x: (-len(x), x)))



# %%%
def decompose(n):
    import time

    time_limit = 10
    final = [n - 1]
    new = n**2 - (n - 1) ** 2
    while new > 0:
        new1 = new
        # while new1 > 0:
        while (new ** (1 / 2)) % 1 != 0:
            new1 -= 1
        final.append(int(new1 ** (1 / 2)))
        new = new - new1
    final = list(reversed(final))
    # if new1 == 0:
    return final


# %%%
def double_char(s):
    return "".join([char * 2 for char in s])


# %%%
# %%%

# %%%
def dice(sides):
    import random

    return random.randint(1, sides)


# %%%
s = 0
k = 9
for i in range(k):
    s += 2 * i + 1
print(s)


# %%%
def get_count(sentence):
    return sum(1 for i in sentence if i in ["a", "e", "i", "o", "u"])


# %%%
mys = "Hello World"
print("".join(mys[i] for i in range(len(mys)) if mys[i] not in "aeiouAEIOU"))


# %%%
def is_prime(num):
    if num == 0 or num == 1 or num < 0:
        return False
    for i in range(round(num / 2)):
        if abs(num) % (i + 2) == 0:
            return False
    return True


# %%%
def find_all(sum_dig, digs):
    start = 10 ** (digs - 1)
    end = 10**digs
    ltw = list(range(start, end))
    fl = []
    wl = []
    for i in range(len(ltw)):
        ltw[i] = str(ltw[i])
        if "0" not in ltw[i]:
            fl.append(list(ltw[i]))
    for i in range(len(fl)):
        for j in range(len(fl[i])):
            fl[i][j] = int(fl[i][j])
        if sum(fl[i]) == sum_dig:
            wl.append(fl[i])
    for i in range(len(wl)):
        for j in range(len(wl[i])):
            wl[i][j] = str(wl[i][j])
        wl[i] = [int("".join(wl[i]))]
    return [len(wl), min(wl[0]), max(wl[-1])]


# %%%
def find_all1(sum_dig, digs):
    def generate_numbers(current_sum, start, current_digs):
        if current_digs == digs:
            if current_sum == sum_dig:
                return [""]
            else:
                return []
        numbers = []
        for digit in range(start, 10):
            if current_sum + digit <= sum_dig:
                for num in generate_numbers(
                    current_sum + digit, digit, current_digs + 1
                ):
                    numbers.append(str(digit) + num)
        return numbers

    valid_numbers = generate_numbers(0, 1, 0)
    if not valid_numbers:
        return []
    valid_numbers = [int(num) for num in valid_numbers]
    return [len(valid_numbers), min(valid_numbers), max(valid_numbers)]


# %%%
def next_bigger(n):
    from itertools import permutations

    (sl, wl) = (list(str(n)), [])
    for perm in permutations(sl):
        wl.append(perm)
    for i in range(len(wl)):
        wl[i] = int("".join(list(wl[i])))
    wl = sorted(list(set(wl)))
    itc = wl.index(n)
    try:
        return wl[itc + 1]
    except IndexError:
        return -1


# %%%
def next_bigger1(n):
    # Convert the number to a list of its digits
    digits = list(str(n))

    # Step 1: Find the pivot - the first digit that is smaller than the digit to its right
    pivot_index = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            pivot_index = i
            break

    # If no such pivot is found, no bigger number can be formed
    if pivot_index == -1:
        return -1

    # Step 2: Find the smallest digit larger than the pivot
    for i in range(len(digits) - 1, pivot_index, -1):
        if digits[i] > digits[pivot_index]:
            # Step 3: Swap with pivot
            digits[i], digits[pivot_index] = digits[pivot_index], digits[i]
            break

    # Step 4: Sort the rest of the digits after the pivot
    digits[pivot_index + 1 :] = sorted(digits[pivot_index + 1 :])

    # Convert back to an integer
    return int("".join(digits))


# %%%
def factorial(n):
    if 0 <= n and n <= 12:
        (ltw, f) = (list(i + 1 for i in range(n)), 1)
        for i in ltw:
            f *= i
        return f
    else:
        raise ValueError


# %%%
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
TILE_SIZE = 32
BOARD_WIDTH, BOARD_HEIGHT = 16, 16
MINE_COUNT = 40
FONT_SIZE = 24
FPS = 60


def get_neighbors(x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_x, neighbor_y = x + i * TILE_SIZE, y + j * TILE_SIZE
            if 0 <= neighbor_x < WIDTH and 0 <= neighbor_y < HEIGHT:
                neighbors.append((neighbor_x, neighbor_y))
    return neighbors


def get_adjacent_mines(x, y, board):
    neighbors = get_neighbors(x, y)
    mine_count = 0
    for neighbor in neighbors:
        if board[neighbor[1] // TILE_SIZE][neighbor[0] // TILE_SIZE] == "M":
            mine_count += 1
    return mine_count


def draw_text(screen, text, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, FONT_SIZE)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()

    board = [["" for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    revealed_board = [["" for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    for i in range(MINE_COUNT):
        x, y = (
            random.randint(0, BOARD_WIDTH - 1) * TILE_SIZE,
            random.randint(0, BOARD_HEIGHT - 1) * TILE_SIZE,
        )
        board[y // TILE_SIZE][x // TILE_SIZE] = "M"

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                tile_x, tile_y = x // TILE_SIZE, y // TILE_SIZE
                if revealed_board[tile_y][tile_x] == "":
                    if board[tile_y][tile_x] == "M":
                        print("Game Over!")
                        running = False
                    else:
                        revealed_board[tile_y][tile_x] = get_adjacent_mines(x, y, board)

        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if revealed_board[y][x] != "":
                    pygame.draw.rect(
                        screen,
                        (255, 255, 255),
                        pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    )
                    draw_text(
                        screen,
                        str(revealed_board[y][x]),
                        x * TILE_SIZE + 5,
                        y * TILE_SIZE + 5,
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (0, 0, 0),
                        pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    )

                if board[y][x] == "M":
                    pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    )

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()


# %%%
def dir_reduc1(arr):
    left = arr.count("WEST")
    right = arr.count("EAST")
    up = arr.count("NORTH")
    down = arr.count("SOUTH")
    hor = right - left
    vert = up - down
    fl = []

    try:
        if hor == 0:
            pass
        elif hor < 0:
            for i in range(abs(int(hor))):
                fl.append("WEST")
        else:
            for i in range(abs(int(hor))):
                fl.append("EAST")
    except:
        ValueError

    try:
        if vert == 0:
            pass
        elif vert < 0:
            for i in range(abs(int(hor))):
                fl.append("SOUTH")
        else:
            for i in range(abs(int(hor))):
                fl.append("NORTH")
    except:
        ValueError

    return fl


# %%%
def dir_reduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []

    for arr in arr:
        if stack and stack[-1] == opposite[arr]:
            stack.pop()
        else:
            stack.append(arr)

    return stack


# %%%
from itertools import zip_longest

def addition_without_carrying(a, b):
    return int(''.join(str((int(d1 or 0) + int(d2 or 0)) % 10) for d1, d2 in zip_longest(str(a)[::-1], str(b)[::-1])))



# %%%
# %%%
def hamming1(n):
    hamms = {1}
    x = 2
    # twos = [2**i for i in range(int(n/4))]
    # threes = [3**i for i in range(int(n/4))]
    # fives = [5**i for i in range(int(n/4))]
    while len(hamms) < n:
        for a in range(1, n):
            i = x % (2**a)
            j = x % (3**a)
            k = x % (5**a)
            if i == 0 or j == 0 or k == 0:
                hamms.add(x)
        x += 1
    hamms = list(hamms)
    return hamms


# %%%
def hamming(n):
    hamming_numbers = [1] * n
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        next_hamming_number = min(
            next_multiple_of_2, next_multiple_of_3, next_multiple_of_5
        )
        hamming_numbers[i] = next_hamming_number

        if next_hamming_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = hamming_numbers[i2] * 2
        if next_hamming_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = hamming_numbers[i3] * 3
        if next_hamming_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = hamming_numbers[i5] * 5

    return hamming_numbers[-1]


# %%%
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



# %%%
def matrix_multiply(A, B):
    return [
        [sum(x * y for x, y in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A
    ]


def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        return matrix_power(matrix_multiply(matrix, matrix), n // 2)
    else:
        return matrix_multiply(
            matrix, matrix_power(matrix_multiply(matrix, matrix), (n - 1) // 2)
        )

def fibonacci_matrix(n):
    if n == 0:
        return 0
    result = matrix_power([[1, 1], [1, 0]], n)
    return result[0][1]


# %%%
def fibonacci_memoized(n, memo={}):
    if n in memo:return memo[n]
    if n <= 2:return 1
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# %%% ASCII (256) to Binary
def ascii_to_binary():
    return {chr(i): f"{i:08b}" for i in range(2048)}

def conv(let):
    ascii_to_bin = ascii_to_binary()
    print(ascii_to_bin[let])


# %%%
spoken = lambda greeting: greeting.capitalize() + "."
shouted = lambda greeting: greeting.upper() + "!"
whispered = lambda greeting: greeting.lower() + "."

greet = lambda style, msg: style(msg)


# %%%
def spin_words(sentence):
    ltw = sentence.split(" ")
    for i in range(len(ltw)):
        if len(ltw[i]) >= 5:
            ltw[i] = ltw[i][::-1]

    return " ".join(ltw)


# %%%
from itertools import product

def krazy_king_blackjack(hand, king_value):
    values = {'A': [1, 11], 'K': [10, king_value], 'Q': 10, 'J': 10}
    hand_values = [values[card] if card in values else int(card) for card in hand]
    all_combinations = product(*(value if isinstance(value, list) else [value] for value in hand_values))
    valid_totals = [sum(comb) for comb in all_combinations if sum(comb) <= 21]
    return max(valid_totals) if valid_totals else False




# %%%
def count_by(x, n):
    return list(i * x for i in range(1, n + 1))


# %%%
def encode(string):
    let, loc, on, stp = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ ",
        [char for char in string.upper()],
        ".",
        "",
    )
    for i in [let.index(loc[i]) + 1 for i in range(len(loc))]:
        # PAGE
        if i <= 9:
            page = 1
        elif 10 <= i <= 18:
            page = 2
        else:
            page = 3
        # COLUMN
        if i % 3 == 0:
            col = 3
        elif (i + 1) % 3 == 0:
            col = 2
        elif (i + 2) % 3 == 0:
            col = 1
        # ROW
        if (i - 1) // 3 == 0 or (i - 1) // 3 == 3 or (i - 1) // 3 == 6:
            row = 1
        elif (i - 1) // 3 == 1 or (i - 1) // 3 == 4 or (i - 1) // 3 == 7:
            row = 2
        else:
            row = 3
        stp += f"{col*on} {row*on} {page*on} "
    return stp[:-1]


def decode(string):
    stp, lets = "", [
        [["ABC"], ["DEF"], ["GHI"]],
        [["JKL"], ["MNO"], ["PQR"]],
        [["STU"], ["VWX"], ["YZ "]],
    ]
    if len(string.split(" ")) > 3:
        elements = string.split()
        grouped = [elements[i : i + 3] for i in range(0, len(elements), 3)]
        for i in range(len(grouped)):
            col, row, page = (
                len(grouped[i][0]) - 1,
                len(grouped[i][1]) - 1,
                len(grouped[i][2]) - 1,
            )
            stp += lets[page][row][0][col]
        return stp
    else:
        parts = string.split(" ")
        col, row, page = len(parts[0]) - 1, len(parts[1]) - 1, len(parts[2]) - 1
    return lets[page][row][0][col]


decode(".. . ... .. .. . . . ... .. . ...")


# %%%
def summ(n):
    count = 0
    for i in range(n):
        count += i
    return count


# summ(100000000)


def sumb(n):
    return int((n * (n + 1)) / 2)


sumb(1000000000)
#%%%
def binarySearch(nums, target):
	(left, right) = (0, len(nums) - 1)
	while left <= right:
		mid = (left + right) // 2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return -1




nums = [i for i in range(100)]
target = (43)
binarySearch(nums,target)
#%%%
import random
def findPair(nums, target):
    solution_list = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
              solution_list.append((nums[i],nums[j]))
    x = int(len(solution_list)/2)
    for i in range(x):
        print(solution_list[i]) 




findPair(list(set([random.randint(1,100) for i in range(100)])),17)
#%%%
def dec_to_bin(num):
    binary = []
    while num > 0:
        binary.insert(0,str(num%2))
        num = num//2
    print(int(''.join(binary)))


dec_to_bin(25)

def bin_to_dec(num):
    print(sum([int(num) for num in str(num)][i] * 
              (2 ** (len([int(num) for num in str(num)]) - i - 1)) 
              for i in range(len([int(num) for num in str(num)]))))

bin_to_dec(11001)
#%%%
import random
work = [['300 push-ups'], ['300 sit-ups', '150 sit-ups \n100 crunches', '200 crunches'], ['2 miles run', '5 mile bike']]



with open('WorkOut.txt', 'w') as file:
    for i in range(60):
        file.write(f'Workout {i+1} \n')
        file.write('-------------------\n')
        for i in range(len(work)):
            file.write(f'{random.choice(work[i])} \n')
        file.write('\n')

#%%%
def binarySearch(l, n):
    (left, right) = (0, len(l) - 1)
    while left <= right:
        mid = (left + right) // 2
        if n == l[mid]:
            return mid
        elif n < l[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

binarySearch([1, 3, 5, 7, 9, 11, 13, 15, 17], 7)

#%%%
def sortArray(nums):
    zeros = []
    ones = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append(nums[i])
        else:
            ones.append(nums[i])
    nums = zeros + ones
    print(nums)



sortArray([1, 0, 1, 0, 1, 0, 0, 1])
#%%%
def constructMaxSumNumber(nums):
		if len(nums) == 0:
			return ()
		else:
			nums.sort()
			nums = nums[::-1]
			first = []
			second = []
			for i in range(len(nums)):
				if i%2 == 0:
					first.append(str(nums[i]))
				else:
					second.append(str(nums[i]))
		first = int(''.join(first))
		second = int(''.join(second))			
					
					
		return first, second


constructMaxSumNumber([1,2,3,4,5,6,7,8,9])

#%%%

def solution(n, m):
    final_list = []
    for i in range(n,m+1):
        check_set = set()
        for j in range(i//2-1):
            if i % (j+2) == 0:
                check_set.add(j)
        if len(list(check_set)) == 3:
            final_list.append(i)
        check_set = set()


    return final_list

solution(2, 100000)




# %%
def solution(n, m):
    output = 0
    final = []
    i = 0
    while output <= m:
        output = i**4
        final.append(output)
        i+=1
    final.remove(0)
    return final

solution(2, 100)

# %%
import sympy
def solution(n,m):
    final = []
    for i in range(int(m**(1/4)+1)):
        if sympy.isprime(i) == True and i**4 >= n and i**4 <= m:
            final.append(i**4)
    return final




n = 95652679637664
m = 502559178816286656
solution(n,m)
# %%
def binary_ssearch(arr: list, k: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
    
    
    
binary_ssearch([1,2,2,2,3,3,4,5,6,7,8,9,],6)



#%%%
def bubble_sort(arr):

    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(f"{arr[i]}", end=" ")

#%%%
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
#%%%
import random
import time as t
def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(1,100) for i in range(100000)]
start = t.time()
insertion_sort(arr)
end = t.time()
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
print(end - start)

#%%%
import random
import time

def shell_sort(arr):

    n = len(arr)
    gap = n // 2 

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        
        gap //= 2  

arr = [random.randint(1,100) for i in range(100000)]
start = time.time()
shell_sort(arr)
end = time.time()
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
print(f'\n\nShell sort sorted the list in {end - start} seconds')
#%%%
def test_pal(txt: str, test: str):
    if len(txt) == len(test):
        txt = [i for i in txt]
        test = [i for i in test]
        txt.sort()
        test.sort()
        if txt == test:
            return True
        
    return False

test_pal('bla', 'alb')
#%%%
def my_bub_sort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    for i in range(len(arr)):
        print(arr[i], end=' ')



my_bub_sort([64, 34, 25, 12, 22, 11, 90])

#%%%
def bin_s(arr: list, k: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


bin_s([1,2,3,4,5,6,7,8],5)
#%%%
numList = [5,10,20,40,80]
if 40 in numList:
    index = numList.index(40)
    print(index)
#%%%
import random

def gen_list(rng: int):
    ltp = [ random.randint(0,100) for i in range(10)]
    return ltp
    
def sequentialSearch(alist, item):
    count = 0
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
            count += 1
        else:
            pos = pos + 1
            count += 1
    return found, count

def orderedSequentialSearch(alist, item):
    count = 0
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
        count += 1 

    return found, count




alist = gen_list(10)
k = random.randint(0,100)
print(k)
print(alist)
print(sequentialSearch(alist, k))
alist.sort()
print(alist)
print(orderedSequentialSearch(alist, k))

#%%%
def bin_ss(arr: list, k: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else: 
            right = mid - 1
            
    return -1
        
            
bin_ss([68, 37, 2, 49, 91, 22, 94, 18, 13, 1], 91)

#%%%
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)

#%%%
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)

#%%%
import random
import time as t


def my_bub_sort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def time_test():
    x = [1000,2000,4000,8000]
    for i in range(len(x)):
        ml = [random.randint(1,100) for j in range(x[i])]
        start = t.time()
        my_bub_sort(ml)
        end = t.time()
        print(f'List of length {x[i]}::: {end - start}')


def main():
    time_test()
    
  
    
checkL = [main() for i in range(60)]
print(min(checkL))


#%%%
import random
import time as t


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def time_test():
    x = [1000,2000,4000,8000]
    for i in range(len(x)):
        ml = [random.randint(1,100) for j in range(x[i])]
        start = t.time()
        bubbleSort(ml)
        end = t.time()
        print(f'List of length {x[i]}::: {end - start}')


def main():
    time_test()
    
    
main()
#%%%
# import random

# arr = [random.randint(1,9) for i in range(10)]
# summ = random.randint(2,18)

# print(arr)
# print(summ)




arr = [3,3]
summ = 6

def find_pair_sum(arr: list, summ: int):
    hash_t = {}
    for i in range(len(arr)):
        if summ - arr[i] in hash_t:
            return [hash_t[summ - arr[i]], i]
        else:
            hash_t[arr[i]] = i
    return -1
                

find_pair_sum(arr, summ)

#%%%

def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False

isPalindrome(121)


#%%%
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """Adds a child to this node"""
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Removes a child from this node"""
        self.children = [child for child in self.children if child is not child_node]

    def __repr__(self, level=0):
        """Helper method to print the tree structure"""
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


# Example usage
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child1_1 = TreeNode("Child 1.1")
child1_2 = TreeNode("Child 1.2")
child2_1 = TreeNode("Child 2.1")
child1_3 = TreeNode("Child 1.3")

root.add_child(child1)
root.add_child(child2)
child1.add_child(child1_1)
child1.add_child(child1_2)
child2.add_child(child2_1)
child1.add_child(child1_3)

print(root)

#%%%
def fac_tri():
    print("Print factorials in a triangular form in Python. ")
    from math import factorial
    rows = int(input("Please enter the number of rows:"))
    for i in range(rows):
        for j in range(rows-i+1):
            print(end=" ") # Leaving spaces on the left side.
        for j in range(i+1):
            print(factorial(i), end=" ")
        print() # for printing a new line
   



def generate_pascals_triangle(rows):
    triangle = []
    for n in range(rows):
        row = []
        for k in range(n + 1):
            row.append(factorial(n) // (factorial(k) * factorial(n - k)))
        triangle.append(row)
    return triangle



print("Print the list of elements of a Power set")
A={1,2,3}
length = len(A)
l = [a for a in A]
ps = set()
for i in range(2 ** length):
    selector = f'{i:0{length}b}'
    subset = {l[j] for j, bit in enumerate(selector) if bit == '1'}
    ps.add(frozenset(subset))
print("A=",A)
print("Elements of P(A) are:")
[set(s) for s in ps]

#%%%
from itertools import chain, combinations

def custom_power_set(lst):

    ps = list(chain.from_iterable(combinations(lst, r) for r in range(len(lst) + 1)))
    formatted_ps = []
    
    for subset in ps:
        if len(subset) == 0:
            formatted_ps.append("()")
        elif len(subset) == 1:
            formatted_ps.append(f"({subset[0]})")  
        else:
            formatted_ps.append(f"({', '.join(map(str, subset))})")  

    return formatted_ps, len(formatted_ps)


example_list = [2, 4, 6, 8, 10, 'one']


formatted_power_set = custom_power_set(example_list)
formatted_power_set
#%%%
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr




list1 = [54,26,93,17]
list2 = [77,31,44,55,20]
list3 = list1 + list2

print(merge_sort(list1))
print(merge_sort(list2))
print(merge_sort(list3))
#%%%
from itertools import product
import random



def create_stu_dict():
    total_students = 120
    grades = ['1/C', '2/C', '3/C', '4/C']
    genders = ['M', 'F']
    students_per_grade = total_students // len(grades)
    students_per_gender_per_grade = students_per_grade // len(genders)
    
    student_ids = list(range(1, total_students + 1))
    
    grade_gender_combinations = list(product(grades, genders))
    
    student_mapping = {}
    
    for grade, gender in grade_gender_combinations:
        eligible_student_ids = [student_id for student_id in student_ids if student_id not in student_mapping]
        selected_students = random.sample(eligible_student_ids, students_per_gender_per_grade)
        for student_id in selected_students:
            potential_roommates = [
                sid for sid in selected_students if sid != student_id
            ]
            roommates = random.sample(potential_roommates, 3)
            
            student_mapping[student_id] = {
                'gender': gender,
                'grade': grade,
                'rooming_preference': roommates
            }
    
    assert len(student_mapping) == total_students, "Total students do not match."
    for details in student_mapping.values():
        assert len(details['rooming_preference']) == 3, "Rooming preferences do not match."
    
    dos = dict(list(student_mapping.items()))

    return dos



class Student:
    def __init__(self, student_id, gender, grade, rooming_preference):
        self.name = student_id
        self.gender = gender
        self.grade = grade
        self.rooming_preference = rooming_preference
        self.room = None  

    @classmethod
    def create_students_from_dict(cls, student_dict):
        return [cls(student_id=key, **details) for key, details in student_dict.items()]



class Room:
    last_room_number = 999 

    def __init__(self, capacity):
        Room.last_room_number += 1  
        self.room_number = Room.last_room_number 
        self.capacity = capacity
        self.students = []  

    def __str__(self):
        return f"Room {self.room_number} (Capacity: {self.capacity}, Occupants: {len(self.students)})"



class Housing:
    def __init__(self, num_two_person_rooms, num_three_person_rooms):
        self.rooms = self.create_rooms(num_two_person_rooms, num_three_person_rooms)

    def create_rooms(self, num_two_person, num_three_person):
        rooms = []
        for _ in range(num_two_person):
            rooms.append(Room(2)) 
        for _ in range(num_three_person):
            rooms.append(Room(3)) 
        return rooms

    def __str__(self):
        room_strs = [str(room) for room in self.rooms]
        return "\n".join(room_strs)



def assign_students_to_rooms(students, housing):
    grouped_students = {}
    for student in students:
        key = (student.gender, student.grade)
        grouped_students.setdefault(key, []).append(student)
    
    room_index = 0

    for _, student_group in grouped_students.items():
        student_group.sort(key=lambda x: len(x.rooming_preference), reverse=True) 
        for student in student_group:
            if student.room is not None:
                continue

            while room_index < len(housing.rooms) and len(housing.rooms[room_index].students) == housing.rooms[room_index].capacity:
                room_index += 1 

            if room_index < len(housing.rooms):
                room = housing.rooms[room_index]
                student.room = room
                room.students.append(student)


                for preferred_id in student.rooming_preference:
                    if len(room.students) < room.capacity:
                        for potential_roommate in student_group:
                            if potential_roommate.name == preferred_id and potential_roommate.room is None:
                                potential_roommate.room = room
                                room.students.append(potential_roommate)
                                break

                if len(room.students) == room.capacity:
                    room_index += 1  

    print("\nRoom Assignments:")
    for room in housing.rooms:
        if room.students:
            print(f"Room {room.room_number} ({room.capacity}-person room):")
            for student in room.students:
 
                student_name_str = str(student.name)

                print(f" - Student {student_name_str}")
        else:
            break 



def score_for_student(student, room):
    score = 0
    preferences = student.rooming_preference
    for roommate in room.students:
        if roommate == student:
            continue  
        if roommate.name in preferences:
            score += (3 - preferences.index(roommate.name)) * 2 + 1  
        else:
            score -= 3
    return score / (len(room.students) - 1)



def calculate_average_score(housing):
    total_score = 0
    num_students = 0
    
    for room in housing.rooms:
        if not room.students:
            continue 
        room_score = 0
        for student in room.students:
            room_score += score_for_student(student, room)
        total_score += room_score
        num_students += len(room.students)
    
    average_score = total_score / num_students if num_students else 0
    return average_score



def swap_students(student1, student2, room1, room2):
    try:
        if student1 in room1.students and student2 in room2.students:
            room1.students[room1.students.index(student1)], room2.students[room2.students.index(student2)] = student2, student1
            
            student1.room, student2.room = student2.room, student1.room
            return True 
    except ValueError:
        pass 

    return False  



def optimize_assignments_for_max_score(housing):    
    improvement_found = True
    while improvement_found:
        improvement_found = False
        current_score = calculate_average_score(housing)
        print(f"Current Average Score: {current_score}")  
        
        for room1 in housing.rooms:
            for student1 in room1.students[:]: 
                for room2 in housing.rooms:
                    if room1 == room2:
                        continue
                    
                    for student2 in room2.students[:]:  
                        if swap_students(student1, student2, room1, room2):
                            new_score = calculate_average_score(housing)
                            
                            if new_score > current_score:
                                current_score = new_score
                                improvement_found = True
                            else:
                                swap_students(student1, student2, room2, room1)




def print_room_assignments(housing):
    print("\nCurrent Room Assignments:")
    for room in housing.rooms:
        if room.students:
            print(f"Room {room.room_number} ({room.capacity}-person room):")
            for student in room.students:
                print(f" - Student {student.name}")
        else:
            print(f"Room {room.room_number} is empty.")
            continue  



def iterative_optimization(housing):
    previous_score = calculate_average_score(housing)
    print(f"Starting Average Score: {previous_score}")
    
    while True:
        optimize_assignments_for_max_score(housing)
        new_score = calculate_average_score(housing)
        print(f"New Optimized Average Score: {new_score}")
        
        if new_score <= previous_score:
            print("Optimization has converged to the best solution.")
            break  
        
        print("Improvement found, printing new room assignments.")
        print_room_assignments(housing) 
        
        previous_score = new_score



def main():
    
    # DOS = create_stu_dict()
    DOS = {18: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [69, 120, 95]}, 118: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [18, 111, 97]}, 76: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [17, 118, 31]}, 69: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [18, 17, 76]}, 27: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [76, 97, 4]}, 17: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [31, 69, 27]}, 31: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [27, 69, 2]}, 103: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [97, 120, 118]}, 97: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [2, 103, 4]}, 5: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [95, 118, 18]}, 
           2: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [97, 111, 118]}, 4: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [111, 17, 18]}, 111: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [76, 97, 95]}, 95: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [118, 2, 120]}, 120: {'gender': 'M', 'grade': '1/C', 'rooming_preference': [118, 31, 97]}, 108: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [6, 105, 87]}, 40: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [105, 6, 114]}, 114: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [46, 10, 104]}, 6: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [40, 104, 10]}, 89: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [87, 22, 6]}, 
           41: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [88, 25, 34]}, 87: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [6, 34, 22]}, 46: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [25, 40, 10]}, 34: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [114, 40, 104]}, 105: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [87, 10, 89]}, 22: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [114, 25, 105]}, 104: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [41, 25, 46]}, 10: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [22, 40, 105]}, 88: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [10, 108, 87]}, 25: {'gender': 'F', 'grade': '1/C', 'rooming_preference': [41, 34, 88]}, 
           75: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [59, 38, 61]}, 42: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [39, 61, 81]}, 61: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [106, 42, 71]}, 113: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [39, 73, 42]}, 91: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [59, 42, 94]}, 38: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [61, 102, 73]}, 73: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [102, 94, 61]}, 94: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [61, 113, 59]}, 59: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [73, 75, 71]}, 102: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [71, 39, 59]}, 
           106: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [73, 38, 81]}, 81: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [73, 45, 106]}, 45: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [94, 91, 81]}, 71: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [59, 102, 42]}, 39: {'gender': 'M', 'grade': '2/C', 'rooming_preference': [91, 102, 106]}, 62: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [44, 60, 43]}, 74: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [79, 72, 56]}, 72: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [110, 56, 52]}, 55: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [72, 79, 43]}, 56: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [52, 55, 44]}, 
           52: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [74, 66, 62]}, 79: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [72, 110, 43]}, 70: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [56, 62, 79]}, 66: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [52, 43, 79]}, 53: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [70, 44, 66]}, 110: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [56, 53, 79]}, 15: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [110, 52, 44]}, 60: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [56, 79, 15]}, 43: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [62, 56, 66]}, 44: {'gender': 'F', 'grade': '2/C', 'rooming_preference': [110, 53, 62]}, 
           80: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [112, 29, 78]}, 58: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [35, 48, 37]}, 117: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [35, 100, 48]}, 37: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [96, 33, 100]}, 35: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [78, 7, 80]}, 26: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [112, 100, 83]}, 100: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [58, 48, 7]}, 83: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [80, 26, 112]}, 7: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [112, 29, 33]}, 96: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [7, 80, 48]}, 
           78: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [100, 33, 58]}, 112: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [80, 58, 7]}, 29: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [83, 35, 80]}, 33: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [26, 78, 100]}, 48: {'gender': 'M', 'grade': '3/C', 'rooming_preference': [100, 78, 96]}, 90: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [1, 109, 86]}, 101: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [51, 86, 49]}, 36: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [101, 49, 92]}, 11: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [36, 1, 68]}, 93: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [86, 51, 49]}, 
           14: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [64, 36, 93]}, 85: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [14, 101, 51]}, 109: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [90, 86, 93]}, 1: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [14, 109, 85]}, 51: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [93, 85, 101]}, 92: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [11, 101, 86]}, 68: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [86, 109, 51]}, 64: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [85, 86, 92]}, 86: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [90, 68, 92]}, 49: {'gender': 'F', 'grade': '3/C', 'rooming_preference': [109, 101, 92]}, 
           3: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [8, 20, 116]}, 116: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [98, 19, 63]}, 63: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [30, 84, 65]}, 21: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [50, 63, 30]}, 8: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [21, 98, 116]}, 19: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [107, 99, 20]}, 50: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [8, 77, 63]}, 84: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [77, 65, 116]}, 107: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [30, 116, 8]}, 99: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [98, 107, 77]}, 
           98: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [99, 116, 8]}, 30: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [20, 84, 107]}, 77: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [50, 98, 21]}, 20: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [21, 98, 116]}, 65: {'gender': 'M', 'grade': '4/C', 'rooming_preference': [8, 50, 99]}, 82: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [24, 23, 67]}, 13: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [28, 115, 82]}, 23: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [119, 32, 54]}, 119: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [28, 54, 47]}, 57: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [16, 9, 23]}, 
           47: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [119, 12, 9]}, 24: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [47, 119, 67]}, 115: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [12, 119, 47]}, 9: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [54, 115, 13]}, 28: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [82, 47, 24]}, 32: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [24, 54, 16]}, 54: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [13, 32, 119]}, 16: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [119, 115, 23]}, 67: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [32, 13, 82]}, 12: {'gender': 'F', 'grade': '4/C', 'rooming_preference': [28, 115, 9]}}
    
    
    
    students = Student.create_students_from_dict(DOS)
    num_two_person_rooms = 30
    num_three_person_rooms = 30
    housing = Housing(num_two_person_rooms, num_three_person_rooms)
    

    assign_students_to_rooms(students, housing)
    
    iterative_optimization(housing)
    
    final_optimized_score = calculate_average_score(housing)
    print(f"Final Optimized Score: {final_optimized_score}")



main()
#%%%
import time as t
import random as r

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
def insertionSort(aList) :
    for index in range(1, len(aList)) :
        currentValue = aList[index]
        position = index
        while position > 0 and aList[position-1] > currentValue :
            aList[position] = aList[position-1]
            position = position - 1
        aList[position] = currentValue
    return aList

def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i<len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j<len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp
        
def shell_sort(arr):
    n = len(arr)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 
    return arr

def main():
    my_list = [r.randint(1,10) for i in range(8000)]
    
    start = t.time()
    bubbleSort(my_list)
    end = t.time()
    
    bubble_sort_time = end - start
    
    
    start = t.time()
    insertionSort(my_list)
    end = t.time()
    
    insertion_sort_time = end - start
    
    
    start = t.time()
    mergeSort(my_list)
    end = t.time()
    
    merge_sort_time = end - start
    
    
    start = t.time()
    quick_sort(my_list)
    end = t.time()
    
    quick_sort_time = end - start
    
    
    start = t.time()
    selectionSort(my_list)
    end = t.time()
    
    selection_sort_time = end - start
    
    
    start = t.time()
    shell_sort(my_list)
    end = t.time()
    
    shell_sort_time = end - start
    
    
    start = t.time()
    my_list.sort()
    end = t.time()
    
    tim_sort_time = end - start
    
    
    
    print(f'Bubble Sort Time::: {bubble_sort_time}\nInsertion Sort Time::: {insertion_sort_time}\nMerge Sort Time::: {merge_sort_time}\nQuick Sort Time::: {quick_sort_time}\nSelection Sort Time::: {selection_sort_time}\nShell Sort Time::: {shell_sort_time}\nPython Sort Time::: {tim_sort_time}\n')

main()

#%%%
def binary_ssearch(arr: list, k: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

#%%%
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)





gcd(345, 92)
#%%%
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_dist = float("inf")
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not sptSet[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not sptSet[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Example usage
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]



#%%%
import cv2
import imutils
import socket
import base64

host_name = socket.gethostname()
host = socket.gethostbyname(host_name)
port = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
BUFF_SIZE = 65535

server_socket.bind((host, port))
print(f"Server IP address: {host}")

vid = cv2.VideoCapture('USCGA.mp4')
WIDTH = 400


while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print(msg.decode('utf-8'))
    
    while vid.isOpened():
        chk, frame = vid.read()
        if not chk:
            print("Not recieving data... quitting")
            break
    
        frame = imutils.resize(frame, width=WIDTH)
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)

        server_socket.sendto(message, client_addr)
        cv2.imshow('SERVER VIDEO', frame)
        
    if cv2.waitKey(10) & 0xFF == 13:
        break
#%%%

import cv2
import socket
import numpy as np
import base64


host_name = socket.gethostname()
host = socket.gethostbyname(host_name)
port = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
BUFF_SIZE = 65535

message = b'Ready for stream'
client_socket.sendto(message, (host, port))

while True:
    packet, server_addy = client_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet)
    
    np_array = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imencode(np_array, 1)
    cv2.imshow("CLIENT", frame)
    
    if cv2.waitKey(10) & 0xFF == 13:
        break
#%%%
import sympy
import random


def create_public_key(p: int, q: int): # returns e, n
    def euler_phi_efficient(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    n = p * q
    phi_n = euler_phi_efficient(n)
    
    primes = list(sympy.primerange(2, n))
    
    coprime_primes = [prime for prime in primes if sympy.gcd(prime, phi_n) == 1]
    
    if not coprime_primes:
        raise ValueError("No valid prime found for e that is coprime to phi(n)")
    e = random.choice(coprime_primes)

    return e, n




def digitalize(mess: str): # returns message
    message = [format(ord(char), '08b') for char in mess]
    return message




def RSA_E(public_key: tuple, message: list): # returns message
    e, n = public_key
    for i in range(len(message)):
        message[i] = (message[i] ** e) % n
        
    return message
    
    
    
def RSA_D(private_key: tuple, encrypted_message: list): # returns message
    n, d = private_key
    decrypted_message = [(c ** d) % n for c in encrypted_message]
    return decrypted_message



def asciize(mess: list): # returns message
    message = ''.join(chr(int(binary, 2)) for binary in mess)
    return message



def find_possible_private_keys(n: int, e: int): # returns d

    factors = sympy.ntheory.factorint(n)
    if len(factors) != 2 or any(factors.values()) != 1:
        raise ValueError("n must be a product of two distinct primes")
    
    primes = list(factors.keys())
    p, q = primes[0], primes[1]

    phi_n = (p - 1) * (q - 1)
    

    d = sympy.mod_inverse(e, phi_n)
    
    if d is None:
        return []
    
    return d


"""
How to send:::
    1) create your public key (insert 2 prime numbers)
    2) now digitalize your message (input your message as a string)
    3) now you may encrypt using the public key and the message as your inputs
    4) send :)
    
How to recieve:::
    1) decrypt by inputing the private key and the message
        1a) if you do not have the private key, attempt to find it using the find_possible_private_keys by inputting the public key
    2) asciize the message to read
    3) done :)
"""


#%%%
import random
import time
import matplotlib.pyplot as plt

BEST_FIT_VAL = 100000000
MAX_NUM_GENERATIONS = 100000
MIN_ACCEPTANCE_RATE = 4
VALUE_RANGE = (0, 10000)
MUTATION_RATE = 0.01
GENERATIONS_PER_SECOND = 150

def foo(x, y, z):
    return 81*x**6 + 2*y**4 + 900*z - 100

def fitness(x, y, z):
    ans = foo(x, y, z)
    if ans == 0:
        return BEST_FIT_VAL
    else:
        return abs(1/ans)

def gen_algo():
    datapt = []
    
    solutions = []
    for s in range(1000):
        solutions.append((random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE), 
                          random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE), 
                          random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)))
    
    for i in range(MAX_NUM_GENERATIONS):
        start_time = time.time() 
        
        rankedsolutions = []
        for s in solutions:
            rankedsolutions.append((fitness(s[0], s[1], s[2]), s))
        rankedsolutions.sort(reverse=True)
        
        best_fitness = rankedsolutions[0][0]
        datapt.append((i, best_fitness))  
        
        print(f"=== Gen {i} best solutions === ")
        print(rankedsolutions[0])
        
        if best_fitness > 10 ** (MIN_ACCEPTANCE_RATE + 1):
            break
    
        bestsolutions = rankedsolutions[:100]
    
        elements = []
        for s in bestsolutions:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
    
        newGen = []
        for _ in range(1000):
            e1 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            e2 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            e3 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            newGen.append((e1, e2, e3))
        
        solutions = newGen
    
        elapsed_time = time.time() - start_time
        sleep_time = max(0, 1/GENERATIONS_PER_SECOND - elapsed_time) 
        time.sleep(sleep_time)

    generations, fitness_scores = zip(*datapt)  
    plt.figure(figsize=(12, 6))
    plt.bar(generations, fitness_scores, color='blue')
    plt.title('Best Fitness Score by Generation')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness Score')
    plt.grid(True)
    plt.show()





for i in range(15):
    gen_algo()

#%%%













































































































































































































































































































































# %%
