# misc/bad-patterns

Author: BaboonWithTheGoon

A hacker was too lazy to do proper encryption. However, they left us some examples of how their encryption "algo" was supposed to work.

original text : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." 

encoded: "Lpthq jrvym!frpos"vmt!cpit-"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu"oebpth$eu"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp"oebptlw okvm vv#eljsxmp!g{$eb"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo"svojfhrt-"vynu"lr dwota!sxm phimcjc#hetguynu"pslmkw$aokp$ie"hwt!ndfoswp2"

Find the pattern!

Maybe you should try the same pattern on this string: 
bagelarenotwholewheatsometimes

Make sure you wrap your solution with dam{...}!

---

I was stumped at this challenge for quite a while (due to my imcompetence in classical ciphers)

I kinda guessed that it was a Vigenere-style cipher (because I could see some sort of rotating pattern in the letters) but online Vigenere bruteforcers failed to give me back the Lorem ipsum plaintext.

After doing some research, I stumbled on this [site](https://www.quora.com/If-I-know-the-encrypted-and-decrypted-message-how-do-I-find-the-key). Thus I wrote a script to test this out, and indeed I get a rotating pattern of [0, -1, -2, -3, -4] by subtracting the ords of pt by ct. 

Applying this pattern to the string, we get bbihpasgqstxjrpexjhettqpitjohw... strange choice for a flag, but wrap it with dam{} and it in fact is the flag. 
