# Securing-Strings
Using a GUI(tkinter) this algorithm encryptes &amp; decryptes the given key(string/character/sentence)
Hello Guys, 
Thnx for testing/using my GUI(Built using tkinter). The repository in GitHub is named as 'Securing Strings', which contains Encryption and Decryption Algorithm.

I have named them like BasiEncrypt and BasiDecrypt. 
<h1>Installation</h1>
1. Install Python 3.x or latest version on your computer.<br>
2. (Optional)You can also set up and IDE for Python or can use the official python.org interpreter.<br>
3. Copy-Paste the code  or download the repository and run that with your IDE or Interpreter.<br>
<h1>How it works??</h1>

<h4>Encryption(BasiEncrypt):</h4>

1. Run the python code and the output will be the GUI.
2. Enter a string/sentence/character and click-on Encrypt
3. The output will be displayed on the GUI and also in the console.
Eg: If your input is abcdABCD0123. The Encrypted output for it is [\]^:;<=)*+,
4. Finally, You have encrypted the string/sentence/character.... Fantastic!!!

<h4>Decryption(BasiDecrypt):</h4>

1. Run the python code.
2. Enter the string/sentence/character. Here, we'll enter(input) the previous(Encrypted) string [\]^:;<=)*+, and click-on Decrypt
3. So, if your string contains special characters, it'll ask you whether you want special characters in the output or not.
   If you want spl chars, click-on Yes. else click-on No.
4. The output looks like this.....
   Yes ---> [\]^:;<=)*+,  
   No  ---> abcdABCD0123

<h4>Note: SPACE AND SOME SPECIAL CHARACTERS CANNOT BE DECRYPTED PROPERLY ACCORDINGLY TO YOUR INPUT.</h4>

<h1>An Example:</h1> 

<h4>Case(i):</h4>
GIVE INPUT AS abcd@gmail.com
Copy-paste the encrypted string in the decryptor.
Clicking on Yes gives you ====> [\]^@gm[il.]om
Clicking on No gives you  ====> abcdGgmail5com

So, here you have inputted an E-mail id and the outputs are based on our choice. If we need spl chars(output:[\]^@gm[il.]om). If not needed(output:abcdGgmail5com)

So, if you need '@' in place of G and '.' in place of 5, you can write down that manually on a piece of paper.

<h4>Case(ii):</h4>
ab cd(Input)-->Encrypt it---> [\ ]^ (Encrypted Key) ---->Decrypt it----->Click-Yes---->[\]^(Output)
             							         Click-No----->abcd(Output)

Here, there is a spacing character in the input but for the input is not there.
