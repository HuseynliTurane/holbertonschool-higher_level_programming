import os

def generate_invitations(template, attendees):
    """
    Şablon və iştirakçı siyahısı əsasında fərdiləşdirilmiş dəvətnamələr yaradır.
    """

    # 1. Giriş tiplərinin yoxlanılması (Input Types Check)
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # 2. Boş girişlərin yoxlanılması (Empty Inputs Check)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. İştirakçıları emal edib faylları yaradırıq
    for i, attendee in enumerate(attendees, start=1):
        # Şablonun surətini çıxarırıq ki, hər dəfə sıfırdan başlayaq
        invitation_content = template

        # Lazım olan bütün açarlar (placeholders)
        keys = ["name", "event_title", "event_date", "event_location"]

        for key in keys:
            # Məlumat yoxdursa və ya None-dırsa "N/A" qoyuruq
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            # {key} hissəsini real dəyərlə əvəzləyirik
            invitation_content = invitation_content.replace(f"{{{key}}}", str(value))

        # 4. Faylın adını təyin edirik (Dırnaq işarəsinə diqqət!)
        filename = f"output_{i}.txt"

        # 5. Faylı yazırıq
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(invitation_content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
