#include <iostream>
#include <vector>

using std::vector;

class Minesweeper
{
private:
    size_t r, k;
    vector<vector<int>> Table;

public:
    Minesweeper(size_t _m, size_t _n) : r(_m), k(_n)
    {
        Table.resize(r, vector<int>(k));
        for (auto row: Table)
        {
            row.resize(k, 0);
        }
    }

    size_t Rows() const
    {
        return r;
    }

    size_t Columns() const
    {
        return k;
    }

    int operator()(size_t i, size_t j) const
    {
        return Table[i][j];
    }
    void SetMine(size_t i, size_t j)
    {
        Table[i][j] = -1;
    }

    void CheckForMinesAround()
    {
        for (size_t i = 0; i != r; i++)
        {
            for (size_t j = 0; j != k; j++)
            {
                CheckForMinesAround(i, j);
            }
        }
    }

private:
    void CheckForMinesAround(size_t i, size_t j)
    {
        if (Table[i][j] == -1)
            return;
        int counter = 0;
        for (int dx = -1; dx <= 1; ++dx)
        {
            for (int dy = -1; dy <= 1; ++dy)
            {
                if (0 <= i + dx && i + dx < r &&
                    0 <= j + dy && j + dy < k &&
                    Table[i + dx][j + dy] == -1)
                {
                    ++counter;
                }
            }
        }
        Table[i][j] = counter;
    }
};

std::ostream& operator<<(std::ostream& out, const Minesweeper& ms)
{
    for (size_t i = 0; i != ms.Rows(); i++)
    {
        for (size_t j = 0; j != ms.Columns(); j++)
        {
            if (ms(i, j) == -1)
                out << '*';
            else
                out << ms(i, j);
        }
        out << "\n";
    }
    return out;
}

int main()
{
    size_t m, n;
    std::cin >> m >> n;
    Minesweeper ms(m, n);

    int minesCount;
    std::cin >> minesCount;
    while (minesCount-- > 0)
    {
        size_t x, y;
        std::cin >> x >> y;
        ms.SetMine(x, y);
    }

    ms.CheckForMinesAround();

    std::cout << ms;
}