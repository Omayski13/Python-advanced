class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


emails = input()

while emails != "End":
    if "@" not in emails:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(emails.split("@")[0]) <= 4:
        raise NameTooShortError("Name must contain more than 4 characters")

    elif "." not in emails:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain = emails.split(".")[-1]

    domains = ["com", "bg", "net", "org"]

    valid_domain = False

    for dom in domains:
        if domain == dom:
            valid_domain = True
            break

    if not valid_domain:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    emails = input()
