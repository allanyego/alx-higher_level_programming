#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    out = []
    # choose the control
    cntrl, othr = tuple_b, tuple_a
    if len(tuple_a) > len(tuple_b):
        cntrl, othr = tuple_a, tuple_b

    for i, num_a in enumerate(cntrl):
        if i > 1:
            break
        
        num_b = 0
        if i < len(othr):
            num_b = othr[i] 
        out.append(num_a + num_b)
        
    return tuple(out)
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
print(add_tuple((3, 21), (8,)))
print(add_tuple((11, 8), (12, 12, 9)))
