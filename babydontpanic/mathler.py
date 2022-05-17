class Mathler:

	def ValidCharacters (character):

		set_of_characters = "1234567890+-*/"
		for i in set_of_characters:
			if (i == character):
				return (1)
		return (0)

	def CheckCharacters(guess):

		x = len(guess)
		i = 0
		while (i < x):
			if (Mathler.ValidCharacters (guess[i]) == 0):
				return (0)
			i += 1
		if (Mathler.SequenceOfCharacters (guess) == 0):
			return (0)
		return (1)

	def SequenceOfCharacters(guess):
		x = len(guess)
		limit = 1

		if (Mathler.IsAOperator (guess[0]) == 1 or Mathler.IsAOperator (guess[x - 1]) == 1):
			return (0)
		while (limit < x - 1):
			if (Mathler.IsAOperator(guess[limit]) == 1 and
				(Mathler.IsAOperator(guess[limit - 1]) == 1 or
				Mathler.IsAOperator(guess[limit + 1]) == 1)):
				return (0)
			limit += 1
		return (1)

	def IsAOperator (character):

		operations = "+-*/"
		for i in operations:
			if (character == i):
				return (1)
		return (0)

	def IsAValidSequence(guess):
		if (Mathler.CheckCharacters(guess) == 0):
			return (0)
		return (1)


	def	IsAValidEquation(guess):

		array_of_numbers = []
		operators = ""

		numbers = 1

		for i in guess:
			if (Mathler.IsAOperator(i) == 1):
				numbers += 1
				array_of_numbers.append("")
		array_of_numbers.append("")

		t = 0
		for x in guess:
			if (Mathler.IsAOperator(x) == 0):
				array_of_numbers[t] += x
			if (Mathler.IsAOperator(x) == 1):
				t += 1
		print (array_of_numbers)
		return (1)


