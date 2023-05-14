# include<stdio.h>

int main(void)
{
  int i;
  unsigned int local_b8 [20];
  double local_68;
  double local_60;
  double local_58;
  double local_50;
  double local_48;
  double local_40;
  double local_38;
  double local_30;
  double local_28;
  unsigned int local_20;
  long local_10;

  local_b8[0] = 0xf781fc86;
  local_b8[1] = 0xc5afc9bb;
  local_b8[2] = 0xd5a5de9f;
  local_b8[3] = 0xefa1efa4;
  local_b8[4] = 0xefb4dfac;
  local_b8[5] = 0xc49fd6af;
  local_b8[6] = 0xefa5dda9;
  local_b8[7] = 0xefa4dea1;
  local_b8[8] = 0xdfa6d6a5;
  local_b8[9] = 0xc49fc4b2;
  local_b8[10] = 0xdfb3efaf;
  local_b8[11] = 0xefa5c6ac;
  local_b8[12] = 0xd5b6d5b2;
  local_b8[13] = 0xdea9c3b2;
  local_b8[14] = 0x80f2efa7;
  local_b8[15] = 0x87f4d2f8;
  local_b8[16] = 0x86f6d4a2;
  local_b8[17] = 0xd4a382a3;
  local_b8[18] = 0xb0c0cdf8;
  local_68 = 0;
  local_60 = 0;
  local_58 = 0;
  local_50 = 0;
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  for (i = 0; i < 19; i = i + 1) {
    *(char *)((long)&local_68 + (long)(i << 2)) = (char)local_b8[i] ^ 0xc0;
    *(char *)((long)&local_68 + (long)(i * 4 + 1)) = (char)((unsigned int)local_b8[i] >> 8) ^ 0xb0;
    *(char *)((long)&local_68 + (long)(i * 4 + 2)) = (char)((unsigned int)local_b8[i] >> 16) ^ 0xc0;
    *(char *)((long)&local_68 + (long)(i * 4 + 3)) = (char)((unsigned int)local_b8[i] >> 24) ^ 0xb0;
  }
  puts((char *)&local_68);
  return 0;
}