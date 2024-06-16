# A basic Data Class

# Importing dataclass module
from dataclasses import dataclass

@dataclass
class GfgArticle():
	"""A class for holding an article content"""

	# Attributes Declaration
	# using Type Hints

	title: str
	author: str
	language: str
	upvotes: int

# A DataClass object
article = GfgArticle("DataClasses",
					"Karan",
					"Python", 0)
print(article)
