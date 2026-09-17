# Libraries
`#include <stdio.h>`       Standard input/output functions (printf, scanf, fopen)

`#include <math.h>`        Math functions (pow, sqrt, round) — compile with -lm on Linux

`#include <stdbool.h>`     Boolean data type (`bool`, `true`, `false`)

`#include <string.h>`      String manipulation (strlen, strcpy, strcmp)

`#include <windows.h>`     Windows sleep function: Sleep(1000); (in milliseconds)

`#include <unistd.h>`      POSIX/Linux sleep function: sleep(1); (in seconds)

`#include <time.h>`        Time functions used to seed PRNG (time)

`#include <stdlib.h>`      General utilities: memory allocation (malloc, calloc), rand(), exit()

`// comment`               Single-line comment (like # in Python)

`/* comment */`            Multi-line block comment

# Basic Structure
```c
#include <stdio.h>  // standard in/out lib

// The main function (program starts here)
int main() {
    printf("Hello, World!\n");
    return 0; // Returning 0 to OS (all went good)
}
```

# Data types
```c
int a = 5; // 4 bytes typical (-2,147,483,648 to 2,147,483,647)

float b = 5.5f; // 4 bytes, ~6-7 decimal places (single precision; add 'f' suffix)

double c = 3.14159265358979; // 8 bytes, ~15-17 decimal places (double precision)

char d = 'A'; // 1 byte, stores a single character enclosed in single quotes

char name[] = "Ahoj jak je"; // Array of characters terminated by '\0'; uses double quotes

bool isTrue = true; // 1 byte, requires <stdbool.h>, stores 1 (true) or 0 (false)
```

# Format specifiers

Special tokens that begin with `%` followed by a specifier character and optional flags (width, precision, alignment).
```c
printf("Je mi %d\n", 18); // %d or %i expects int

printf("Cena %f\n", 19.548f); // %f expects float

printf("Cena %lf\n", 19.54545454545); // %lf expects double (long float)

printf("Znamka %c\n", 'A'); // %c expects single char in single quotes

printf("Text: %s\n", "Ahoj"); // %s expects null-terminated string

printf("Address: %p\n", (void*)&a); // %p expects a pointer address (cast to void* is best practice)

printf("%4d\n", 10); // Prints right-justified within width of 4: "  10"

printf("%-4d\n", 10); // Prints left-justified within width of 4: "10  "

printf("%04d\n", 10); // Pads with leading zeros: "0010"

printf("%+d\n", 10); // Explicitly displays sign: "+10"

printf("%.2f\n", 10.5481); // Restricts to 2 decimal places with rounding: "10.55"

printf("%+7.2f\n", 10.5481); // Explicit sign, right-aligned to 7 characters wide: "  +10.55"
```

# Operators

| Operator | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| `+` | Addition | Adds two operands | `a + b` |
| `-` | Subtraction | Subtracts right from left operand | `a - b` |
| `*` | Multiplication | Multiplies two operands | `a * b` |
| `/` | Division | Divides left by right operand | `a / b` |
| `%` | Modulus | Remainder of integer division | `a % b` |
| `++` | Increment | Increases value by 1 (`a++` post, `++a` pre) | `++a`, `a++` |
| `--` | Decrement | Decreases value by 1 | `--a`, `a--` |
| `&&` | Logical AND | Returns true if both conditions are true | `a && b` |
| `\|\|` | Logical OR | Returns true if at least one condition is true | `a \|\| b` |
| `!` | Logical NOT | Inverts boolean truth value | `!a` |
| `==` | Equality | Returns true if operands are equal | `a == b` |
| `!=` | Inequality | Returns true if operands are not equal | `a != b` |

# Integer division caution:
```c
int b = 5, c = 2;
float bad = b / c; // Evaluates to 2.0 because integer division truncates decimals
float good = (float)b / c; // Evaluates to 2.5 because 'b' was explicitly cast to float
```

# Variables and Type Casting
```c
int a = 0; // Declaration and initialization

int b; // Declaration without initialization: contains garbage memory values!

const int MAX_USERS = 100; // Read-only constant; cannot be modified later

// Implicit Casting (automatic promotion by compiler)
int x = 5;
double y = x; // 5 converted to 5.0 automatically

// Explicit Type Casting: (type)variable
int total = 17;
int count = 5;
double average = (double)total / count; // 3.4 instead of 3.0
```

# User Input
```c
int age = 0;
char grade = '\0';
char name[30];

printf("Enter age: ");
scanf("%d", &age); // Pass pointer address (&age) so scanf can write directly into memory

printf("Enter grade: ");
// Leading space before %c skips leftover newline ('\n') from prior input in stdin buffer
scanf(" %c", &grade);

// Read full line containing spaces
printf("Enter your name: ");
getchar(); // Consumes the trailing '\n' left behind by scanf
fgets(name, sizeof(name), stdin); // Reads up to 29 characters + null terminator safely
name[strcspn(name, "\n")] = '\0'; // Idiomatic way to strip trailing newline added by fgets
```

# Strings
```c
char name[] = "Dave"; // 4 visible characters + 1 hidden '\0' (null terminator) = 5 bytes

// Modifying the last character to null terminator to truncate the string:
name[strlen(name) - 1] = '\0'; 

// Common string functions (<string.h>):
char dest[50];
strcpy(dest, "Hello "); // Copies second argument into dest
strcat(dest, "World"); // Appends to destination: "Hello World"
int len = strlen(dest); // Returns number of characters excluding '\0'
int cmp = strcmp("apple", "banana"); // Returns <0 if first string is lexicographically smaller
```

# Math Functions
Requires `<math.h>`.
```c
double sq = sqrt(9); // 3.0
double p = pow(2, 3); // 8.0 (2 raised to 3rd power)
double r = round(3.14); // 3.0 (rounds to nearest integer)
double c = ceil(3.14); // 4.0 (rounds upwards)
double f = floor(3.14); // 3.0 (rounds downwards)
int a = abs(-4); // 4 (absolute value from <stdlib.h>)
double l = log(3); // ~1.0986 (natural logarithm base e)
double s = sin(1.5708); // Radians input (1.5708 rad = 90 deg -> 1.0)
double co = cos(0); // 1.0
double t = tan(0.7853); // ~1.0
```

# Control Flow

### If / Else
```c
int age = 18;

if (age >= 65) {
    printf("Senior\n");
} else if (age >= 18) {
    printf("Adult\n");
} else {
    printf("Kid\n");
}
```

### Ternary Operator
Inline conditional shorthand for simple if-else expressions: `condition ? value_if_true : value_if_false`
```c
int x = 5, y = 6;
int max = (x > y) ? x : y; // Evaluates to 6
```

### Switch Case
```c
int day = 1;

switch (day) {
    case 1:
        printf("Monday\n");
        break; // break prevents execution from falling through into case 2
    case 2:
        printf("Tuesday\n");
        break;
    default:
        printf("Other day\n");
        break;
}
```

# Loops

### For Loop
```c
// (initialization; condition; increment/decrement)
for (int i = 0; i < 10; i++) {
    if (i == 3) continue; // Skips iteration 3 and proceeds to i=4
    if (i == 8) break; // Exits loop entirely
    printf("%d ", i);
}
```

### While Loop
Condition checked before the loop body runs.
```c
int a = 0;
while (a <= 10) {
    printf("%d ", a);
    a++;
}
```

### Do-While Loop
Guaranteed to execute the loop body at least once before checking condition.
```c
int a = 0;
do {
    printf("%d ", a);
    a++;
} while (a <= 10);
```

# Functions and Prototypes

Function prototypes declare a function's name and signature so the compiler recognizes it when called in `main()` before its actual implementation appears lower in the file.
```c
// Prototype: return_type function_name(parameter_types);
void greet(char name[], int age);
void addOne(int *num); // Pass-by-reference using pointers

int main(void) {
    greet("Dave", 18);
    
    int val = 10;
    addOne(&val); // Passes address so the function can alter 'val'
    // val is now 11
    
    return 0;
}

// Implementation
void greet(char name[], int age) {
    printf("Hey %s, you are %d years old.\n", name, age);
}

void addOne(int *num) {
    (*num)++; // Dereference pointer to modify value stored at that address
}
```

# Arrays

### 1D Arrays
```c
int numbers[] = {10, 15, 20, 54, 81};

// Calculate array length at runtime: (total array bytes / single element bytes)
int len = sizeof(numbers) / sizeof(numbers[0]); // 20 / 4 = 5 elements

// Zero-initialization for all elements:
int empty[5] = {0}; // [0, 0, 0, 0, 0]
```

### 2D Arrays
Inner dimensions must always be specified; the first dimension can be inferred.
```c
// 3 rows, 2 columns
int matrix[][2] = {
    {1, 2},
    {3, 4},
    {5, 6}
};

int val = matrix[1][0]; // Accesses second row, first column (value: 3)
```

### Array of Strings
```c
// 3 strings, each allocated space for up to 9 characters + '\0'
char fruits[][10] = {"Apple", "Banana", "Coconut"};

printf("%s\n", fruits[1]); // "Banana"
```

# Pseudo-Random Numbers
Requires `<stdlib.h>` and `<time.h>`.
```c
// Seed generator once using current Unix epoch timestamp
srand((unsigned int)time(NULL));

int min = 1;
int max = 100;

// Formula to generate a number within [min, max] range:
int randomNum = (rand() % (max - min + 1)) + min;

// RAND_MAX is a library constant containing the maximum integer rand() can output
```

# Typedef and Enums

### Typedef
Defines an alias for an existing type to improve readability.
```c
typedef unsigned long ulong;
typedef char String50[50];

ulong bigNum = 4294967295;
String50 user = "Alice";
```

### Enums
Maps descriptive names to integral constants (starts at index 0 by default).
```c
enum Day { SUNDAY, MONDAY, TUESDAY, WEDNESDAY };
// SUNDAY=0, MONDAY=1, TUESDAY=2, WEDNESDAY=3

enum Status { PENDING = 1, SUCCESS = 200, ERROR = 500 };

int main(void) {
    enum Day today = SUNDAY; // today holds integer value 0
    if (today == SUNDAY) {
        printf("Weekend!\n");
    }
    return 0;
}
```

# Structs

Used to bundle variables of different types together into a single custom type.
```c
struct Student {
    char name[50];
    int age;
    float gpa;
    bool isFullTime;
};

// Array of Structs
struct Car {
    char model[50];
    int year;
    int price;
};

int main(void) {
    struct Student student1 = {"Dave", 18, 2.5f, true};
    strcpy(student1.name, "Tom"); // Update string member via strcpy

    struct Car fleet[] = {
        {"Mustang", 2025, 32000},
        {"Corvette", 2026, 68000},
        {"Challenger", 2024, 29000}
    };

    // Arrow operator (->) is used when accessing struct fields through a pointer:
    struct Student *pStudent = &student1;
    printf("%s\n", pStudent->name); // Equivalent to (*pStudent).name

    return 0;
}
```

# Pointers

Pointers hold memory addresses of other variables instead of direct values.
```c
int age = 25;

// Declaration: '*' denotes pAge is a pointer to an int
int *pAge = &age; // '&' gets address of 'age'

// Dereferencing: '*' accesses/updates the value stored at that target address
(*pAge)++; // Increments 'age' to 26

printf("Value: %d\n", *pAge); // Prints 26
printf("Memory Address: %p\n", (void*)pAge); // Prints hex address (e.g., 0x7ffd...)
```

# Dynamic Memory Allocation (Heap)
Memory allocated via `malloc`, `calloc`, or `realloc` persists until explicitly freed with `free()`. Always check if allocation returned `NULL`.

### Malloc
Allocates uninitialized raw memory of specified size in bytes.
```c
int n = 5;
char *grades = (char*)malloc(n * sizeof(char)); // 5 * 1 = 5 bytes

if (grades == NULL) {
    fprintf(stderr, "Allocation failed!\n");
    return 1;
}

free(grades);   // Releases allocated memory back to OS heap
grades = NULL;  // Prevent dangling pointer bug (avoids pointing to deallocated memory)
```

### Calloc
Allocates memory and clears all bytes to zero (`number_of_items`, `size_per_item`).
```c
int count = 4;
int *scores = (int*)calloc(count, sizeof(int)); // Cleared to zeros

if (scores == NULL) return 1;

free(scores);
scores = NULL;
```

### Realloc
Resizes previously allocated heap block.
```c
int initial = 5;
float *prices = (float*)calloc(initial, sizeof(float));

int expanded = 7;
// Always use a temporary pointer so you don't leak memory if realloc returns NULL
float *temp = (float*)realloc(prices, expanded * sizeof(float));

if (temp != NULL) {
    prices = temp; // Reassignment safe
} else {
    // Original 'prices' block remains intact if reallocation failed
    free(prices);
    return 1;
}

free(prices);
prices = NULL;
```

# File Management

### Writing to a File
```c
char text[] = "Ahoj jak\nJe";

// "w" mode creates or overwrites an existing file; "a" appends without overwriting
FILE *pFile = fopen("output.txt", "w");
if (pFile == NULL) {
    perror("Error opening file"); // Prints standard system error details
    return 1;
}

fprintf(pFile, "%s", text);
fclose(pFile); // Flushes buffer and closes file descriptor
```

### Reading from a File
```c
char buffer[1024] = {0};

FILE *pFile = fopen("output.txt", "r");
if (pFile == NULL) {
    perror("Error opening file");
    return 1;
}

// fgets reads file line-by-line until end of file (EOF returns NULL)
while (fgets(buffer, sizeof(buffer), pFile) != NULL) {
    printf("%s", buffer);
}

fclose(pFile); // Always close open file handles
```