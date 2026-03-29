; 1. Two Sum
; https://leetcode.com/problems/two-sum/
; Pattern: Hash Table
;
; Hints:
;   1. For each number, calculate target - num
;   2. Store each number's index in a hash map
;   3. Check if the complement already exists before storing
;
; Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
; Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global two_sum

; int* two_sum(int* nums, int numsSize, int target, int* returnSize)
; Args: rdi=nums, rsi=numsSize, rdx=target, rcx=returnSize
two_sum:
    push    rbx
    push    r12
    push    r13
    push    r14
    push    r15

    mov     r12, rdi            ; r12 = nums
    mov     r13d, esi           ; r13d = numsSize
    mov     r14d, edx           ; r14d = target
    mov     r15, rcx            ; r15 = returnSize

    ; Outer loop: i = 0
    xor     ebx, ebx            ; ebx = i
.outer:
    cmp     ebx, r13d
    jge     .not_found

    ; Inner loop: j = i + 1
    lea     ecx, [ebx + 1]     ; ecx = j
.inner:
    cmp     ecx, r13d
    jge     .next_i

    ; Check if nums[i] + nums[j] == target
    movsxd  rax, ebx
    mov     eax, [r12 + rax*4]  ; eax = nums[i]
    movsxd  rdx, ecx
    add     eax, [r12 + rdx*4]  ; eax = nums[i] + nums[j]
    cmp     eax, r14d
    je      .found

    inc     ecx
    jmp     .inner

.next_i:
    inc     ebx
    jmp     .outer

.found:
    ; Allocate 2 ints (8 bytes) via malloc
    push    rcx                 ; save j
    mov     edi, 8
    call    malloc wrt ..plt
    pop     rcx                 ; restore j

    mov     [rax], ebx          ; result[0] = i
    mov     [rax + 4], ecx      ; result[1] = j
    mov     dword [r15], 2      ; *returnSize = 2
    jmp     .done

.not_found:
    xor     eax, eax            ; return NULL
    mov     dword [r15], 0      ; *returnSize = 0

.done:
    pop     r15
    pop     r14
    pop     r13
    pop     r12
    pop     rbx
    ret
