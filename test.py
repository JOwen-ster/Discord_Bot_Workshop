from pistonapi import PistonAPI

piston = PistonAPI()

code = '''
print("Hello, World!")
i = 0
'''

print(f"Running the following code: {code}")
print()
print("Got the following response:")
response = piston.execute(language="py3", version="3.10.0", code=code)
print(response)