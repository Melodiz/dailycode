#include <map>

class MyCalendar
{
private:
    std::map<int, int> calendar;

public:
    MyCalendar()
    {
    }

    bool book(int start, int end)
    {
        auto next = calendar.lower_bound(start);
        if (next != calendar.end() && next->first < end)
            return false;
        if (next != calendar.begin() && std::prev(next)->second > start)
            return false;
        calendar[start] = end;
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */