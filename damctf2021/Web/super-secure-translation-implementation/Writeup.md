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

As expected it didn't work. After trying a few more payloads (most of them became too long for the limit of 161 chars) I finally gave up and went on to do other challs. The scripts and other stuff I suffered much to make can be found in this folder
