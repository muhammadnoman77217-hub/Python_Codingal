basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("orange")
print("Fruits is both baskets:", basket1)

common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts after adding items:", fruit_counts)

fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("Fruit counts after adding items:", fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Number of items 4 appears:", count_of_4)

fruit_counts.reverse()
print("Reversed fruits counts array:", fruit_counts)

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket1:", basket1)
print("Basket2:", basket2)
print("shared fruits:", common_fruits)
print("Fruit counts:", fruit_counts)
print("==================================")