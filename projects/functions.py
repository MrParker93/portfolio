import random
import time


def list_creator(list):
    """
    Create a list from the listber inserted
    :param list: int
    :return:
    """
    new_list = [i for i in range(list)]
    return new_list


def choose_random_answer(li):
    """
    Select a random element from the list provided
    :param li: int
    :return:
    """
    answer = random.choice(li)
    return answer


def give_hint(guesses_left, answer, list):
    """
    Gives the user a hint to help guess the answer.
    Hint returned based on the listber of guesses left used.
    :param list:
    :return:
    """
    if guesses_left == 4:
        print(f"Hint: {answer * 7} is a multiple of the answer")

    if guesses_left == 3:
        if answer % 2 != 0:
            print("Hint: The answer is an odd number")

        else:
            print("Hint: The answer is an even number")

    if guesses_left == 2:
        if len(list) % 2 != 0:
            halfway = int(len(list) - 1 / 2)
            halfway_plus_1 = int((len(list) - 1 / 2) + 1)
            if answer in list[0:halfway]:
                print(f"Hint: The answer is between {list[0]} and {list[halfway]}")
            elif answer in list[halfway_plus_1:]:
                print(f"Hint: The answer is between {list[halfway_plus_1]} and {list[len(list) - 1]}")
        else:
            halfway = int(len(list) / 2)
            if answer in list[0: halfway]:
                print(f"Hint: The answer is between {list[0]} and {list[halfway]}")
            elif answer in list[halfway:]:
                print(f"Hint: The answer is between {list[halfway]} and {list[len(list) - 1]}")


def timed_func(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        result = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return result
    return timed