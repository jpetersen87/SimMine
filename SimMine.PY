class Mine(object):

	def __init__(self):
		self.type = "Underground"
		self.resource = "Coal"
		self.name = "Skyline"
		self.location = "Scofield, Utah"

Skyline = Mine()

print("\n")
print("%s is an %s %s mine located in %s." % (Skyline.name, Skyline.type, Skyline.resource, Skyline.location))
print("\n")