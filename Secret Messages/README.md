# Secret Messages

You  would  like  to  send  messages  back  and  forth  with  a  friend  (or  co-consiprator!)  but want to make sure that other people cannot easily read those messages.
However, rather than use a  xed encryption scheme, you decide to take your message string and apply a series of transformations to it to generate the encrypted message.The transformations you have agreed to use are the following:<br>
![](http://oi68.tinypic.com/2uhn33p.jpg)
    
   
This program reads in two  files and output the results to a third file (the names of which should come from user input). The user can specify the file  names  in  one  of  two  ways.  The  user  can  pass  the   file  names  as  arguments  to  the program  in  this  format <message  instruction  output  e/d> where  message  is  the  input message  file name which will contain one message per line, instruction is the  file name containing the transformation instructions (instructions will be applied to the matchingline  in  the  message   le),  output  is  the  output   file  name,  and  e/d  will  either  beeordeither  for  encryption  (apply  the  transformation  instructions)  or  decryption  (the  giventransformations have already been applied to generate the messages). If no arguments arepassed to the program, then the user will be prompted for this information
