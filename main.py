from pyscript import document

club_members = [
    "Ynigo Sindo",
    "Liam Alip",
    "Carlos Borromeo",
    "Matt Pagsanhan",
    "Dustin Cunanan",
    "Joanna Evangelista"
]

def run_check(event):
    # Get the first and last name values from the inputs and combine them into a full name
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value
    full_name = first_name + " " + last_name

    # Check if the full name is in the list and store the result in a variable
    is_member = full_name in club_members

    # 0 is false (meaning its not on the list) and 1 would be true (on the list)
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club.",
    ]

    # displays the matching message in the result area
    result_area = document.getElementById("result-area")
    result_area.innerText = messages[is_member]