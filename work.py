
cord_1 = tuple(int(x) for x in input("ENTER THE COORDINATES WITH SPACE PROVIDED: ").split())
cord_2 = tuple(int(x) for x in input("ENTER THE COORDINATES WITH SPACE PROVIDED: ").split())
dist = ((cord_1[0] - cord_2[0]) ** 2 + (cord_1[1] - cord_2[1]) ** 2+(cord_1[2] - cord_2[2]) ** 2) ** 0.5
print(f"The distance between {cord_1} and {cord_2} is {dist:.2f}")
