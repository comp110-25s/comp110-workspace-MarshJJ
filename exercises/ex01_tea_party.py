"""My Code for Exercise 01 - Tea Party!"""

__author__ = "730665617"


def main_planner(guests: int) -> None:
    """The entrypoint of the program, describes all of the details about the party"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests),
                               treat_count=treats(people=guests))))


def tea_bags(people: int) -> int:
    """Returns the total amount of tea bags required for some amount of people"""
    return 2 * people


def treats(people: int) -> int:
    """Returns the total amount of treats required for some amount of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of the party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
