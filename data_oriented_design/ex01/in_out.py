def square(x: int | float) -> int | float:
	return x ** 2


def pow(x: int | float) -> int | float:
	return x ** x


def outer(x: int | float, function) -> object:
	def inner() -> float:
		nonlocal x
		a = function(x)
		x = a
		return a
	return inner
