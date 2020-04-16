stuff = {"name": "Steven", "Age": "39", "HeightCM": "179"}
print(stuff["name"])
stuff["name"] = "Bob"
print(stuff["name"])
del stuff["name"]
print(stuff)

states = {
    "newsouthwales": "nsw",
    "westernaustralia": "wa",
    "northernterritory": "nt",
    "victoria": "vic",
    "queensland": "qld",
    "southaustralia": "sa",
    "tasmania": "tas",
    "australiancapitolterritory": "act",
}

cities = {
    "nsw": "sydney",
    "vic": "melbourne",
    "qld": "brisbane",
    "wa": "perth",
    "act": "canbera",
    "nt": "darwin",
    "sa": "adelaide",

}

cities["tas"] = "hobart"

print(cities)

print('-' * 10)
print("nsw state has:", cities["nsw"])
print("qld state has:", cities[states["queensland"]])

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated to... {abbrev}")

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    print(f"{state} has the cities {cities[abbrev]}")

for k, v in states.items():
    print(f"I have this key - {k} and this value - {v}")

## Return all keys sorted
print(sorted(states))
## Return all keys in original order
print(list(states))