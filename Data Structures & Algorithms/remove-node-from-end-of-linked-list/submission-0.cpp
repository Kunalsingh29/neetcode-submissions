class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) return nullptr;

        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* fast = dummy;
        ListNode* slow = dummy;

        // Move fast n+1 steps ahead to maintain a gap of n
        for (int i = 0; i <= n; ++i) {
            fast = fast->next;
        }

        // Move both pointers until fast reaches the end
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // Remove nth node
        slow->next = slow->next->next;

        return dummy->next;
    }
};
