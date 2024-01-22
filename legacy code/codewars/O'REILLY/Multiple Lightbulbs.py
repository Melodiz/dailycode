# Taken from mission Lightbulb End Watching

# Taken from mission Lightbulb Start Watching
# Taken from mission Lightbulb Intro
from typing import List, Optional
from datetime import datetime
from typing import List
def sum_light(els: List[datetime]) -> int:
    x = 0
    i = 0
    while True:
        try:
            x += int((els[i+1]-els[i]).total_seconds())
            i += 2
        except:
            break
    return x


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
    )
    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
            ]
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 12, 10, 10),
            ]
        )
        == 4820
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 1),
            ]
        )
        == 1
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
        == 86410
    )
    print(
        "The first mission in series is completed? Click 'Check' to earn cool rewards!"
    )
def sum_light(els, start_watching: Optional[datetime] = None):
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
if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )
    assert (sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10)
    ])) == 1220
def sum_light(els: List[datetime],
              start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None,):
    
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
def edit_mass(els, end_watching = None):
    
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
if __name__ == "__main__":
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 7),
        )
        == 7
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 3),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 7
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 30, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 50, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 0, 0),
            datetime(2015, 1, 12, 10, 5, 0),
        )
        == 300
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 12, 0, 0),
        )
        == 310
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 11, 10, 0),
        )
        == 300
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    print(
        "The third mission in series is completed? Click 'Check' to earn cool rewards!"
    )


from datetime import datetime
from typing import List, Optional, Union, Tuple

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



if __name__ == "__main__":
    print("Example:")

    print(
        sum_light(
            els=[
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 1, 0),
        )
    )

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

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 11, 0, 0), 2),
                (datetime(2015, 1, 12, 11, 1, 0), 2),
            ]
        )
        == 70
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 3),
                (datetime(2015, 1, 12, 10, 1, 20), 3),
            ]
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 50
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            els=[
                (datetime(2015, 1, 11, 0, 0, 0), 3),
                datetime(2015, 1, 12, 0, 0, 0),
                (datetime(2015, 1, 13, 0, 0, 0), 3),
                (datetime(2015, 1, 13, 0, 0, 0), 2),
                datetime(2015, 1, 14, 0, 0, 0),
                (datetime(2015, 1, 15, 0, 0, 0), 2),
            ],
            start_watching=datetime(2015, 1, 10, 0, 0, 0),
            end_watching=datetime(2015, 1, 16, 0, 0, 0),
        )
        == 345600
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
