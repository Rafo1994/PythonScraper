from dotenv import dotenv_values

config = dotenv_values()

print(config["API_KEY"])