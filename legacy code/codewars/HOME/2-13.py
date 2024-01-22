def safe_pawns(pawns: set) -> int:
    alf = '0abcdefgh0'
    save_slots = []

    for pn in pawns:
        letter = alf.find(pn[0])
        
        first_save_pos = alf[letter+1]
        second_save_pos = alf[letter-1]
        
        first_save_pos += str(int(pn[1])+1)
        second_save_pos += str(int(pn[1])+1)

        save_slots.append(first_save_pos)
        save_slots.append(second_save_pos)
    
    counter = 0
    
    for el in pawns:
        if el in save_slots:
            counter+=1
    return counter

print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
