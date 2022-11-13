# TODO решить с помощью list comprehension и распечатать его
import pprint

result = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pp = pprint.PrettyPrinter()
pp.pprint(result)
