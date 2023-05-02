import random
import string


def randon_string():
    return "".join(
        [random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 5))]
    )


class User:
    # shared instance
    full_names = []

    def __init__(self, full_name: str):
        def get_name_index(s: str):
            if s in self.full_names:
                return self.full_names.index(s)
            else:
                self.full_names.append(s)
                return len(self.full_names) - 1

        self.full_name = [get_name_index(s) for s in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.full_names[x] for x in self.full_name])


if __name__ == "__main__":
    users = []
    first_names = [randon_string() for x in range(100)]
    last_names = [randon_string() for x in range(100)]

    for first_name in first_names:
        for last_name in last_names:
            users.append(User(f"{first_name} {last_name}"))

    for user in users:
        print(user)
