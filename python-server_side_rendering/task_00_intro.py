def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str) or not isinstance(attendees, list) \
       or not all(isinstance(i, dict) for i in attendees):
        print(
            "Invalid input type: template must be a string and attendees must be a list of dictionaries."
        )
        return

    # Handle empty inputs
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output_content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output_content = output_content.replace("{" + key + "}", str(value))

        with open(f"output_{index}.txt", "w") as file:
            file.write(output_content)
