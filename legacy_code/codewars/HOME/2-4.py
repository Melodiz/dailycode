def left_join(phrases: tuple) -> str:

    output = ""
    """
   for el in list(phrases):
        start = 0
        while el[start:].find('right') != -1:
            output += el[:el[start:].find('right')]
            output += 'left'
            start = el[start:].find('right')+1+start
            print(start)
        if el.find('right') == -1:
            #print(el.find('right'))
            output += el
        if el != phrases[-1]:
            output +=','
    print(output)
    return output"""
    for el in phrases:
        output += el.replace('right', 'left')
        output+=','
    return output[:-1]        


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")


a='lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis'
b='lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quissem,nulla,consequat,massa,quis'

for el in range(1000):
    if a[el]!=b[el]:
        print(a[el], b[el], el)
        break