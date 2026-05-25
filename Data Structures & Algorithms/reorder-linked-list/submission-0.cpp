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
    void reorderList(ListNode* head) {
        int length = 0;
        ListNode* temp = head;
        // find length
        while(temp!= NULL){
            length++;
            temp = temp->next;
        }
        cout<<length<<endl;
        temp = head;
        // go to mid point and split into 2
        for(int i = 0; i<length/2; i++){
            temp = temp->next;
        }
        ListNode* shead = temp->next;
        temp->next = NULL;
        // Reverse split_head list;
        ListNode* current = shead;
        ListNode* prev = NULL;
        ListNode* next1 = NULL;
        while(current != NULL){
            next1 = current->next;
            current->next = prev;
            prev = current;
            current = next1;

        }
        cout<< "linkedlist reversed"<<endl;
        // head and shead;
        shead = prev;
        ListNode* first = head;
        ListNode* second = shead;

        while (second != NULL) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;
            second->next = tmp1;

            first = tmp1;
            second = tmp2;
        }

    }
};