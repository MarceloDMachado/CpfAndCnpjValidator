import array as arr
import functools

CNPJ_VALIDATOR_FACTORS = arr.array("i", [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
CPF_VALIDATOR_FACTORS = arr.array("i", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

def hasOnlyNumericChars(cnpj: str) -> bool:
    return cnpj.isnumeric()

def isCnpjComplete(cnpj: str) -> bool:
    return len(cnpj) == 14

def isCpfComplete(cpf: str) -> bool:
    return len(cpf) == 11

def getModResult(value: int) -> int:
    return value % 11

def sumAlgarisms(algarismis: arr.array) -> int:
    return functools.reduce(lambda a, b: a + b, algarismis)

def multiplyAlgarisms(primaryFactors: arr.array, secondaryFactors: arr.array) -> arr.array:
    productArray = arr.array("i",[])

    for index, factor in enumerate(primaryFactors):
        productArray.append(factor * secondaryFactors[index])
    
    return productArray

def transmuteStringToArray(stringValue: str) -> arr.array:
    result = arr.array("i", [])
    
    for char in stringValue: 
        result.append(int(char))
            
    return result

def addAlgarismAtArrayStart(alg: int, orignArray: arr.array) -> arr.array:
    newArray = arr.array("i", [alg])
    newArray.extend(orignArray)

    return newArray

def validateFirstCnpjDigit(cnpj: str) -> bool:
    modResult = getModResult( sumAlgarisms( multiplyAlgarisms( transmuteStringToArray(cnpj[:12]), CNPJ_VALIDATOR_FACTORS)))
    return int(cnpj[12]) == modResult if modResult < 2 else int(cnpj[12]) == 11 - modResult

def validateSecondCnpjDigit(cnpj: str) -> bool: 
    modResult = getModResult( sumAlgarisms( multiplyAlgarisms( transmuteStringToArray(cnpj[:13]), addAlgarismAtArrayStart(6, CNPJ_VALIDATOR_FACTORS))))
    return int(cnpj[13]) == modResult if modResult < 2 else int(cnpj[13]) == 11 - modResult

def isThisCnpjValid(cnpj: str) -> bool:
    return True if (
        hasOnlyNumericChars(cnpj)
        and
        isCnpjComplete(cnpj)
        and
        validateFirstCnpjDigit(cnpj) 
        and 
        validateSecondCnpjDigit(cnpj)        
    ) else False
    
def validateFirstCpfDigit(cpf: str) -> bool:
    modResult = getModResult( sumAlgarisms( multiplyAlgarisms( transmuteStringToArray(cpf[:9]), CPF_VALIDATOR_FACTORS)))
    return int(cpf[9]) == modResult if modResult < 2 else int(cpf[9]) == 11 - modResult

def validateSecondCpfDigit(cpf: str) -> bool:
    modResult = getModResult( sumAlgarisms( multiplyAlgarisms( transmuteStringToArray(cpf[:10]), addAlgarismAtArrayStart(11, CPF_VALIDATOR_FACTORS))))
    return int(cpf[10]) == modResult if modResult < 2 else int(cpf[10]) == 11 - modResult

def isThisCpfValid(cpf: str) -> bool:
    return True if (
        hasOnlyNumericChars(cpf)
        and
        isCpfComplete(cpf)
        and
        validateFirstCpfDigit(cpf)
        and
        validateSecondCpfDigit(cpf)
    ) else False

#print('Is this cnpj valid? ', isThisCnpjValid('50567038000119'))
#print('Is this cpf valid? ', isThisCpfValid('44862720803'))