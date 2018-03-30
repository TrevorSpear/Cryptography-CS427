import md5
import random


def main():
    # Calls encr
    answer1, answer2, answer3, answer4 = encrypt()

    # Once a collision is found it is printed out
    print "Collision found:"
    print answer2
    print answer4

    print "Hash is:"
    print answer1
    print answer3


def encrypt():
    # Mapping and setting up variables
    encryptMapping = {}
    done1 = True

    # Continues until collision is found
    while done1:

        # Random username with due date
        current_username = username() + "|20180226"

        # Hashes username
        encr = md5.new()
        encr.update(current_username)

        # Grabs the first 10 characters
        new_hash = encr.hexdigest()
        current_hash = new_hash[0:10]

        # Check if the first 10 characters are in hash map
        if current_hash not in encryptMapping:
            encryptMapping[current_hash] = (new_hash, current_username)
        else:
            (check1, check2) = encryptMapping[current_hash]

            if check2[0:6] == "mikero":
                return check1, check2, new_hash, current_username

        # Username with random date
        rand_num = "mikero|" + randDate()

        # Hashes username
        encr = md5.new()
        encr.update(rand_num)

        # Grabs first 10 characters
        new_hash = encr.hexdigest()
        current_hash = new_hash[0:10]

        # Checking if first 10 characters are in hash map
        if current_hash not in encryptMapping:
            encryptMapping[current_hash] = (new_hash, rand_num)
        else:
            (check1, check2) = encryptMapping[current_hash]

            if check2.endswith("20180226"):
                # Found a collision of what I want
                return check1, check2, new_hash, rand_num


# Gives back a random length username (0,8) with random characters in it
def username():
    num_char = random.randint(1, 8)
    str_name = ""

    for x in range(0, num_char):
        numAl = random.randint(0, 25)
        str_name = str_name + chr(ord('a') + numAl)

    return str_name


# Gives back a random date yyyymmdd as a string
def randDate():
    year = 2018
    month = 2
    day = 26

    # While it isn't a valid date
    while year == 2018 and month >= 2 and day >= 26:
        year = random.randint(1, 2018)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

    syear = str(year)
    smonth = str(month)
    sday = str(day)

    # Need to make sure it is a certain length
    while len(syear) != 4:
        syear = "0" + syear

    if len(smonth) != 2:
        smonth = "0" + smonth

    if len(sday) != 2:
        sday = "0" + sday

    return syear + smonth + sday


if __name__ == "__main__":
    main()
