import hashlib

with open("input.txt", "r") as f:
    lines = f.readlines()

secretKey = lines[0].strip()

i = 0
fiveZeros = -1
sixZeros = -1
done = 0
while done < 2:
    toHash = secretKey + str(i)
    m = hashlib.md5()
    m.update(toHash.encode("utf-8"))
    hash = m.hexdigest()
    if hash[0:5] == "00000" and fiveZeros < 0:
        fiveZeros = i
        done +=1
    if hash[0:6] == "000000" and sixZeros < 0:
        sixZeros = i
        done += 1
    i += 1

print("Solution (part 1): " + str(fiveZeros))
print("Solution (part 2): " + str(sixZeros))
