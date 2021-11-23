#include <iostream>


using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// class Solution {
// public:
//     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//         return ;
//     }
// };

int main(){
    ListNode l1 = ListNode(3);
    for(auto i; i<=3; i++){
        *i
    }
    cout << l1.val<<endl;
    return 0;
}