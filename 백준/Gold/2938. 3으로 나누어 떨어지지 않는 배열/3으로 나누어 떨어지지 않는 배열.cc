#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    cin >> n;

    vector<int> s(n);
    queue<int> q0, q1, q2;

    for (int i = 0; i < n; i++)
    {
        cin >> s[i];
        if (s[i] % 3 == 0)
        {
            q0.push(s[i]);
        }
        else if (s[i] % 3 == 1)
        {
            q1.push(s[i]);
        }
        else if (s[i] % 3 == 2)
        {
            q2.push(s[i]);
        }
    }
    if (q0.size() > (n + 1) / 2 || (q0.empty() && !q1.empty() && !q2.empty()))
    {
        cout << -1;
        return 0;
    }
    while (!q1.empty())
    {
        if (q0.size() > 1)
        {
            cout << q0.front() << ' ';
            q0.pop();
        }
        cout << q1.front() << ' ';
        q1.pop();
    }
    if (!q0.empty())
    {
        cout << q0.front() << ' ';
        q0.pop();
    }
    while (!q2.empty())
    {
        cout << q2.front() << ' ';
        q2.pop();

        if (q0.size())
        {
            cout << q0.front() << ' ';
            q0.pop();

        }
    }
    return 0;
}