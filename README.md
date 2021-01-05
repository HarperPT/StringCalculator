<h1>String Calculator</h1>

<h6>The objective is to write a simple string calculator application with the following requirements
listed below.
You should choose how many or few of the requirements below to implement for the test
submission, in the time you have available. The more working requirements you implement the
better your score. However, do not attempt to complete all requirements at the expense of neat
and maintainable code and a working solution!</h6>

***String Calculator Requirements***
Pick from the following for your test submission:
1. Create a simple String calculator with a method int Add(string numbers)
a) The method will return the sum of comma-separated integer numbers parsed from
the numbers parameter (for an empty string it will return 0). Examples for the
numbers parameter are: “” or “1” or “1,2”
b) The Add method should handle an unknown amount of numbers
2. In addition to commas, allow the Add method to handle new lines between numbers.
a) the following input is ok:  “1\n2,3” (will equal 6)
b) the following input is NOT ok: “1,\n”
3. As well as comma-separated and new lines, allow the Add method to support different
delimiters
a) To set the delimiter, the beginning of the input string will contain a separate line
that looks like this: “//[delimiter]\n[numbers…]” for example
“//;\n1;2” should return 3 where the default delimiter is ‘;’.
b) the first line is optional. all existing scenarios should still be supported.
4. The Add method when called with a negative number will throw an exception
“negatives not allowed”. The exception string should include a comma-
separated list of each negative number passed to the Add method.

5. The Add method should ignore any numbers bigger than 1000, so adding 2 + 1001 = 2
6. Allow the Add method to support Delimiters of any length with the following format:
“//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6.
7. In addition to point 6, allow the Add method to support multiple delimiters like this:
“//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.
8. In addition to point 7, allow the Add method to support multiple delimiters of any length
like this:
“//[delim1][delim2]\n” for example “//[**][%%%]\n1**2%%%3” should return
6.
