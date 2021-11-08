# web/super-secure-translation-implementation

Author: lyellread

Get creative and try to bypass the unhackable security measures that keep this site safe.

---

Name gave it away: SSTI

In essence, this is a pyjail challenge in the form of an SSTI vuln. Looking at the source, we are allowed to view other files in the same directory as app.py. To check which files we can view we need to use the Dockerfile provided. Thus, we can view filters.py and see that there are several string manipulation functions for us, as well as an eval().

I thought this would be an easy challenge, but it just shows how much I'm lacking in pyjail escapes.

First, I generated a list of printable ASCII chars using a script, and then pasted it into the payload to get all illegal chars. (At this point I hadn't realized I can simply read check.py for the allowed chars)

Then I copied the output of illegal chars and removed them from the list of ASCII chars in the script.

Now comes the escape portion. First I tried using b64d recursively to escape illegal characters, but it quickly became too long.

Then I realized that we're given chr(), and 1, 4, and 6. In my script, you can see my pathetic attempt to take advantage of this. I printed the ord of all illegal characters and manually decomposed them to math statements with 1, 4 and 6. After a painstaking hour or so, I was finally done with my first payload, and hoped for the best...

As expected it didn't work. After trying a few more payloads (most of them became too long for the limit of 161 chars) I finally gave up and went on to do other challs. The scripts and other stuff can be found in this folder

---

ps. soln for this was [https://super-secure-translation-implementation.chals.damctf.xyz/secure_translate/?payload=%7B%7B%28%27%28o%27%2B%28111%2B1%29%7Cch%2B%27e%27%2B%2866%2B44%29%7Cch%2B%27%28%22%27%2B%2844%2B1%2B1%2B1%29%7Cch%2B%2866%2B16%2B16%2B4%29%7Cch%2B%27l%27%2B%2866%2B16%2B14%2B1%29%7Cch%2B%2866%2B16%2B16%2B4%2B1%29%7Cch%2B%27%22%29%27%2B%2844%2B1%2B1%29%7Cch%2B%27re%27%2B%2866%2B16%2B14%2B1%29%7Cch%2B%27d%28%29%29%27%29%7Ce%7D%7D](https://super-secure-translation-implementation.chals.damctf.xyz/secure_translate/?payload=%7B%7B%28%27%28o%27%2B%28111%2B1%29%7Cch%2B%27e%27%2B%2866%2B44%29%7Cch%2B%27%28%22%27%2B%2844%2B1%2B1%2B1%29%7Cch%2B%2866%2B16%2B16%2B4%29%7Cch%2B%27l%27%2B%2866%2B16%2B14%2B1%29%7Cch%2B%2866%2B16%2B16%2B4%2B1%29%7Cch%2B%27%22%29%27%2B%2844%2B1%2B1%29%7Cch%2B%27re%27%2B%2866%2B16%2B14%2B1%29%7Cch%2B%27d%28%29%29%27%29%7Ce%7D%7D), which evals to (open('/flag').read())... I never thought of using redundant parentheses to bypass the check for open :(
