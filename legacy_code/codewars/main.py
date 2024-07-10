from datetime import datetime


def sum_light(
        els,
        start_watching=None,
        end_watching=None,):

    els = edit_mass(els, end_watching)

    x = 0
    i = 0
    if start_watching == None:
        start_watching = els[0]
    while True:
        try:
            if els[i] >= start_watching:
                x += int((els[i+1]-els[i]).total_seconds())
            if els[i] < start_watching and els[i+1] >= start_watching:
                x += int((els[i+1]-start_watching).total_seconds())
            i += 2
        except:
            break
    return x

def edit_mass(els,end_watching):
    els = edm_for_multi_bulbs(els)
    els = edm_for_end_watching(els, end_watching)
    return els


def edm_for_end_watching(els, end_watching = None):
    
    output = []
    if end_watching == None:
        return els
    if len(els)%2==0:
        
        for el in (els):
            if el>end_watching:
                output.append(end_watching)
                break
            else:
                output.append(el)
    else:
        
        for i in range(len(els)):
            if els[i]>end_watching:
                output.append(end_watching)
                break
            else:
                output.append(els[i])
        output.append(end_watching)
    return output


def edm_for_multi_bulbs(els):
    turned_on_bulbs = []
    output = []

    for el in els:
        number = -1
        try:
            number = el[1]
        except:
            number = 1

        if number in turned_on_bulbs:
            turned_on_bulbs.remove(number)
            # val_before -= 1
            if len(turned_on_bulbs) == 0:
                # print(el, turned_on_bulbs, val_before)
                try:
                    output.append(el[0])
                except:
                    output.append(el)
            

        else:
            if len(turned_on_bulbs) == 0:
                # print(el, turned_on_bulbs, val_before)
                try:
                    output.append(el[0])
                except:
                    output.append(el)

            turned_on_bulbs.append(number)
    return output


assert (
    sum_light(
        [
            datetime(2015, 1, 12, 10, 0, 0),
            (datetime(2015, 1, 12, 10, 0, 0), 2),
            datetime(2015, 1, 12, 10, 0, 10),
            (datetime(2015, 1, 12, 10, 1, 0), 2),
        ]
    )
    == 60
)

print('ok')