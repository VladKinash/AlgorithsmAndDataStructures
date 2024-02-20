def right_align(a, b):
  length = len(a)
  b_str = str(b)
  b_len = len(b_str)
  if b_len > length:
      return "Error: b is too long to fit in a"
  spaces = length - b_len
  result = " " * spaces + b_str
  return result


def make_hyphens(longest_oper):
  hyphens = "--"
  for i in range(longest_oper):
      hyphens += "-"
  return hyphens


def make_spaces(hyphens):
  spaces = ""
  for i in range(len(hyphens)):
      spaces += " "
  return spaces


def make_spacesB(hyphens):
  spaces = ""
  for i in range(len(hyphens) -1):
      spaces += " "
  return spaces


def longest_operand(nums):
  length = 0
  for i in nums:
      if len(i) > length:
          length = len(i)
  return length

def place_numbers(string):
  numbers = []
  for char in string[::-1]:
      if char.isdigit():
          numbers.append(char)
  numbers.reverse()
  return string.replace(''.join(numbers), ''.join(numbers[::-1]), 1)


def calculation(operands):
  if operands[1] == "+":
      return int(operands[0]) + int(operands[2])
  else:
      return int(operands[0]) - int(operands[2])


def formatter(operation):
  operands = operation.split()
  biggest_oper = longest_operand(operands)
  hyphens = make_hyphens(biggest_oper)
  operandA = right_align((make_spaces(hyphens)), operands[0])
  operator = operands[1]
  operandB =  operator + right_align((make_spacesB(hyphens)), operands[2])
  result = calculation(operands)
  result_str = right_align((make_spaces(hyphens)), result)
  operation_deck = []
  operation_deck.extend([operandA, operandB, hyphens, result_str])


  return operation_deck


def adding_sublists(operation_deck):
  main_deck = []
  for i in operation_deck:
      main_deck.append(formatter(i))
  return main_deck

def error_handle(deck):
  temp = []
  for operation in deck:
      temp = operation.split()
      if temp[1] not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."
      elif not temp[0].isdigit() or not temp[2].isdigit():
          return "Error: Numbers must only contain digits."
      elif len(temp[0]) > 4 or len(temp[2]) > 4:
          return "Error: Numbers cannot be more than four digits."
  return "No error"


def arithmetic_arranger(oper_deck, boolean=False):
  if error_handle(oper_deck) != "No error":
      return error_handle(oper_deck)
  elif len(oper_deck) > 5: 
      return  "Error: Too many problems."
  oper_deck_sub = adding_sublists(oper_deck)
  line1 = []
  line2 = []
  hyphens_line = []
  result_line = []

  for sublist in oper_deck_sub:
      for i in range(len(sublist)):
          if i == 0:
              line1.append(sublist[i])
          elif i == 1:
              line2.append(sublist[i])
          elif i == 2:
              hyphens_line.append(sublist[i])
          elif i == 3:
              result_line.append(sublist[i])

  line1 = '    '.join(line1)
  line2 = '    '.join(line2)
  hyphens_line = '    '.join(hyphens_line)
  result_line = '    '.join(result_line)

  if boolean == True:
      return line1 + "\n" + line2 + "\n" + hyphens_line + "\n" + result_line
  else: 
      return line1 + "\n" + line2 + "\n" + hyphens_line
