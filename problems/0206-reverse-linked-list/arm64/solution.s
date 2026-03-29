// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
// Pattern: Linked List
//
// Hints:
//   1. Initialize prev = null, curr = head
//   2. Save next = curr.next before changing pointer
//   3. Set curr.next = prev
//   4. Advance: prev = curr, curr = next
//
// Brute Force: Store all values, create new reversed list. O(n) time, O(n) space.
// Optimal: In-place pointer reversal. O(n) time, O(1) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global reverse_list
    .type reverse_list, %function

reverse_list:
    // TODO: implement
    mov x0, #0          // return 0
    ret
