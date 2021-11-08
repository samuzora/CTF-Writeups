# rev/seed

Author: m0x

Having a non-weak seed when generating "random" numbers is super important! Can you figure out what is wrong with this PRNG implementation?

`seed.py` is the Python script used to generate the flag for this challenge. `log.txt` is the output from the script when the flag was generated.

What is the flag?

---

Seed is based on epoch time (seconds since 1 Jan 1970, the Unix epoch)

Since the challenge was probably made this year, we can do a simple bruteforce for all seconds since the start of the year. I used [this tool](https://www.epochconverter.com/) to obtain the Epoch time for 1 Jan 2021, 00:00:00 and the time which I attempted the challenge. 

The script I used to bruteforce the flag can be found in sol.py. Since printing is quite expensive time-wise, I commented out the print line to save time. Flag: dam{f6f73f022249b67e0ff840c8635d95812bbb5437170464863eda8ba2b9ff3ebf}
