# C Programming Cheat Sheet

## Libraries & Environment
```c
#include <stdio.h>       // standard input/output (printf, scanf, fopen)
#include <stdlib.h>      // random int, dynamic memory (malloc, free)
#include <math.h>        // math functions (sqrt, pow, sin)
#include <stdbool.h>     // standard boolean (true/false)
#include <string.h>      // string manipulation (strlen, strcpy)
#include <windows.h>     // Windows API: Sleep(1000); in milliseconds
#include <unistd.h>      // POSIX API: sleep(1); in seconds for linux/mac
#include <time.h>        // time functions, used for seeding randoms
```
## Data Types & Format Specifiers
```c
int a = 5;               // 4 bytes, format %d
float b = 5.5f;          // 4 bytes, 7 decimal points, format %f
double c = 3.14159;      // 8 bytes, 15 decimal points, format %lf
char d = 'A';            // 1 byte, format %c
char name[] = "Ahoj";    // array of chars (string), format %s n+1 bytes (null terminator)
bool isTrue = true;      // 1 byte
void *ptr;               // pointer address, format %p 8bytes

// Format Modifiers
// %4d (right justified spaces), %-4d (left justified), %04d (pads zeros), %+d (forces +/- sign), %.2f (rounds to 2 decimal places)
```
## Control Flow & Operators
```c
// Operators: +, -, *, /, %, ++, --, &&, ||, !
// Warning: float a = b / c; (If b and c are ints, it performs integer division first)
// Bitwise: & (AND), | (OR), ^ (XOR), << (Left Shift), >> (Right Shift)
// Ternary Operator
int max = (x > y) ? x : y; // if x > y return x, else return y

// Switch Case
switch(a) { 
    case 1: printf("Monday"); 
    break;

    default: printf("Other"); 
}
```
## Input, Strings & Quirks
```c
scanf("%d", &age);       // & means address of
scanf(" %c", &grade);    // Space before %c ignores leftover \n in buffer
fgets(name, sizeof(name), stdin); // Better for strings, reads spaces
getchar();               // Consumes single character, clears \n
name[strlen(name)-1] = '\0'; // Replaces trailing newline with null terminator
```
## Arrays, Structs, Enums & Typedef
```c
int number[] = {10,15,20,54,81}; // 1D array, length = sizeof(number)/sizeof(number[0])
int number2D[][2] = {{1,2}, {3,4}}; // 2D array
typedef unsigned char byte; // Typedef renames types
enum Day { SUNDAY = 0, MONDAY, TUESDAY }; // Enum groups constants

struct Student { char name[50]; int age; float gpa; }; // Struct declaration
struct Student student1 = {"Dave", 18, 2.5}; // Struct initialization
```
## Pointers & Pointer to Structs (Ptr->x)
```c
int age = 25;
int *pAge = &age;        // Stores memory address of age
(*pAge)++;               // Dereferences pointer to access/modify the value

// --- Struct Pointers Explanation ---
// When you have a regular struct, you access properties with a dot: student1.age
// When you have a POINTER to a struct, you use the arrow operator (->).
// Example:
// struct Student *ptr = &student1;
// ptr->age = 19; 
// The arrow (ptr->age) is the exact same as (*ptr).age
// It automatically dereferences the pointer and accesses the member in one clean step.
```
## Advanced: Function Pointers
```c
// Functions live in memory, so you can point to them: return_type (*name)(params)
int add(int a, int b) { return a + b; }
int (*op)(int, int) = add;
int result = op(5, 10); // Calls add(5, 10), returns 15
```
## Dynamic Memory (Heap)
```c
// malloc(size) allocates raw bytes. calloc(count, size) allocates and zeroes them.
// realloc(ptr, new_size) resizes. free(ptr) returns memory to OS.
int *scores = calloc(4, sizeof(int));
free(scores); scores = NULL; // Prevents dangling pointers
```
## File Management (I/O)
```c
FILE *pFile = fopen("output.txt", "w"); // "w" to write, "r" to read
if (pFile != NULL) { fprintf(pFile, "Text"); fclose(pFile); }
// Read line by line: while (fgets(buffer, sizeof(buffer), pFile) != NULL)
```