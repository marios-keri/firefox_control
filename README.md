Firefox control through shortcut

# DESCRIPTION
This program allows you to automate the boring stuff by using the power of shortcut keys.
This program is designed to work just for Linux, been tested under Ubuntu 19.10
It can be used to contorl any program that uses shortcutes. 
Future releases will contain:
- Bookmarks
- Histor
- Windows and Tabs
- Add timeing in the body of the function.

NOTE: In the current version of the software the browser needs to be initialized by the user, 
and then use this program to create the shortcuts you need to get the job done.
It is a good idea to use the "time" module form the python standard library to separate the function shortcut 
between each other.


Allows you to automate:
- Fill forms
- Log in
- Download software
- Play games
- Copy and Paste
- Manipulate text
- Search

Almost anything a human can do with a browser the firefox_control can do.


# USAGE 
```import firefox_control
   
   browser = firefox_control.main()
   navigation = borwser.Navigation()
   
   navigation.back()
   navigation.forward()
   navigation.home()
   navigation.open_file()
   navigation.reload()
   
```
# USAGE COMBINATIONS WITH TIME MODULE
```import firefox_control
   import time
   
   browser = firefox_control.main()
   navigation = borwser.Navigation()
   
   navigation.back()
   time.sleep(1)             # 
   navigation.forward()
   time.sleep(1) 
   navigation.home()
   time.sleep(1) 
   navigation.open_file()
   time.sleep(1) 
   navigation.reload()

# NOTE
The shortcuts only work if they are not used by the desktop environment or window anager. 
If you have enabled Emacs-style text editing shortcuts in GNOME, 
they will also work in Firefox. 
When an Emacs text editing shortcut conflicts with the default shortcuts (as occurs with Ctrl+K), 
the Emacs shortcut will take precedence if focus is inside a text box (which would include the location bar and search bar). 
In such cases you should use the alternate keyboard shortcut if one is


