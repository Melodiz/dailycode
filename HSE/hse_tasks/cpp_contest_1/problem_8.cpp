#include <iostream>
using namespace std;

int main()
{
    short day;
    short month;
    int year;

    cin >> day >> month >> year;

    switch (month)
    { // 31 day cases
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        switch (day)
        {
        case 30:
            day = 1;
            month += 1;
            break;

        case 31:
            day = 2;
            month += 1;
            break;

        default:
            day += 2;
            break;
        }

        break;

    // 30 day cases
    case 4:
    case 6:
    case 9:
    case 11:
        switch (day)
        {
        case 30:
            day = 2;
            month += 1;
            break;
        case 29:
            day = 1;
            month += 1;
            break;

        default:
            day += 2;
            break;
        }
        break;

    case 2:
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        {
            switch (day)
            {
            case 29:
                day = 2;
                month = 3;
                break;
            case 28:
                day = 1;
                month = 3;
                break;

            default:
                day += 2;
                break;
            }
        }
        else
        {
            switch (day)
            {
            case 28:
                day = 2;
                month = 3;
                break;
            case 27:
                day = 1;
                month = 3;
                break;
            default:
                day += 2;
                break;
            }
        }
        break;
    default:
        break;
    }

    if (month == 13)
    {
        cout << day << " " << 1 << " " << year + 1 << " " << endl;
    }
    else
    {
        cout << day << " " << month << " " << year << " " << endl;
    }

    return 0;
}