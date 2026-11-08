import sqlite3


def main():
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    while True:
        person_id = int(input("Enter a person's ID number (-1 to quit): "))

        if person_id == -1:
            break

        cursor.execute(
            "SELECT first_name, last_name, age FROM person WHERE id = ?",
            (person_id,)
        )

        person = cursor.fetchone()

        if person is None:
            print("That person does not exist.")
            print()
        else:
            first_name = person[0]
            last_name = person[1]
            age = person[2]

            print(
                first_name,
                last_name + ",",
                age,
                "years old"
            )

            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet
                ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))

            pets = cursor.fetchall()

            for pet in pets:
                pet_name = pet[0]
                breed = pet[1]
                pet_age = pet[2]
                dead = pet[3]

                if dead == 1:
                    status = "deceased"
                else:
                    status = "alive"

                print(
                    first_name,
                    last_name,
                    "owned",
                    pet_name + ",",
                    "a",
                    breed + ",",
                    "that was",
                    pet_age,
                    "years old.",
                    "Status:",
                    status
                )

            print()

    connection.close()
    print("Program ended.")


if __name__ == "__main__":
    main()