#include "iostream"
#include <string>
#include <vector>
using namespace std;

vector< vector<char> > fillWithMines(vector< vector<char> > data, int bomb);
vector< vector<char> > fillWithNums(vector< vector<char> > data, int row, int col);
char fillWithNumsHelper(vector< vector<char> > data, int x, int y, int row, int col);
void printField(vector< vector<char> > data, int row, int col);

int main()
{
    int row, col, bomb;
    cin >> row >> col >> bomb;
    vector< vector<char> > data(row, vector<char>(col, '0'));
    data = fillWithMines(data, bomb);
    data = fillWithNums(data, row, col);
    printField(data, row, col);
    return 0;
}

vector< vector<char> > fillWithMines(vector< vector<char> > data, int bomb)
{
    for (size_t i = 0; i < bomb; i++)
    {
        int a, b;
        cin >> a >> b;
        data[a-1][b-1] = '*';
    }
    return data;
}

vector< vector<char> > fillWithNums(vector< vector<char> > data, int row, int col)
{
    for (size_t x = 0; x < row; x++)
    {
       for (size_t y = 0; y < col; y++)
       {    
            if (data[x][y] != '*')
            {
                data[x][y] = fillWithNumsHelper(data, x, y, row, col);
            }
       }
    }
    return data;
}

char fillWithNumsHelper(vector< vector<char> > data, int x, int y, int row, int col)
{
  int sus[8][2] = {{x+1, y},{x, y+1},{x+1, y+1},{x-1, y},
                    {x,y-1},{x-1,y-1},{x+1,y-1},{x-1,y+1}};
  int res = 0;

  for (int i = 0; i < 8; i++) {
    if ((0 <= sus[i][0] && sus[i][0] < row)&&(0 <= sus[i][1] && sus[i][1] < col)) {
      if (data[sus[i][0]][sus[i][1]] == '*') {
        res++;
      }
    }
  }
  return char(48+res);
}
void printField(vector< vector<char> > data, int row, int col){
    for (size_t i = 0; i < row; i++)
    {
        for (size_t j = 0; j < col; j++)
        {
            cout << data[i][j] << ' ';
        }
        cout << endl;
    }
}
