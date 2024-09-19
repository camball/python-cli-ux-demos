import questionary

questionary.text("What's your first name").ask()
questionary.password("Enter password").ask()
questionary.confirm("Confirm yes or no").ask()

questionary.select(
    "What do you want to do?",
    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
).ask()

questionary.rawselect(
    "What do you want to do?",
    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
).ask()

questionary.checkbox("Select toppings", choices=["foo", "bar", "bazz"]).ask()

questionary.path("Path to the projects version file").ask()
