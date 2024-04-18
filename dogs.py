# Name: Xinnan Wei
# Prog Purpose: This program demostrates how to manipulate a list, including: 
# finding number of items in the list, sorting the list, sorting the list, adding/ removing items,
# copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie","Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle",
        "Gonzo", "Sweetie-Pie", "Diego"]
dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of dogs in the list, using len): " + str(how_many))
    print("\nOriginal list of dog names:")
    print(dogs)
    pause()

    dogs.reverse()
    print("\nList from last to first, using reverse():")
    print(dogs)
    pause()

    dogs.sort()
    print("\nAlphabetized list, using reverse()")
    print(dogs)
    pause()

    dogs.sort(reverse = True)
    print("\nList in reverse alphabetized order, using sort(reverse = True)")
    print(dogs)
    pause()

    dogs.append("Ranger")
    print("\nAdd a dog to the end of a list, using append(): ")
    print(dogs)
    pause()

    doggy = dogs.pop(0)
    print("\nRemove a dog off rom the front of the list, using pop():")
    print(dogs)
    pause()

    another_dog = dogs.pop(3)
    print("Remove a dog from position 3 (the 4th dog) in the list, using pop(index-here):")
    print(dogs)
    print(another_dog + " was ermoved from position 3 of the list.")
    pause()

    dogs.remove('AnnaBelle')
    print("\nRemove a dog by name rather than position in the list, using remove(name-here):")
    print(dogs)
    pause()

    dogs2 = dogs
    print("\nA list can be copied into another list by setting one equal to the other:")
    print("Dogs: ")
    print(dogs)
    print("Dogs2: ")
    print(dogs2)
    pause()

    print("\nUse a FOR loop to give each dog in the the same last name, using the for loop:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Wei"
        print(dogs)

def pause():
    press_enter = input("\n\nPress ENTER to continue... ")

main()

