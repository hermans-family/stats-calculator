"""
This is a multi-line comment.  Anything include between the triple quotes is
ignored by Python.  This is where we put notes for people.

It might help to read this program from the bottom up.  Start with the main function and work your way back up
to this.
"""

# This is a single-line comment.  You can include a one line comment using the # symbol.


def calculate_vig_hp(stat_value):
    """
    This is a function.  It takes in a parameter called stat_value and outputs its contribution to
    HP.  This function only calculates the contributions from the Vigor attribute.  HP scales with vigor
    differently than the other attributes.

    At 0 Vigor, players have 500 max HP
    From level 0 to 20, Vigor raises max HP by 30 points per attribute point
    From level 21 to 50, Vigor raises max HP by 20 points per attribute point
    From level 51 to 99, Vigor raises max HP by 5 points per attribute point
    """

    # If the stat_value is greater than or equal to 51, use the calculations from this part
    if stat_value >= 51:
        levels_51_to_99 = stat_value - 50
        levels_21_to_50 = 30  # Why is this 30?
        levels_0_to_20 = 20  # Why is this 20?
    # If the stat value is less than or equal to 50 and greater than or equal to 21, use these numbers
    elif 21 <= stat_value <= 50:
        levels_51_to_99 = 0  # Why is this 0?
        levels_21_to_50 = stat_value - 20
        levels_0_to_20 = 20
    # If the stat value is not greater than or equal to 51 or between 21 and 51.
    else:
        levels_51_to_99 = 0
        levels_21_to_50 = 0
        levels_0_to_20 = stat_value

    # This calculates the amount of hp_from_vig. There is 500 base HP, plus the results from each level
    hp_from_vig = 500 + levels_0_to_20 * 30 + levels_21_to_50 * 20 + levels_51_to_99 * 5

    # Finally, we return the value of the calculation
    return hp_from_vig


def calculate_other_hp(stat_value):
    """
    This function needs to calculate stat values for attributes other than vigor.  It should look a lot like the
    one for vigor, but should have different contributions.

    From level 0 to 20, any stat besides Vigor raises max HP by 2 points per attribute point
    From level 21 to 50, any stat besides Vigor raises max HP by 1 point per attribute point
    From level 51 to 99, any stat besides Vigor raises max HP by 0 points per attribute point
    """
    return 0


def calculate_hp(attributes):
    """
    This is a function that takes in the attributes and calculates the HP.
    """
    hp = 0  # HP starts out at zero and we add to it

    for stat_name, stat_value in attributes.items():
        if stat_value > 99:
            # This is checking to
            raise Exception('Value for stat %s is %s.  Maximum value for stat is 99.' % (stat_name, stat_value))
        elif stat_value < 0:
            raise Exception('Value for stat %s is %s. Stats cannot be negative!' % (stat_name, stat_value))

        # If the stat is vigor, use the special vigor calculation function.
        if stat_name == 'vig':

            vig_hp = calculate_vig_hp(stat_value)

            #  This is short for hp = hp + vig_hp. Programmers are lazy.
            hp += vig_hp
        else:
            other_hp = calculate_other_hp(stat_value)

            # This is short for hp = hp + other_hp.  See statement above.
            hp += other_hp

    return hp


def main():
    """
    This is the main function.  Basically, it is where you put all the pieces together to make a functioning
    program.
    """

    '''
    We store our attributes in a Python dictionary.  A dictionary is a way to associate keys and values.  In this
    case our keys are the names of the attributes and our values are the values for those attributes.  In this case,
    vig is a key and its value is 5. str is another key and its value is 10.  dex is another key and its value is 7.

    We can't have two entries in this dictionary with the same key.  For example, we couldn't have two entries in this
    dictionary with dex for a key name.  If it did, then it wouldn't know how to lookup the value for dex.  Think of
    this kind of like a regular dictionary.  You have a word and you want to look up the definition.
    '''
    attributes = {
        'vig': 5,
        'str': 10,
        'dex': 7,
        'int': 3
    }

    # This calls the calculate_hp function and returns the result.
    hp = calculate_hp(attributes)

    # This prints the results out to the command line. The %s tells python to substitute the results of hp into %s
    print('Your HP is %s' % hp)

if __name__ == '__main__':
    """
    This is just something Python needs to run the main function.  It is pretty much standard for Python
    projects.
    """
    main()
