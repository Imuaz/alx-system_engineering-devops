# 0x06. Regular expression:heavy_dollar_sign:

**Concept**

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

[Some people, when confronted with a problem, think](http://regex.info/blog/2006-09-15/247) [“I know, I’ll use regular expressions.”   Now they have two problems](http://regex.info/blog/2006-09-15/247). (super classic joke in the industry)

One thing you have to be careful with is that different languages use different regexp engines. That means that a regexp in Python, for example, will be interpreted differently in Javascript:

Regular expressions are everywhere and software engineers, no matter their positions, will have to use them during their careers. System administrators and DevOps are the ones using them the most because they are very handy for log parsing.

Read about regexp:
- [http://www.regular-expressions.info/](https://www.regular-expressions.info/)
- [http://www.w3schools.com/jsref/jsref_obj_regexp.asp](https://www.w3schools.com/jsref/jsref_obj_regexp.asp) Play with regexp (or compose them):
- Ruby:[http://rubular.com/](https://rubular.com/)
- PHP/Javascript/Python:[https://regex101.com/](https://regex101.com/)

## Resources:books:
**Read or watch:**
- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The first line of all Bash scripts should be exactly `#!/usr/bin/env ruby`
- All regex must be built for the Oniguruma library

## Tasks:page_with_curl:

**0. Simply matching School**
- [0-simply_match_school.rb](./0-simply_match_school.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method
  - The regular expression matches `School`
**1. Repetition Token #0**
- [1-repetition_token_0.rb](./1-repetition_token_0.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method.

**2. Repetition Token #1**
- [2-repetition_token_1.rb](./2-repetition_token_1.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method

**3. Repetition Token #2**
- [3-repetition_token_2.rb](./3-repetition_token_2.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method

**4. Repetition Token #3**
- [4-repetition_token_3.rb](./4-repetition_token_3.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method
  - the regex does not contain square brackets

**5. Not quite HBTN yet**
- [5-beginning_and_end.rb](./5-beginning_and_end.rb): A Ruby script that accepts one argument and pass it to a regular expression matching method
  - Regular expression should exactly matching a string that starts with `h` ends with `n` and can have any single character in between

**6. Call me maybe**
- [6-phone_number.rb](./6-phone_number.rb): The regular expression matches a 10 digit phone number

**7. OMG WHY ARE YOU SHOUTING?**
- [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb): The regular expression matching: only capital letters

**8. Textme**
- [100-textme.rb](./100-textme.rb): A script that outputs:
  - `[SENDER],[RECEIVER],[FLAGS]`
    - The sender phone number or name (including country code if present)
    - The receiver phone number or name (including country code if present)
    - The flags that were used

    :+1:
