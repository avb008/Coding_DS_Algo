Find Majority element(element that occurs more than n/2 times) in a array  : 
    Algorithm : (Moore's voting algorithm) , the majority element cannot be cancelled out .
        -  Initialize the count to 0 and candidate to None
        - For each element in the array:
            - If count is 0, assign the current element as candidate
            - If current element is same as candidate, increment the count
            - Else decrement the count
        - Return the candidate

