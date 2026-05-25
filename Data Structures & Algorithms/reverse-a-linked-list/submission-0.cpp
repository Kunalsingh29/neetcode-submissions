/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
         // Reach end of LL
        //connect head to last element, 
        // connect and revese each element from last
        // take prev, current, next/.

        ListNode* prev, *curr, *next;
        if(head == nullptr){
            return head;
        }
        curr = head;
        prev = nullptr;
        next = nullptr;

        while(curr != nullptr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            // handshake.
            curr = next;


        }
        head = prev;
        return head;

    }
};