#123-12-1234
def validateSSN2(ssn):
    numArray = ssn.split('-')
    # SSN should have 3 parts
    if len(numArray) == 3:
        for num in numArray:
            # SSN should have 3 parts and each part should be numeric
            if not num.isnumeric():
                return None
        # if ssn is valid then mask it
        maskedSSN = ''
        for s in ssn[0:7]:  #substring which gives from 0 index to 7 index (123-12-)
            if s != '-':
                maskedSSN += 'x'
            else:
                maskedSSN += '-'

        return maskedSSN + ssn[7:12]  #substring which givies the last 4 digits
    else:
        return None


print(validateSSN2('123-12-1234'))
print(validateSSN2('123121234'))
print(validateSSN2('123-AB-1234'))
print(validateSSN2('12-1234'))