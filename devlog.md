12/5 1:37 pm
Time to begin. A little dogged with other stuff is why I'm starting now. Oops. But yeah, I'll have to start with the UI--I need it to test the program functionality, after all. Then I'll begin implementing functionality. This project doesn't seem as bad as the other ones, so I figure I should be able to get this in by midnight. I've already done some of the project, but ig I can just add it to this repo as it's done.

12/5 3:05 pm
Just got back from lunch and finished the menu. Next, I'll try to get the file access and parsing working. Hopefully this should be easy, as I've got a lot of experience building crappy little parsers.

12/5 8:22 pm
I finally completed the parser and the btree. I thought that implementing a btree would be pretty easy, seeing as I already did that for one of my other classes, but the code that I wrote was a little broken (it wouldn't split properly, so I had to effectively rewrite it from scratch). The parser was also a whole other thing; it wasn't the worst thing in the world to write (big thanks to whoever mentioned the "to_bytes()" function in the instructions), but testing it necessitated I write the "open" function, which had a lot of issues when it came to opening files and whatnot. I also completed the create function since a lot of code could be reused from the open function, and I completed the insert function because the btree I created had it's own insert function just begging to be implemented. Next, I'll probably try to implement search and print functions next. The print function can just be a recursive function, which are simple to develop, and the search function I can also achieve recursively. These next ones should be pretty simple.

12/5 9:50 pm
I was able to do the search function and the print function. They were both pretty simple--just matters of being able to simply and effectively write recursive functions to traverse the list. Next up to implement are the load method and the extract method, then I should be done. The load method seems to be similar to the insert function, so I'll see if I can reuse some of the code. The extract method I feel like I can achieve through modification of the print method.

12/5 11:49 pm
I was able to complete the load function and the extract function. These functions were essentially inversion of one another, so it was only natural to do these two together. It was kind of difficult to get used to working with .csv files, but they are really simple and intuitive to work with. I also attempted to address a bug with the open function where it can sometimes fail to properly read an index file and instead shows nothing, but in the end the bug still managed to elude me. Welp, I guess that's it.
