# Web Penetration Testing with Kali Linux - Third Edition
This is the code repository for [Web Penetration Testing with Kali Linux - Third Edition](https://www.packtpub.com/networking-and-servers/web-penetration-testing-kali-linux-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788623377), published by [Packt](www.packtpub.com). It contains all the supporting project files necessary to work through the book from start to finish.

## About the Book
Web Penetration Testing with Kali Linux - Third Edition shows you how to set up a lab, helps you understand the nature and mechanics of attacking websites, and explains classical attacks in great depth. This edition is heavily updated for the latest Kali Linux changes and the most recent attacks. Kali Linux shines when it comes to client-side attacks and fuzzing in particular.

From the start of the book, you'll be given a thorough grounding in the concepts of hacking and penetration testing, and you'll see the tools used in Kali Linux that relate to web application hacking. You'll gain a deep understanding of classicalSQL, command-injection flaws, and the many ways to exploit these flaws. Web penetration testing also needs a general overview of client-side attacks, which is rounded out by a long discussion of scripting and input validation flaws.

There is also an important chapter on cryptographic implementation flaws, where we discuss the most recent problems with cryptographic layers in the networking stack.

The importance of these attacks cannot be overstated, and defending against them is relevant to most internet users and, of course, penetration testers.

At the end of the book, you'll use an automated technique called fuzzing to identify flaws in a web application. Finally, you'll gain an understanding of web application vulnerabilities and the ways they can be exploited using the tools in Kali Linux.
 
## Instructions and Navigations
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.

The code will look like the following:
```
<?php 
  if(!empty($_GET['k'])) { 
    $file = fopen('keys.txt', 'a'); 
    fwrite($file, $_GET['k']); 
    fclose($file); 
  } 
?> 
```

To successfully take advantage of this book, the reader is recommended to have a basic understanding of the following topics:
* Linux OS installation
* Unix/Linux command-line usage
* The HTML language
* PHP web application programming
* Python programming

The only hardware necessary is a personal computer, with an operation system capable of running VirtualBox or other virtualization software. As for specifications, the recommended setup is as follows:

* Intel i5, i7, or a similar CPU
* 500 GB on hard drive
* 8 GB on RAM
* An internet connection

## Related Products
* [Kali Linux Wireless Penetration Testing Beginner’s Guide - Third Edition](https://www.packtpub.com/networking-and-servers/kali-linux-wireless-penetration-testing-beginner’s-guide-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788831925)

* [Digital Forensics with Kali Linux](https://www.packtpub.com/networking-and-servers/digital-forensics-kali-linux-0?utm_source=github&utm_medium=repository&utm_campaign=9781788625005)

* [Kali Linux Wireless Penetration Testing Cookbook](https://www.packtpub.com/networking-and-servers/kali-linux-wireless-penetration-testing-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781783554089)

