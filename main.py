import tkinter as tk
from tkinter import messagebox

# Set up the color scheme
BG_COLOR = '#00FF00' # Soft white
TEXT_COLOR = '#010101' # Soft black
BUTTON_COLOR = '#FFF' # Soft green

activity_level = {
    "Низкая активность": 1.2,
    "Небольшая активность": 1.375,
    "Умеренная активность": 1.55,
    "Повышенная активность": 1.725,
    "Высокая активность": 1.9
}

def calculate_calories():
    height = entry_height.get()
    weight = entry_weight.get()
    age = entry_age.get()

    if not height or not weight or not age:
        messagebox.showerror("Error", "Неправильный ввод.")
        return

    height = float(height)
    weight = float(weight)
    age = float(age)

    # Calculate the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    # Calculate the total number of calories needed per day
    total_calories = int(bmr * activity_level[var_activity.get()])

    # Suggest a possible diet with that number of calories
    breakfast = int(total_calories * 0.3)
    lunch = int(total_calories * 0.4)
    dinner = int(total_calories - breakfast - lunch)

    print(breakfast, lunch, dinner)

    # Generating meals
    breakfast_example = ""
    if 0 <= breakfast <= 750:
        breakfast_example = "Овсяные хлопья, вода"
    elif 750 <= breakfast <= 1000:
        breakfast_example = "Яичница из 2 яиц с сыром и фруктовый салат"
    elif 1000 <= breakfast <= 1500:
        breakfast_example = "Печеные яйца с беконом и овощами"
    else:
        breakfast_example = "Кол-во ккал больше лимита"

    lunch_example = ""
    if 0 <= lunch <= 750:
        lunch_example = "Макароны с томатным соусом"
    elif 750 <= lunch <= 1100:
        lunch_example = "Тушеная курица с овощами"
    elif 1100 <= lunch <= 1700:
        lunch_example = "Куриный суп с овощами"
    else:
        lunch_example = "Кол-во ккал больше лимита"

    dinner_example = ""
    if 0 <= dinner <= 750:
        dinner_example = "Паста с морепродуктами"
    elif 750 <= dinner <= 1000:
        dinner_example = "Стейк из тунца, овощной салат"
    elif 1000 <= dinner <= 1500:
        dinner_example = "Рис с курицей и соусом, хлеб"
    else:
        dinner_example = "Кол-во ккал больше лимита"
    
    message = f"Вы должны есть {total_calories} ккал в день.\nВы должны потреблять {int(int(weight) * activity_level[var_activity.get()])}г. белков в день.\nВы должны потреблять {int(int(weight) * 1.2)}г. жиров в день.\nВы должны потреблять {int(int(weight)*2)}г. углвеводов в день\n\n"
    message += f"Завтрак: {breakfast_example}\n"
    message += f"Обед: {lunch_example}\n"
    message += f"Ужин: {dinner_example}"

    # Create a new window to display the menu
    menu_window = tk.Toplevel(root)
    menu_window.title("Меню")
    menu_window.geometry("400x300")

    menu_label = tk.Label(menu_window, text=message)
    menu_label.pack()

    # Add a button to close the menu window
    close_button = tk.Button(menu_window, text="Закрыть", command=menu_window.destroy)
    close_button.pack()

root = tk.Tk()
root.geometry("800x600")
root.resizable(True, True)
root.title("Калькулятор")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Рост (см):", bg='white', fg=TEXT_COLOR).pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Вес (кг):", bg='blue', fg=TEXT_COLOR).pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Возраст (лет):", bg='red', fg=TEXT_COLOR).pack()
entry_age = tk.Entry(root)
entry_age.pack()

var_activity = tk.StringVar(root)
var_activity.set("Низкая активность")

tk.Label(root, text="Уровень активности:", bg=BG_COLOR, fg=TEXT_COLOR).pack()
for text, mode in activity_level.items():
    tk.Radiobutton(root, text=text, variable=var_activity, value=text, bg=BG_COLOR, fg=TEXT_COLOR).pack()

tk.Button(root, text="Calculate", command=calculate_calories, bg=BUTTON_COLOR, fg='#000').pack()

welcome_window = tk.Toplevel(root)
welcome_window.title("Приветствие")
welcome_window.geometry("400x200")

tk.Label(welcome_window, text="Имя: ", bg='white', fg=TEXT_COLOR).pack()
name = tk.Entry(welcome_window)
name.pack()

def next():
    welcome_win2()
    welcome_window.destroy()

close_button = tk.Button(welcome_window, text="ОК", command=next)
close_button.pack()

def welcome_win2():
    welcome_window2 = tk.Toplevel(root)
    welcome_window2.title("Приветствие")
    welcome_window2.geometry("500x500")

    about_label = tk.Label(welcome_window2, text="О программе")
    about_label.pack(pady=10)

    hello_label = tk.Label(welcome_window2, text="Привет,"+name.get())
    hello_label.pack(pady=10)

    description_label = tk.Label(welcome_window2, text="Описание сам пиши")
    description_label.pack(pady=10)

    close_button2 = tk.Button(welcome_window2, text="ОК", command=welcome_window2.destroy)
    close_button2.pack()

root.mainloop()
