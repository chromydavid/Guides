# C compiler + Makefile

## C compiler (GCC UCRT64)

### 1. Download and install MSYS2
[msys.org](https://www.msys2.org/) download the  `msys2-x86_64` for x86 or the ` msys2-arm64` for ARM depending on your CPU architecture

Install it (dont change anything just click next and finish) after that the UCRT64 terminal shoud pop up

### 2. Install the GCC compiler toolchain
Paste `pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain` into the UCRT64 terminal and hit enter

After that just confirm (`y`) everything until the instalation finishes

### 3. Add the compiler to Windows PATH
Press Win + R and type `sysdm.cpl` then press Enter

Go to the Advanced tab and click Environment Variables

Under System variables select Path and click Edit

Click New and add `C:\msys64\ucrt64\bin` then click `OK` on all windows to apply the changes

## Add Make for Makefile
### 1. Install Make via UCRT64
Open your MSYS2 UCRT64 terminal 

Paste `pacman -S mingw-w64-ucrt-x86_64-make` into the terminal and again hit enter while confirming everything

### 2. Change the default keyword to Make
At this point the makefile already works but by default the command to activate it is `mingw32-make` since we want to only type `make` to use it we need to make a little change

Open File Explorer and navigate to the directory where your compiler lives (by default) `C:\msys64\ucrt64\bin`

Locate `mingw32-make.exe`

Copy and paste it in the same folder then rename the copy to `make.exe` (if you want a different keyword just rename it to your liking ex. `doStuff.exe`)

To verify that everything works open a new PowerShell or CMD and run: `make --version` or your keyword if you went with a different one