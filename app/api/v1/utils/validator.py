import re

class validate_inputs():

    def validate_email(self, email):
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)

    def validate_password(self, password):

        if len(password) < 6:
            return False

        total = {}

        for letter in password:
            if letter.islower():
                total['has_lower'] = 1

            if letter.isupper():
                total['has_upper'] = 1

            if letter.isdigit():
                total['has_digit'] = 1

        return sum(total.values()) == 3

