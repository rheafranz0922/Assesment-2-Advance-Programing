import tkinter as tk
import requests
from threading import Thread
# meal data link
api = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"
meals = []
meal_number = 0

window = tk.Tk()
window.geometry("600x200")
window.title("Meal Database")
window.resizable(False, False)
window.configure(bg="blue")

#preload the meals in the background
def preload_meals():
    global meals

    print("***more meals***")
    for x in range(15):
        random_meal = requests.get(api).json()["meals"][0]
        content = random_meal["strMeal"]
        chef = random_meal["strArea"]
        meal_text = f"{content}\n\nBy {chef}"
        print(content)
# Append the formatted meal to information the list of a meals.
        meals.append(meal_text)

    print("***Finished loading more meals!***")

#to display the details of a random meal.
def get_random_meal():
    global meals_label
    global meals
    global meal_number

    # Check if all meals are displayed.
    if meal_number == len(meals):
        preload_meals()

    meals_label.configure(text=meals[meal_number])
    print(meal_number)
    meal_number += 1

meals_label = tk.Label(window, text="Click on the button to get the details of a meal!",
                       height=5,
                       pady=10,
                       wraplength=500,
                       font=("Helvetica", 16))
meals_label.pack(pady=30)
# Create a button to trigger the display of a random meal
button = tk.Button(window, text="Generate", command=get_random_meal, bg='#CCCCFF', fg="#ffffff",
                   activebackground='white', font=("Helvetica", 16))
button.pack(pady=10)

if __name__ == "__main__":
    preload_meals() 
    window.mainloop()
