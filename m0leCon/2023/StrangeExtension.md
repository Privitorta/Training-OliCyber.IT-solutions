> I've found this strange file in our super secret project. Can you figure out where the flag is?

Dal file dato `strangefile.ptm` tento un intuitivo:
```
strings strangefile.ptm | grep "ptm{"
```
Che sorprendentemente, mi dona:

**ptm{m4k3_r3tr0_g4m1ng_gr34t_4g41n!!}**