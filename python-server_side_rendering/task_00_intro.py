import os

def generate_invitations(template, attendees):
    """
    Şablon və iştirakçı siyahısı əsasında fərdiləşdirilmiş dəvətnamələr yaradır.
    """

    # Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal prosesi
    for i, attendee in enumerate(attendees, start=1):
        try:
            personalized_msg = template

            # Əvəzlənəcək açarların siyahısı
            placeholders = ["name", "event_title", "event_date", "event_location"]

            for key in placeholders:
                # Əgər açar yoxdursa və ya dəyəri None-dırsa "N/A" ilə əvəzlə
                val = attendee.get(key)
                if val is None:
                    val = "N/A"

                # {key} formasını dəyərlə əvəz edirik
                personalized_msg = personalized_msg.replace(f"{{{key}}}", str(val))

            # Çıxış faylının adı (output_1.txt, output_2.txt və s.)
            filename = f"output_{i}.txt

            # Faylı yazırıq
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(personalized_msg)

        except Exception as e:
            print(f"An error occurred while processing attendee {i}: {e}")
