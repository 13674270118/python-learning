"""
def create_profile(username, **info):
    ...

调用：
create_profile(
    "James",
    age=23,
    city="Hong Kong",
    major="Mathematics"
)

要求输出：
Username: James
age: 23
city: Hong Kong
major: Mathematics
"""
def create_profile(username, **info):
    print(f"Username: {username}")
    for k, v in info.items():
        print(f"{k}: {v}")


create_profile(
        "James",
        age=23,
        city="Hong Kong",
        major="Mathematics"
    )

