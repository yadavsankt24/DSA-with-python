# Remove Duplicates from Sorted List--inplace

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# array--sorted
# no_of_unique to be returned

def duplicate_inplace(arr):
    officer = 0
    no_of_unique=1
    cm=1 
    while cm < len(arr):
        if arr[cm] == arr[cm-1]: #cm is checking duplicate of the 1st position and the 0th position and if duplicate then cm bhai aage badh jate h rukte nai h kisi ke liye
            cm +=1
            continue
        else:
            arr[officer+1] = arr[cm] #agar mil jata h unique to ofiicer ke aage wale ko ghar dedete h aur aur ghar wo dete h jispe cm ko unique mila h piche wala check karne pe
            officer +=1
            no_of_unique+=1
            cm +=1

    return arr[:no_of_unique] #if array is needed 
    # return no_of_unique # if number if unique is needed

arr = [1,1,1,2,2,3]
print(duplicate_inplace(arr))


