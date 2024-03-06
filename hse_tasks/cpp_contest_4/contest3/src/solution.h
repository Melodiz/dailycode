#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

struct Task {
    std::string text;
    std::string date;
    std::map<std::string, int> workloads;
    using Workload = std::map<std::string, int>::value_type;

    Task(const std::string& text, const std::string& date, const std::map<std::string, int>& workloads);
    int getTotalLoad() const;
};

// task 1
Task::Task(const std::string& inptext, const std::string& _date, const std::map<std::string, int>& _workloads)
{
    text = inptext;
    date = _date;
    workloads = _workloads;
}

struct Worker {
    std::string name;
    std::string login;
    int maxLoad;

    Worker(const std::string& name, const std::string& login, int maxLoad);

    // might be needed for task 5
    bool isOverworked(const std::vector<Task>& tasks) const;
};


// task 1
Worker::Worker(const std::string& _name, const std::string& _login, int _maxLoad)
{
    name = _name;
    login = _login;
    maxLoad = _maxLoad;
}


// task 2
int Task::getTotalLoad() const
{
    size_t ans = 0;

    for (const Task::Workload& w: workloads)
    {
        ans += w.second;
    }

    return ans;
}

// task 3

bool compForTasks(Task a, Task b)
{
    if (a.getTotalLoad() < b.getTotalLoad())
    {
        return true;
    }
    else if (a.getTotalLoad() > b.getTotalLoad())
    {
        return false;
    }

    else
    {
        if (a.date < b.date)
        {
            return true;
        }
        else if (a.date > b.date)
        {
            return false;
        }
        else
        {
            if (a.text < b.text)
            {
                return true;
            }
            else
                return false;
        }
    }
}

void sortTasks(std::vector<Task>& tasks)
{
    sort(tasks.begin(), tasks.end(), compForTasks);
}

// task 4
int getWorkerLoad(const std::vector<Task>& allTasks, const Worker& worker)
{
    size_t ans = 0;
    for (size_t i = 0; i < allTasks.size(); i++)
    {
        Task currentTask = allTasks[i];
        for (std::map<std::string, int>::iterator data = currentTask.workloads.begin();
             data != currentTask.workloads.end(); data++)
        {
            std::pair<std::string, int> vals;
            vals = *data;
            if (vals.first == worker.login)
                ans += vals.second;
        }
    }
    return ans;
}


// task 5
void addTask(std::vector<Task>& tasks, const Task& newTask, const std::vector<Worker>& workers)
{
    std::map<std::string, int> NewTaksdata = newTask.workloads;
    for (int i = 0; i < workers.size(); i++)
    {
        std::map<std::string, int> NewTaksdata = newTask.workloads;
        for (std::map<std::string, int>::iterator data = NewTaksdata.begin();
             data != NewTaksdata.end(); data++)
        {
            std::pair<std::string, int> vals;
            vals = *data;

            if (vals.first == workers[i].login){
                if (workers[i].maxLoad < getWorkerLoad(tasks, workers[i]) + vals.second){
                    throw std::runtime_error("Overworked");
                }
                else
                {
                    tasks.push_back(newTask);
                }
            }   
        }
    }
}

// task 6
// struct OverworkedWorker {
//     std::string name;
//     size_t hours;
// };

// bool compForWorkersOverworks(OverworkedWorker a, OverworkedWorker b)
// {
//     return a.name <= b.name;
// }
bool compForWorkersOverworks(std::vector<std::string>& a, std::vector<std::string>& b)
{
    return a[0]<=b[0];
}

void addTaskVerbose(std::vector<Task>& tasks, const Task& newTask, const std::vector<Worker>& workers)
{
    // std::vector<OverworkedWorker> ans;
    std::vector<std::vector<std::string>> ans;

    tasks.push_back(newTask);
    std::map<std::string, int> NewTaksdata = newTask.workloads;
    // if (max_load < load) {
    //   error.push_back({login, std::to_string(load - max_load)});
    // }
    for (size_t i = 0; i < workers.size(); i++)
    {
        int val = getWorkerLoad(tasks, workers[i]) - workers[i].maxLoad;
        if (val > 0)
        {
            ans.push_back({workers[i].login, std::to_string(val)});
        }
    }
    size_t n = ans.size();
    if (!n){
        return;
    }

    // sort by logins
    sort(ans.begin(), ans.end(), compForWorkersOverworks);
    // yeah, I wanna write my own struct and comparetor for that
    // 'cause why not

    std::string errorMessage = "Overworked: ";
    for (int i = 0; i < n; i++) {
        errorMessage += ans[i][0] + " by " + ans[i][1];
        if (i + 1 != n)
            errorMessage += ", ";
    }
    throw std::runtime_error(errorMessage);
}