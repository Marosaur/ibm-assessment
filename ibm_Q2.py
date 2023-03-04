#IBM Assessment Q2

import numpy as np

#Read data from input file

numberofrecords = input()
inputs = np.empty(int(numberofrecords), dtype = int)

for x in range(int(numberofrecords)):
  inputs[x] = input()

#allValid = true

allValid = np.empty(int(numberofrecords), dtype = bool)
allValid.fill(True)


#errorCodes = []

errorCodes = np.empty(int(numberofrecords), dtype = str)

#for each record in input file:
    #allValid = record.isValid
    #if record.isValid is not true:
        #errorCodes append error message
splitInputs = np.empty(3)

for x in range(numberofrecords):
  splitInput = inputs[x].split(' ')
  if (splitInput[1] == 'true'):
    pass
  else:
    allValid[x] = False
    np.append(errorCodes, splitInput[2])

if False in allValid:
    print("No")
    print(errorCodes)
else:
    print("Yes")