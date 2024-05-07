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
class Solution
{
public:
    ListNode* doubleIt(ListNode* head)
    {
        head = reverseList(head);// reverse the list
        bool prev;
        ListNode* current = head;
        while (current != nullptr)
        {
            int value = (current->val) * 2 + prev;
            if (value > 9) { prev = true; }
            else { prev = false; }
            current->val = value % 10;
            current = current->next;
        }
        if (prev)
        {
            ListNode* extraNode = new ListNode(1);
            current->next = extraNode;
        }
        head = reverseList(head);
        return head;
    }

    ListNode* reverseList(ListNode* node)
    {
        ListNode *previous = nullptr, *current = node, *nextNode;

        // Traverse the original linked list
        while (current != nullptr)
        {
            // Store the next node
            nextNode = current->next;
            // Reverse the link
            current->next = previous;
            // Move to the next nodes
            previous = current;
            current = nextNode;
        }
        // Previous becomes the new head of the reversed list
        return previous;
    }
};