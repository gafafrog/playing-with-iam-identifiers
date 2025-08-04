# playing-with-iam-identifiers

IAM Identifiersのエンコーディングで遊んでみる。

## Base32 decode

```
$ python3 b32_to_bits.py "ABCDE"
Base32文字列: ABCDE
ビット配列: 00000 00001 00010 00011 00100
```

## Search account id in IAM identifier

```
$ python3 find_account_id.py AIDACKCEVSQ6C2EXAMPLE 159057810492
Base32文字列: AIDACKCEVSQ6C2EXAMPLE
ビット配列: 00000 01000 00011 00000 00010 01010 00010 00100 10101 10010 10000 11110 00010 11010 00100 10111 00000 01100 01111 01011 00100
開始  0 bit目: 008690673732
開始  1 bit目: 017381347465
開始  2 bit目: 034762694930
開始  3 bit目: 069525389861
開始  4 bit目: 139050779722
開始  5 bit目: 278101559445
開始  6 bit目: 556203118891
開始  7 bit目: 012894610006
開始  8 bit目: 025789220012
開始  9 bit目: 051578440025
開始 10 bit目: 103156880050
開始 11 bit目: 206313760101
開始 12 bit目: 412627520202
開始 13 bit目: 825255040404
開始 14 bit目: 550998453032
開始 15 bit目: 002485278288
開始 16 bit目: 004970556577
開始 17 bit目: 009941113155
開始 18 bit目: 019882226311
開始 19 bit目: 039764452623
開始 20 bit目: 079528905246
開始 21 bit目: 159057810492 <== Found!!
開始 22 bit目: 318115620984
開始 23 bit目: 636231241968
開始 24 bit目: 172950856161
開始 25 bit目: 345901712322
開始 26 bit目: 691803424645
開始 27 bit目: 284095221515
開始 28 bit目: 568190443030
開始 29 bit目: 036869258285
開始 30 bit目: 073738516570
開始 31 bit目: 147477033140
開始 32 bit目: 294954066280
開始 33 bit目: 589908132561
開始 34 bit目: 080304637346
開始 35 bit目: 160609274692
開始 36 bit目: 321218549385
開始 37 bit目: 642437098770
開始 38 bit目: 185362569765
開始 39 bit目: 370725139531
開始 40 bit目: 741450279063
開始 41 bit目: 383388930350
開始 42 bit目: 766777860700
開始 43 bit目: 434044093624
開始 44 bit目: 868088187248
開始 45 bit目: 636664746720
開始 46 bit目: 173817865664
開始 47 bit目: 347635731329
開始 48 bit目: 695271462659
開始 49 bit目: 291031297542
開始 50 bit目: 582062595084
開始 51 bit目: 064613562392
開始 52 bit目: 129227124785
開始 53 bit目: 258454249571
開始 54 bit目: 516908499143
開始 55 bit目: 103381699828
開始 56 bit目: 968122368798
開始 57 bit目: 836733109821
開始 58 bit目: 573954591866
開始 59 bit目: 048397555957
開始 60 bit目: 096795111915
開始 61 bit目: 193590223830
開始 62 bit目: 387180447660
開始 63 bit目: 774360895321
開始 64 bit目: 449210162866
```

## あわせて読みたい
- [A short note on AWS KEY ID - Medium](https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489)
- [AWS Access Key ID formats - Aidan Steele's blog (usually about AWS)](https://awsteele.com/blog/2020/09/26/aws-access-key-format.html)
- [Get Account ID from AWS Access Keys - Hacking The Cloud](https://hackingthe.cloud/aws/enumeration/get-account-id-from-keys/)
