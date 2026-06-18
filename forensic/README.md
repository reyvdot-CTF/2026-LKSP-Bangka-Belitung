# WriteUp - Pinging

## Overview

* **Name:** Pinging
* **Category:** Forensic
* **Point:** 500
* **Author:** Aseng
* **Desc:** My buddy sends me something inside that ICMP protocol data, can you parse and help me figure out what’s the message?
* **File:** [snippet.pcap](../forensic/snippet.pcap)

## Summary
* **Looking for hidden messages within ICMP**

## Attack Idea
When I scroll using the Page Down key, I suspect that some characters in the Data table are changing.
>![alt text](../assets/unnamed_11.png) 
>![alt text](../assets/unnamed_12.png) 

Then, I write all the text appear on that table one by one (manualy).

> ![alt text](../assets/unnamed_13.png) 

Here, I am using dcode.fr for automatic analysis and decryption.
Then I got this:
> ![alt text](../assets/unnamed_14.png) 

<b>FLAG:
----
LKS{baby_ICMP_but_not_exfil_morelike_transfer_fl4g??} </b>

