#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 1993309L
#include <iostream>
#include <limits.h>
#include <unistd.h>

using namespace std;

void compileTime() {
    cout << "\n\nMANIFEST CONSTANTS\n\n";
    #ifdef _SC_CLK_TCK
        cout << "SYSTEM SUPPORTS CLK_TCK which is " << _SC_CLK_TCK << endl;
    #else
        cout << "SYSTEM DOES NOT SUPPORT CLK_TCK" << endl;
    #endif

    #ifdef _POSIX_CHILD_MAX
        cout << "Man number of child processes is " << _POSIX_CHILD_MAX << endl;
    #else
        cout << "CHILD_MAX is not defined" << endl;
    #endif

    #ifdef _POSIX_PATH_MAX
        cout << "Maximum path length is " << _POSIX_PATH_MAX << endl;
    #else
        cout << "PATH_MAX is not defined" << endl;
    #endif
    #ifdef _POSIX_OPEN_MAX
        cout << "Maximum number of open files per process is " << _POSIX_OPEN_MAX << endl; 
    #else
        cout << "OPEN_MAX is not defined" << endl;
    #endif
    #ifdef _POSIX_NAME_MAX
        cout << "Maximum number of characters in a filename is " << _POSIX_NAME_MAX << endl;
    #else
        cout << "SYSTEM DOES NOT SUPPORT _POSIX_NAME_MAX" << endl;
    #endif
}

void runTime() {
    cout << "\n\nRUNTIME CONSTANTS\n\n";
    long arg_max = sysconf(_SC_ARG_MAX);
    cout << "Maximum length of arguments to exec is " << arg_max << endl;
    long child_max = sysconf(_SC_CHILD_MAX);
    cout << "Maximum number of child processes is " << child_max << endl;
    long clk_tck = sysconf(_SC_CLK_TCK);
    cout << "Number of clock ticks per second is " << clk_tck << endl;
    long open_max = sysconf(_SC_OPEN_MAX);
    cout << "Maximum number of open files per process is " << open_max << endl;
    long name_max = sysconf(_PC_NAME_MAX);
    cout << "Maximum number of characters in a filename is " << name_max << endl;
    long path_max = pathconf("/", _PC_PATH_MAX);
    cout << "Maximum path length is " << path_max << endl;
}

int main() {
    compileTime();
    runTime();
    return 0;
}
