from data import *
from utils import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

first_try = True
second_try = None


def random_stuff():
    '''
    Guess what happens after pressing the 'Randomize' button?
    '''
    global first_try, second_try
    
    # Determines which randomizer to use based on selected options    
    checking_buttons = (
        boolean_route.get(), boolean_char.get(), boolean_stage.get(), boolean_boss.get()
    )
    
    match checking_buttons:
        case (True, False, False, False):
            randomize("route")
        case(False, True, False, False):
            randomize("character")
        case(True, True, False, False) | (False, True, True, False) | (False, True, False, True):
            randomize("char_another_option")
        case (False, True, True, True):
            randomize("char_stage_boss")
        case(False, False, True, False):
            randomize("stage")
        case(False, False, False, True):
            randomize("boss")
        case(False, False, True, True):
            randomize("stage_boss")
        case _:
            if first_try:
                make_label(root, "What did you expect to happen by not selecting anything?")
                first_try = False
                second_try = True
            elif second_try:
                make_label(root, "Just select an option, not that hard.")
                second_try = False
            else:
                make_label(root, please_select_an_option())
            
        

def randomize(checkbox_options):
    '''
    Randomizes based on the selected checkbox(es).
    
    :param checkbox_options: A string which indicates the selected checkbox(es)
    :return: A string with the randomization result displayed in a label.
    '''
    match checkbox_options:
        case "route": lbl_text = pick_route()
        
        case "character": lbl_text = pick_character()
        
        case "char_another_option": lbl_text = pick_char_another_option(boolean_route, boolean_stage, boolean_boss)

        case "char_stage_boss": lbl_text = pick_char_stage_boss()
            
        case "stage": lbl_text = pick_stage()
    
        case "boss": lbl_text = pick_boss()

        case "stage_boss": lbl_text = pick_stage_boss()
        
    make_label(root, lbl_text)


# Tkinter window
root = tk.Tk()
root.title("Shadow the Hedgehog Random Choice")
root.geometry("450x400")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(6, weight=1)

# Style
style = ThemedStyle(root)
style.set_theme("plastik")

# Checkbuttons
boolean_route = tk.BooleanVar()
boolean_char = tk.BooleanVar()
boolean_stage = tk.BooleanVar()
boolean_boss = tk.BooleanVar()

all_vars = (boolean_route, boolean_char, boolean_stage, boolean_boss)

create_checkbutton("Random Route?", boolean_route, root, 0, 0, all_vars)
create_checkbutton("Character?", boolean_char, root, 1, 0, all_vars)
create_checkbutton("Stages?", boolean_stage, root, 2, 0, all_vars)
create_checkbutton("Bosses?", boolean_boss, root, 3, 0, all_vars)

ttk.Button(root, text="Randomize", command=random_stuff).grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
root.mainloop()