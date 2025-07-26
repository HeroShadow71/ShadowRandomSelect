import tkinter as tk
from tkinter import ttk
from random import choice
from data import *

randomlbl = None


def pick_route():
    """Return a formatted string for a random route."""
    route = choice(list(routes.keys()))
    return f"Route:\n{route} - {routes[route][0]} - {routes[route][1]}"


def pick_character():
    """Return a formatted string for a random character."""
    character = choice(characters)
    return f"Character:\n{character}"


def pick_char_another_option(boolean_route, boolean_stage, boolean_boss):
    """
    Return a formatted string with a character and either a route/stage/boss, depending on checkbutton states.
    
    :param boolean_route, boolean_stage, boolean_boss: tk.BooleanVars indicating the selected options alongside the character.
    """
    character = choice(characters)
    is_android = character in ("Gun Android", "Cannon Android")
    
    if boolean_route.get():
        pool = exclude_routes if is_android else routes
        route = choice(list(pool.keys()))
        return f"Character: {character}\nRoute: {route} - {pool[route][0]} - {pool[route][1]}"
    
    elif boolean_stage.get():
        pool = exclude_levels if is_android else levels
        stage = choice(list(pool.keys()))
        stage_mission = choice(pool[stage])
        return f"Character and Stage:\n{character} : {stage} - {stage_mission} Mission"
    else:
        pool = exclude_boss if is_android else bosses
        boss = choice(list(pool.keys()))
        boss_mission = choice(pool[boss])
        return f"Character and Boss:\n{character} : {boss} - {boss_mission} Mission"


def pick_char_stage_boss():
    """Return a formatted string with a character, and stage/boss."""
    character = choice(characters)
    is_android = character in ("Gun Android", "Cannon Android")
    
    pool = exclude_levels_and_boss if is_android else levels_and_bosses
    stage_or_boss = choice(list(pool.keys()))
    stage_or_boss_mission = choice(pool[stage_or_boss])
    return f"Character and Level/Boss:\n{character} : {stage_or_boss} - {stage_or_boss_mission} Mission"


def pick_stage():
    """Return a formatted string with a stage"""
    stage = choice(list(levels.keys()))
    stage_mission = choice(levels[stage])
    return f"Level:\n{stage} - {stage_mission} Mission"


def pick_boss():
    """Return a formatted string with a boss"""
    boss = choice(list(bosses.keys()))
    boss_mission = choice(bosses[boss])
    return f"Boss:\n{boss} - {boss_mission} Mission"


def pick_stage_boss():
    """Return a formatted string with a stage/boss"""
    stage_or_boss = choice(list(levels_and_bosses.keys()))
    stage_or_boss_mission = choice(levels_and_bosses[stage_or_boss])
    return f"Level/Boss:\n{stage_or_boss} - {stage_or_boss_mission} Mission"


def uncheck_buttons(changed_var, boolean_route, boolean_char, boolean_stage, boolean_boss):
    """
    Unchecks other buttons depending on which one is currently selected.
    
    :param changed_var: The BooleanVar that triggered the change.
    :param boolean_route, boolean_char, boolean_stage, boolean_boss: BooleanVars linked to the checkbuttons.
    """
    # Selecting 'route' unchecks 'stage' and 'boss'
    if changed_var == boolean_route and boolean_route.get():
        boolean_stage.set(False)
        boolean_boss.set(False)

    # Selecting 'stage' or 'boss' unchecks 'route'
    if changed_var in (boolean_stage, boolean_boss) and changed_var.get():
        boolean_route.set(False)


def create_checkbutton(text, var, root, row, column, all_vars):
    """
    Creates and places a Tkinter Checkbutton on the grid.

    :param text: The label text for the Checkbutton.
    :param var: The associated BooleanVar for the Checkbutton state.
    :param root: Main window.
    :param row: The grid row position.
    :param column: The grid column position.
    :param all_vars: A tuple of all BooleanVars used for managing checkbutton states.
    :return: The created ttk.Checkbutton widget.
    """
    btn = ttk.Checkbutton(root, text=text, variable=var, command=lambda: uncheck_buttons(var, *all_vars))
    btn.grid(row=row, column=column, columnspan=2, pady=5, sticky="ew")
    return btn
    

def make_label(root, text):
    """
    Create and display a label with the given text in the specified window.

    :param root: The main window where the label will be placed.
    :param text: The string content to display in the label.
    :return: The created ttk.Label widget.
    """
    global randomlbl
    
    if randomlbl is not None:
        randomlbl.destroy()

    randomlbl = ttk.Label(root, text=text, font=("Arial", 12))
    randomlbl.grid(row=5, column=0, columnspan=2)
    return randomlbl


def please_select_an_option():
    """
    Or not, up to you.
    
    :return: A random string from a list to remind the user still doesn't have an option selected.
    """
    no_option_selected = [
        "Happy?", "Keep Going.", "You realize you are wasting your time on nothing, right?",
        "Still not selecting any option?", "Where's that DAMN selected option?", "Find the option checkbox - Vector",
        "But like, what's a checkbox?", "I guess you are actually getting something random.",
        "Who I am and what is this checkbox?", "Checkbox == False", "Mad Matrix Dark sucks.",
        "Long time no see!", "Did you find Froggy?", "Damn, no option selected.", "This GUI sucks.",
        "Why?", "if character == 'Gun Android':\n    hold_B_button = True", "Let's destroy some nermies together.",
        "I have no idea what I'm doing.", "*Almost Dead playing in the background*", "What about you Billy your room?"
    ]
    return choice(no_option_selected)