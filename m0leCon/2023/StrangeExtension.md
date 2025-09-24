> I've found this strange file in our super secret project. Can you figure out where the flag is?

Dal file dato `strangefile.ptm`, runna:
```bash
strings strangefile.ptm | grep "ptm{"
```

Che darà la flag.