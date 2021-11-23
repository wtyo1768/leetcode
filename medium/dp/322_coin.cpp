#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int coinChange(vector<int> number, int amount){
    vector<int> outputs;

    // init outputs array
    outputs.push_back(0);
    for(int i=1; i<=amount; i++) outputs.push_back(amount+1);
    
    // main
    for(int i=1; i<=amount; i++)
    {
        // outputs.push_back(amount);
        for(int j=0; j<number.size(); j++)
        {
            if(number[j] > i) continue;
            outputs[i] = min(outputs[i-number[j]]+1, outputs[i]);
        }

        // cout << outputs[i] << ' ';
    }
    
    for (auto i = outputs.begin(); i != outputs.end(); ++i)
        cout << *i << ' ';
    
    cout << endl;
    
    if (outputs[amount] == amount+1)
        return -1;
    else
        return outputs[amount];
}


int main(){
    vector<int> inputs = {1, 2, 5};
    int amount = 11;

    coinChange(inputs, amount);
    int a = 3;
    cout<<a--<<endl;
    cout<<a;
    return 0;
}