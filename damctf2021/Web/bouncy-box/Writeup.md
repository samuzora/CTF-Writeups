# web/bouncy-box

Author: BobbySinclusto

This game is extremely fun. So fun that some people have been playing it for over 3 years!

[https://bouncy-box.chals.damctf.xyz/](https://bouncy-box.chals.damctf.xyz/)

---

This challenge is a 2-part SQLi challenge. The aim is to log into one of the 'VIP' accounts in a flappy-bird clone. 

The first login is quite easy to bypass: through a basic SQLi payload, `boxy_mcbounce'#`. 

However, there is a second login that we need to bypass to get the flag, and that login isn't vulnerable to several SQLi payloads I tried (whether due to a filter or proper escaping, I'm not sure...) Anyway, after trying many many times to bypass the second login, I realized that I could probably attack the first login to get his password instead. 

I wasn't too familiar with SQLi so I thought that we could show the table to get his password. Since the comment character used was '#', we can assume that we're dealing with MySQL. Thus, I tried `boxy_mcbounce'; SHOW TABLES LIKE '%'` to get the table name, and from there the password. However, I soon realized that this form of SQLi with no output is known as blind SQLi, and there's really no way we can show the table.

Since we're dealing with semi-blind SQLi (only true/false output), we can use that to error our statement if something isn't true. For example, we can guess the table name or the password of the user character by character, failing the login if that specific character is wrong, or otherwise. 

After hours of googling I finally found something that would work, [here](https://book.hacktricks.xyz/pentesting-web/sql-injection#exploiting-blind-sqli). (This site is really useful btw)

Thus, we have our payload, `boxy_mcbounce' AND IF(SUBSTRING(Password,n,1)='x', True, False)#` which we can use to manually guess the password letter by letter. (I think we can automate this with Burp Suite Intruder, but at the time I couldn't be bothered to learn how to use it)

Finally, we get our password, `b0unceBounc3`. We can now pass the second login with boxy_mcbounce:b0uncyBounc3 and get our flag, `dam{b0uNCE_B0UNcE_b0uncE_B0uNCY_B0unce_b0Unce_b0Unc3}`.  

Overall this was a pretty fun challenge, and I did learn quite a bit from this (especially given my incompetence in SQLi)
