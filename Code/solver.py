#checks if the equation is in the appropriate form, then solves.


def solve(expression):

	expn = ["", "", ""]
	soln = ""
	numeric = "1234567890"
	operators = "+-*"
	equals = "="
	
	foundOp = False;
	
	for i in expression:
		if(foundOp == False):
			if(i in numeric):
				expn[0] += i
			elif (i in operators):
				expn[1] += i
				foundOp = True
			else:
				return ""
		else:
			if(i in numeric):
				expn[2] += i
			elif(i == equals):
				break
			else:
				return ""
		
	for j in expn: #check if any fields are illegally empty
		if j == "":
			return ""
			
	operand1 = int(expn[0])
	operator = expn[1]
	operand2 = int(expn[2])
	
	if (operator == "+"):
		soln = str(operand1 + operand2)
	elif (operator == "-"):
		soln = str(operand1 - operand2)
	elif (operator == "*"):
		soln = str(operand1*operand2)
	
	return soln