def main():
    permutation('abc', '')

def permutation(str:str):
    permutation(str, "")

def permutation(str: str, prefix: str):
    print(f'str={str}, prefix={prefix}')
    if len(str) == 0:
        print(prefix);
    else:
        for i in range(len(str)):
            rem = str[0:i] + str[i+1:]
            
            permutation(rem, prefix + str[i])

if __name__ == "__main__":
    main()


'''
|Iteration|str|prefix|
|---|---|---|
|1|abc|''|
|2|a

'''