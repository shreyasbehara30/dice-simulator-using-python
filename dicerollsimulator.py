import tkinter as tk
import random


DICE_FACES = {
    1: "\u2680",  # ⚀
    2: "\u2681",  # ⚁
    3: "\u2682",  # ⚂
    4: "\u2683",  # ⚃
    5: "\u2684",  # ⚄
    6: "\u2685",  # ⚅
}

def roll_dice():
   
    dice_result = random.randint(1, 6)
    result_label.config(text=f"You rolled a {dice_result}!")
    dice_label.config(text=DICE_FACES[dice_result], font=("Helvetica", 100))


root = tk.Tk()
root.title("Dice Roll Simulator")
root.geometry("300x400")
root.resizable(False, False)


title_label = tk.Label(root, text="Dice Roll Simulator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Click 'Roll Dice' to start", font=("Helvetica", 14))
result_label.pack(pady=10)

dice_label = tk.Label(root, text="", font=("Helvetica", 100))
dice_label.pack(pady=20)


roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 12), command=roll_dice)
roll_button.pack(pady=10)


exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
