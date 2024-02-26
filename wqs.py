import itertools
from itertools import permutations
# import timer

#wordApi = WordApi.WordApi(client)
##example = wordApi.getTopExample('irony')
#print(example.text)


# Access the English words

# Example: Check if a word is in the English dictionary

#permutatitions
    

def get_permutations(input_string, intMin, intMax):
    all_perms = []
    for r in range(intMin, intMax + 1):
        perms = permutations(input_string, r)
        all_perms.extend([''.join(perm) for perm in perms])
    return all_perms

def binary_search_in_file(file_path, target):
    lines = file_path.readlines()
    low, high = 0, len(lines) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_line = lines[mid].strip().strip('"')

        if mid_line == target:
            return True  # Target found, return the index
        elif mid_line < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half


    return False  # Target not found
    
        





if __name__ == "__main__":
    strInput = str(input("Enter character combination: "))
    minChar = int(input("3 or 4 min characters: "))
    result = get_permutations(strInput, minChar, len(strInput))
    #print(result)

    final = []

    with open('wordlist-20210729.txt') as myfile:
        for element in result:
            myfile.seek(0)
            if element in final:
                continue
            elif binary_search_in_file(myfile, element):
                final.append(element)
            else:
                continue
    
    final = list(set(final))

    print(sorted(final, key=len))

    
    
        
                    
                    
                
                
            
        

