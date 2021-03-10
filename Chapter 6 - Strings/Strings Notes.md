# Notes for String Concepts:

### Key functions to know from Python:


### Key ideas to remember:

1. **STRINGS ARE IMMUTABLE** (Operations like s = s[1:] or s += '123' mean "create a new array of characters and assign to s" --> Concatenating a character to string n times means time complexity is *O(N^2)* not O(N).
2. Because of (1) above, use lists instead of strings for concatenating.
3. Consider updating a mutable string from the back instead of the front

|Python  Libraries | Time Complexity | Space Complexity | Description      | Rationale of Complexities  |
|------------------|-----------------|------------------|------------------|----------------------------|
|s[3]              | O(1)            | O(1)             | Simple Index     |       (-)                     |
|len(s)            | O(1)            | O(1)             | Length of the string|     (-)                    |
|s + t             | O(S + T)        | O(S + T)         | Concatenation of Strings| Strings are immutable|
|s[2:4]            | O(k)            | O(k)             | Slicing          | Let k be subset to pull where k can be the entire string S   |
|s in t            | O(T)            | O(1)             | Included in string |                (-)          |
|s.strip()         | O(S)            | (-)              | Remove spaces/characters on left and right  |(-) |
|s.startswith(prefix)| O(S*T)        | (-)              | Starts with the specified string prefix|  (-)    |
|s.endswith(prefix)| O(S*T)          | (-)              | Ends with the specified string prefix |  (-)     |
|s.split('')       | O(S)            | O(S)             | Split into list of smaller strings (max of individual characters - S length)|(-) |
|''.join(('a','b','c'))| O(S)       | O(S)              | Creates one new string of len S, S = sum of all individual component lenghts |(-) |
|s.tolower()       | O(S)           | O(S)              | Lower case all characters|      (-)              |
|s.toupper()       | O(S)           | O(S)              | Upper case all characters|        (-)            |
|'Test: {test}, Sample: {sample}'.format(test = 'Hello', sample = 'World')|   (-)     | (-)    |  (-)  | (-)  |

