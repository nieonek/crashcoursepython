file_counts={"jpg":10,"txt":14,"csv":2,"py":23}
for ext in file_counts:
    print(ext)

for ext, amount in file_counts.items():
    print(F"There are {amount} files with the .{ext} extension")


def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] +=1
    return result
print(count_letters("abrakadabra"))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for ciuch, kolor in wardrobe.items():
    for k in kolor:
        print(F"{k}{ciuch}")

        # Dictionary Methods
        #
        # Definition
        #
        # x = {key1: value1, key2: value2}
        #
        # Operations
        #
        # len(dictionary) - Returns the number of items in the dictionary
        # for key in dictionary - Iterates over each key in the dictionary
        # for key, value in dictionary.items() - Iterates over each key, value pair in the dictionary
        # if key in dictionary - Checks whether the key is in the dictionary
        #
        # dictionary[key] - Accesses the item with key key of the dictionary
        #
        # dictionary[key] = value - Sets the value associated with key
        # del dictionary[key] - Removes the item with key key from the dictionary
        #
        # Methods
        #
        # dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
        #
        # dict.keys() - Returns a sequence containing the keys in the dictionary
        #
        # dict.values() - Returns a sequence containing the values in the dictionary
        # dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary.
        #                                 Existing entries will be replaced; new entries will be added.
        #
        # dict.clear() - Removes all the items of the dictionary

