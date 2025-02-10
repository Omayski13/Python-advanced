class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

EMAIL_MINIMUM_LENGHT = 5
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

email = input()

while True:
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < EMAIL_MINIMUM_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." + email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()