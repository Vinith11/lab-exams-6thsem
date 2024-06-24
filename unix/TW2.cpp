#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199309L
#include <iostream>
#include <unistd.h>

using namespace std;

int main() {
    #ifdef _POSIX_JOB_CONTROL
        cout << "System supports POSIX Job Control." << endl;
    #else
        cout << "System doesn't support POSIX Job Control." << endl;
    #endif

    #ifdef _POSIX_SAVED_IDS
        cout << "System supports saved set-UID and saved set-GID." << endl;
    #else
        cout << "System doesn't support POSIX saved IDs." << endl;
    #endif

    #ifdef _POSIX_CHOWN_RESTRICTED
        cout << "Chown restricted option is: " << _POSIX_CHOWN_RESTRICTED << endl;
    #else
        cout << "System doesn't support chown restricted option." << endl;
    #endif

    #ifdef _POSIX_NO_TRUNC
        cout << "Truncation option is: " << _POSIX_NO_TRUNC << endl;
    #else
        cout << "System doesn't support POSIX truncation." << endl;
    #endif

    #ifdef _POSIX_VDISABLE
        cout << "Disable char for terminal files: " << _POSIX_VDISABLE << endl;
    #else
        cout << "System doesn't support POSIX disability." << endl;
    #endif

    return 0;
}
